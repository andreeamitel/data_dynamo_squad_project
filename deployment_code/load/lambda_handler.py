"""Contains lambda_handler function
to upload to totesys database"""

import json
import logging
import warnings
from datetime import datetime
import boto3
import awswrangler as wr
from botocore.exceptions import ClientError
import pg8000
from pg8000.native import DatabaseError

logger = logging.getLogger("Logger")
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    This function is responsible for periodically\n
    scheduling an update of the data warehouse by taking\n
    the parquet file from the processed bucket.

    Args:
    - event: a valid S3 PutObject event
    - context: Not used


    Functionality:
    get database connection from secrets manager
    get parquet data from processed bucket
    load data to RDS
    """
    try:
        warnings.filterwarnings(
            "ignore",
            message="promote has been superseded by promote_options='default'.",
            category=FutureWarning,
            module="awswrangler",
            )
        s3 = boto3.client("s3")
        secretsmanager = boto3.client(
            "secretsmanager",
            region_name="eu-west-2"
            )
        secret = secretsmanager.get_secret_value(
            SecretId="load_database_creds")
        secret_string = json.loads(secret["SecretString"])
        bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
        timestamp_key = event["Records"][0]["s3"]["object"]["key"]

        last_processed = (
            s3.get_object(
                Bucket=bucket_name,
                Key=timestamp_key,
            )["Body"]
            .read()
            .decode("UTF-8")
        )
        bucket_contents = s3.list_objects_v2(Bucket=bucket_name)["Contents"]

        files = []
        for obj in bucket_contents:
            if last_processed in obj["Key"]:
                files.append(obj["Key"])
        files.sort()

        dbapi_con = pg8000.connect(
            host=secret_string["hostname"],
            port=secret_string["port"],
            user=secret_string["username"],
            password=secret_string["password"],
            database=secret_string["database"],
        )

        timestamp = str(datetime.now().isoformat()).split("T")
        date = timestamp[0]
        time = timestamp[1]

        for file in files:
            table_name = file.split("/")[0]
            record_id_col = table_name.split("_")[1]
            test_parquet_read = wr.s3.read_parquet(
                f"s3://{bucket_name}/{file}")
            rows = len(test_parquet_read)
            if "date" not in file:
                test_parquet_read.insert(
                    0,
                    f"{record_id_col}_record_id",
                    test_parquet_read[
                        f"{test_parquet_read.columns.values[0]}"]
                    )
            test_parquet_read['last_updated_date'] = date
            test_parquet_read['last_updated_time'] = time

            lists_keys = str(test_parquet_read.columns.values.tolist()[0])
            wr.postgresql.to_sql(
                df=test_parquet_read,
                con=dbapi_con,
                table=table_name,
                mode="upsert",
                schema=secret_string["schema"],
                upsert_conflict_columns=[lists_keys],
                use_column_names=True,
            )
            logger.info(
                f"Successfully inserted {rows} rows into {table_name} table."
            )
    except ClientError as err:
        response_code = err.response["Error"]["Code"]
        response_msg = err.response["Error"]["Message"]
        logger.error(f"ClientError: {response_code}: {response_msg}")
    except DatabaseError as err:
        logger.error(f"DatabaseError {err}")
    except Exception as err:
        logger.error(err)

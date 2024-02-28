import boto3
import pg8000
import awswrangler as wr
import json
import logging
from botocore.exceptions import ClientError
from pg8000.native import DatabaseError
from datetime import datetime

logger = logging.getLogger("Logger")
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    """
    This function is responsible for periodically scheduling an
    update of the data warehouse by taking the parquet file
    from the processed bucket.

    Args:
    event:
        a valid S3 PutObject event
    context:
        a valid AWS lambda Python context object - see
            https://docs.aws.amazon.com/lambda/latest/dg/python-context.html

    Functionality:
    get database connection from secrets manager
    get parquet data from processed bucket
    load data to RDS
    """

    try:
        s3 = boto3.client("s3")
        secretsmanager = boto3.client(
            "secretsmanager", region_name="eu-west-2"
            )
        secret = secretsmanager.get_secret_value(
            SecretId="load_database_creds"
            )
        secret_string = json.loads(secret["SecretString"])
        bucket_name = secretsmanager.get_secret_value(
            SecretId="processed_bucket3"
            )["SecretString"]

        last_processed = (
            s3.get_object(
                Bucket=bucket_name,
                Key="Last_Processed.txt",
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
        print(files)
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
                f"s3://{bucket_name}/{file}"
                )

            if "date" not in file:
                test_parquet_read.insert(
                    0,
                    f"{record_id_col}_record_id",
                    test_parquet_read[
                        f"{test_parquet_read.columns.values[0]}"
                        ],
                )
            test_parquet_read["last_updated_date"] = date
            test_parquet_read["last_updated_time"] = time

            lists_keys = str(test_parquet_read.columns.values.tolist()[0])
            insert_rows = wr.postgresql.to_sql(
                df=test_parquet_read,
                con=dbapi_con,
                table=table_name,
                mode="upsert",
                schema=secret_string["schema"],
                upsert_conflict_columns=[lists_keys],
                use_column_names=True,
            )
            logger.info(
                f"Inserted {insert_rows} rows into {table_name} table "
            )
    except ClientError as err:
        response_code = err.response["Error"]["Code"]
        response_msg = err.response["Error"]["Message"]
        logger.error(f"ClientError: {response_code}: {response_msg}")
    except DatabaseError as err:
        logger.error(f"DatabaseError {err}")
    except Exception as err:
        logger.error(err)

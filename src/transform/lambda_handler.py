import boto3
from src.transform.get_latest_data import get_latest_data
from src.transform.dim_counterparty import dim_counterparty
from src.transform.dim_currency import dim_currency
from src.transform.dim_design import dim_design
from src.transform.dim_location import dim_location
from src.transform.dim_staff import dim_staff
from src.transform.fact_sales_order import fact_sales_order
from src.transform.python_to_parquet import python_to_parquet
from src.transform.dim_date import dim_date
from datetime import datetime
from botocore.exceptions import ClientError
import logging
import pandas as pd
import awswrangler as wr

logger = logging.getLogger("Logger")
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    """
    ### Functionality:
    Uses function get_latest_data() to get data from
    ingestion bucket and converts it to python
    with the help of unit functions to change data from OLTP to OLAP.
    This function then puts the processed data into a bucket.
    ### Args:
        event:
            a valid S3 PutObject event
        context:
            a valid AWS lambda Python context object
    """
    try:
        s3 = boto3.client("s3")
        secretsmanager = boto3.client("secretsmanager", region_name="eu-west-2")

        ingestion_bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
        ingestion_timestamp_key = event["Records"][0]["s3"]["object"]["key"]

        ingestion_timestamp = s3.get_object(
            Bucket=ingestion_bucket_name, Key=ingestion_timestamp_key
        )
        ingestion_time = ingestion_timestamp["Body"].read().decode("utf-8")

        updated_data = get_latest_data(ingestion_bucket_name, s3, ingestion_time)

        current_time = datetime.now().isoformat()
        processed_bucket = secretsmanager.get_secret_value(
            SecretId="processed_bucket3"
        )["SecretString"]

        table_names = list(updated_data.keys())
        counter = 0
        for table in table_names:
            counter += 1
            if table == "counterparty":
                dim_counterparty_dict = {"dim_counterparty": dim_counterparty(
                    updated_data["address"], updated_data[table]
                )}
                python_to_parquet(
                    dim_counterparty_dict, processed_bucket, current_time
                )
                print("hi")
            elif table == "staff":
                dep_df = updated_data["department"]
                staff_df = updated_data[table]
                dim_staff_df_dict = {"dim_staff": dim_staff(staff_df, dep_df)}
                python_to_parquet(dim_staff_df_dict, processed_bucket, current_time)
            elif table == "currency":
                dim_currency_dict_df = {"dim_currency": dim_currency(updated_data[table])}
                python_to_parquet(
                    dim_currency_dict_df, processed_bucket, current_time
                    )
            elif table == "design":
                dim_design_df_dict = {"dim_design": dim_design(updated_data[table])}
                python_to_parquet(
                    dim_design_df_dict, processed_bucket, current_time
                    )
            elif table == "address":
                dim_location_dict_df = {"dim_location":dim_location(updated_data[table])}
                python_to_parquet(
                    dim_location_dict_df, processed_bucket, current_time
                    )
            elif table == "sales_order":
                sales_df = updated_data[table]
                dim_date_dict_df = {"dim_date": dim_date(sales_df)}
                python_to_parquet(dim_date_dict_df, processed_bucket, current_time)
                fact_sales_order_dict_df = {"fact_sales_order": fact_sales_order(sales_df)}
                python_to_parquet(fact_sales_order_dict_df, processed_bucket, current_time)
                print("finished sales wow")
        s3.put_object(
            Body=f"{current_time}",
            Bucket=processed_bucket,
            Key="Last_Processed.txt",
        )
        print("everything done i hope")

    except ClientError as err:
        response_code = err.response["Error"]["Code"]
        response_msg = err.response["Error"]["Message"]
        logger.error(f"ClientError: {response_code}: {response_msg}")
    except Exception as err:
        logger.error(err)

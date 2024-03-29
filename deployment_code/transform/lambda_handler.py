import boto3
from transform.get_latest_data import get_latest_data
from transform.dim_counterparty import dim_counterparty
from transform.dim_currency import dim_currency
from transform.dim_design import dim_design
from transform.dim_location import dim_location
from transform.dim_staff import dim_staff
from transform.fact_sales_order import fact_sales_order
from transform.python_to_parquet import python_to_parquet
from transform.dim_date import dim_date
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
        secretsmanager = boto3.client("secretsmanager")

        ingestion_bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
        ingestion_timestamp_key = event["Records"][0]["s3"]["object"]["key"]

        ingestion_timestamp = s3.get_object(
            Bucket=ingestion_bucket_name, Key=ingestion_timestamp_key
        )
        ingestion_time = ingestion_timestamp["Body"].read().decode("utf-8")

        new_data = get_latest_data(ingestion_bucket_name, s3, ingestion_time)

        current_time = datetime.now().isoformat()
        processed_bucket = secretsmanager.get_secret_value(
            SecretId="processed_bucket3"
        )["SecretString"]

        table_names = [list(table.keys())[0] for table in new_data]
        updated_data = {list(table.keys())[0]: table for table in new_data}
        counter = 0
        for table in table_names:
            counter += 1
            if table == "counterparty":
                dim_counterparty_table = dim_counterparty(
                    updated_data["address"], updated_data[table]
                )
                python_to_parquet(
                    dim_counterparty_table, processed_bucket, current_time
                )
            elif table == "staff":
                dep_df = pd.DataFrame(updated_data['department']['department'])
                staff_df = pd.DataFrame(updated_data[table]['staff'])
                dim_staff_df = dim_staff(staff_df, dep_df)
                wr.s3.to_parquet(
                dim_staff_df,
                path=f"s3://{processed_bucket}/dim_staff/{current_time}.parquet",
                index=False,
                )
            elif table == "currency":
                dim_currency_table = dim_currency(updated_data[table])
                python_to_parquet(dim_currency_table,
                                  processed_bucket, current_time)
            elif table == "design":
                dim_design_table = dim_design(updated_data[table])
                python_to_parquet(dim_design_table,
                                  processed_bucket, current_time)
            elif table == "address":
                dim_location_table = dim_location(updated_data[table])
                python_to_parquet(dim_location_table,
                                  processed_bucket, current_time)
            elif table == "department":
                pass
            else:
                sales_df = pd.DataFrame(updated_data[table]["sales_order"])
                dim_date_df = dim_date(sales_df)
                wr.s3.to_parquet(
                    dim_date_df,
                    path=f"""
                    s3://{processed_bucket}/dim_date/{current_time}.parquet
                    """,
                    index=False,
                )
                fact_sales_order_df = fact_sales_order(sales_df)
                wr.s3.to_parquet(
                    fact_sales_order_df,
                    path=f"""
                    s3://{processed_bucket}/fact_sales_order/{current_time}.parquet
                    """,
                    index=False,
                )
        s3.put_object(
            Body=f"{current_time}",
            Bucket=processed_bucket,
            Key="Last_Processed.txt",
        )
    except ClientError as err:
        response_code = err.response["Error"]["Code"]
        response_msg = err.response["Error"]["Message"]
        logger.error(f"ClientError: {response_code}: {response_msg}")
    except Exception as err:
        logger.error(err)
        print(err)

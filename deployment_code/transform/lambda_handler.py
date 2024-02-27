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
        print("new_data >>>>>", new_data)

        current_time = datetime.now().isoformat()
        bucket = secretsmanager.get_secret_value(SecretId="processed_bucket3")[
            "SecretString"
        ]

        table_names = [list(table.keys())[0] for table in new_data]
        print("table_names >>>>>", table_names)
        updated_data = {list(table.keys())[0]: table for table in new_data}
        print("updated_data >>>>>", updated_data)
        counter = 0
        for table in table_names:
            counter += 1
            if table == "counterparty":
                print("counterparty loop")
                dim_counterparty_table = dim_counterparty(
                    updated_data["address"], updated_data[table]
                )
                python_to_parquet(dim_counterparty_table, bucket, current_time)
            elif table == "staff":
                print("staff loop")
                dim_staff_table = dim_staff(
                    updated_data[table], updated_data["department"]
                )
                python_to_parquet(dim_staff_table, bucket, current_time)
            elif table == "currency":
                print("currency loop")
                dim_currency_table = dim_currency(updated_data[table])
                python_to_parquet(dim_currency_table, bucket, current_time)
            elif table == "design":
                print("design loop")
                dim_design_table = dim_design(updated_data[table])
                python_to_parquet(dim_design_table, bucket, current_time)
            elif table == "address":
                print("address loop")
                dim_location_table = dim_location(updated_data[table])
                python_to_parquet(dim_location_table, bucket, current_time)
            elif table == "department":
                print("department loop")
                pass
            else:
                print("sales loop")

                sales_order, dim_date_table = dim_date(updated_data[table])
                print("unpacked sales and dates")
                python_to_parquet(dim_date_table, bucket, current_time)
                print("wrote dim dates to parquet")

                fact_sales = fact_sales_order(sales_order)
                print("did fact sales order")
                python_to_parquet(fact_sales, bucket, current_time)
                print("wrote to parquet")

            print(counter, "<<< counter")
        s3.put_object(
            Body=f"{current_time}",
            Bucket=bucket,
            Key="Last_Processed.txt",
        )
        print("end of lambda2")
    except ClientError as err:
        response_code = err.response["Error"]["Code"]
        response_msg = err.response["Error"]["Message"]
        logger.error(f"ClientError: {response_code}: {response_msg}")
    except Exception as err:
        logger.error(err)
        print(err)
        print("ERROR FFS")

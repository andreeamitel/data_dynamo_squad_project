import boto3
from src.transform.get_latest_data import get_latest_data
from dim_counterparty import dim_counterparty
from dim_currency import dim_currency
from dim_design import dim_design
from dim_location import dim_location
from dim_staff import dim_staff
from python_to_parquet import python_to_parquet
from datetime import datetime

def lambda_handler(event, context):
    """
    ### Args:
        event:
            a valid S3 PutObject event -
            see https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-content-structure.html
        context:
            a valid AWS lambda Python context object - see
            https://docs.aws.amazon.com/lambda/latest/dg/python-context.html
    ### Functionality:
    - uses function get_latest_data() to get data from ingestion bucket and convert to python
    - passed into unit functions to change from OLTP to OLAP
    - calls python_to_parquet function -  which changes python to parquet and stores in processed bucket
    """

    ingestion_bucket_name = event["Records"]["s3"]["bucket"]["name"]
    timestamp_key = event["Records"]["s3"]["object"]["key"]
    s3 = boto3.client("s3")
    timestamp = s3.get_object(Bucket=ingestion_bucket_name, key=timestamp_key)

    updated_data = get_latest_data(ingestion_bucket_name, timestamp)
    file_function_dict = {
        "date": dim_date,
        "currency": dim_currency,
        "counterparty": dim_counterparty,
        "design": dim_design,
        "address": dim_location,
        "staff": dim_staff,
        # "sales_order": dim_sales_order,
    }
    processed_timestamp = datetime.now().isoformat()
    secrets_manager = boto3.client("secretsmanager")
    processed_bucket_name = secrets_manager.get_secret_value("processed_bucket")
    for table in updated_data:
        file_process_function = file_function_dict[f"{table}"]
        if str(table) == "counterparty":
            updated_table = file_process_function(table, updated_data["address"])
        elif str(table) == "staff":
            updated_table = file_process_function(table, updated_data["department"])
        elif str(table) == "department":
            pass
        else:
            updated_table = file_process_function(table)
        python_to_parquet(updated_table, processed_bucket_name, processed_timestamp)

    # python_to_parquet(table, processed_bucket_name, timestamp)
    # finished :)


lambda_handler(1, 2)

import boto3
from src.transform.get_latest_data import get_latest_data
from src.transform.dim_counterparty import dim_counterparty
from src.transform.dim_currency import dim_currency
from src.transform.dim_design import dim_design
from src.transform.dim_location import dim_location
from src.transform.dim_staff import dim_staff
from src.transform.fact_sales_order import fact_sales_order
from src.transform.python_to_parquet import python_to_parquet
from datetime import datetime
from pprint import pprint
from botocore.exceptions import ClientError
import logging


logger = logging.getLogger("Logger")
logger.setLevel(logging.INFO)


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
    try:
        s3 = boto3.client("s3")
        secrets_manager = boto3.client("secretsmanager")
        

        ingestion_bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
        ingestion_timestamp_key = event["Records"][0]["s3"]["object"]["key"]
        
        ingestion_timestamp_dict = s3.get_object(
            Bucket=ingestion_bucket_name, Key=ingestion_timestamp_key
        )
        ingestion_timestamp = ingestion_timestamp_dict["Body"].read().decode("utf-8")
        
        updated_data = get_latest_data(ingestion_bucket_name, s3, ingestion_timestamp)
        print(updated_data, "<<<< data first collected")

        processed_timestamp = datetime.now().isoformat()
        processed_bucket_name = secrets_manager.get_secret_value(
            SecretId="processed_bucket3"
        )["SecretString"]

        table_names = [list(table.keys())[0] for table in updated_data]

        updated_data_dict = {list(table.keys())[0]: table for table in updated_data}
        counter = 0
        for table_name in table_names:
            counter+=1
            if table_name == "counterparty":
                print("counterparty loop")
                dim_counterparty_table = dim_counterparty(
                    updated_data_dict[table_name], updated_data_dict["address"]
                )
                python_to_parquet(
                    dim_counterparty_table, processed_bucket_name, processed_timestamp
                )
            elif table_name == "staff":
                print("staff loop")
                dim_staff_table = dim_staff(
                    updated_data_dict[table_name], updated_data_dict["department"]
                )
                python_to_parquet(
                    dim_staff_table, processed_bucket_name, processed_timestamp
                )
            elif table_name == "currency":
                print("currency loop")
                dim_currency_table = dim_currency(updated_data_dict[table_name])
                python_to_parquet(
                    dim_currency_table, processed_bucket_name, processed_timestamp
                )
            elif table_name == "design":
                print("design loop")
                dim_design_table = dim_design(updated_data_dict[table_name])
                python_to_parquet(
                    dim_design_table, processed_bucket_name, processed_timestamp
                )
            elif table_name == "address":
                print("address loop")
                dim_location_table = dim_location(updated_data_dict[table_name])
                python_to_parquet(
                    dim_location_table, processed_bucket_name, processed_timestamp
                )
            elif table_name == "department":
                print("department loop")
                pass
            else:
                print("sales loop")
                fact_sales, dim_dates = fact_sales_order(updated_data_dict[table_name])
                python_to_parquet(
                    fact_sales, processed_bucket_name, processed_timestamp
                )
                python_to_parquet(dim_dates, processed_bucket_name, processed_timestamp)
            print(counter, "<<< counter")
        s3.put_object(
            Body=f"{processed_timestamp}",
            Bucket=processed_bucket_name,
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

import boto3
from botocore.exceptions import ClientError
import json
from datetime import datetime 
from pg8000.native import Connection, DatabaseError
from src.extract.check_for_changes import check_for_changes
from src.extract.extract_data import extract_data
from pprint import pprint
from src.extract.conversion_and_write_data import convert_and_write_data
def lambda_handler():
    """
    ### Args:
        event:
            a valid S3 PutObject event -
            see https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-content-structure.html
        context:
            a valid AWS lambda Python context object - see
            https://docs.aws.amazon.com/lambda/latest/dg/python-context.html

    ### Functionality:
    - Establishes connection to totesys database.
    - Uses `check_for_updates()` to see if totesys database has any new or updated data.
    - Loop of `check_for_updates()` return list of `table_names` IF empty kill process:
        - Runs `extract_data()` with `table_name` as argument returning `list` of `dicts` (`table_dict`)
        - Runs `write_table_dict_to_JSON()` printing to bucket
    
    ### Returns a JSON file:
        `{last_ingested_time: timestamp, new_data_found: boolean}`
    
    ### Errors:
        - Database Connection Error
        - Functions Errors
        - AWS Errors - S3, SecretsManager, Trigger Errors
        - Exception
    ### Examples:

    """

    try:
        s3 = boto3.client("s3")
        secretsmanager = boto3.client("secretsmanager")
        obj = s3.list_objects_v2(Bucket = "ingested-bucket-20240213151611822700000004")["Contents"]
        test = [object["Key"] for object in obj if object["Key"] == "Last_Ingested.json"]
        if test != []:
            timestamp = s3.get_object(Bucket = "ingested-bucket-20240213151611822700000004",
            Key = "Last_Ingested.json")
            last_ingested_timestamp_obj = json.load(timestamp["Body"])
            last_ingested_timestamp = last_ingested_timestamp_obj["last_ingested_time"]
        else:
            last_ingested_timestamp = "2000-02-14 16:54:36.774180"

        secret=secretsmanager.get_secret_value(SecretId = "database_creds")
        secret_string=json.loads(secret["SecretString"])

        conn = Connection(
            host = secret_string["hostname"],
            port = secret_string["port"],
            user = secret_string["username"],
            password = secret_string["password"],
            database=secret_string["database"],
        )
        needs_fetching_tables = check_for_changes(conn, last_ingested_timestamp)
        for table in needs_fetching_tables:
            table_data = extract_data(table, conn, last_ingested_timestamp)
            convert_and_write_data(table_data, table)

        date_time = datetime.now().isoformat()
        with open("./src/extract/Last_Ingested.json", "w") as f:
            json.dump({'last_ingested_time': date_time,"new_data_found" : True}, f)
        s3.upload_file("./src/extract/Last_Ingested.json", "ingested-bucket-20240213151611822700000004","Last_Ingested.json")
    except Exception as Excep:
        print(Excep, "gone tits up")

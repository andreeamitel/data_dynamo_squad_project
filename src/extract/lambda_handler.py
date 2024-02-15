import boto3
import json
from datetime import datetime 
from pg8000.native import Connection
from src.extract.check_for_changes import check_for_changes
from src.extract.extract_data import extract_data
from pprint import pprint
def data_conversion():
    pass
def lambda_handler():
    """
    ### Args:
    - event:
    - context:

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
    s3 = boto3.client("s3")
    secretsmanager = boto3.client("secretsmanager")
    timestamps3.get_object(Bucket = "ingested-bucket-20240213151611822700000004",
    Key = "Last_Ingested.json")
    last_ingested_timestamp = json.load(result["Body"])
    secret=secretsmanager.get_secret_value(SecretId = "database_creds")
    secret_string=json.loads(secret["SecretString"])

    conn = Connection(
    host = secret_string["hostname"],
    port = secret_string["port"],
    user = secret_string["username"],
    password = secret_string["password"],
    database=secret_string["database"],
    )
    
    check_for_changes(conn, last_ingested_timestamp)
    test_extract = extract_data("staff", conn, "2022-02-14 16:54:36")
    test_conversion = data_conversion()

    date_time = datetime.now().isoformat()
    with open("./src/extract/Last_Ingested.json", "w") as f:
        json.dump({'last_ingested_time': date_time,"new_data_found" : True}, f)
    s3.upload_file("./src/extract/Last_Ingested.json", "ingested-bucket-20240213151611822700000004","Last_Ingested.json")
    
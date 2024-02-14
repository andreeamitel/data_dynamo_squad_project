import boto3
import json
from datetime import datetime 
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
    date_time = datetime.now().isoformat()
    with open("./src/extract/Last_Ingested.json", "w") as f:
        json.dump({'last_ingested_time': date_time,"new_data_found" : True}, f)
    s3.upload_file("./src/extract/Last_Ingested.json", "ingested-bucket-20240213151611822700000004","Last_Ingested.json")
    
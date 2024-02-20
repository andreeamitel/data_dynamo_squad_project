'''
Conatains a function that converts data to json.
Functions:\n
    conversion_and_write_data
'''

import json
from datetime import datetime
import boto3


def convert_and_write_data(list_of_selection, table_name, bucket_name):
    """
    This function should convert the data from a list of dictionaries to 
    json, write it in a file and put it in the ingested-bucket.

    Args:\n
        list of dictionaries
        table_name(str)

    Returns:\n
        None
    """
    
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    file_name = f'{date_time}/{table_name}.json'
    s3 = boto3.client('s3')
    s3.put_object(
        Body=f'{json.dumps({table_name:list_of_selection})}',
        Bucket=bucket_name,
        Key=f'{file_name}',
        )
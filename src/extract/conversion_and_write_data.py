import json
from datetime import datetime
import boto3


def convert_and_write_data(list_of_selection, table_name):
    """
    This function should convert the data from a list to 
    json file and write this in a bucket

    Args:\n
        list of dictionaries(list)
        table_name(str)

    Returns:\n
        None
    """
    try:
        date_time = datetime.now().isoformat()
        file_name = f'{table_name}-{date_time}.json'
        s3 = boto3.client('s3')
        s3.put_object(
            Body=f'{json.dumps(list_of_selection)}',
            Bucket='ingested-bucket-20240213151611822700000004',
            Key=f'{file_name}',
        )
    except Exception as err:
        print(err)
        raise err



# arg = [
#                 {
#                     "currency_id": 1,
#                     "currency_code": "GBP",
#                     "created_at": "2024-02-13",
#                     "last_updated": "2024-02-13",
#                 }
#             ]
# convert_and_write_data(arg, 'currency')
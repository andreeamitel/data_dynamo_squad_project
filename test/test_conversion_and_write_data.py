from datetime import datetime
from moto import mock_aws
from src.extract.conversion_and_write_data import convert_and_write_data
import boto3

@mock_aws
def test_puts_file_in_bucket():
    arg = [
                {
                    "currency_id": 1,
                    "currency_code": "GBP",
                    "created_at": "2024-02-13",
                    "last_updated": "2024-02-13",
                }
            ]
    date_time = datetime.now().isoformat()
    file_name = f'currency-{date_time}.json'
    s3 = boto3.client('s3')
    s3.create_bucket(
            Bucket='ingested-bucket',
            CreateBucketConfiguration={
           'LocationConstraint': 'eu-west-2',
        },
        )
    convert_and_write_data(arg, 'currency')
    result = s3.get_object(
            Bucket='ingested-bucket',
            Key=f'{file_name}',
        )
    print(result)
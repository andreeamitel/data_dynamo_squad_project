'''Tests conversion_and_write_data function.'''

from datetime import datetime
import json
import pytest
from moto import mock_aws
import boto3
from src.extract.conversion_and_write_data import convert_and_write_data


@pytest.mark.describe("conversion_and_write_data")
@pytest.mark.it("puts the json file in a bucket")
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
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    file_name = f'{date_time}/currency.json'
    s3 = boto3.client('s3')
    s3.create_bucket(
            Bucket='ingested-bucket',
            CreateBucketConfiguration={
           'LocationConstraint': 'eu-west-2',
        },
        )
    convert_and_write_data(arg, 'currency', "ingested-bucket")
    result = s3.list_objects(
    Bucket='ingested-bucket',
    )
    expected = file_name
    assert result['Contents'][0]['Key'] == expected

@pytest.mark.describe("conversion_and_write_data")
@pytest.mark.it("puts a json file inside the bucket")
@mock_aws
def test_puts_json_file():
     arg =  [
                {
                    "currency_id": 1,
                    "currency_code": "GBP",
                    "created_at": "2024-02-13",
                    "last_updated": "2024-02-13",
                }
     ]
     s3 = boto3.client('s3')
     s3.create_bucket(
            Bucket='ingested-bucket',
            CreateBucketConfiguration={
           'LocationConstraint': 'eu-west-2',
        },
        )
     convert_and_write_data(arg, 'currency', "ingested-bucket")
     result = s3.list_objects(
     Bucket='ingested-bucket',
      )
     expected = 'json'
     assert result['Contents'][0]['Key'][-4:] == expected

@pytest.mark.describe("conversion_and_write_data")
@pytest.mark.it("writes correct data to the json file")     
@mock_aws
def test_writes_data_of_table_to_json_file():
    arg = [
            {
                "currency_id": 1,
                "currency_code": "GBP",
                "created_at": "2024-02-13",
                "last_updated": "2024-02-13",
            }
    ]
    s3 = boto3.client('s3')
    s3.create_bucket(
        Bucket='ingested-bucket',
        CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-2',
    },
    )
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    file_name= f'{date_time}/currency.json'
    convert_and_write_data(arg, 'currency', "ingested-bucket")
    result = s3.get_object(
    Bucket='ingested-bucket',
    Key=f'{file_name}'
    )
    expected = json.dumps({"currency": arg})
    assert result['Body'].read().decode('utf-8') == expected

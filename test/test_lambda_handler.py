from src.extract.lambda_handler import lambda_handler
import pytest
import boto3
from datetime import datetime 
from moto import mock_aws
from unittest.mock import patch

@pytest.mark.describe("lambda_handler")
@pytest.mark.it("Test that a json file gets written to the ingestion bucket in aws")
@mock_aws
@patch("src.extract.lambda_handler.datetime")
def test_write_json_file(mock_time):
    mock_time.now().isoformat.return_value = "2024-02-14 16:54:36.774180"
    s3 = boto3.client("s3")
    s3.create_bucket(Bucket = "ingested-bucket-20240213151611822700000004",
    CreateBucketConfiguration = {
        'LocationConstraint': 'eu-west-2',
    })
    lambda_handler()
    result = s3.get_object(Bucket = "ingested-bucket-20240213151611822700000004",
    Key = "Last_Ingested.json")
    #need to finish assert
    print((result["Body"].read()))
    assert result['ResponseMetadata']['HTTPStatusCode']==200

lambda_handler()
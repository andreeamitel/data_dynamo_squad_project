from src.transform import dim_design

from moto import mock_aws
import json
import pytest
import boto3
import os


@pytest.fixture
def valid_data():
    with open("test/transform/valid_test_data.json") as v_json:
        test_data = json.loads(v_json)
        print(test_data, "VALID_DATA")
    return test_data


@pytest.fixture(scope="function")
def aws_credentials():
    os.environ["AWS_ACCESS_KEY_ID"] = "test"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "test"
    os.environ["AWS_SECURITY_TOKEN"] = "test"
    os.environ["AWS_SESSION_TOKEN"] = "test"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"


@pytest.fixture(scope="function")
def s3(aws_credentials):
    with mock_aws():
        yield boto3.client("s3", region_name="eu-west-2")


@pytest.fixture
def bucket(s3):
    s3.create_bucket(
        Bucket="test_ingested_bucket",
        CreateBucketConfiguration={"LocationConstraint": "eu-west-2"},
    )
    
    with open("test/transform/valid_test_data.json") as v_json:
        design_data = json.load(v_json)
    s3.put_object(
            Body=design_data, Bucket="test_ingested_bucket", Key="test/design_data.json"
        )
    data = s3.get_object(Bucket="test_ingested_bucket", Key="test/design_data.json")
    return data


@pytest.mark.describe("dim_design")
@pytest.mark.it("function dim_design read a file from the bucket")
def test_read_file_from_bucket(bucket, valid_data):
    contents = bucket.data['Body'].read()
    assert contents == valid_data

# test_jso
# @mock_s3
# def test_read_file_from_bucket(s3_boto):
#     bucket = "test-ingested-bucket"
#     key = "test-key"
#     body = '{[[{"design_id": 1, "currency_code": "GBP", "created_at": "2024-02-13", "last_updated": "2024-02-13"}]]}'
#     s3_boto.create_bucket(Bucket=bucket)

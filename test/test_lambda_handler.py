from src.extract.lambda_handler import lambda_handler
import pytest
import boto3
from datetime import datetime 
from moto import mock_aws 
from unittest.mock import patch
import json

@pytest.fixture(scope="function")
def aws_s3():
    with mock_aws():
        yield boto3.client("s3", region_name="eu-west-2")
@pytest.fixture(scope="function")
def aws_secrets():
    with mock_aws():
        yield boto3.client("secretsmanager")

@pytest.fixture
def create_bucket1(aws_s3):
    boto3.client("s3").create_bucket(Bucket = "ingested-bucket-20240213151611822700000004",
    CreateBucketConfiguration = {
        'LocationConstraint': 'eu-west-2'
    })
@pytest.fixture
def secretmanager(aws_secrets):
    boto3.client("secretsmanager").create_secret(Name = "database_creds", 
    SecretString = '{"hostname":"example_host.com","port": "4321", "database" : "example_database", "username": "project_team_0", "password":"EXAMPLE-PASSWORD"}')

@pytest.fixture
def mock_conn():
    with patch("src.extract.lambda_handler.Connection", return_value = True) as conn:
        yield conn
        


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("Test that a json file gets written to the ingestion bucket in aws")
@patch("src.extract.lambda_handler.datetime")
@mock_aws
def test_write_json_file(mock_time,create_bucket1,secretmanager, mock_conn):
    mock_time.now().isoformat.return_value = "2024-02-14 16:54:36.774180"
    lambda_handler()
    result = boto3.client("s3").get_object(Bucket = "ingested-bucket-20240213151611822700000004",
    Key = "Last_Ingested.json")
    dict_result=json.load(result["Body"])
    print(dict_result)
    assert dict_result=={"last_ingested_time": "2024-02-14 16:54:36.774180", "new_data_found": True}

@pytest.mark.describe("lambda_handler")
@pytest.mark.it("Test that a connection has been established to a database - using secretsmanager")
@patch("src.extract.lambda_handler.Connection")
@mock_aws
def test_database_conn(mock_conn, create_bucket1, secretmanager):
    lambda_handler()
    mock_conn.assert_called_with(host="example_host.com",port= "4321", database = "example_database", user= "project_team_0", password = "EXAMPLE-PASSWORD")
    




@pytest.mark.describe("lambda_handler")
@pytest.mark.it("Test that all internal functions are called")
@patch("src.extract.lambda_handler.check_for_changes")
@patch("src.extract.lambda_handler.extract_data")
@patch("src.extract.lambda_handler.data_conversion")
def test_functions_are_called(mock_data_conv, mock_extract_data, mock_check_changes):
    pass

@pytest.mark.describe("lambda_handler")
@pytest.mark.it("Integration test - Test that data_conversion gets called with outputs from extract_data and appears in bucket")
@patch("src.extract.lambda_handler.check_for_changes")
@patch("src.extract.lambda_handler.extract_data")
@mock_aws
def test_data_conversion(mock_extract_data, mock_check_changes):
    pass


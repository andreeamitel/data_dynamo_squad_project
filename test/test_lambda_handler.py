from src.extract.lambda_handler import lambda_handler
import pytest
import boto3
from datetime import datetime 
from moto import mock_aws 
from unittest.mock import patch, Mock
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
def create_object(create_bucket1):
    with open("./test/Last_Ingested.json", "w") as f:
        json.dump({'last_ingested_time': "2022-02-14 16:54:36.774180","new_data_found" : True}, f)
    boto3.client("s3").upload_file("test/Last_Ingested.json", "ingested-bucket-20240213151611822700000004","Last_Ingested.json")


@pytest.fixture
def secretmanager(aws_secrets):
    boto3.client("secretsmanager").create_secret(Name = "database_creds", 
    SecretString = '{"hostname":"example_host.com","port": "4321", "database" : "example_database", "username": "project_team_0", "password":"EXAMPLE-PASSWORD"}')

@pytest.fixture
def mock_conn():
    with patch("src.extract.lambda_handler.Connection") as conn:
        yield conn
        


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("Test that a json file gets written to the ingestion bucket in aws")
@patch("src.extract.lambda_handler.datetime")
@mock_aws
def test_write_json_file(mock_time,create_bucket1,secretmanager, mock_conn, create_object):
    mock_time.now().isoformat.return_value = "2024-02-14 16:54:36.774180"
    lambda_handler()
    result = boto3.client("s3").get_object(Bucket = "ingested-bucket-20240213151611822700000004",
    Key = "Last_Ingested.json")
    dict_result=json.load(result["Body"])
    print(dict_result)
    assert dict_result=={"last_ingested_time": "2024-02-14 16:54:36.774180", "new_data_found": True}

@pytest.mark.describe("lambda_handler")
@pytest.mark.it("Test that a connection has been established to a database - using secretsmanager")
@mock_aws
def test_database_conn(mock_conn, create_bucket1, secretmanager,create_object):
    lambda_handler()
    mock_conn.assert_called_with(host="example_host.com",port= "4321", database = "example_database", user= "project_team_0", password = "EXAMPLE-PASSWORD")
  
@pytest.mark.describe("lambda_handler")
@pytest.mark.it("Test that all internal functions are called")
@patch("src.extract.lambda_handler.check_for_changes", return_value = ["currency", "staff"])
@patch("src.extract.lambda_handler.extract_data")
@patch("src.extract.lambda_handler.data_conversion")
def test_functions_are_called(mock_data_conv, mock_extract_data, mock_check_changes, mock_conn, create_bucket1, secretmanager, create_object):
    lambda_handler()
    print(dir(mock_check_changes))
    assert mock_data_conv.call_count == 2
    assert mock_extract_data.call_count == 2
    mock_check_changes.assert_called_once()

@pytest.mark.describe("lambda_handler")
@pytest.mark.it("Test that check_for_changes uses last_ingested_time stored in bucket json")
@patch("src.extract.lambda_handler.check_for_changes")
@patch("src.extract.lambda_handler.extract_data")
@patch("src.extract.lambda_handler.data_conversion")
@mock_aws
def test_check_changes_uses_correct_date(mock_data_conv, mock_extract_data, mock_check_changes, mock_conn, create_bucket1, secretmanager, create_object):
    lambda_handler()
    mock_check_changes.assert_called_with(mock_conn(),"2022-02-14 16:54:36.774180")




@pytest.mark.describe("lambda_handler")
@pytest.mark.it("Integration test - Test that data_conversion gets called with outputs from extract_data and appears in bucket")
@patch("src.extract.lambda_handler.check_for_changes")
@patch("src.extract.lambda_handler.extract_data")
@mock_aws
def test_data_conversion(mock_extract_data, mock_check_changes):
    pass


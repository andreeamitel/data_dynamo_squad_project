from src.extract.lambda_handler import lambda_handler
import pytest
import boto3
from botocore.exceptions import ClientError
from datetime import datetime
from moto import mock_aws
from unittest.mock import patch, Mock
import json
import logging
from pg8000.native import Connection, DatabaseError


@pytest.fixture(scope="function")
def aws_s3():
    with mock_aws():
        yield boto3.client("s3", region_name="eu-west-2")


@pytest.fixture(scope="function")
def aws_secrets():
    with mock_aws():
        yield boto3.client("secretsmanager", region_name="eu-west-2")


@pytest.fixture
def create_bucket1(aws_s3):
    boto3.client("s3").create_bucket(
        Bucket="ingested-bucket-20240213151611822700000004",
        CreateBucketConfiguration={"LocationConstraint": "eu-west-2"},
    )


@pytest.fixture
def create_error_bucket(aws_s3):
    boto3.client("s3").create_bucket(
        Bucket="error_bucket",
        CreateBucketConfiguration={"LocationConstraint": "eu-west-2"},
    )


@pytest.fixture
def create_object(create_bucket1):
    with open("./test/Last_Ingested.json", "w") as f:
        json.dump(
            {
                "last_ingested_time": "2022-02-14 16:54:36.774180",
                "new_data_found": True,
            },
            f,
        )
    boto3.client("s3").upload_file(
        "test/Last_Ingested.json",
        "ingested-bucket-20240213151611822700000004",
        "Last_Ingested.json",
    )


@pytest.fixture
def secretmanager(aws_secrets):
    aws_secrets.create_secret(
        Name="database_creds_test",
        SecretString='{"hostname":"example_host.com","port": "4321", "database" : "example_database", "username": "project_team_0", "password":"EXAMPLE-PASSWORD"}',
    )
    aws_secrets.create_secret(
        Name="ingestion_bucket_02",
        SecretString="ingested-bucket-20240213151611822700000004",
    )


@pytest.fixture
def mock_conn():
    with patch("src.extract.lambda_handler.Connection") as conn:
        yield conn


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("Test that a txt file gets written to the ingestion bucket in aws")
@patch("src.extract.lambda_handler.datetime")
@patch(
    "src.extract.lambda_handler.check_for_changes", return_value=["currency", "staff"]
)
@patch("src.extract.lambda_handler.extract_data")
@patch("src.extract.lambda_handler.convert_and_write_data")
@mock_aws
def test_write_txt_file(
    convert_mock,
    extract_mock,
    check_mock,
    mock_time,
    create_bucket1,
    secretmanager,
    mock_conn,
    create_object,
):
    mock_time.now().isoformat.return_value = "2024-02-14 16:54:36.774180"
    lambda_handler("thing1", "thing2")
    result = boto3.client("s3").get_object(
        Bucket="ingested-bucket-20240213151611822700000004", Key="Last_Ingested.txt"
    )
    txt_result = result["Body"].read().decode("utf-8")
    print(txt_result)
    assert txt_result == "2024-02-14 16:54:36.774180"


@pytest.mark.describe("lambda_handler")
@pytest.mark.it(
    "Test that a connection has been established to a database - using secretsmanager"
)
@mock_aws
def test_database_conn(mock_conn, create_bucket1, secretmanager, create_object):
    lambda_handler("thing1", "thing2")
    mock_conn.assert_called_with(
        host="example_host.com",
        port="4321",
        database="example_database",
        user="project_team_0",
        password="EXAMPLE-PASSWORD",
    )


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("Test that all internal functions are called")
@patch(
    "src.extract.lambda_handler.check_for_changes", return_value=["currency", "staff"]
)
@patch("src.extract.lambda_handler.extract_data")
@patch("src.extract.lambda_handler.convert_and_write_data")
def test_functions_are_called(
    mock_data_conv,
    mock_extract_data,
    mock_check_changes,
    mock_conn,
    create_bucket1,
    secretmanager,
    create_object,
):
    lambda_handler("thing1", "thing2")
    assert mock_data_conv.call_count == 2
    assert mock_extract_data.call_count == 2
    mock_check_changes.assert_called_once()


@pytest.mark.describe("lambda_handler")
@pytest.mark.it(
    "Test that check_for_changes uses last_ingested_time stored in bucket json"
)
@patch("src.extract.lambda_handler.check_for_changes")
@patch("src.extract.lambda_handler.extract_data")
@patch("src.extract.lambda_handler.convert_and_write_data")
@mock_aws
def test_check_changes_uses_correct_date(
    mock_data_conv,
    mock_extract_data,
    mock_check_changes,
    mock_conn,
    create_bucket1,
    secretmanager,
    create_object,
):
    lambda_handler("thing1", "thing2")
    mock_check_changes.assert_called_with(mock_conn(), "2022-02-14 16:54:36.774180")


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("Error: ClientError - for bucket")
@mock_aws
def test_client_error_bucket(caplog, secretmanager):
    with caplog.at_level(logging.INFO):
        lambda_handler("thing1", "thing2")
        assert "The specified bucket does not exist" in caplog.text


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("Error: ClientError - for secretsmanager")
@mock_aws
def test_client_error_secrets(caplog, create_bucket1, create_object, aws_secrets):
    with caplog.at_level(logging.INFO):
        lambda_handler("thing1", "thing2")
        assert "Secrets Manager can't find the specified secret." in caplog.text


# may not be needed as no key found handled different way
# @pytest.mark.describe("lambda_handler")
# @pytest.mark.it("Error: KeyError - for bucket object")
# @mock_aws
# def test_key_error(caplog,create_bucket1, secretmanager):
#     with caplog.at_level(logging.INFO):
#         lambda_handler("thing1", "thing2")
#         assert "KeyError: 'Contents'" in caplog.text


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("Error: DatabaseError")
@patch("src.extract.lambda_handler.check_for_changes", side_effect=DatabaseError())
@mock_aws
def test_database_error(
    mock_check_changes, mock_conn, caplog, create_bucket1, create_object, secretmanager
):
    with caplog.at_level(logging.INFO):
        lambda_handler("thing1", "thing2")
        assert "DatabaseError" in caplog.text

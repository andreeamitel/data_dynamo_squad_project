from src.load.lambda_handler import lambda_handler
import logging
import pytest
import boto3
from moto import mock_aws
from unittest.mock import patch
from pg8000.native import DatabaseError

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
        Bucket="processed-bucket",
        CreateBucketConfiguration={"LocationConstraint": "eu-west-2"},
    )


@pytest.fixture
def create_parquet_file(create_bucket1):
    s3 = boto3.client("s3")
    s3.upload_file(
        "test/load/2024-02-27T17_46_46.226025.parquet",
        "processed-bucket",
        "dim_address/2022-02-14 16:54:36.774180.parquet",
    )


@pytest.fixture
def create_last_processed_file(create_bucket1):
    s3 = boto3.client("s3")
    s3.upload_file(
        "./test/load/Last_Processed.txt",
        "processed-bucket",
        "Last_Processed.txt",
    )

    s3.upload_file(
        "test/load/dim_address_copy/2024-02-27T15_35_57.764941.parquet",
        "processed-bucket",
        "dim_null/2024-02-25T14_01_42.316404.parquet",
    )


@pytest.fixture
def secretmanager(aws_secrets):
    aws_secrets.create_secret(
        Name="load_database_creds",
        SecretString='{"hostname":"example_host.com","port": "4321", "database" : "example_database", "username": "project_team_0", "password":"EXAMPLE-PASSWORD", "schema": "test"}',
    )

@pytest.fixture
def mock_conn():
    with patch("src.load.lambda_handler.pg8000.connect") as conn:
        yield conn

event = {
    "Records": [
        {
            "s3": {
                "bucket": {
                    "name": "processed-bucket",
                },
                "object": {
                    "key": "Last_Processed.txt",
                },
            },
        }
    ]
}


@pytest.mark.describe("lambda_handler")
@pytest.mark.it(
    "Test that a connection has been established to a database - using secretsmanager"
)
@mock_aws
@patch("src.load.lambda_handler.wr.postgresql.to_sql")
def test_database_conn(
    mock_to_sql,
    mock_conn,
    create_bucket1,
    secretmanager,
    create_parquet_file,
    create_last_processed_file,
):
    lambda_handler(event, "thing2")
    mock_conn.assert_called_with(
        host="example_host.com",
        port="4321",
        database="example_database",
        user="project_team_0",
        password="EXAMPLE-PASSWORD",
    )


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("should read one file")
@patch("src.load.lambda_handler.wr.postgresql.to_sql")
def test_read_one_file(
    mock_to_sql,
    secretmanager,
    create_parquet_file,
    create_last_processed_file,
    mock_conn,
    caplog,
):
    
    with caplog.at_level(logging.INFO):
        lambda_handler(event, "context")
        expected = "Successfully inserted 489 rows into dim_address"
        assert expected in caplog.text


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("should read one file")
@patch("src.load.lambda_handler.wr.postgresql.to_sql")
def test_ignore_timestamp(
    mock_to_sql,
    secretmanager,
    create_parquet_file,
    create_last_processed_file,
    mock_conn,
    caplog,
):
    with caplog.at_level(logging.INFO):
        lambda_handler(event, "thing2")
        expected = "Successfully inserted 3 rows into dim_address_copy table."
        assert expected not in caplog.text


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("should read one file")
@patch("src.load.lambda_handler.wr.postgresql.to_sql")
def test_client_error(
    mock_to_sql, create_parquet_file, create_last_processed_file, mock_conn, caplog
):
    with caplog.at_level(logging.INFO):
        lambda_handler(event, "thing2")
        expected = "ClientError: ResourceNotFoundException: Secrets Manager can't find the specified secret."
        assert expected in caplog.text


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("should read one file")
@patch("src.load.lambda_handler.wr.postgresql.to_sql")
@patch("src.load.lambda_handler.pg8000.connect")
def test_ignore_timestamp_database_error(
    mock_to_sql,
    mock_fail_conn,
    secretmanager,
    create_parquet_file,
    create_last_processed_file,
    caplog,
):
    mock_fail_conn.side_effect = DatabaseError()
    
    with caplog.at_level(logging.INFO):
        lambda_handler(event, "thing2")
        expected = "DatabaseError"
        assert expected in caplog.text


@pytest.mark.it("should read one file")
@patch("src.load.lambda_handler.wr.postgresql.to_sql")
def test_ignore_timestamp_sql_error(
    mock_to_sql,
    mock_conn,
    secretmanager,
    create_parquet_file,
    create_last_processed_file,
    caplog,
):
    mock_to_sql.side_effect = Exception(
        {
            "S": "ERROR",
            "V": "ERROR",
            "C": "22P02",
            "M": 'invalid input syntax for type integer: "2.43"',
            "F": "numutils.c",
            "L": "323",
            "R": "pg_strtoint32",
        }
    )
    with caplog.at_level(logging.INFO):
        lambda_handler(event, "thing2")
        expected = "invalid input"
        assert expected in caplog.text

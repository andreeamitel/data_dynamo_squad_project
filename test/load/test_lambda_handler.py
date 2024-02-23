from src.load.lambda_handler import lambda_handler
from src.transform.python_to_parquet import python_to_parquet
import pytest
import boto3
from moto import mock_aws
from unittest.mock import patch, Mock
import json
import pandas as pd
import pprint
import awswrangler as wr


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
        Bucket="processed-bucket-20240222143124212400000004",
        CreateBucketConfiguration={"LocationConstraint": "eu-west-2"},
    )


@pytest.fixture
def create_parquet_file(create_bucket1):
    with open("./test/load/sales_order.json", "r") as f:
        file = json.load(f)
        python_to_parquet(
            file,
            "processed-bucket-20240222143124212400000004",
            "2022-02-14 16:54:36.774180",
        )

@pytest.fixture
def mock_conn():
    with patch("src.load.lambda_handler.Connection") as conn:
        yield conn

@pytest.mark.describe("lambda_handler")
@pytest.mark.it("should read one file")
def test_read_one_file(create_parquet_file):
    lambda_handler('event', 'context')
    # print(isinstance(create_parquet_file, pd.DataFrame))
    
    




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
from sqlalchemy import Numeric
from decimal import Decimal,getcontext
json_with_datatypes =  {"sales_order": [
        {
            "sales_order_id": 1,
            "created_at": "2022-11-03T14:20:52.186",
            "last_updated": "2022-11-03T14:20:52.186",
            "design_id": 9,
            "staff_id": 16,
            "counterparty_id": 18,
            "units_sold": 84754,
            "unit_price":  Decimal(2.43),
            "currency_id": 3,
            "agreed_delivery_date": "2022-11-10",
            "agreed_payment_date": "2022-11-03",
            "agreed_delivery_location_id": 4,
        },
        {
            "sales_order_id": 2,
            "created_at": "2022-11-03T14:20:52.186",
            "last_updated": "2022-11-03T14:20:52.186",
            "design_id": 3,
            "staff_id": 19,
            "counterparty_id": 8,
            "units_sold": 42972,
            "unit_price": Decimal(2.43),
            "currency_id": 2,
            "agreed_delivery_date": "2022-11-07",
            "agreed_payment_date": "2022-11-08",
            "agreed_delivery_location_id": 8,
        },
        {
            "sales_order_id": 3,
            "created_at": "2022-11-03T14:20:52.188",
            "last_updated": "2022-11-03T14:20:52.188",
            "design_id": 4,
            "staff_id": 10,
            "counterparty_id": 4,
            "units_sold": 65839,
            "unit_price": Decimal(2.43),
            "currency_id": 3,
            "agreed_delivery_date": "2022-11-06",
            "agreed_payment_date": "2022-11-07",
            "agreed_delivery_location_id": 19,
        },
    ]
}

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
<<<<<<< HEAD
    lambda_handler("event", "context")
    # print(isinstance(create_parquet_file, pd.DataFrame))
=======
    lambda_handler('event', 'context')
   
    
    



>>>>>>> main

from src.transform.lambda_handler import lambda_handler
import pytest
from unittest.mock import patch, call
import boto3
from moto import mock_aws
from datetime import datetime
import logging
from pprint import pprint


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
        Bucket="ingested-bucket-20240222080432331400000006",
        CreateBucketConfiguration={"LocationConstraint": "eu-west-2"},
    )


@pytest.fixture
def create_bucket2(aws_s3):
    boto3.client("s3").create_bucket(
        Bucket="processed_bucket123",
        CreateBucketConfiguration={"LocationConstraint": "eu-west-2"},
    )


@pytest.fixture
def create_object(create_bucket1):
    date_time = "2024-02-22T15:41:59.776283"
    print(date_time)
    boto3.client("s3").put_object(
        Body=f"{date_time}",
        Bucket="ingested-bucket-20240222080432331400000006",
        Key="Last_Ingested.txt",
    )


@pytest.fixture
def secretmanager(aws_secrets):
    aws_secrets.create_secret(
        Name="processed_bucket", SecretString="processed_bucket123"
    )


test_event = {
    "Records": [
        {
            "eventVersion": "2.2",
            "eventSource": "aws:s3",
            "awsRegion": "us-west-2",
            "eventTime": "The time, in ISO-8601 format, for example, 1970-01-01T00:00:00.000Z, when Amazon S3 finished processing the request",
            "eventName": "event-type",
            "userIdentity": {
                "principalId": "Amazon-customer-ID-of-the-user-who-caused-the-event"
            },
            "requestParameters": {
                "sourceIPAddress": "ip-address-where-request-came-from"
            },
            "responseElements": {
                "x-amz-request-id": "Amazon S3 generated request ID",
                "x-amz-id-2": "Amazon S3 host that processed the request",
            },
            "s3": {
                "s3SchemaVersion": "1.0",
                "configurationId": "ID found in the bucket notification configuration",
                "bucket": {
                    "name": "ingested-bucket-20240222080432331400000006",
                    "ownerIdentity": {
                        "principalId": "Amazon-customer-ID-of-the-bucket-owner"
                    },
                    "arn": "bucket-ARN",
                },
                "object": {
                    "key": "Last_Ingested.txt",
                    "size": "object-size in bytes",
                    "eTag": "object eTag",
                    "versionId": "object version if bucket is versioning-enabled, otherwise null",
                    "sequencer": "a string representation of a hexadecimal value used to determine event sequence, only used with PUTs and DELETEs",
                },
            },
            "glacierEventData": {
                "restoreEventData": {
                    "lifecycleRestorationExpiryTime": "The time, in ISO-8601 format, for example, 1970-01-01T00:00:00.000Z, of Restore Expiry",
                    "lifecycleRestoreStorageClass": "Source storage class for restore",
                }
            },
        }
    ]
}

test_context = 2


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("should test that the get_latest_data is called")
@patch("src.transform.lambda_handler.get_latest_data", return_value={})
def test_get_latest_data(
    mock_get_latest_data, create_bucket1, create_bucket2, create_object, secretmanager
):
    lambda_handler(test_event, test_context)
    mock_get_latest_data.assert_called_once()


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("test that dim_currency gets called with correct values")
@patch(
    "src.transform.lambda_handler.get_latest_data",
    return_value={
        "currency": {
            "currency": [
                {
                    "currency_id": 1,
                    "currency_code": "GBP",
                    "created_at": "2022-11-03T14:20:49.962",
                    "last_updated": "2022-11-03T14:20:49.962",
                },
                {
                    "currency_id": 2,
                    "currency_code": "USD",
                    "created_at": "2022-11-03T14:20:49.962",
                    "last_updated": "2022-11-03T14:20:49.962",
                },
            ]
        }
    },
)
@patch("src.transform.lambda_handler.dim_currency")
@patch("src.transform.lambda_handler.python_to_parquet")
@mock_aws
def test_dim_currency(
    mock_python_to_parquet,
    mock_dim_currency,
    mock_get_latest_data,
    create_bucket1,
    create_bucket2,
    create_object,
    secretmanager,
):
    lambda_handler(test_event, test_context)
    mock_dim_currency.assert_called_once_with(
        mock_get_latest_data.return_value["currency"]
    )


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("test that dim_counterparty gets called with correct values")
@patch(
    "src.transform.lambda_handler.get_latest_data",
    return_value={
        "counterparty": {
            "counterparty": [
                {
                    "counterparty_id": 1,
                    "counterparty_legal_name": "Orcs",
                    "legal_address_id": 1,
                    "commercial_contact": "devil",
                    "delivery_contact": "angel",
                    "created_at": datetime(2022, 11, 3, 15, 20, 49, 962000),
                    "last_updated": datetime(2022, 11, 3, 15, 20, 49, 962000),
                }
            ]
        },
        "address": {
            "address": [
                {
                    "address_id": 1,
                    "address_line_1": "64 zoo lane",
                    "address_line_2": "Mount Doom",
                    "district": "Mordor",
                    "city": "chicago",
                    "postal_code": "dhu483",
                    "country": "MiddleEarth",
                    "phone": "73837483",
                    "created_at": datetime(2022, 11, 3, 15, 20, 49, 962000),
                    "last_updated": datetime(2022, 11, 3, 15, 20, 49, 962000),
                }
            ]
        },
    },
)
@patch("src.transform.lambda_handler.python_to_parquet")
@patch("src.transform.lambda_handler.dim_counterparty")
# @patch("src.tranform.lambda_handler.dim_location")
@mock_aws
def test_dim_counterparty(
    mock_dim_counterparty,
    mock_python_to_parquet,
    mock_get_latest_data,
    create_bucket1,
    create_bucket2,
    create_object,
    secretmanager,
):
    lambda_handler(test_event, test_context)
    mock_dim_counterparty.assert_called_once_with(
        mock_get_latest_data.return_value["counterparty"],
        mock_get_latest_data.return_value["address"],
    )


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("test that python gets called with correct variables for fact sales")
@patch(
    "src.transform.lambda_handler.get_latest_data",
    return_value={
        "sales_order": {
            "sales_order": [
                {
                    "sales_order_id": 1,
                    "created_at": "2022-11-03T14:20:52.186",
                    "last_updated": "2022-11-03T14:20:52.186",
                    "design_id": 9,
                    "staff_id": 16,
                    "counterparty_id": 18,
                    "units_sold": 84754,
                    "unit_price": 2.43,
                    "currency_id": 3,
                    "agreed_delivery_date": "2022-11-10",
                    "agreed_payment_date": "2022-11-03",
                    "agreed_delivery_location_id": 4,
                }
            ]
        }
    },
)
@patch("src.transform.lambda_handler.python_to_parquet")
@patch(
    "src.transform.lambda_handler.fact_sales_order",
    return_value=(
        {
            "fact_sales": {
                "sales_order": [
                    {
                        "sales_record_id": 1,
                        "sales_order_id": 1,
                        "created_date": "2022-11-03",
                        "created_time": "14:20:52.186",
                        "last_updated_date": "2022-11-03",
                        "last_updated_time": "14:20:52.186",
                        "design_id": 9,
                        "sales_staff_id": 16,
                        "counterparty_id": 18,
                        "units_sold": 84754,
                        "unit_price": 2.43,
                        "currency_id": 3,
                        "agreed_delivery_date": "2022-11-10",
                        "agreed_payment_date": "2022-11-03",
                        "agreed_delivery_location_id": 4,
                    }
                ]
            }
        },
        {
            "dim_date": [
                {
                    "date_id": "2022-11-03",
                    "year": 2022,
                    "month": 11,
                    "day": 3,
                    "day_of_week": 4,
                    "day_name": "Thursday",
                    "month_name": "November",
                    "quarter": 4,
                }
            ]
        },
    ),
)
@patch("src.transform.lambda_handler.datetime")
@mock_aws
def test_fact_sales_parquet(
    mock_date,
    mock_fact_sales,
    mock_python_to_parquet,
    mock_get_latest_data,
    create_bucket1,
    create_bucket2,
    create_object,
    secretmanager,
):
    mock_date.now().isoformat.return_value = "2024-02-22T16:41:59.776283"
    lambda_handler(test_event, test_context)
    fact_sales, dim_dates = mock_fact_sales.return_value
    mock_python_to_parquet.assert_called_with(
        dim_dates, "processed_bucket123", "2024-02-22T16:41:59.776283"
    )


@pytest.mark.describe("lambda_handler")
@pytest.mark.it(
    "Test that the last processed timestamp gets put in processed bucket in txt format"
)
@mock_aws
@patch("src.transform.lambda_handler.datetime")
@patch("src.transform.lambda_handler.get_latest_data", return_value={})
def test_last_processed_timestamp(
    get_latest_data,
    mock_date,
    create_bucket1,
    create_bucket2,
    secretmanager,
    create_object,
):
    mock_date.now().isoformat.return_value = "2024-02-22T16:41:59.776283"
    s3 = boto3.client("s3")
    lambda_handler(test_event, test_context)
    response = s3.get_object(Bucket="processed_bucket123", Key="Last_Processed.txt")
    time = response["Body"].read().decode("utf8")
    assert time == "2024-02-22T16:41:59.776283"


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("Error: ClientError - for bucket")
@mock_aws
def test_client_error_bucket(caplog, secretmanager):
    with caplog.at_level(logging.INFO):
        lambda_handler(test_event, test_context)
        assert "The specified bucket does not exist" in caplog.text

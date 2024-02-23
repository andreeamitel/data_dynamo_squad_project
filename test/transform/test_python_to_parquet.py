from src.transform.python_to_parquet import python_to_parquet
from moto import mock_aws
import boto3
import pytest
import awswrangler as wr


@pytest.mark.describe("python_to_parquet")
@pytest.mark.it("create parquet file in s3")
@mock_aws
def test_creates_parquet():
    s3 = boto3.client("s3")
    s3.create_bucket(
        Bucket="processed-test-bucket",
        CreateBucketConfiguration={"LocationConstraint": "eu-west-2"},
    )
    dim_counterparty_data = {
        "dim_counterparty": [
            {
                "counterparty_id": 1,
                "counterparty_legal_name": "Orcs",
                "counterparty_legal_address_line_1": "64 zoo lane",
                "counterparty_legal_address_line_2": "Mount Doom",
                "counter_legal_district": "Mordor",
                "counter_party_legal_city": "chicago",
                "counterparty_legal_postal_code": "dhu483",
                "counterparty_legal-country": "MiddleEarth",
                "counterparty_legal_phone_number": "73837483",
            }
        ]
    }
    python_to_parquet(dim_counterparty_data, "processed-test-bucket", "test-folder")
    result = s3.list_objects(Bucket="processed-test-bucket")
    key = result["Contents"][0]["Key"]
    assert key == "dim_counterparty/test-folder.parquet"


@pytest.mark.describe("python_to_parquet")
@pytest.mark.it("check new parquet file in s3")
@mock_aws
def test_check_parquet():
    s3 = boto3.client("s3")
    s3.create_bucket(
        Bucket="processed-test-bucket",
        CreateBucketConfiguration={"LocationConstraint": "eu-west-2"},
    )
    dim_counterparty_data = {
        "dim_counterparty": [
            {
                "counterparty_id": 1,
                "counterparty_legal_name": "Orcs",
                "counterparty_legal_address_line_1": "64 zoo lane",
                "counterparty_legal_address_line_2": "Mount Doom",
                "counter_legal_district": "Mordor",
                "counter_party_legal_city": "chicago",
                "counterparty_legal_postal_code": "dhu483",
                "counterparty_legal-country": "MiddleEarth",
                "counterparty_legal_phone_number": "73837483",
            }
        ]
    }
    python_to_parquet(dim_counterparty_data, "processed-test-bucket", "test-folder")
    result = s3.get_object(
        Bucket="processed-test-bucket", Key="dim_counterparty/test-folder.parquet"
    )
    result = wr.s3.read_parquet(
        "s3://processed-test-bucket/dim_counterparty/test-folder.parquet"
    )

    assert result.to_dict("records") == dim_counterparty_data["dim_counterparty"]

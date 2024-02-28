"""Tests the function get_latest_data."""
import pytest
import boto3
from moto import mock_aws
from src.transform.get_latest_data import get_latest_data


@pytest.mark.describe("get latest data")
@pytest.mark.it("function returns dict")
@mock_aws
def test_returns_dict():
    s3 = boto3.client("s3", region_name="eu-west-2")
    s3.create_bucket(
        Bucket="ingested-bucket",
        CreateBucketConfiguration={"LocationConstraint": "eu-west-2"},
    )
    s3.put_object(
        Body='{"sales_order": [{"sales_order_id": 6922, "created_at": "2024-02-22T10:12:10.155", "last_updated": "2024-02-22T10:12:10.155", "design_id": 316, "staff_id": 13, "counterparty_id": 11, "units_sold": 70190, "unit_price": 3.32, "currency_id": 1, "agreed_delivery_date": "2024-02-26", "agreed_payment_date": "2024-02-23", "agreed_delivery_location_id": 22}]}',
        Bucket="ingested-bucket",
        Key="sales_order/2024-02-14 16:54:36.774180.json",
    )
    s3.put_object(
        Body='{"sales_order": [{"sales_order_id": 6922, "created_at": "2024-02-22T10:12:10.155", "last_updated": "2024-02-14T16:55:36.774180", "design_id": 316, "staff_id": 13, "counterparty_id": 11, "units_sold": 70190, "unit_price": 3.32, "currency_id": 1, "agreed_delivery_date": "2024-02-26", "agreed_payment_date": "2024-02-23", "agreed_delivery_location_id": 22}]}',
        Bucket="ingested-bucket",
        Key="sales_order/2024-02-14 16:55:36.774180.json",
    )
    last_updated_time = "2024-02-14 16:55:36.774180"
    result = get_latest_data("ingested-bucket", s3, last_updated_time)
    assert isinstance(result, dict)


@pytest.mark.describe("get latest data")
@pytest.mark.it(
    "function returns dict with updated data for one table and correct key"
)
@mock_aws
def test_returns_updated_data_for_one_table():
    s3 = boto3.client("s3", region_name="eu-west-2")
    s3.create_bucket(
        Bucket="ingested-bucket",
        CreateBucketConfiguration={"LocationConstraint": "eu-west-2"},
    )
    s3.put_object(
        Body='{"sales_order": [{"sales_order_id": 6922, "created_at": "2024-02-22T10:12:10.155", "last_updated": "2024-02-22T10:12:10.155", "design_id": 316, "staff_id": 13, "counterparty_id": 11, "units_sold": 70190, "unit_price": 3.32, "currency_id": 1, "agreed_delivery_date": "2024-02-26", "agreed_payment_date": "2024-02-23", "agreed_delivery_location_id": 22}]}',
        Bucket="ingested-bucket",
        Key="sales/2024-02-14 16:54:36.774180.json",
    )
    s3.put_object(
        Body='{"sales_order": [{"sales_order_id": 6922, "created_at": "2024-02-22T10:12:10.155", "last_updated": "2024-02-14T16:55:36.774180", "design_id": 316, "staff_id": 13, "counterparty_id": 11, "units_sold": 70190, "unit_price": 3.32, "currency_id": 1, "agreed_delivery_date": "2024-02-26", "agreed_payment_date": "2024-02-23", "agreed_delivery_location_id": 22}]}',
        Bucket="ingested-bucket",
        Key="sales_order/2024-02-14 16:55:36.774180.json",
    )
    last_updated_time = "2024-02-14 16:55:36.774180"
    result = get_latest_data("ingested-bucket", s3, last_updated_time)
    assert list(result.keys())[0] == "sales_order"
    assert result["sales_order"].to_dict() == {
        "sales_order_id": {0: 6922},
        "created_at": {0: "2024-02-22T10:12:10.155"},
        "last_updated": {0: "2024-02-14T16:55:36.774180"},
        "design_id": {0: 316},
        "staff_id": {0: 13},
        "counterparty_id": {0: 11},
        "units_sold": {0: 70190},
        "unit_price": {0: 3.32},
        "currency_id": {0: 1},
        "agreed_delivery_date": {0: "2024-02-26"},
        "agreed_payment_date": {0: "2024-02-23"},
        "agreed_delivery_location_id": {0: 22},
    }


@pytest.mark.describe("get latest data")
@pytest.mark.it(
    "function returns dict with updated data for more than one table and keys are correct"
)
@mock_aws
def test_returns_updated_data_for_more_than_one_table():
    s3 = boto3.client("s3", region_name="eu-west-2")
    s3.create_bucket(
        Bucket="ingested-bucket",
        CreateBucketConfiguration={"LocationConstraint": "eu-west-2"},
    )
    s3.put_object(
        Body='"design_id": 316, "staff_id": 13, "counterparty_id": 11, "units_sold": 70190, "unit_price": 3.32, "currency_id": 1, "agreed_delivery_date": "2024-02-26", "agreed_payment_date": "2024-02-23", "agreed_delivery_location_id": 22}]}',
        Bucket="ingested-bucket",
        Key="sales/2024-02-14 16:54:36.774180.json",
    )
    s3.put_object(
        Body='{"sales_order": [{"sales_order_id": 6922, "created_at": "2024-02-22T10:12:10.155", "last_updated": "2024-02-14T16:55:36.774180", "design_id": 316, "staff_id": 13, "counterparty_id": 11, "units_sold": 70190, "unit_price": 3.32, "currency_id": 1, "agreed_delivery_date": "2024-02-26", "agreed_payment_date": "2024-02-23", "agreed_delivery_location_id": 22}]}',
        Bucket="ingested-bucket",
        Key="sales_order/2024-02-14 16:55:36.774180.json",
    )
    s3.put_object(
        Body=' "department_name": "Sales", "location": "Manchester", "manager": "Richard Roma", "created_at": "2022-11-03T14:20:49.962", "last_updated": "2022-11-03T14:20:49.962"}, {"department_id": 2, "department_name": "Purchasing", "location": "Manchester", "manager": "Naomi Lapaglia", "created_at": "2022-11-03T14:20:49.962", "last_updated": "2022-11-03T14:20:49.962"}, {"department_id": 3, "department_name": "Production", "location": "Leeds", "manager": "Chester Ming", "created_at": "2022-11-03T14:20:49.962", "last_updated": "2022-11-03T14:20:49.962"}, {"department_id": 4, "department_name": "Dispatch", "location": "Leds", "manager": "Mark Hanna", "created_at": "2022-11-03T14:20:49.962", "last_updated": "2022-11-03T14:20:49.962"}, {"department_id": 5, "department_name": "Finance", "location": "Manchester", "manager": "Jordan Belfort", "created_at": "2022-11-03T14:20:49.962", "last_updated": "2022-11-03T14:20:49.962"}, {"department_id": 6, "department_name": "Facilities", "location": "Manchester", "manager": "Shelley Levene", "created_at": "2022-11-03T14:20:49.962", "last_updated": "2022-11-03T14:20:49.962"}, {"department_id": 7, "department_name": "Communications", "location": "Leeds", "manager": "Ann Blake", "created_at": "2022-11-03T14:20:49.962", "last_updated": "2022-11-03T14:20:49.962"}, {"department_id": 8, "department_name": "HR", "location": "Leeds", "manager": "James Link", "created_at": "2022-11-03T14:20:49.962", "last_updated": "2022-11-03T14:20:49.962"}]}',
        Bucket="ingested-bucket",
        Key="department/2024-02-14 16:54:36.774180.json",
    )
    s3.put_object(
        Body='{"department": [{"department_id": 1, "department_name": "Sales", "location": "Manchester", "manager": "Richard Roma", "created_at": "2022-11-03T14:20:49.962", "last_updated": "2022-11-03T14:20:49.962"}, {"department_id": 2, "department_name": "Purchasing", "location": "Manchester", "manager": "Naomi Lapaglia", "created_at": "2022-11-03T14:20:49.962", "last_updated": "2022-11-03T14:20:49.962"}, {"department_id": 3, "department_name": "Production", "location": "Leeds", "manager": "Chester Ming", "created_at": "2022-11-03T14:20:49.962", "last_updated": "2022-11-03T14:20:49.962"}, {"department_id": 4, "department_name": "Dispatch", "location": "Leds", "manager": "Mark Hanna", "created_at": "2022-11-03T14:20:49.962", "last_updated": "2022-11-03T14:20:49.962"}, {"department_id": 5, "department_name": "Finance", "location": "Manchester", "manager": "Jordan Belfort", "created_at": "2022-11-03T14:20:49.962", "last_updated": "2022-11-03T14:20:49.962"}, {"department_id": 6, "department_name": "Facilities", "location": "Manchester", "manager": "Shelley Levene", "created_at": "2022-11-03T14:20:49.962", "last_updated": "2022-11-03T14:20:49.962"}, {"department_id": 7, "department_name": "Communications", "location": "Leeds", "manager": "Ann Blake", "created_at": "2022-11-03T14:20:49.962", "last_updated": "2022-11-03T14:20:49.962"}, {"department_id": 8, "department_name": "HR", "location": "Leeds", "manager": "James Link", "created_at": "2022-11-03T14:20:49.962", "last_updated": "2022-11-03T14:20:49.962"}]}',
        Bucket="ingested-bucket",
        Key="department/2024-02-14 16:55:36.774180.json",
    )
    last_updated_time = "2024-02-14 16:55:36.774180"
    result = get_latest_data("ingested-bucket", s3, last_updated_time)
    assert list(result.keys()) == ["department", "sales_order"]
    assert result["department"].to_dict() == {
        "department_id": {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8},
        "department_name": {
            0: "Sales",
            1: "Purchasing",
            2: "Production",
            3: "Dispatch",
            4: "Finance",
            5: "Facilities",
            6: "Communications",
            7: "HR",
        },
        "location": {
            0: "Manchester",
            1: "Manchester",
            2: "Leeds",
            3: "Leds",
            4: "Manchester",
            5: "Manchester",
            6: "Leeds",
            7: "Leeds",
        },
        "manager": {
            0: "Richard Roma",
            1: "Naomi Lapaglia",
            2: "Chester Ming",
            3: "Mark Hanna",
            4: "Jordan Belfort",
            5: "Shelley Levene",
            6: "Ann Blake",
            7: "James Link",
        },
        "created_at": {
            0: "2022-11-03T14:20:49.962",
            1: "2022-11-03T14:20:49.962",
            2: "2022-11-03T14:20:49.962",
            3: "2022-11-03T14:20:49.962",
            4: "2022-11-03T14:20:49.962",
            5: "2022-11-03T14:20:49.962",
            6: "2022-11-03T14:20:49.962",
            7: "2022-11-03T14:20:49.962",
        },
        "last_updated": {
            0: "2022-11-03T14:20:49.962",
            1: "2022-11-03T14:20:49.962",
            2: "2022-11-03T14:20:49.962",
            3: "2022-11-03T14:20:49.962",
            4: "2022-11-03T14:20:49.962",
            5: "2022-11-03T14:20:49.962",
            6: "2022-11-03T14:20:49.962",
            7: "2022-11-03T14:20:49.962",
        },
    }
    assert result["sales_order"].to_dict() == {
        "sales_order_id": {0: 6922},
        "created_at": {0: "2024-02-22T10:12:10.155"},
        "last_updated": {0: "2024-02-14T16:55:36.774180"},
        "design_id": {0: 316},
        "staff_id": {0: 13},
        "counterparty_id": {0: 11},
        "units_sold": {0: 70190},
        "unit_price": {0: 3.32},
        "currency_id": {0: 1},
        "agreed_delivery_date": {0: "2024-02-26"},
        "agreed_payment_date": {0: "2024-02-23"},
        "agreed_delivery_location_id": {0: 22},
    }

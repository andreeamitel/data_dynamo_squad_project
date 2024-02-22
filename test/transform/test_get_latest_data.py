from src.transform.get_latest_data import get_latest_data
import pytest
from moto import mock_aws 
import boto3
from pprint import pprint


@pytest.mark.describe("get latest data")
@pytest.mark.it("function returns dictionary")
@mock_aws
def test_returns_dict():
    s3 = boto3.client("s3", region_name="eu-west-2")
    s3.create_bucket(Bucket = "ingested-bucket",
    CreateBucketConfiguration = {
        'LocationConstraint': 'eu-west-2'
    })
    s3.put_object(Body = '{"sales_order": [{"sales_order_id": 6922, "created_at": "2024-02-22T10:12:10.155", "last_updated": "2024-02-22T10:12:10.155", "design_id": 316, "staff_id": 13, "counterparty_id": 11, "units_sold": 70190, "unit_price": 3.32, "currency_id": 1, "agreed_delivery_date": "2024-02-26", "agreed_payment_date": "2024-02-23", "agreed_delivery_location_id": 22}]}', Bucket='ingested-bucket', Key='sales_order/2024-02-14 16:54:36.774180')
    s3.put_object(Body = '{"sales_order": [{"sales_order_id": 6922, "created_at": "2024-02-22T10:12:10.155", "last_updated": "2024-02-14T16:55:36.774180", "design_id": 316, "staff_id": 13, "counterparty_id": 11, "units_sold": 70190, "unit_price": 3.32, "currency_id": 1, "agreed_delivery_date": "2024-02-26", "agreed_payment_date": "2024-02-23", "agreed_delivery_location_id": 22}]}', Bucket='ingested-bucket', Key='sales_order/2024-02-14 16:55:36.774180')
    last_updated_time = "2024-02-14 16:55:36.774180"
    result = get_latest_data(last_updated_time, s3, "ingested-bucket")
    assert type(result) == dict

@pytest.mark.describe("get latest data")
@pytest.mark.it("function returns list with updated data for one table")
@mock_aws
def test_returns_updated_data_for_one_table():
    s3 = boto3.client("s3", region_name="eu-west-2")
    s3.create_bucket(Bucket = "ingested-bucket",
    CreateBucketConfiguration = {
        'LocationConstraint': 'eu-west-2'
    })
    s3.put_object(Body = '{"sales_order": [{"sales_order_id": 6922, "created_at": "2024-02-22T10:12:10.155", "last_updated": "2024-02-22T10:12:10.155", "design_id": 316, "staff_id": 13, "counterparty_id": 11, "units_sold": 70190, "unit_price": 3.32, "currency_id": 1, "agreed_delivery_date": "2024-02-26", "agreed_payment_date": "2024-02-23", "agreed_delivery_location_id": 22}]}', Bucket='ingested-bucket', Key='sales/2024-02-14 16:54:36.774180')
    s3.put_object(Body = '{"sales_order": [{"sales_order_id": 6922, "created_at": "2024-02-22T10:12:10.155", "last_updated": "2024-02-14T16:55:36.774180", "design_id": 316, "staff_id": 13, "counterparty_id": 11, "units_sold": 70190, "unit_price": 3.32, "currency_id": 1, "agreed_delivery_date": "2024-02-26", "agreed_payment_date": "2024-02-23", "agreed_delivery_location_id": 22}]}', Bucket='ingested-bucket', Key='sales_order/2024-02-14 16:55:36.774180')
    last_updated_time = "2024-02-14 16:55:36.774180"
    result = get_latest_data(last_updated_time, s3, "ingested-bucket")
    assert result == {'sales_order':{"sales_order": [{"sales_order_id": 6922, "created_at": "2024-02-22T10:12:10.155", "last_updated": "2024-02-14T16:55:36.774180", "design_id": 316, "staff_id": 13, "counterparty_id": 11, "units_sold": 70190, "unit_price": 3.32, "currency_id": 1, "agreed_delivery_date": "2024-02-26", "agreed_payment_date": "2024-02-23", "agreed_delivery_location_id": 22}]}}

@pytest.mark.describe("get latest data")
@pytest.mark.it("function returns list with updated data for one table")
@mock_aws
def test_returns_updated_data_for_one_table():
    s3 = boto3.client("s3", region_name="eu-west-2")
    s3.create_bucket(Bucket = "ingested-bucket",
    CreateBucketConfiguration = {
        'LocationConstraint': 'eu-west-2'
    })
    s3.put_object(Body = '{"sales_order": [{"sales_order_id": 6922, "created_at": "2024-02-22T10:12:10.155", "last_updated": "2024-02-22T10:12:10.155", "design_id": 316, "staff_id": 13, "counterparty_id": 11, "units_sold": 70190, "unit_price": 3.32, "currency_id": 1, "agreed_delivery_date": "2024-02-26", "agreed_payment_date": "2024-02-23", "agreed_delivery_location_id": 22}]}', Bucket='ingested-bucket', Key='sales/2024-02-14 16:54:36.774180')
    s3.put_object(Body = '{"sales_order": [{"sales_order_id": 6922, "created_at": "2024-02-22T10:12:10.155", "last_updated": "2024-02-14T16:55:36.774180", "design_id": 316, "staff_id": 13, "counterparty_id": 11, "units_sold": 70190, "unit_price": 3.32, "currency_id": 1, "agreed_delivery_date": "2024-02-26", "agreed_payment_date": "2024-02-23", "agreed_delivery_location_id": 22}]}', Bucket='ingested-bucket', Key='sales_order/2024-02-14 16:55:36.774180')
    last_updated_time = "2024-02-14 16:55:36.774180"
    result = get_latest_data(last_updated_time, s3, "ingested-bucket")
    assert result == {'sales_order':{"sales_order": [{"sales_order_id": 6922, "created_at": "2024-02-22T10:12:10.155", "last_updated": "2024-02-14T16:55:36.774180", "design_id": 316, "staff_id": 13, "counterparty_id": 11, "units_sold": 70190, "unit_price": 3.32, "currency_id": 1, "agreed_delivery_date": "2024-02-26", "agreed_payment_date": "2024-02-23", "agreed_delivery_location_id": 22}]}}
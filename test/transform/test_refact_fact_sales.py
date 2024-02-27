import pandas as pd 
import pytest
from src.transform.fact_sales_order import fact_sales_order
@pytest.mark.describe("fact_sales_order")
@pytest.mark.it("function returns dataframe with correct columns")
def test_returns_correct_columns():
    sales_order_dataframe = {
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
            },
            {
                "sales_order_id": 2,
                "created_at": "2022-11-03T14:20:52.186",
                "last_updated": "2022-11-03T14:20:52.186",
                "design_id": 3,
                "staff_id": 19,
                "counterparty_id": 8,
                "units_sold": 42972,
                "unit_price": 3.94,
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
                "unit_price": 2.91,
                "currency_id": 3,
                "agreed_delivery_date": "2022-11-06",
                "agreed_payment_date": "2022-11-07",
                "agreed_delivery_location_id": 19,
            },
        ]
    }
    df = pd.DataFrame(sales_order_dataframe["sales_order"])
    result = fact_sales_order(df)
    bool_list = [
        column_name in result
        for column_name in [
            "sales_record_id", "sales_order_id", "created_date", "created_time", "last_updated_time", "sales_staff_id", "counterparty_id", "units_sold", "unit_price", "currency_id", "design_id", "agreed_payment_date", "agreed_delivery_date", "agreed_delivery_location_id"
        ]
    ]
    print(result.columns)
    assert all(bool_list)

@pytest.mark.describe("fact_sales_order")
@pytest.mark.it("function returns dataframe with correct values")
def test_returns_correct_values():
    sales_order_dataframe = {
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
            },
            {
                "sales_order_id": 2,
                "created_at": "2022-11-03T14:20:52.186",
                "last_updated": "2022-11-03T14:20:52.186",
                "design_id": 3,
                "staff_id": 19,
                "counterparty_id": 8,
                "units_sold": 42972,
                "unit_price": 3.94,
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
                "unit_price": 2.91,
                "currency_id": 3,
                "agreed_delivery_date": "2022-11-06",
                "agreed_payment_date": "2022-11-07",
                "agreed_delivery_location_id": 19,
            },
        ]
    }
    df = pd.DataFrame(sales_order_dataframe["sales_order"])
    result = fact_sales_order(df)
    print(result.to_dict())

    assert result.to_dict() == {'sales_record_id': {0: 1, 1: 2, 2: 3}, 'sales_order_id': {0: 1, 1: 2, 2: 3}, 'created_date': {0: '2022-11-03', 1: '2022-11-03', 2: '2022-11-03'}, 'created_time': {0: '14:20:52.186', 1: '14:20:52.186', 2: '14:20:52.188'}, 'last_updated_time': {0: '14:20:52.186', 1: '14:20:52.186', 2: '14:20:52.188'}, 'sales_staff_id': {0: 16, 1: 19, 2: 10}, 'counterparty_id': {0: 18, 1: 8, 2: 4}, 'units_sold': {0: 84754, 1: 42972, 2: 65839}, 'unit_price': {0: 2.43, 1: 3.94, 2: 2.91}, 'currency_id': {0: 3, 1: 2, 2: 3}, 'design_id': {0: 9, 1: 3, 2: 4}, 'agreed_payment_date': {0: '2022-11-03', 1: '2022-11-08', 2: '2022-11-07'}, 'agreed_delivery_date': {0: '2022-11-10', 1: '2022-11-07', 2: '2022-11-06'}, 'agreed_delivery_location_id': {0: 4, 1: 8, 2: 19}}

from src.transform.dim_date import dim_date
import pytest
import pandas as pd


@pytest.mark.describe("dim_date")
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
    result = dim_date(df)
    bool_list = [
        column_name in result
        for column_name in [
            "date_id",
            "year",
            "month",
            "day",
            "day_of_week",
            "day_name",
            "month_name",
            "quarter",
        ]
    ]
    assert all(bool_list)


@pytest.mark.describe("dim_date")
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
    result = dim_date(df)

    assert result.to_dict() == {
        "date_id": {
            0: "2022-11-10",
            1: "2022-11-07",
            2: "2022-11-06",
            3: "2022-11-03",
            4: "2022-11-08",
        },
        "year": {0: "2022", 1: "2022", 2: "2022", 3: "2022", 4: "2022"},
        "month": {0: "11", 1: "11", 2: "11", 3: "11", 4: "11"},
        "day": {0: "10", 1: "07", 2: "06", 3: "03", 4: "08"},
        "day_of_week": {0: 4, 1: 1, 2: 7, 3: 4, 4: 2},
        "day_name": {
            0: "Thursday",
            1: "Monday",
            2: "Sunday",
            3: "Thursday",
            4: "Tuesday",
        },
        "month_name": {
            0: "November",
            1: "November",
            2: "November",
            3: "November",
            4: "November",
        },
        "quarter": {0: 4, 1: 4, 2: 4, 3: 4, 4: 4},
    }

'''Tests the function fact_sales_order.'''

import pytest
from src.transform.fact_sales_order import fact_sales_order

test_sales_order = {
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


@pytest.mark.describe("fact_sales_order")
@pytest.mark.it("function returns an empty list if given and empty table_list")
def test_returns_empty_list():
    result_1, result_2 = fact_sales_order({"sales_order": []})
    assert result_1 == {"fact_sales_order": []}
    assert result_2 == {"dim_date": []}


@pytest.mark.describe("fact_sales_order")
@pytest.mark.it(
    "function returns edited staff_id and add sales_record_id - single item"
)
def test_returns_edited_properties_single():
    arg = {
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
        ]
    }
    expected = {
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
    result_1, result_2 = fact_sales_order(arg)
    assert result_1["fact_sales_order"][0] == expected


@pytest.mark.describe("fact_sales_order")
@pytest.mark.it(
    "function returns edited staff_id and add sales_record_id - single item"
)
def test_returns_edited_properties_multiple():
    expected = [
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
        },
        {
            "sales_record_id": 2,
            "sales_order_id": 2,
            "created_date": "2022-11-03",
            "created_time": "14:20:52.186",
            "last_updated_date": "2022-11-03",
            "last_updated_time": "14:20:52.186",
            "design_id": 3,
            "sales_staff_id": 19,
            "counterparty_id": 8,
            "units_sold": 42972,
            "unit_price": 3.94,
            "currency_id": 2,
            "agreed_delivery_date": "2022-11-07",
            "agreed_payment_date": "2022-11-08",
            "agreed_delivery_location_id": 8,
        },
        {
            "sales_record_id": 3,
            "sales_order_id": 3,
            "created_date": "2022-11-03",
            "created_time": "14:20:52.188",
            "last_updated_date": "2022-11-03",
            "last_updated_time": "14:20:52.188",
            "design_id": 4,
            "sales_staff_id": 10,
            "counterparty_id": 4,
            "units_sold": 65839,
            "unit_price": 2.91,
            "currency_id": 3,
            "agreed_delivery_date": "2022-11-06",
            "agreed_payment_date": "2022-11-07",
            "agreed_delivery_location_id": 19,
        },
    ]
    result_1, result_2 = fact_sales_order(test_sales_order)
    assert result_1["fact_sales_order"] == expected


@pytest.mark.describe("fact_sales_order")
@pytest.mark.it("function does not mutate original data")
def test_mutation_test():
    arg = {
        "sales_order": [
            {
                "sales_order_id": 3,
                "created_at": "2020-01-03T14:20:52.188",
                "last_updated": "2022-04-03T14:20:52.188",
                "design_id": 4,
                "staff_id": 10,
                "counterparty_id": 4,
                "units_sold": 65839,
                "unit_price": 2.91,
                "currency_id": 3,
                "agreed_delivery_date": "2022-09-06",
                "agreed_payment_date": "2022-11-07",
                "agreed_delivery_location_id": 19,
            }
        ]
    }
    fact_sales_order(arg)
    assert arg == {
        "sales_order": [
            {
                "sales_order_id": 3,
                "created_at": "2020-01-03T14:20:52.188",
                "last_updated": "2022-04-03T14:20:52.188",
                "design_id": 4,
                "staff_id": 10,
                "counterparty_id": 4,
                "units_sold": 65839,
                "unit_price": 2.91,
                "currency_id": 3,
                "agreed_delivery_date": "2022-09-06",
                "agreed_payment_date": "2022-11-07",
                "agreed_delivery_location_id": 19,
            }
        ]
    }

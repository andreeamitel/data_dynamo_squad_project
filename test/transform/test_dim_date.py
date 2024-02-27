'''Tests the function dim_date.'''

import pytest
from src.transform.dim_date import dim_date

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


@pytest.mark.describe("dim_date")
@pytest.mark.it("function returns an empty list if given and empty table_list")
def test_returns_empty_list():
    result_1, result_2 = dim_date({"sales_order": []})
    assert result_1 == {"sales_order": []}
    assert result_2 == {"dim_date": []}


@pytest.mark.describe("dim_date")
@pytest.mark.it("function returns one item of sales_order table")
def test_returns_one_item_each_tables():
    arg = {"sales_order": [test_sales_order["sales_order"][0]]}
    result = dim_date(arg)[0]["sales_order"]
    expected = [
        {
            "sales_order_id": 1,
            "created_date": "2022-11-03",
            "created_time": "14:20:52.186",
            "last_updated_date": "2022-11-03",
            "last_updated_time": "14:20:52.186",
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
    assert result == expected


@pytest.mark.describe("dim_date")
@pytest.mark.it("function returns items of of sales_order table")
def test_returns_one_items_each_tables():
    result = dim_date(test_sales_order)[0]["sales_order"]
    excepted = [
        {
            "sales_order_id": 1,
            "created_date": "2022-11-03",
            "created_time": "14:20:52.186",
            "last_updated_date": "2022-11-03",
            "last_updated_time": "14:20:52.186",
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
            "created_date": "2022-11-03",
            "created_time": "14:20:52.186",
            "last_updated_date": "2022-11-03",
            "last_updated_time": "14:20:52.186",
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
            "created_date": "2022-11-03",
            "created_time": "14:20:52.188",
            "last_updated_date": "2022-11-03",
            "last_updated_time": "14:20:52.188",
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
    assert result == excepted


@pytest.mark.describe("dim_date")
@pytest.mark.it("function returns one item of dim_date table")
def test_returns_dim_date_schema_single_item():
    arg = {"sales_order": [test_sales_order["sales_order"][2]]}
    result = dim_date(arg)[1]
    excepted = {
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
            },
            {
                "date_id": "2022-11-07",
                "year": 2022,
                "month": 11,
                "day": 7,
                "day_of_week": 1,
                "day_name": "Monday",
                "month_name": "November",
                "quarter": 4,
            },
            {
                "date_id": "2022-11-06",
                "year": 2022,
                "month": 11,
                "day": 6,
                "day_of_week": 7,
                "day_name": "Sunday",
                "month_name": "November",
                "quarter": 4,
            },
        ]
    }
    result_all = [
        dict_result in excepted["dim_date"] for dict_result in result["dim_date"]
    ]
    assert all(result_all)


@pytest.mark.describe("dim_date")
@pytest.mark.it("function returns items of dim_date table")
def test_returns_dim_date_schema_multiple_items():
    arg = {"sales_order": test_sales_order["sales_order"]}
    result = dim_date(arg)[1]
    excepted = {
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
            },
            {
                "date_id": "2022-11-07",
                "year": 2022,
                "month": 11,
                "day": 7,
                "day_of_week": 1,
                "day_name": "Monday",
                "month_name": "November",
                "quarter": 4,
            },
            {
                "date_id": "2022-11-06",
                "year": 2022,
                "month": 11,
                "day": 6,
                "day_of_week": 7,
                "day_name": "Sunday",
                "month_name": "November",
                "quarter": 4,
            },
            {
                "date_id": "2022-11-08",
                "year": 2022,
                "month": 11,
                "day": 8,
                "day_of_week": 2,
                "day_name": "Tuesday",
                "month_name": "November",
                "quarter": 4,
            },
            {
                "date_id": "2022-11-10",
                "year": 2022,
                "month": 11,
                "day": 10,
                "day_of_week": 4,
                "day_name": "Thursday",
                "month_name": "November",
                "quarter": 4,
            },
        ]
    }

    result_all = [
        dict_result in excepted["dim_date"] for dict_result in result["dim_date"]
    ]
    assert all(result_all)


@pytest.mark.describe("dim_date")
@pytest.mark.it("function returns both sales_order and dim_date tables")
def test_returns_both_tables():
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
    sales_order_result, dim_date_result = dim_date(arg)
    dim_date_expected = {
        "dim_date": [
            {
                "date_id": "2020-01-03",
                "year": 2020,
                "month": 1,
                "day": 3,
                "day_of_week": 5,
                "day_name": "Friday",
                "month_name": "January",
                "quarter": 1,
            },
            {
                "date_id": "2022-04-03",
                "year": 2022,
                "month": 4,
                "day": 3,
                "day_of_week": 7,
                "day_name": "Sunday",
                "month_name": "April",
                "quarter": 2,
            },
            {
                "date_id": "2022-11-07",
                "year": 2022,
                "month": 11,
                "day": 7,
                "day_of_week": 1,
                "day_name": "Monday",
                "month_name": "November",
                "quarter": 4,
            },
            {
                "date_id": "2022-09-06",
                "year": 2022,
                "month": 9,
                "day": 6,
                "day_of_week": 2,
                "day_name": "Tuesday",
                "month_name": "September",
                "quarter": 3,
            },
        ]
    }
    sales_order_expected = {
        "sales_order": [
            {
                "sales_order_id": 3,
                "created_date": "2020-01-03",
                "created_time": "14:20:52.188",
                "last_updated_date": "2022-04-03",
                "last_updated_time": "14:20:52.188",
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
    dim_date_result_all = [
        dict_result in dim_date_expected["dim_date"]
        for dict_result in dim_date_result["dim_date"]
    ]
    assert all(dim_date_result_all)
    assert sales_order_result["sales_order"] == sales_order_expected["sales_order"]


@pytest.mark.describe("dim_date")
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
    dim_date(arg)
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

'''Tests the function dim_currency.'''
import pandas as pd
import pytest
from src.transform.dim_currency import dim_currency


@pytest.mark.describe("dim_currency")
@pytest.mark.it("function returns an empty list if given empty table lists")
def test_returns_empty_list_when_given_empty_dict():
    result = dim_currency({})
    assert result == {}


@pytest.mark.describe("dim_currency")
@pytest.mark.it("function returns a dictionary which has corrrect key")
def test_returns_dict_with_correct_key():

    currency_df =  {
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
                {
                    "currency_id": 3,
                    "currency_code": "EUR",
                    "created_at": "2022-11-03T14:20:49.962",
                    "last_updated": "2022-11-03T14:20:49.962",
                },
            ]
        }
    df = pd.DataFrame(currency_df["currency"])
    print(df)
    result = dim_currency(df)
    expected = list(result.keys())[0]
    assert expected == "currency"


@pytest.mark.describe("dim_currency")
@pytest.mark.it("function returns a dictionary which has corrrect values")
def test_returns_dict_with_correct_values():
    result = dim_currency(
        {
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
                {
                    "currency_id": 3,
                    "currency_code": "EUR",
                    "created_at": "2022-11-03T14:20:49.962",
                    "last_updated": "2022-11-03T14:20:49.962",
                },
            ]
        }
    )
    expected = {
        "dim_currency": [
            {
                "currency_id": 1,
                "currency_code": "GBP",
                "currency_name": "Great British Pound",
            },
            {
                "currency_id": 2,
                "currency_code": "USD",
                "currency_name": "United States Dollar",
            },
            {
                "currency_id": 3,
                "currency_code": "EUR",
                "currency_name": "Euro",
            },
        ]
    }
    assert result == expected


@pytest.mark.describe("dim_currency")
@pytest.mark.it("check result is different reference than input")
def test_check_result_has_diff_ref():
    test_input = {
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
            {
                "currency_id": 3,
                "currency_code": "EUR",
                "created_at": "2022-11-03T14:20:49.962",
                "last_updated": "2022-11-03T14:20:49.962",
            },
        ]
    }
    result = dim_currency(test_input)
    assert result is not test_input


@pytest.mark.describe("dim_currency")
@pytest.mark.it("check input has not been changed")
def test_check_input_not_changed():
    test_input = {
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
            {
                "currency_id": 3,
                "currency_code": "EUR",
                "created_at": "2022-11-03T14:20:49.962",
                "last_updated": "2022-11-03T14:20:49.962",
            },
        ]
    }
    dim_currency(test_input)

    assert test_input == {
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
            {
                "currency_id": 3,
                "currency_code": "EUR",
                "created_at": "2022-11-03T14:20:49.962",
                "last_updated": "2022-11-03T14:20:49.962",
            },
        ]
    }


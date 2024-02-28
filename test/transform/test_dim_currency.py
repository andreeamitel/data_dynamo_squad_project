import pandas as pd
import pytest
from src.transform.dim_currency import dim_currency


@pytest.mark.describe("dim_currency")
@pytest.mark.it("function returns a dataframe which has correct columns")
def test_returns_data_frame_with_correct_columns():
    currency_df = {
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
    result = dim_currency(df)
    bool_list = [
        column in result
        for column in [
            "currency_id",
            "currency_code",
            "currency_name",
        ]
    ]
    assert all(bool_list)


@pytest.mark.describe("dim_currency")
@pytest.mark.it("function returns a data frame which has correct values")
def test_returns_data_frame_with_correct_values():
    currency_df = {
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
    result = dim_currency(df)
    assert result.to_dict() == {
        "currency_id": {0: 1, 1: 2, 2: 3},
        "currency_code": {0: "GBP", 1: "USD", 2: "EUR"},
        "currency_name": {
            0: "Great British Pound",
            1: "United States Dollar",
            2: "Euro",
        },
    }


@pytest.mark.describe("dim_currency")
@pytest.mark.it("check result is different reference than input")
def test_check_result_has_diff_ref():
    currency_df = {
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
    result = dim_currency(df)
    assert result is not currency_df


@pytest.mark.describe("dim_currency")
@pytest.mark.it("check input has not been changed")
def test_check_input_not_changed():
    currency_df = {
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
    dim_currency(df)

    assert currency_df == {
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

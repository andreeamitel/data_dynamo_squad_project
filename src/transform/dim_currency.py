import pandas as pd


def dim_currency(currency_df):
    if currency_df == {}:
        return {}
    currency_copy = currency_df.copy(deep=True)
    currency_copy = currency_copy.drop(columns=["created_at", "last_updated"])
    currency_code_name = {
        "GBP": "Great British Pound",
        "USD": "United States Dollar",
        "EUR": "Euro"
    }
    currency_copy["currency_name"] = currency_copy["currency_code"].map(currency_code_name)

    return currency_copy

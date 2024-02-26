import copy
import pandas as pd


def dim_currency(currency_table_data):
    if currency_table_data == {}:
        return {}
    currency_dict = copy.deepcopy(currency_table_data)
    dim_curr = {"dim_currency": []}

    for currency in currency_dict["currency"]:
        if currency["currency_code"] == "GBP":
            currency_name = "Great British Pound"
        elif currency["currency_code"] == "USD":
            currency_name = "United States Dollar"
        elif currency["currency_code"] == "EUR":
            currency_name = "Euro"
        dim_curr["dim_currency"].append(
            {
                "currency_id": currency["currency_id"],
                "currency_code": currency["currency_code"],
                "currency_name": currency_name,
            }
        )

    return dim_curr


def dim_currency_to_dataframe(dim_curr_data):
    dataframe = pd.DataFrame(dim_curr_data["dim_currency"])
    dataframe["currency_id"] = dataframe["currency_id"].astype(int)
    dataframe["currency_code"] = dataframe["currency_code"].astype(str)
    dataframe["currency_name"] = dataframe["currency_name"].astype(str)

    return dataframe

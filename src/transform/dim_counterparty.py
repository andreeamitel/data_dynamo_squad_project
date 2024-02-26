import copy
import pandas as pd
import numpy as np


def dim_counterparty(address_table_data, counterparty_table_data):
    """This function takes a two dictionaries from the counterparty and address tables and returns amended dictionary with key = table name and value list for the dim_counterparty table.
    Args: 'counterparty' and 'address' dictionaries
    Returns: dim_counterparty dictionary
    """
    address_table = copy.deepcopy(address_table_data["address"])
    counterparty_table = copy.deepcopy(counterparty_table_data["counterparty"])
    dim_counterparty_list = []

    for counterparty in counterparty_table:
        for address in address_table:
            if address["address_id"] == counterparty["legal_address_id"]:
                dim_counterparty = {
                    "counterparty_id": counterparty["counterparty_id"],
                    "counterparty_legal_name": counterparty["counterparty_legal_name"],
                    "counterparty_legal_address_line_1": address["address_line_1"],
                    "counterparty_legal_address_line_2": address["address_line_2"],
                    "counterparty_legal_district": address["district"],
                    "counterparty_legal_city": address["city"],
                    "counterparty_legal_postal_code": address["postal_code"],
                    "counterparty_legal_country": address["country"],
                    "counterparty_legal_phone_number": address["phone"],
                }
        dim_counterparty_list.append(dim_counterparty)
    return {"dim_counterparty": dim_counterparty_list}


# def dim_counterparty_to_dataframe(dim_counterparty):
#     dataframe = pd.DataFrame(dim_counterparty["dim_counterparty"])
#     print(dataframe.to_csv())
#     dataframe[["address_id"]] = dataframe[["address_id"]].astype(np.int4)
#     print(dataframe[["address_id"]])

# pass

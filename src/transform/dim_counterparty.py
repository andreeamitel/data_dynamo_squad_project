import copy


def dim_counterparty(address_table_data, counterparty_table_data):
    """This function takes a two lists of dictionaries from the counterparty and address tables and returns amended list of dictionaries for the dim_counterparty table.
    Args: 'counterparty' and 'address' table lists
    Returns: dim_counterparty table list of dict
    """
    address_table = copy.deepcopy(address_table_data)
    counterparty_table = copy.deepcopy(counterparty_table_data)
    dim_counterparty_list = []
    for counterparty, address in zip(counterparty_table, address_table):
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
                "counterparty_legal_phone_number": address["phone"]
            }
            dim_counterparty_list.append(dim_counterparty)
    return dim_counterparty_list

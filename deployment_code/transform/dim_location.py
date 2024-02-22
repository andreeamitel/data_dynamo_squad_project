import copy


def dim_location(address_table_data):
    if address_table_data == {}:
        return {}
    location_dict = copy.deepcopy(address_table_data)
    dim_loca = {"dim_location": []}

    for address in location_dict["address"]:
        dim_loca["dim_location"].append(
            {
                "location_id": address["address_id"],
                "address_line_1": address["address_line_1"],
                "address_line_2": address["address_line_2"],
                "district": address["district"],
                "city": address["city"],
                "postal_code": address["postal_code"],
                "country": address["country"],
                "phone": address["phone"],
            }
        )

    return dim_loca

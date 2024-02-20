from src.transform.dim_counterparty import dim_counterparty_func
from datetime import datetime

# def test_dim_counterparty_func():
#     address_data = [{
#         "address_id": 1, 
#         "address_line_1": "64 zoo lane", 
#         "address_line_2": "Mount Doom", 
#         "district": "Mordor", 
#         "city": "chicago", 
#         "postal_code": "dhu483", 
#         "country": "MiddleEarth", 
#         "phone": "73837483", 
#         "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000), 
#         "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000)
#         }]
#     counterparty_data = [{
#         "counterparty_id": 1, 
#         "counterparty_legal_name": "Orcs", 
#         "legal_address_id": 1, 
#         "commercial_contact": "devil", 
#         "delivery_contact": "angel", 
#         "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000), 
#         "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000)
#         }]
#     result = dim_counterparty_func(address_data, counterparty_data)
#     expected = [{
#     "counterparty_id": 1, 
#     "counterparty_legal_name": "Orcs", 
#     "counterparty_legal_address_line_1": "64 zoo lane",
#     "counterparty_legal_address_line_2": "Mount Doom", 
#     "counter_legal_district": "Mordor", 
#     "counter_party_legal_city": "chicago", 
#     "counterparty_legal_postal_code": "dhu483", 
#     "counterparty_legal-country": "MiddleEarth", 
#     "counterparty_legal_phone_number": "73837483"
#     }]
    #assert result == expected
    # pass
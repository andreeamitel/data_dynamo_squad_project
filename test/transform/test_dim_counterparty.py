from transform.dim_counterparty import dim_counterparty_func

def test_dim_counterparty_func():
    address_data = [{
        "address_id": 1, 
        "address_line_1": "64 zoo lane", 
        "address_line_2": "Mount Doom", 
        "district": "Mordor", 
        "city": "chicago", 
        "postal_code": "dhu483", 
        "country": "MiddleEarth", 
        "phone": "73837483", 
        "created_at": datetime, 
        "last_updated": datetime
        }]
    counterparty_data = [{
        "counterparty_id": 1, 
        "counterparty_legal_name": "Orcs", 
        "legal_address_id": 1, 
        "commercial_contact": "devil", 
        "delivery_contact": "angel", 
        "created_at": datetime, 
        "last_updated": datetime
        }]
    result = dim_counterparty_func(address_data, counterparty_data)
    pass
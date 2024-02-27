'''Tests the function dim_counterparty.'''
import datetime
import pytest
from src.transform.dim_counterparty import dim_counterparty



@pytest.mark.describe("dim_counterparty")
@pytest.mark.it("function returns an empty list if given empty table lists")
def test_returns_empty_list():
    result = dim_counterparty({"address": []}, {"counterparty": []})
    assert result == {"dim_counterparty": []}


@pytest.mark.describe("dim_counterparty")
@pytest.mark.it("function returns a list of dictionaries")
def test_returns_a_list_of_dictionary_type():
    address_data = {
        "address": [
            {
                "address_id": 1,
                "address_line_1": "64 zoo lane",
                "address_line_2": "Mount Doom",
                "district": "Mordor",
                "city": "chicago",
                "postal_code": "dhu483",
                "country": "MiddleEarth",
                "phone": "73837483",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            }
        ]
    }
    counterparty_data = {
        "counterparty": [
            {
                "counterparty_id": 1,
                "counterparty_legal_name": "Orcs",
                "legal_address_id": 1,
                "commercial_contact": "devil",
                "delivery_contact": "angel",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            }
        ]
    }
    result = dim_counterparty(address_data, counterparty_data)
    result1 = type(result)
    result2 = [
        type(returned_data) is dict for returned_data in result["dim_counterparty"]
    ]
    assert result1 is dict
    assert all(result2) is True


@pytest.mark.describe("dim_counterparty")
@pytest.mark.it(
    "function returns a list of one dictionary with the amended column names from the the address and counterparty tables"
)
def test_returns_a_list_of_one_dictionary():
    address_data = {
        "address": [
            {
                "address_id": 1,
                "address_line_1": "64 zoo lane",
                "address_line_2": "Mount Doom",
                "district": "Mordor",
                "city": "chicago",
                "postal_code": "dhu483",
                "country": "MiddleEarth",
                "phone": "73837483",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            }
        ]
    }
    counterparty_data = {
        "counterparty": [
            {
                "counterparty_id": 1,
                "counterparty_legal_name": "Orcs",
                "legal_address_id": 1,
                "commercial_contact": "devil",
                "delivery_contact": "angel",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            }
        ]
    }
    result = dim_counterparty(address_data, counterparty_data)
    expected = {
        "dim_counterparty": [
            {
                "counterparty_id": 1,
                "counterparty_legal_address_line_1": "64 zoo lane",
                "counterparty_legal_address_line_2": "Mount Doom",
                "counterparty_legal_city": "chicago",
                "counterparty_legal_country": "MiddleEarth",
                "counterparty_legal_district": "Mordor",
                "counterparty_legal_name": "Orcs",
                "counterparty_legal_phone_number": "73837483",
                "counterparty_legal_postal_code": "dhu483",
            }
        ]
    }
    assert result == expected


@pytest.mark.describe("dim_counterparty")
@pytest.mark.it(
    "function returns a list of dictionaries with the amended column names from the address and counterparty tables"
)
def test_return_a_list_of_dictionaries():
    address_data = {
        "address": [
            {
                "address_id": 1,
                "address_line_1": "64 zoo lane",
                "address_line_2": "Mount Doom",
                "district": "Mordor",
                "city": "chicago",
                "postal_code": "dhu483",
                "country": "MiddleEarth",
                "phone": "73837483",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            },
            {
                "address_id": 2,
                "address_line_1": "64 zoo lan",
                "address_line_2": "Mount Doo",
                "district": "Mordo",
                "city": "chicag",
                "postal_code": "dhu48",
                "country": "MiddleEart",
                "phone": "7383748",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            },
            {
                "address_id": 3,
                "address_line_1": "64 zoo la",
                "address_line_2": "Mount Do",
                "district": "Mord",
                "city": "chica",
                "postal_code": "dhu4",
                "country": "MiddleEar",
                "phone": "738374",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            },
        ]
    }
    counterparty_data = {
        "counterparty": [
            {
                "counterparty_id": 1,
                "counterparty_legal_name": "Orcs",
                "legal_address_id": 1,
                "commercial_contact": "devil",
                "delivery_contact": "angel",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            },
            {
                "counterparty_id": 2,
                "counterparty_legal_name": "Orc",
                "legal_address_id": 2,
                "commercial_contact": "devi",
                "delivery_contact": "ange",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            },
            {
                "counterparty_id": 3,
                "counterparty_legal_name": "Or",
                "legal_address_id": 3,
                "commercial_contact": "dev",
                "delivery_contact": "ang",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            },
        ]
    }
    result = dim_counterparty(address_data, counterparty_data)
    expected = {
        "dim_counterparty": [
            {
                "counterparty_id": 1,
                "counterparty_legal_address_line_1": "64 zoo lane",
                "counterparty_legal_address_line_2": "Mount Doom",
                "counterparty_legal_city": "chicago",
                "counterparty_legal_country": "MiddleEarth",
                "counterparty_legal_district": "Mordor",
                "counterparty_legal_name": "Orcs",
                "counterparty_legal_phone_number": "73837483",
                "counterparty_legal_postal_code": "dhu483",
            },
            {
                "counterparty_id": 2,
                "counterparty_legal_address_line_1": "64 zoo lan",
                "counterparty_legal_address_line_2": "Mount Doo",
                "counterparty_legal_city": "chicag",
                "counterparty_legal_country": "MiddleEart",
                "counterparty_legal_district": "Mordo",
                "counterparty_legal_name": "Orc",
                "counterparty_legal_phone_number": "7383748",
                "counterparty_legal_postal_code": "dhu48",
            },
            {
                "counterparty_id": 3,
                "counterparty_legal_address_line_1": "64 zoo la",
                "counterparty_legal_address_line_2": "Mount Do",
                "counterparty_legal_city": "chica",
                "counterparty_legal_country": "MiddleEar",
                "counterparty_legal_district": "Mord",
                "counterparty_legal_name": "Or",
                "counterparty_legal_phone_number": "738374",
                "counterparty_legal_postal_code": "dhu4",
            },
        ]
    }
    assert result == expected


@pytest.mark.describe("dim_counterparty")
@pytest.mark.it("function does not mutate input data")
def test_does_not_mutate():
    address_data = {
        "address": [
            {
                "address_id": 1,
                "address_line_1": "64 zoo lane",
                "address_line_2": "Mount Doom",
                "district": "Mordor",
                "city": "chicago",
                "postal_code": "dhu483",
                "country": "MiddleEarth",
                "phone": "73837483",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            },
            {
                "address_id": 2,
                "address_line_1": "64 zoo lan",
                "address_line_2": "Mount Doo",
                "district": "Mordo",
                "city": "chicag",
                "postal_code": "dhu48",
                "country": "MiddleEart",
                "phone": "7383748",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            },
            {
                "address_id": 3,
                "address_line_1": "64 zoo la",
                "address_line_2": "Mount Do",
                "district": "Mord",
                "city": "chica",
                "postal_code": "dhu4",
                "country": "MiddleEar",
                "phone": "738374",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            },
        ]
    }
    counterparty_data = {
        "counterparty": [
            {
                "counterparty_id": 1,
                "counterparty_legal_name": "Orcs",
                "legal_address_id": 1,
                "commercial_contact": "devil",
                "delivery_contact": "angel",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            },
            {
                "counterparty_id": 2,
                "counterparty_legal_name": "Orc",
                "legal_address_id": 2,
                "commercial_contact": "devi",
                "delivery_contact": "ange",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            },
            {
                "counterparty_id": 3,
                "counterparty_legal_name": "Or",
                "legal_address_id": 3,
                "commercial_contact": "dev",
                "delivery_contact": "ang",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            },
        ]
    }
    dim_counterparty(address_data, counterparty_data)
    assert address_data == {
        "address": [
            {
                "address_id": 1,
                "address_line_1": "64 zoo lane",
                "address_line_2": "Mount Doom",
                "district": "Mordor",
                "city": "chicago",
                "postal_code": "dhu483",
                "country": "MiddleEarth",
                "phone": "73837483",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            },
            {
                "address_id": 2,
                "address_line_1": "64 zoo lan",
                "address_line_2": "Mount Doo",
                "district": "Mordo",
                "city": "chicag",
                "postal_code": "dhu48",
                "country": "MiddleEart",
                "phone": "7383748",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            },
            {
                "address_id": 3,
                "address_line_1": "64 zoo la",
                "address_line_2": "Mount Do",
                "district": "Mord",
                "city": "chica",
                "postal_code": "dhu4",
                "country": "MiddleEar",
                "phone": "738374",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            },
        ]
    }
    assert counterparty_data == {
        "counterparty": [
            {
                "counterparty_id": 1,
                "counterparty_legal_name": "Orcs",
                "legal_address_id": 1,
                "commercial_contact": "devil",
                "delivery_contact": "angel",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            },
            {
                "counterparty_id": 2,
                "counterparty_legal_name": "Orc",
                "legal_address_id": 2,
                "commercial_contact": "devi",
                "delivery_contact": "ange",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            },
            {
                "counterparty_id": 3,
                "counterparty_legal_name": "Or",
                "legal_address_id": 3,
                "commercial_contact": "dev",
                "delivery_contact": "ang",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            },
        ]
    }


@pytest.mark.describe("dim_counterparty")
@pytest.mark.it("the function always returns the same value given the same parameters")
def test_always_returns_the_same_value():
    address_data = {
        "address": [
            {
                "address_id": 1,
                "address_line_1": "64 zoo lane",
                "address_line_2": "Mount Doom",
                "district": "Mordor",
                "city": "chicago",
                "postal_code": "dhu483",
                "country": "MiddleEarth",
                "phone": "73837483",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            },
            {
                "address_id": 2,
                "address_line_1": "64 zoo lan",
                "address_line_2": "Mount Doo",
                "district": "Mordo",
                "city": "chicag",
                "postal_code": "dhu48",
                "country": "MiddleEart",
                "phone": "7383748",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            },
            {
                "address_id": 3,
                "address_line_1": "64 zoo la",
                "address_line_2": "Mount Do",
                "district": "Mord",
                "city": "chica",
                "postal_code": "dhu4",
                "country": "MiddleEar",
                "phone": "738374",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            },
        ]
    }
    counterparty_data = {
        "counterparty": [
            {
                "counterparty_id": 1,
                "counterparty_legal_name": "Orcs",
                "legal_address_id": 1,
                "commercial_contact": "devil",
                "delivery_contact": "angel",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            },
            {
                "counterparty_id": 2,
                "counterparty_legal_name": "Orc",
                "legal_address_id": 2,
                "commercial_contact": "devi",
                "delivery_contact": "ange",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            },
            {
                "counterparty_id": 3,
                "counterparty_legal_name": "Or",
                "legal_address_id": 3,
                "commercial_contact": "dev",
                "delivery_contact": "ang",
                "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            },
        ]
    }
    dim_counterparty(address_data, counterparty_data)
    dim_counterparty(address_data, counterparty_data)
    expected = {
        "dim_counterparty": [
            {
                "counterparty_id": 1,
                "counterparty_legal_address_line_1": "64 zoo lane",
                "counterparty_legal_address_line_2": "Mount Doom",
                "counterparty_legal_city": "chicago",
                "counterparty_legal_country": "MiddleEarth",
                "counterparty_legal_district": "Mordor",
                "counterparty_legal_name": "Orcs",
                "counterparty_legal_phone_number": "73837483",
                "counterparty_legal_postal_code": "dhu483",
            },
            {
                "counterparty_id": 2,
                "counterparty_legal_address_line_1": "64 zoo lan",
                "counterparty_legal_address_line_2": "Mount Doo",
                "counterparty_legal_city": "chicag",
                "counterparty_legal_country": "MiddleEart",
                "counterparty_legal_district": "Mordo",
                "counterparty_legal_name": "Orc",
                "counterparty_legal_phone_number": "7383748",
                "counterparty_legal_postal_code": "dhu48",
            },
            {
                "counterparty_id": 3,
                "counterparty_legal_address_line_1": "64 zoo la",
                "counterparty_legal_address_line_2": "Mount Do",
                "counterparty_legal_city": "chica",
                "counterparty_legal_country": "MiddleEar",
                "counterparty_legal_district": "Mord",
                "counterparty_legal_name": "Or",
                "counterparty_legal_phone_number": "738374",
                "counterparty_legal_postal_code": "dhu4",
            },
        ]
    }

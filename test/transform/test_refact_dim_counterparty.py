from src.transform.dim_counterparty import dim_counterparty
import pytest
import pandas as pd
import datetime


@pytest.mark.describe("dim_counterparty")
@pytest.mark.it("function returns dataframe with correct columns")
def test_returns_correct_columns():
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
                "created_at": datetime.datetime
                (2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime
                (2022, 11, 3, 15, 20, 49, 962000),
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
                "created_at": datetime.datetime
                (2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime
                (2022, 11, 3, 15, 20, 49, 962000),
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
                "created_at": datetime.datetime
                (2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime
                (2022, 11, 3, 15, 20, 49, 962000),
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
                "created_at": datetime.datetime
                (2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime
                (2022, 11, 3, 15, 20, 49, 962000),
            },
            {
                "counterparty_id": 2,
                "counterparty_legal_name": "Orc",
                "legal_address_id": 2,
                "commercial_contact": "devi",
                "delivery_contact": "ange",
                "created_at": datetime.datetime
                (2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime
                (2022, 11, 3, 15, 20, 49, 962000),
            },
            {
                "counterparty_id": 3,
                "counterparty_legal_name": "Or",
                "legal_address_id": 3,
                "commercial_contact": "dev",
                "delivery_contact": "ang",
                "created_at": datetime.datetime
                (2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime
                (2022, 11, 3, 15, 20, 49, 962000),
            },
        ]
    }

    address_df = pd.DataFrame(address_data["address"])
    counterparty_df = pd.DataFrame(counterparty_data["counterparty"])
    result = dim_counterparty(address_df, counterparty_df)
    bool_list = [
        column_name in result
        for column_name in [
            "counterparty_id",
            "counterparty_legal_name",
            "counterparty_legal_address_line_1",
            "counterparty_legal_address_line_2",
            "counterparty_legal_district",
            "counterparty_legal_city",
            "counterparty_legal_postal_code",
            "counterparty_legal_country",
            "counterparty_legal_phone_number",
        ]
    ]
    assert all(bool_list)


@pytest.mark.describe("dim_counterparty")
@pytest.mark.it("function returns dataframe with correct values")
def test_returns_correct_values():
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
                "created_at": datetime.datetime
                (2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime
                (2022, 11, 3, 15, 20, 49, 962000),
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
                "created_at": datetime.datetime
                (2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime
                (2022, 11, 3, 15, 20, 49, 962000),
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
                "created_at": datetime.datetime
                (2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime
                (2022, 11, 3, 15, 20, 49, 962000),
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
                "created_at": datetime.datetime
                (2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime
                (2022, 11, 3, 15, 20, 49, 962000),
            },
            {
                "counterparty_id": 2,
                "counterparty_legal_name": "Orc",
                "legal_address_id": 2,
                "commercial_contact": "devi",
                "delivery_contact": "ange",
                "created_at": datetime.datetime
                (2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime
                (2022, 11, 3, 15, 20, 49, 962000),
            },
            {
                "counterparty_id": 3,
                "counterparty_legal_name": "Or",
                "legal_address_id": 3,
                "commercial_contact": "dev",
                "delivery_contact": "ang",
                "created_at": datetime.datetime
                (2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": datetime.datetime
                (2022, 11, 3, 15, 20, 49, 962000),
            },
        ]
    }
    address_df = pd.DataFrame(address_data["address"])
    counterparty_df = pd.DataFrame(counterparty_data["counterparty"])
    result = dim_counterparty(address_df, counterparty_df)
    assert result.to_dict() == {
        "counterparty_id": {0: 1, 1: 2, 2: 3},
        "counterparty_legal_name": {0: "Orcs", 1: "Orc", 2: "Or"},
        "counterparty_legal_address_line_1": {
            0: "64 zoo lane",
            1: "64 zoo lan",
            2: "64 zoo la",
        },
        "counterparty_legal_address_line_2": {
            0: "Mount Doom",
            1: "Mount Doo",
            2: "Mount Do",
        },
        "counterparty_legal_district": {0: "Mordor", 1: "Mordo", 2: "Mord"},
        "counterparty_legal_city": {0: "chicago", 1: "chicag", 2: "chica"},
        "counterparty_legal_postal_code": {0: "dhu483", 1: "dhu48", 2: "dhu4"},
        "counterparty_legal_country": {
            0: "MiddleEarth",
            1: "MiddleEart",
            2: "MiddleEar",
        },
        "counterparty_legal_phone_number": {
            0: "73837483",
            1: "7383748",
            2: "738374"
            },
    }

import pytest
import pandas as pd
from src.transform.dim_location import dim_location


@pytest.mark.describe("dim_location")
@pytest.mark.it("ffunction returns a dataframe which has correct columns")
def test_returns_dataframe():
    address_df = {
        "address": [
            {
                "address_id": 1,
                "address_line_1": "6826 Herzog Via",
                "address_line_2": None,
                "district": "Avon",
                "city": "New Patienceburgh",
                "postal_code": "28441",
                "country": "Turkey",
                "phone": "1803 637401",
                "created_at": "2022-11-03T14:20:49.962",
                "last_updated": "2022-11-03T14:20:49.962",
            },
            {
                "address_id": 2,
                "address_line_1": "179 Alexie Cliffs",
                "address_line_2": None,
                "district": None,
                "city": "Aliso Viejo",
                "postal_code": "99305-7380",
                "country": "San Marino",
                "phone": "9621 880720",
                "created_at": "2022-11-03T14:20:49.962",
                "last_updated": "2022-11-03T14:20:49.962",
            },
        ]
    }
    df = pd.DataFrame(address_df["address"])
    result = dim_location(df)
    bool_list = [
        column in result
        for column in [
            "address_id",
            "address_line_1",
            "address_line_2",
            "district",
            "city",
            "postal_code",
            "country",
            "phone",
        ]
    ]
    assert all(bool_list)


@pytest.mark.describe("dim_location")
@pytest.mark.it("function returns a dataframe with correct values")
def test_returns_dataframe_with_correct_values():
    address_df = {
        "address": [
            {
                "address_id": 1,
                "address_line_1": "6826 Herzog Via",
                "address_line_2": None,
                "district": "Avon",
                "city": "New Patienceburgh",
                "postal_code": "28441",
                "country": "Turkey",
                "phone": "1803 637401",
                "created_at": "2022-11-03T14:20:49.962",
                "last_updated": "2022-11-03T14:20:49.962",
            },
            {
                "address_id": 2,
                "address_line_1": "179 Alexie Cliffs",
                "address_line_2": None,
                "district": None,
                "city": "Aliso Viejo",
                "postal_code": "99305-7380",
                "country": "San Marino",
                "phone": "9621 880720",
                "created_at": "2022-11-03T14:20:49.962",
                "last_updated": "2022-11-03T14:20:49.962",
            },
        ]
    }
    df = pd.DataFrame(address_df["address"])
    result = dim_location(df)
    assert result.to_dict() == {
        "address_id": {0:1, 1:2},
        "address_line_1" :{0:"6826 Herzog Via", 1:"179 Alexie Cliffs"},
        "address_line_2" :{0:None, 1:None},
        "district" :{0:"Avon", 1:None},
        "city" :{0:"New Patienceburgh", 1:"Aliso Viejo"},
        "postal_code" :{0:"28441", 1:"99305-7380"},
        "country" :{0:"Turkey", 1:"San Marino"},
        "phone" :{0:"1803 637401", 1:"9621 880720"}
    }

@pytest.mark.describe("dim_location")
@pytest.mark.it("check result has different reference")
def test_check_result_has_diff_ref():
    address_df = {
        "address": [
            {
                "address_id": 1,
                "address_line_1": "6826 Herzog Via",
                "address_line_2": None,
                "district": "Avon",
                "city": "New Patienceburgh",
                "postal_code": "28441",
                "country": "Turkey",
                "phone": "1803 637401",
                "created_at": "2022-11-03T14:20:49.962",
                "last_updated": "2022-11-03T14:20:49.962",
            },
            {
                "address_id": 2,
                "address_line_1": "179 Alexie Cliffs",
                "address_line_2": None,
                "district": None,
                "city": "Aliso Viejo",
                "postal_code": "99305-7380",
                "country": "San Marino",
                "phone": "9621 880720",
                "created_at": "2022-11-03T14:20:49.962",
                "last_updated": "2022-11-03T14:20:49.962",
            },
        ]
    }
    df = pd.DataFrame(address_df["address"])
    result = dim_location(df)
    assert address_df is not result

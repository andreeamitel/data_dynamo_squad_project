'''Tests the function dim_location.'''

import pytest
from src.transform.dim_location import dim_location


@pytest.mark.describe("dim_location")
@pytest.mark.it("function returns an empty dictionary if given empty dictionary")
def test_returns_empty_dict_when_given_empty_dict():
    result = dim_location({})
    assert result == {}


@pytest.mark.describe("dim_location")
@pytest.mark.it("function returns dictionary with dim_location key")
def test_returns_dict_with_correct_key():
    result = dim_location(
        {
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
    )
    expected = list(result.keys())[0]
    assert expected == "dim_location"


@pytest.mark.describe("dim_location")
@pytest.mark.it("function returns dictionary with correct values")
def test_returns_dict_with_correct_values():
    result = dim_location(
        {
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
    )
    expected = {
        "dim_location": [
            {
                "address_id": 1,
                "address_line_1": "6826 Herzog Via",
                "address_line_2": None,
                "district": "Avon",
                "city": "New Patienceburgh",
                "postal_code": "28441",
                "country": "Turkey",
                "phone": "1803 637401",
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
            },
        ]
    }
    assert expected == result


@pytest.mark.describe("dim_location")
@pytest.mark.it("check result has different reference")
def test_check_result_has_diff_ref():
    test_input = {
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
    result = dim_location(test_input)
    assert test_input is not result


@pytest.mark.describe("dim_location")
@pytest.mark.it("check input is same after function is called")
def test_check_input_not_changed():
    test_input = {
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
    dim_location(test_input)
    assert test_input == {
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

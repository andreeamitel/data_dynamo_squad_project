'''Tests the function dim_staff.'''

import pytest
from src.transform.dim_staff import dim_staff


@pytest.mark.describe("dim_staff")
@pytest.mark.it("function returns dictionary with correct key")
def test_returns_dict_with_correct_key():
    test_staff_data = {
        "staff": [
            {
                "staff_id": 1,
                "first_name": "Jeremie",
                "last_name": "Franey",
                "department_id": 2,
                "email_address": "jeremie.franey@terrifictotes.com",
                "created_at": "2022-11-03T14:20:51.563",
                "last_updated": "2022-11-03T14:20:51.563",
            }
        ]
    }
    test_department_data = {
        "department": [
            {
                "department_id": 2,
                "department_name": "Purchasing",
                "location": "Manchester",
                "manager": "Naomi Lapaglia",
                "created_at": "2022-11-03T14:20:49.962",
                "last_updated": "2022-11-03T14:20:49.962",
            },
        ]
    }
    result = dim_staff(test_staff_data, test_department_data)
    expected = list(result.keys())[0]
    assert expected == "dim_staff"


@pytest.mark.describe("dim_staff")
@pytest.mark.it("function returns dictionary with correct values")
def test_returns_dict_with_correct_values():
    test_staff_data = {
        "staff": [
            {
                "staff_id": 1,
                "first_name": "Jeremie",
                "last_name": "Franey",
                "department_id": 2,
                "email_address": "jeremie.franey@terrifictotes.com",
                "created_at": "2022-11-03T14:20:51.563",
                "last_updated": "2022-11-03T14:20:51.563",
            }
        ]
    }
    test_department_data = {
        "department": [
            {
                "department_id": 2,
                "department_name": "Purchasing",
                "location": "Manchester",
                "manager": "Naomi Lapaglia",
                "created_at": "2022-11-03T14:20:49.962",
                "last_updated": "2022-11-03T14:20:49.962",
            },
        ]
    }
    result = dim_staff(test_staff_data, test_department_data)
    expected = {
        "dim_staff": [
            {
                "staff_id": 1,
                "first_name": "Jeremie",
                "last_name": "Franey",
                "department_name": "Purchasing",
                "location": "Manchester",
                "email_address": "jeremie.franey@terrifictotes.com",
            },
        ]
    }
    assert result == expected


@pytest.mark.describe("dim_staff")
@pytest.mark.it(
    "function returns dictionary with correct values when passed in with many staff and department data"
)
def test_returns_dict_with_correct_values_when_passed_in_many_staff_and_dep_data():
    test_staff_data = {
        "staff": [
            {
                "staff_id": 1,
                "first_name": "Jeremie",
                "last_name": "Franey",
                "department_id": 2,
                "email_address": "jeremie.franey@terrifictotes.com",
                "created_at": "2022-11-03T14:20:51.563",
                "last_updated": "2022-11-03T14:20:51.563",
            },
            {
                "staff_id": 2,
                "first_name": "Jeremie",
                "last_name": "Franey",
                "department_id": 1,
                "email_address": "jeremie.franey@terrifictotes.com",
                "created_at": "2022-11-03T14:20:51.563",
                "last_updated": "2022-11-03T14:20:51.563",
            },
        ]
    }
    test_department_data = {
        "department": [
            {
                "department_id": 2,
                "department_name": "Purchasing",
                "location": "Manchester",
                "manager": "Naomi Lapaglia",
                "created_at": "2022-11-03T14:20:49.962",
                "last_updated": "2022-11-03T14:20:49.962",
            },
            {
                "department_id": 1,
                "department_name": "Sales",
                "location": "London",
                "manager": "Naomi Lapaglia",
                "created_at": "2022-11-03T14:20:49.962",
                "last_updated": "2022-11-03T14:20:49.962",
            },
        ]
    }
    result = dim_staff(test_staff_data, test_department_data)
    expected = {
        "dim_staff": [
            {
                "staff_id": 1,
                "first_name": "Jeremie",
                "last_name": "Franey",
                "department_name": "Purchasing",
                "location": "Manchester",
                "email_address": "jeremie.franey@terrifictotes.com",
            },
            {
                "staff_id": 2,
                "first_name": "Jeremie",
                "last_name": "Franey",
                "department_name": "Sales",
                "location": "London",
                "email_address": "jeremie.franey@terrifictotes.com",
            },
        ]
    }
    assert result == expected


@pytest.mark.describe("dim_staff")
@pytest.mark.it("check result is different reference than input")
def test_check_result_has_diff_ref():
    test_staff_data = {
        "staff": [
            {
                "staff_id": 1,
                "first_name": "Jeremie",
                "last_name": "Franey",
                "department_id": 2,
                "email_address": "jeremie.franey@terrifictotes.com",
                "created_at": "2022-11-03T14:20:51.563",
                "last_updated": "2022-11-03T14:20:51.563",
            },
            {
                "staff_id": 2,
                "first_name": "Jeremie",
                "last_name": "Franey",
                "department_id": 1,
                "email_address": "jeremie.franey@terrifictotes.com",
                "created_at": "2022-11-03T14:20:51.563",
                "last_updated": "2022-11-03T14:20:51.563",
            },
        ]
    }
    test_department_data = {
        "department": [
            {
                "department_id": 2,
                "department_name": "Purchasing",
                "location": "Manchester",
                "manager": "Naomi Lapaglia",
                "created_at": "2022-11-03T14:20:49.962",
                "last_updated": "2022-11-03T14:20:49.962",
            },
            {
                "department_id": 1,
                "department_name": "Sales",
                "location": "London",
                "manager": "Naomi Lapaglia",
                "created_at": "2022-11-03T14:20:49.962",
                "last_updated": "2022-11-03T14:20:49.962",
            },
        ]
    }
    result = dim_staff(test_staff_data, test_department_data)
    assert result is not test_staff_data
    assert result is not test_department_data


@pytest.mark.describe("dim_staff")
@pytest.mark.it("check input hasnt not changed")
def test_check_input_hasnt_changed():
    test_staff_data = {
        "staff": [
            {
                "staff_id": 1,
                "first_name": "Jeremie",
                "last_name": "Franey",
                "department_id": 2,
                "email_address": "jeremie.franey@terrifictotes.com",
                "created_at": "2022-11-03T14:20:51.563",
                "last_updated": "2022-11-03T14:20:51.563",
            },
            {
                "staff_id": 2,
                "first_name": "Jeremie",
                "last_name": "Franey",
                "department_id": 1,
                "email_address": "jeremie.franey@terrifictotes.com",
                "created_at": "2022-11-03T14:20:51.563",
                "last_updated": "2022-11-03T14:20:51.563",
            },
        ]
    }
    test_department_data = {
        "department": [
            {
                "department_id": 2,
                "department_name": "Purchasing",
                "location": "Manchester",
                "manager": "Naomi Lapaglia",
                "created_at": "2022-11-03T14:20:49.962",
                "last_updated": "2022-11-03T14:20:49.962",
            },
            {
                "department_id": 1,
                "department_name": "Sales",
                "location": "London",
                "manager": "Naomi Lapaglia",
                "created_at": "2022-11-03T14:20:49.962",
                "last_updated": "2022-11-03T14:20:49.962",
            },
        ]
    }
    dim_staff(test_staff_data, test_department_data)
    assert test_staff_data == {
        "staff": [
            {
                "staff_id": 1,
                "first_name": "Jeremie",
                "last_name": "Franey",
                "department_id": 2,
                "email_address": "jeremie.franey@terrifictotes.com",
                "created_at": "2022-11-03T14:20:51.563",
                "last_updated": "2022-11-03T14:20:51.563",
            },
            {
                "staff_id": 2,
                "first_name": "Jeremie",
                "last_name": "Franey",
                "department_id": 1,
                "email_address": "jeremie.franey@terrifictotes.com",
                "created_at": "2022-11-03T14:20:51.563",
                "last_updated": "2022-11-03T14:20:51.563",
            },
        ]
    }
    assert test_department_data == {
        "department": [
            {
                "department_id": 2,
                "department_name": "Purchasing",
                "location": "Manchester",
                "manager": "Naomi Lapaglia",
                "created_at": "2022-11-03T14:20:49.962",
                "last_updated": "2022-11-03T14:20:49.962",
            },
            {
                "department_id": 1,
                "department_name": "Sales",
                "location": "London",
                "manager": "Naomi Lapaglia",
                "created_at": "2022-11-03T14:20:49.962",
                "last_updated": "2022-11-03T14:20:49.962",
            },
        ]
    }

import pandas as pd
import pytest
from src.transform.dim_staff import dim_staff


@pytest.mark.describe("dim_staff")
@pytest.mark.it("function returns dataframe with correct columns")
def test_returns_correct_columns():
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
    df_staff = pd.DataFrame(test_staff_data["staff"])
    df_department = pd.DataFrame(test_department_data["department"])
    result = dim_staff(df_staff, df_department)
    bool_list = [
        column_name in result
        for column_name in [
            "staff_id",
            "first_name",
            "last_name",
            "department_name",
            "location",
            "email_address",
        ]
    ]
    assert all(bool_list)


@pytest.mark.describe("dim_staff")
@pytest.mark.it("function returns dataframe with correct values")
def test_returns_correct_values():
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
    df_staff = pd.DataFrame(test_staff_data["staff"])
    df_department = pd.DataFrame(test_department_data["department"])
    result = dim_staff(df_staff, df_department)
    print(result.to_dict())
    assert result.to_dict() == {
        "staff_id": {0: 1, 1: 2},
        "first_name": {0: "Jeremie", 1: "Jeremie"},
        "last_name": {0: "Franey", 1: "Franey"},
        "department_name": {0: "Purchasing", 1: "Sales"},
        "location": {0: "Manchester", 1: "London"},
        "email_address": {
            0: "jeremie.franey@terrifictotes.com",
            1: "jeremie.franey@terrifictotes.com",
        },
    }

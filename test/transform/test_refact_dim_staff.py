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
    result = dim_staff(df_staff,df_department)
    print(result.columns)
    assert False

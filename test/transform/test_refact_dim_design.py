from src.transform.dim_design import dim_design
import pytest
import pandas as pd
from datetime import datetime as dt


@pytest.mark.describe("dim_design")
@pytest.mark.it("function returns dataframe with correct columns")
def test_returns_correct_columns():
    design_test = {
        "design": [
            {
                "design_id": 1,
                "created_at": dt(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": dt(2022, 11, 3, 15, 20, 49, 962000),
                "design_name": "design",
                "file_location": "file location",
                "file_name": "file name",
            },
            {
                "design_id": 2,
                "created_at": dt(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": dt(2022, 11, 3, 15, 20, 49, 962000),
                "design_name": "design2",
                "file_location": "file location2",
                "file_name": "file name2",
            },
            {
                "design_id": 3,
                "created_at": dt(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": dt(2022, 11, 3, 15, 20, 49, 962000),
                "design_name": "design3",
                "file_location": "file location3",
                "file_name": "file name3",
            },
        ]
    }

    design_df = pd.DataFrame(design_test["design"])
    result = dim_design(design_df)
    bool_list = [
        column_name in result
        for column_name in [
            "design_id",
            "design_name",
            "file_location",
            "file_name"]
    ]
    assert all(bool_list)


@pytest.mark.describe("dim_design")
@pytest.mark.it("function returns dataframe with correct values")
def test_returns_correct_values():
    design_test = {
        "design": [
            {
                "design_id": 1,
                "created_at": dt(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": dt(2022, 11, 3, 15, 20, 49, 962000),
                "design_name": "design",
                "file_location": "file location",
                "file_name": "file name",
            },
            {
                "design_id": 2,
                "created_at": dt(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": dt(2022, 11, 3, 15, 20, 49, 962000),
                "design_name": "design2",
                "file_location": "file location2",
                "file_name": "file name2",
            },
            {
                "design_id": 3,
                "created_at": dt(2022, 11, 3, 15, 20, 49, 962000),
                "last_updated": dt(2022, 11, 3, 15, 20, 49, 962000),
                "design_name": "design3",
                "file_location": "file location3",
                "file_name": "file name3",
            },
        ]
    }
    design_df = pd.DataFrame(design_test["design"])
    result = dim_design(design_df)
    print(result.to_dict())
    assert result.to_dict() == {
        "design_id": {0: 1, 1: 2, 2: 3},
        "design_name": {0: "design", 1: "design2", 2: "design3"},
        "file_location": {
            0: "file location", 1: "file location2",
            2: "file location3"},
        "file_name": {0: "file name", 1: "file name2", 2: "file name3"},
    }

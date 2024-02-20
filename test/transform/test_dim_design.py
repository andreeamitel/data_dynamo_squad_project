from src.transform.dim_design import dim_design
import pytest
import datetime


@pytest.mark.describe("dim_design")
@pytest.mark.it("function returns an empty list if given and empty table_list")
def test_returns_empty_list():
    result = dim_design([])
    assert result == []

@pytest.mark.describe("dim_design")
@pytest.mark.it("function returns a list of dictionaries")
def test_returns_a_list_of_dictionary_type():
    dim_design_test = [
        {
            "design_id": 1,
            "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "design_name": "design",
            "file_location": "file location",
            "file_name": "file name",
        }]
    result = dim_design(dim_design_test)
    result1 = type(result)
    result2 = [
        type(returned_data) is dict for returned_data in result
    ]
    assert result1 is list
    assert all(result2) is True


@pytest.mark.describe("dim_design")
@pytest.mark.it(
    "function returns a list of one dictionary with the amended column names from the design table"
)
def test_return_a_list_of_one_dictionary():
    dim_design_test = [
        {
            "design_id": 1,
            "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "design_name": "design",
            "file_location": "file location",
            "file_name": "file name",
        }
    ]

    expected = [
        {
            "design_id": 1,
            "design_name": "design",
            "file_location": "file location",
            "file_name": "file name",
        }
    ]
    result = dim_design(dim_design_test)
    assert result == expected

@pytest.mark.describe("dim_design")
@pytest.mark.it(
    "function returns a list of dictionaries with the amended column names from the design tables"
)
def test_return_a_list_of_dictionaries():
    dim_design_test = [
        {
            "design_id": 1,
            "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "design_name": "design",
            "file_location": "file location",
            "file_name": "file name",
        },
        {
            "design_id": 2,
            "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "design_name": "design2",
            "file_location": "file location2",
            "file_name": "file name2",
        },
        {
            "design_id": 3,
            "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "design_name": "design3",
            "file_location": "file location3",
            "file_name": "file name3",
        },
    ]

    expected = [
        {
            "design_id": 1,
            "design_name": "design",
            "file_location": "file location",
            "file_name": "file name",
        },
        {
            "design_id": 2,
            "design_name": "design2",
            "file_location": "file location2",
            "file_name": "file name2",
        },
        {
            "design_id": 3,
            "design_name": "design3",
            "file_location": "file location3",
            "file_name": "file name3",
        }
    ]
    result = dim_design(dim_design_test)
    assert result == expected

@pytest.mark.describe("dim_design")
@pytest.mark.it("function does not mutate input data"
)
def test_does_not_mutate():
    dim_design_test = [
        {
            "design_id": 1,
            "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "design_name": "design",
            "file_location": "file location",
            "file_name": "file name",
        },
        {
            "design_id": 2,
            "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "design_name": "design2",
            "file_location": "file location2",
            "file_name": "file name2",
        },
        {
            "design_id": 3,
            "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "design_name": "design3",
            "file_location": "file location3",
            "file_name": "file name3",
        },
    ]
    dim_design(dim_design_test)
    assert dim_design_test == [
        {
            "design_id": 1,
            "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "design_name": "design",
            "file_location": "file location",
            "file_name": "file name",
        },
        {
            "design_id": 2,
            "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "design_name": "design2",
            "file_location": "file location2",
            "file_name": "file name2",
        },
        {
            "design_id": 3,
            "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "design_name": "design3",
            "file_location": "file location3",
            "file_name": "file name3",
        },
    ]

@pytest.mark.describe("dim_design")
@pytest.mark.it(
    "the function always returns the same value given the same parameters"
)
def test_always_returns_the_same_value():
    dim_design_test = [
        {
            "design_id": 1,
            "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "design_name": "design",
            "file_location": "file location",
            "file_name": "file name",
        },
        {
            "design_id": 2,
            "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "design_name": "design2",
            "file_location": "file location2",
            "file_name": "file name2",
        },
        {
            "design_id": 3,
            "created_at": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "last_updated": datetime.datetime(2022, 11, 3, 15, 20, 49, 962000),
            "design_name": "design3",
            "file_location": "file location3",
            "file_name": "file name3",
        },
    ]
    dim_design(dim_design_test)
    dim_design(dim_design_test)
    expected = [
        {
            "design_id": 1,
            "design_name": "design",
            "file_location": "file location",
            "file_name": "file name",
        },
        {
            "design_id": 2,
            "design_name": "design2",
            "file_location": "file location2",
            "file_name": "file name2",
        },
        {
            "design_id": 3,
            "design_name": "design3",
            "file_location": "file location3",
            "file_name": "file name3",
        }
    ]
    result = dim_design(dim_design_test)
    assert result == expected

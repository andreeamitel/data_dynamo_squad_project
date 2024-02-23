import pytest
from unittest.mock import Mock
from datetime import datetime
from src.extract.extract_data import extract_data
from pg8000.native import Connection
import os
from dotenv import load_dotenv

load_dotenv()


@pytest.mark.describe("extract_data")
@pytest.mark.it("function extract_data returns a list of dictionaries")
def test_returns_list_of_dictionaries():
    my_mock = Mock()
    my_mock.run.return_value = [
        [
            [
                {
                    "currency_id": 1,
                    "currency_code": "GBP",
                    "created_at": "2024-02-13",
                    "last_updated": "2024-02-13",
                }
            ]
        ]
    ]
    result1 = type(extract_data("currency", my_mock, datetime.now()))
    result2 = [
        type(returned_data) is dict
        for returned_data in extract_data("currency", my_mock, datetime.now())
    ]
    assert result1 is list
    assert all(result2) is True


@pytest.mark.describe("extract_data")
@pytest.mark.it(
    """function extract_data returns a dictionary
                with the correct keys as column names"""
)
def test_returns_dictionary():
    my_mock = Mock()
    my_mock.run.return_value = [
        [
            [
                {
                    "currency_id": 1,
                    "currency_code": "GBP",
                    "created_at": "2024-02-13",
                    "last_updated": "2024-02-13",
                }
            ]
        ]
    ]
    result = extract_data("currency", my_mock, datetime.now())
    assert result == [
        {
            "currency_id": 1,
            "currency_code": "GBP",
            "created_at": "2024-02-13",
            "last_updated": "2024-02-13",
        }
    ]


@pytest.mark.describe("extract_data")
@pytest.mark.it(
    """return list of dictionaries
                with last_updated and created_at
                greater than last_run argument"""
)
def test_returns_using_timestamp_query():
    db_user = f"{os.environ['PGUSER']}"
    db_database_name = f"{os.environ['PGDATABASE']}"
    db_password = f"{os.environ['PGPASSWORD']}"
    conn = Connection(db_user, password=db_password, database=db_database_name)
    result = extract_data("currency", conn, "2024-02-13 00:00:00")
    conn.close()
    assert result == [
        {
            "currency_id": 2,
            "currency_code": "EUR",
            "created_at": "2024-02-14T09:00:00",
            "last_updated": "2024-02-14T09:00:00",
        },
        {
            "currency_id": 3,
            "currency_code": "USD",
            "created_at": "1999-01-08T04:05:06",
            "last_updated": "2024-02-14T09:00:00",
        },
        {
            "currency_id": 4,
            "currency_code": "AUD",
            "created_at": "2024-02-14T09:00:00",
            "last_updated": "1999-01-08T04:05:06",
        },
    ]

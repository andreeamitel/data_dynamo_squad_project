import pytest
from unittest.mock import Mock
from datetime import datetime
from src.extract.extract_data import extract_data

@pytest.mark.describe("extract_data")
@pytest.mark.it("function extract_data returns a list of dictionaries")
def test_returns_list_of_dictionaries():
    my_mock = Mock()
    my_mock.run.return_value = [[]]
    result1 = type(extract_data("currency", my_mock))
    result2 = [type(returned_data) is dict for returned_data in extract_data("currency")]
    assert result1 is list
    assert all(result2) is True

@pytest.mark.describe("extract_data")
@pytest.mark.it("function extract_data returns a dictionary with the correct keys as column names")
def test_returns_dictionary():
    my_mock = Mock()
    my_mock.run.return_value = [[1, "GBP", "2024-02-13", "2024-02-13"]]
    result = extract_data("currency", my_mock)
    print(result)
    # assert result == [
    #     {"currency_id": 1, "currency_code": "GBP", "created_at": "2024-02-13", "updated_at": "2024-02-13"
    #      }
    # ]
    my_mock.run.assert_called_with("SELECT * FROM currency;")
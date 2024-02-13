import pytest

from src.extract.extract_data import extract_data

# @pytest.describe("extract_data")
# @pytest.mark.it("function extract_data returns a list of dictionaries")
def returns_list_of_dictionaries():
    result1 = type(extract_data("currency"))
    result2 = [type(returned_data) for returned_data in extract_data("currency")]
    assert result1 is list
    assert all(result2) is dict
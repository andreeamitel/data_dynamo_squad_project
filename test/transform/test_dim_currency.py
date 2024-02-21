from src.transform.dim_currency import dim_currency


@pytest.mark.describe("dim_currency")
@pytest.mark.it("function returns an empty list if given empty table lists")
def test_returns_empty_list_when_given_empty_dict():
    result = dim_currency({}) 
    assert result == []
from src.extract.check_for_changes import check_for_changes
from unittest.mock import patch
from pg8000.native import Connection

@patch('src.extract.check_for_changes.conn')
def test_connects_to_database(mock_conn):
    mock_conn.run.return_value = [[1, 2, 3, 4]]
    result = check_for_changes(mock_conn)
    expected = [[1, 2, 3, 4]]
    assert result == expected
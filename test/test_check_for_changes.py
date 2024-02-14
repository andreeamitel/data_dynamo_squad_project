from src.extract.check_for_changes import check_for_changes
from unittest.mock import patch
from pg8000.native import Connection
import datetime

@patch('src.extract.check_for_changes.conn')
def test_conn_run_has_been_called(mock_conn):
    mock_conn.run.return_value = [[1, 2, 3, 4]]
    check_for_changes(mock_conn)
    mock_conn.run.assert_called_once()

@patch('src.extract.check_for_changes.conn')
def test_checks_for_changes_in_address_table(mock_conn):
    mock_conn.run.return_value = [datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)]
    result = check_for_changes(mock_conn)
    expected = ['address']
    assert result == expected

@patch('src.extract.check_for_changes.conn')
def test_checks_for_changes_in_all_tables(mock_conn):
    mock_conn.run.return_value = [datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)]
    result = check_for_changes(mock_conn)
    expected = ['address']
    assert result == expected
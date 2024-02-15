
from src.extract.check_for_changes import (
    check_for_changes,
    check_table_for_last_updated,
)
from unittest.mock import patch, Mock
from pg8000.exceptions import DatabaseError
import datetime


@patch("src.extract.check_for_changes.conn")
def test_conn_run_has_been_called(mock_conn):
    mock_conn.run.return_value = [[1, 2, 3, 4]]
    check_for_changes(mock_conn, "2022-11-03 14:20:49.962000")
    mock_conn.run.assert_called()


@patch("src.extract.check_for_changes.conn")
def test_checks_for_changes_in_all_tables(mock_conn):
    mock_conn.run.return_value = [
        [datetime.datetime(2022, 11, 3, 15, 20, 49, 962000)],
        [datetime.datetime(2022, 11, 3, 15, 20, 49, 962000)],
        [datetime.datetime(2022, 11, 3, 15, 20, 49, 962000)],
        [datetime.datetime(2022, 11, 3, 15, 20, 49, 962000)],
        [datetime.datetime(2022, 11, 3, 15, 20, 49, 962000)],
    ]
    result = check_for_changes(mock_conn, "2022-11-03 14:20:49.962000")
    expected = [
        "address",
        "staff",
        "design",
        "sales_order",
        "currency",
        "department",
        "counterparty",
    ]
    assert result == expected


@patch("src.extract.check_for_changes.conn")
def test_checks_return_empty_list_when_there_is_no_changes(mock_conn):
    mock_conn.run.return_value = [
        [datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)],
        [datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)],
        [datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)],
        [datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)],
        [datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)],
    ]
    result = check_for_changes(mock_conn, "2022-11-03 14:20:49.962000")
    expected = []
    assert result == expected


@patch("src.extract.check_for_changes.conn")
def test_handles_typeError(mock_conn):
    mock_conn.run.return_value = [
        [datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)],
        [datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)],
        [datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)],
        [datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)],
        [datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)],
    ]

    with pytest.raises(TypeError):
        check_for_changes(
            mock_conn, [datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)]
        )

@patch("src.extract.check_for_changes.conn")
def test_return_true_when_table_was_updated(mock_conn):
    mock_conn.run.return_value = [
        [datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)],
        [datetime.datetime(2022, 11, 3, 15, 20, 49, 962000)],
        [datetime.datetime(2022, 11, 3, 15, 20, 49, 962000)],
        [datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)],
        [datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)],
    ]
    result = check_table_for_last_updated(
        'address', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), mock_conn
        )
    expected = True
    assert result == expected


@patch("src.extract.check_for_changes.conn")
def test_return_false_when_table_was_not_updated(mock_conn):
    mock_conn.run.return_value = [
        [datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)],
        [datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)],
        [datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)],
        [datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)],
        [datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)],
    ]
    result = check_table_for_last_updated(
        'address', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), mock_conn
        )
    expected = False
    assert result == expected


def test_handles_database_error():
    my_mock = Mock()
    test_error = DatabaseError
    test_error.args = [{'M': 'syntax error near $'}]
    my_mock.run.side_effect = test_error
    with pytest.raises(DatabaseError):
        check_table_for_last_updated('address', datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), my_mock)


"""Tests check_for_changes function."""

from unittest.mock import patch
import datetime
import pytest
from src.extract.check_for_changes import (
    check_for_changes,
    check_table_for_last_updated,
)


@pytest.mark.describe("check_for_changes")
@pytest.mark.it("invokes connection.run")
@patch("connection.conn")
def test_conn_run_has_been_called(mock_conn):
    mock_conn.run.return_value = [[1, 2, 3, 4]]
    check_for_changes(mock_conn, "2022-11-03 14:20:49.962000")
    mock_conn.run.assert_called()


@pytest.mark.describe("check_for_changes")
@pytest.mark.it("checks for changes in all tables")
@patch("connection.conn")
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


@pytest.mark.describe("check_for_changes")
@pytest.mark.it("returns empty list when theres no changes")
@patch("connection.conn")
def test_returns_empty_list_when_there_is_no_changes(mock_conn):
    mock_conn.run.return_value = []
    result = check_for_changes(mock_conn, "2025-11-03 14:20:49.962000")
    expected = []
    assert result == expected


@pytest.mark.describe("check_tables_for_last_updated")
@pytest.mark.it("returns true when table is updated")
@patch("connection.conn")
def test_return_true_when_table_was_updated(mock_conn):
    mock_conn.run.return_value = [
        [datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)],
        [datetime.datetime(2022, 11, 3, 15, 20, 49, 962000)],
        [datetime.datetime(2022, 11, 3, 15, 20, 49, 962000)],
        [datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)],
        [datetime.datetime(2022, 11, 3, 15, 20, 49, 962000)],
    ]
    result = check_table_for_last_updated(
        "address", datetime.datetime(2021, 11, 3, 14, 20, 49, 962000), mock_conn
    )
    expected = True
    assert result == expected


@pytest.mark.describe("check_tables_for_last_updated")
@pytest.mark.it("returns false when table is not updated")
@patch("connection.conn")
def test_return_false_when_table_was_not_updated(mock_conn):
    mock_conn.run.return_value = []
    result = check_table_for_last_updated(
        "address", datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), mock_conn
    )
    expected = False
    assert result == expected

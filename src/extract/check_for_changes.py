import boto3
from pprint import pprint
from connection import conn, identifier, literal, DatabaseError
from datetime import datetime


def check_for_changes(db_conn, last_ingested_time):
    try:
        format = "%Y-%m-%d %H:%M:%S.%f"
        date_time = datetime.strptime(last_ingested_time, format)
        table_names = [
            "address",
            "staff",
            "design",
            "sales_order",
            "currency",
            "department",
            "counterparty",
        ]
        result = [
            table
            for table in table_names
            if check_table_for_last_updated(table, date_time, db_conn)
        ]

        return result
    except TypeError as error:
        raise error


def check_table_for_last_updated(table_name, last_ingested_time, conn):
    try:
        table_lists = conn.run(f"SELECT last_updated FROM {identifier(table_name)};")
        for time in table_lists:
            print(time[0], last_ingested_time)
            if time[0] != last_ingested_time:
                return True
        return False
    except DatabaseError as error:
        print(f"Something wrong with query: {error.args[0]['M']}")
        raise error

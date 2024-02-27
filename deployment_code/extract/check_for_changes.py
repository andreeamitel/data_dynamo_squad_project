from pg8000.native import identifier, literal


def check_for_changes(db_conn, last_ingested_time):
    """
    This functions goes through the tables in the database
    and returns the ones that have been changed which is
    determined by the util function check_table_for_last_updated.
    Args:\n
        A connection to the database
        Last_ingested_time: A date of str type

    Returns:\n
        A list of table names
    """

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
        if check_table_for_last_updated(table, last_ingested_time, db_conn)
    ]

    return result


def check_table_for_last_updated(table_name, last_ingested_time, conn):
    """
    This function goes through the last_updated column of
    one table and checks if
    the last updated time is different to the last ingested time.
    Args:\n
        A table name
        Last ingested time: A date in datetime format
        A connection to database

    Returns:\n
        True: If last ingested time is not equal to last updated time
        False: If both times are equal
    """

    times_for_tables = conn.run(
        f"""SELECT last_updated FROM {identifier(table_name)}
        WHERE created_at > '{last_ingested_time}'
        OR last_updated > '{last_ingested_time}';;"""
    )
    print("check_table sql worked")
    if len(times_for_tables) > 0:
        return True
    return False

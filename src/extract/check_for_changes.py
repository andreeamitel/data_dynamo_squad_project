from pg8000.native import Connection as conn, identifier, DatabaseError
from datetime import datetime


'''
Contains functions that check for updated or new data in the database.
Functions:\n
    check_for_changes
    check_table_for_last_updated

'''

def check_for_changes(db_conn, last_ingested_time):
    '''
    This functions goes through the tables in the database 
    and returns the ones that have been changed which is 
    determined by the util function check_table_for_last_updated.
    Args:\n
        A connection to the database
        Last_ingested_time: A date of str type
    
    Returns:\n
        A list of table names
    '''
    try:
        format_to_use = "%Y-%m-%d %H:%M:%S.%f"
        #date_time = datetime.strptime(last_ingested_time, format_to_use)
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
    except TypeError as error:
        raise error


def check_table_for_last_updated(table_name, last_ingested_time, conn):
    '''
    This function goes through the last_updated column of one table and checks if 
    the last updated time is different to the last ingested time.
    Args:\n
        A table name
        Last ingested time: A date in datetime format
        A connection to database

    Returns:\n
        True: If last ingested time is not equal to last updated time
        False: If both times are equal
    '''
    try:
        table_lists = conn.run(
            f"SELECT last_updated FROM {identifier(table_name)};"
            )
        for time in table_lists:
            if time[0] != last_ingested_time:
                return True
        return False
    except DatabaseError as error:
        print(f"Something wrong with query: {error.args[0]['M']}", '<<<<')
        raise error

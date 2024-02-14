from pg8000.native import Connection

def extract_data(table_name, db_conn):
    """
    This function extracts the data from a table in totesys database.

    Args:
    table_name:string

    Returns:
    A list of dictionaries of all the data in the table input.
  
    """
    try:
        rows = db_conn.run(f"SELECT array_to_json(array_agg({table_name}), FALSE) AS table_dict FROM {table_name};")
        data = rows[0][0]
        return data
    except Exception as err:
        print("Error when running SQL query in extract_data function", err)
        raise err
    
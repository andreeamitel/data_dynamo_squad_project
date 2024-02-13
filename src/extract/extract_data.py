from pg8000.native import Connection

def extract_data(table_name, db_conn):
    """
    This function extracts the data from a table in totesys database.

    Args:
    table_name:string

    Returns:
    A list of dictionaries of all the data in the table input.
  
    """
    rows = db_conn.run(f"SELECT * FROM {table_name};")
    data = [{
            "currency_id": row[0],
            "currency_code": row[1],
            "created_at": row[2],
            "updated_at": row[3]
            }
            for row in rows]
    return data
    
from pg8000.exceptions import DatabaseError

def extract_data(table_name, db_conn, last_ingested_time):
    """
    This function extracts the data from a table in totesys database.

    Args:
    `table_name`: `string`
    `db_conn`: `func` = `pg8000.native.Connection()`
    `last_ingested_time`: `string` of `timestamp`

    Returns:
    A list of dictionaries of all the data in the table input.
  
    """
    try:
        rows = db_conn.run(f"""
            SELECT array_to_json(array_agg({table_name}), FALSE) AS table_dict
            FROM {table_name}
            WHERE created_at > '{last_ingested_time}' OR last_updated > '{last_ingested_time}';
            """)
        data = rows[0][0]
        return data
    except Exception:
        return "Error when running SQL query in extract_data function"
    
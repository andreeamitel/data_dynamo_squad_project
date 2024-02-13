from pg8000.native import Connection

def extract_data():
    con = pg8000.native.Connection("postgres", password="cpsnow")
    """
    This function extracts the data from a table in totesys database.

    Args:
    table_name:string

    Returns:
    A list of dictionaries of all the data in the table input.
  
    """
    pass
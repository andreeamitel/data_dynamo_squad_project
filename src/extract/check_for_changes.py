import boto3
from  pprint import pprint
from connection import conn
def check_for_changes(db_conn):
    s3 = boto3.client('s3')
    response = s3.get_object(
        SortOrder='asc'
        )
    result = db_conn.run('SELECT * FROM sales_order;')
    return result

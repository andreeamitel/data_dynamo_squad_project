import boto3
from  pprint import pprint
from connection import conn, literal, identifier
import datetime

# def check_for_changes(db_conn):
#     date_time = get_last_ingested_time()

#     address_last_updated = conn.run('SELECT last_updated FROM address;')

#     return check_table_for_last_updated(address_last_updated, 'address', date_time)




# def check_table_for_last_updated(table_lists, table_name, last_ingested_time):
    # for time in table_lists:
    #     if time != last_ingested_time:
    #         return table_name

def get_last_ingested_time():
    s3 = boto3.client('s3')
    response = s3.get_object(
    Bucket='ingested-bucket-20240213151611822700000004',
    Key='last-ingested-time.txt',
    )
   datetime.strptime('31/01/22 23:59:59.999999',

                  '%d/%m/%y %H:%M:%S.%f')

    print(datetime.strptime(response['Body'].read().decode('utf-8')))

def check_for_changes(db_conn):
    date_time = get_last_ingested_time()
    print(date_time)
    table_names = ["address"]
    result = [table for table in table_names if check_table_for_last_updated(table, date_time, db_conn)]

    return result

def check_table_for_last_updated(table_name, last_ingested_time, conn):
    table_lists = conn.run(f"SELECT last_updated FROM ${identifier(table_name)};")
    for time in table_lists:
        if time > last_ingested_time:
            return True
# print(check_for_changes(conn))
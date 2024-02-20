import boto3
import re
from datetime import datetime
import json
def get_latest_data(table_name, s3, ingested_bucket_name):
    
    #need the bit underneath if we are pulling the entire bucket - otherwise not
    response = s3.list_objects(Bucket = ingested_bucket_name)
    pattern = re.compile(fr'\b{re.escape(table_name)}\b', re.IGNORECASE)

    list_to_use = [file_path for file_path in response if re.search(pattern, file_path)]
    date_pattern = re.compile(r'(\d{4}-\d{2}-\d{2})')  # Assuming dates are in YYYY-MM-DD format
    entries_with_dates = [(entry, datetime.strptime(date_str.group(), '%Y-%m-%d')) for entry in list_to_use if (date_str := re.search(date_pattern, entry))]

    if not entries_with_dates:
        return None

    most_recent_entry = max(entries_with_dates, key=lambda x: x[1])
    lastest_one = most_recent_entry[0]
    needed_json_dict = s3.get_object(bucket = ingested_bucket_name, key = lastest_one)

my_list = ['/2023-01-15/tablename', '/2022-02-20/tablename', '/2021-12-10/tablename', "ifdanoisfanoasnf"]
s3 = boto3.client("s3")
result = get_latest_data(my_list, s3, "hi")
print(result)
# import re
# from datetime import datetime

# def find_most_recent_entry(input_list):
#     date_pattern = re.compile(r'(\d{4}-\d{2}-\d{2})')  # Assuming dates are in YYYY-MM-DD format
#     entries_with_dates = [(entry, datetime.strptime(date_str.group(), '%Y-%m-%d')) for entry in input_list if (date_str := re.search(date_pattern, entry))]

#     if not entries_with_dates:
#         return None

#     most_recent_entry = max(entries_with_dates, key=lambda x: x[1])
#     return most_recent_entry[0]

# # Example usage:
# my_list = ['/2022-01-15/tablename', '/2022-02-20/tablename', '/2021-12-10/tablename']
# result = find_most_recent_entry(my_list)

# print(result)
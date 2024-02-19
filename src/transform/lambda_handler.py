import boto3
import re

def lambda_handler(event, context):
    """
    ### Args:
        event:
            a valid S3 PutObject event -
            see https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-content-structure.html
        context:
            a valid AWS lambda Python context object - see
            https://docs.aws.amazon.com/lambda/latest/dg/python-context.html
    ### Functionality:
    - uses function get_latest_data() to get data from ingestion bucket and convert to python  
    - passed into unit functions to change from OLTP to OLAP
    - calls python_to_parquet function -  which changes python to parquet and stores in processed bucket  
    """
    pass
    sales_dict = get_latest_data("sales_order", s3, bucket_name)
    currency_dict = get_latest_data("currency", s3, bucket_name)
    design_dict = get_latest_data("design", s3, bucket_name)
    address_dict = get_latest_data("address", s3, bucket_name)
    counterparty_dict = get_latest_data("counterparty", s3, bucket_name)
    staff_dict = get_latest_data("staff", s3, bucket_name)
    department_dict = get_latest_data("department", s3, bucket_name)

    #call unit functions --------- ALL OF THESE TAKE A DICTIONARIES WITH KEY VALUE PAIR OF TABLE_NAME AND A THE TABLE  - EACH WILL RETURN A DICTIONARY WITH KEY VALUE PAIR OF NEW TABLE NAME AND THE TABLE ITSELF - sorry for shouting :) - this was nathan and ben
    
    #get bucket name from ingestion bucket
    # get timestamp from ingestion bucket 
    #for loop through new tables
        #python_to_parket(table, processed_bucket_name, timestamp)
    
    
    # finished :)
lambda_handler(1,2)
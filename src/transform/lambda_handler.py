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
    - from ingestion bucket transforms files to python 
    - passed into unit functions to change from OLTP to OLAP
    - calls python_to_parquet function -  which changes python to parquet and stores in processed bucket  
    """
    pass
    list_of_tables = ["currency, sales"]  
    
lambda_handler(1,2)
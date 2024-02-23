from pg8000.native import Connection
import pg8000
import pandas as pd
import awswrangler as wr
from sqlalchemy import create_engine, inspect, Numeric, types
import pyarrow as py
import numpy as np 
from decimal import Decimal,getcontext

def lambda_handler(event, context):
    """
    This function is responsible for periodically scheduling an update of the data warehouse by taking the parquet file from the processed bucket.

    Args:
    event:
        a valid S3 PutObject event -
            see https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-content-structure.html
    context:
        a valid AWS lambda Python context object - see
            https://docs.aws.amazon.com/lambda/latest/dg/python-context.html
    
    Functionality:
    get database connection from secrets manager
    get parquet data from processed bucket
    load data to RDS
    """
    # column_data_types = {
    #         "sales_record_id": "int32",
    #         "sales_order_id": "int64",
    #         "created_date": pd.to_datetime(arg="Series"),
    #         "created_time":  pd.to_datetime(format="%H:%M:%S.%f"),
    #         "last_updated_date": pd.to_datetime(format="%Y-%m-%d"),
    #         "last_updated_time": pd.to_datetime(format="%Y-%m-%d"),
    #         "design_id": "int64",
    #         "sales_staff_id": "int64",
    #         "counterparty_id": "int64",
    #         "units_sold": "int64",
    #         "unit_price": "float",
    #         "currency_id": "int64",
    #         "agreed_delivery_date": pd.to_datetime(format="%Y-%m-%d"),
    #         "agreed_payment_date": pd.to_datetime(format="%Y-%m-%d"),
    #         "agreed_delivery_location_id": "int64",
    # }
    test_parquet_read = wr.s3.read_parquet(
        "s3://processed-bucket-20240222143124212400000004/fact_sales_order/2022-02-14 16:54:36.774180.parquet"
    )

    # test_parquet_read[['created_date', 'created_time']] = test_parquet_read[['created_date', 'created_time']].astype(str)
    # print(test_parquet_read[['unit_price']])

    # test_parquet_read[['unit_price']] = test_parquet_read[['unit_price']].astype("float")
    # print(test_parquet_read.dtypes)
    # print(test_parquet_read[['unit_price']])
    
    dbapi_con = pg8000.connect(      
        host= "nc-data-eng-project-dw-prod.chpsczt8h1nu.eu-west-2.rds.amazonaws.com",
        port= "5432",
        user= "project_team_0",
        password= "Z4s1r0ZGJjJUGC",
        database= "postgres",)
   
    t = wr.postgresql.to_sql(df=test_parquet_read, con=dbapi_con, table="fact_sales_order", dtype= {
        "sales_order_id": types.INTEGER,
        "created_date": types.String,
        "created_time": types.String,
        "last_updated_date": types.String,
        "last_updated_time": types.String,
        "design_id": types.INTEGER,
        "sales_staff_id": types.INTEGER,
        "counterparty_id": types.INTEGER,
        "units_sold": types.INTEGER,
        "unit_price": types.Float,
        "currency_id": types.INTEGER,
        "agreed_delivery_date": types.String,
        "agreed_payment_date": types.String,
        "agreed_delivery_location_id": types.INTEGER
    }, mode="append",index=True, schema="project_team_0")
    print(t)

 
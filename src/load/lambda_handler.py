from pg8000.native import Connection
import pg8000
import awswrangler as wr
from sqlalchemy import create_engine, inspect, Numeric, types
import pyarrow as py
import numpy as np
from decimal import Decimal, getcontext


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
    test_parquet_read = wr.s3.read_parquet(
        "s3://processed-bucket-20240222143124212400000004/fact_sales_order/2022-02-14 16:54:36.774180.parquet"
    )
    print(test_parquet_read.dtypes)

    dbapi_con = pg8000.Connection(
        host="nc-data-eng-project-dw-prod.chpsczt8h1nu.eu-west-2.rds.amazonaws.com",
        port="5432",
        user="project_team_0",
        password="Z4s1r0ZGJjJUGC",
        database="postgres",
    )

    wr.postgresql.to_sql(
        df=test_parquet_read,
        con=dbapi_con,
        table="fact_sales_order",
        mode="overwrite",
        schema="project_team_0",
        use_column_names=True,
    )

from pg8000.native import Connection
import pandas as pd
import awswrangler as wr
from sqlalchemy import create_engine

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
    conn = Connection(
            host = "testdb.eu-west-1.rds.amazonaws.com",
            port = "1234",
            user = "project_team_0",
            password = "Z4s1r0ZGJjJUGC",
            database="postgres",
        )
    test_parquet_read = wr.s3.read_parquet(
        "s3://processed-bucket-20240222143124212400000004/2022-02-14 16:54:36.774180/fact_sales_order.parquet"
    )
    # foo = test_parquet_read.to_sql('fact_sales_order', "testdb.eu-west-1.rds.amazonaws.com", if_exists="append", index=False)

    # conn = Connection(
    #         host = "nc-data-eng-project-dw-prod.chpsczt8h1nu.eu-west-2.rds.amazonaws.com",
    #         port = "5432",
    #         user = "project_team_0",
    #         password = "Z4s1r0ZGJjJUGC",
    #         database="postgres",
    #     )
    # response = conn.run("SELECT * FROM project_team_0;")
    # return response
    # eng_postgresql = wr.postgresql.connect(db_type="postgresql", host="nc-data-eng-project-dw-prod.chpsczt8h1nu.eu-west-2.rds.amazonaws.com", port=5432, database="postgres", user="project_team_0", password="Z4s1r0ZGJjJUGC")
    # # print(dir(wr.sqlserver))

    
# print(lambda_handler())
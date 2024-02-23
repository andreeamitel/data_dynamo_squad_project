from src.load.lambda_handler import lambda_handler
from src.transform.python_to_parquet import python_to_parquet
import pytest
import boto3
from moto import mock_aws
from unittest.mock import patch, Mock
import json
import pandas as pd
import pprint
import awswrangler as wr


@pytest.fixture(scope="function")
def aws_s3():
    with mock_aws():
        yield boto3.client("s3", region_name="eu-west-2")


@pytest.fixture(scope="function")
def aws_secrets():
    with mock_aws():
        yield boto3.client("secretsmanager", region_name="eu-west-2")


@pytest.fixture
def create_bucket1(aws_s3):
    boto3.client("s3").create_bucket(
        Bucket="processed-bucket-20240222143124212400000004",
        CreateBucketConfiguration={"LocationConstraint": "eu-west-2"},
    )


@pytest.fixture
def create_parquet_file(create_bucket1):
    with open("./test/load/sales_order.json", "r") as f:
        file = json.load(f)
        python_to_parquet(
            file,
            "processed-bucket-20240222143124212400000004",
            "2022-02-14 16:54:36.774180",
        )

@pytest.fixture
def mock_conn():
    with patch("src.load.lambda_handler.Connection") as conn:
        yield conn
@pytest.fixture
def rds():
    conn = boto3.client("rds", region_name="eu-west-2")
    database = conn.create_db_instance(
        DBInstanceIdentifier="db-master-1",
        AllocatedStorage=10,
        Engine="postgres",
        DBName="testdb",
        DBInstanceClass="db.m1.small",
        LicenseModel="license-included",
        MasterUsername="root",
        MasterUserPassword="hunter2",
        Port=1234,
        DBSecurityGroups=["my_sg"],
        VpcSecurityGroupIds=["sg-123456"],
    )
    db_instance = database["DBInstance"]
    # pprint(db_instance)

@pytest.mark.describe("lambda_handler")
@pytest.mark.it("should read one file")
@patch("src.load.lambda_handler.wr.sqlserver.to_sql")
def test_read_one_file(to_sql, create_parquet_file, mock_conn, rds):
    result = lambda_handler('event', 'context')
    # print(isinstance(create_parquet_file, pd.DataFrame))
    mock_parquet = wr.s3.read_parquet(
        "s3://processed-bucket-20240222143124212400000004/2022-02-14 16:54:36.774180/fact_sales_order.parquet"
    )
    to_sql.assert_called_once_with(mock_parquet)



# @mock_aws
# class TestData(unittest.TestCase):
#     def setUp(self):
#         """Initial setup."""
#         # Setup db

#         test_instances = db_conn.create_db_instance(
#             DBName='test_db',
#             AllocatedStorage=10,
#             StorageType='standard',
#             DBInstanceIdentifier='instance',
#             DBInstanceClass='db.t2.micro',
#             Engine='postgres',
#             MasterUsername='postgres_user',
#             MasterUserPassword='p$ssw$rd',
#             AvailabilityZone='us-east-1',
#             PubliclyAccessible=True,
#             DBSecurityGroups=["my_sg"],
#             VpcSecurityGroupIds=["sg-123456"],
#             Port=5432
#         )
#         db_instance = test_instances["DBInstance"]

#         user_name = db_instance['MasterUsername']
#         host = db_instance['Endpoint']['Address']
#         port = db_instance['Endpoint']['Port']
#         db_name = db_instance['DBName']
#         conn_str = f'postgresql://{user_name}:p$ssw$rd@{host}:{port}/{db_name}'
#         print(conn_str)
#         engine_con = create_engine(conn_str)
#         engine_con.connect()


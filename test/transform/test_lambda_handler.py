from src.transform.lambda_handler import lambda_handler
import pytest
from unittest.mock import patch
import boto3
from moto import mock_aws


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
    boto3.client("s3").create_bucket(Bucket = "ingested-bucket-20240222080432331400000006",
    CreateBucketConfiguration = {
        'LocationConstraint': 'eu-west-2'
    })
@pytest.fixture
def create_error_bucket(aws_s3):
    boto3.client("s3").create_bucket(Bucket = "error_bucket",
    CreateBucketConfiguration = {
        'LocationConstraint': 'eu-west-2'
    })

@pytest.fixture
def create_object(create_bucket1):
    with open("./test/Last_Ingested.json", "w") as f:
        json.dump({'last_ingested_time': "2022-02-14 16:54:36.774180","new_data_found" : True}, f)
    boto3.client("s3").upload_file("test/Last_Ingested.json", "ingested-bucket-20240213151611822700000004","Last_Ingested.json")


@pytest.fixture
def secretmanager(aws_secrets):
    aws_secrets.create_secret(Name = "database_creds_test", 
    SecretString = '{"hostname":"example_host.com","port": "4321", "database" : "example_database", "username": "project_team_0", "password":"EXAMPLE-PASSWORD"}')
    aws_secrets.create_secret(Name = "ingestion_bucket_02", SecretString = "ingested-bucket-20240213151611822700000004")
@pytest.fixture
def mock_conn():
    with patch("src.extract.lambda_handler.Connection") as conn:
        yield conn
        
test_event = {  
   "Records":[  
      {  
         "eventVersion":"2.2",
         "eventSource":"aws:s3",
         "awsRegion":"us-west-2",
         "eventTime":"The time, in ISO-8601 format, for example, 1970-01-01T00:00:00.000Z, when Amazon S3 finished processing the request",
         "eventName":"event-type",
         "userIdentity":{  
            "principalId":"Amazon-customer-ID-of-the-user-who-caused-the-event"
         },
         "requestParameters":{  
            "sourceIPAddress":"ip-address-where-request-came-from"
         },
         "responseElements":{  
            "x-amz-request-id":"Amazon S3 generated request ID",
            "x-amz-id-2":"Amazon S3 host that processed the request"
         },
         "s3":{  
            "s3SchemaVersion":"1.0",
            "configurationId":"ID found in the bucket notification configuration",
            "bucket":{  
               "name":"ingested-bucket-20240222080432331400000006",
               "ownerIdentity":{  
                  "principalId":"Amazon-customer-ID-of-the-bucket-owner"
               },
               "arn":"bucket-ARN"
            },
            "object":{  
               "key":"2024-02-22 08:05/staff.json",
               "size":"object-size in bytes",
               "eTag":"object eTag",
               "versionId":"object version if bucket is versioning-enabled, otherwise null",
               "sequencer": "a string representation of a hexadecimal value used to determine event sequence, only used with PUTs and DELETEs"
            }
         },
         "glacierEventData": {
            "restoreEventData": {
               "lifecycleRestorationExpiryTime": "The time, in ISO-8601 format, for example, 1970-01-01T00:00:00.000Z, of Restore Expiry",
               "lifecycleRestoreStorageClass": "Source storage class for restore"
            }
         }
      }
   ]
}

test_context = 2
@pytest.mark.describe("lambda_handler")
@pytest.mark.it("should test that the get_latest_data is called")
@patch("src.transform.lambda_handler.get_latest_data", return_value = {})
def test_get_latest_data(mock_get_latest_data, test_event, test_context):
    lambda_handler(test_event, test_context)
    mock_get_latest_data.assert_called_once()
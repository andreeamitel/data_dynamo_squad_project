from src.transform.lambda_handler import lambda_handler
import pytest
from unittest.mock import patch
import boto3
from moto import mock_aws
from datetime import datetime

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
def create_object(create_bucket1):
    date_time = datetime.now().isoformat()
    boto3.client("s3").put_object(Body = f"{date_time}", Bucket = "ingested-bucket-20240222080432331400000006", Key = "last_ingested.txt")

@pytest.fixture
def secretmanager(aws_secrets):
    aws_secrets.create_secret(Name = "processed_bucket", SecretString = "processed_bucket123")

        
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
               "key":"last_ingested.txt",
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
def test_get_latest_data(mock_get_latest_data, create_bucket1, create_object, secretmanager):
    lambda_handler(test_event, test_context)
    mock_get_latest_data.assert_called_once()
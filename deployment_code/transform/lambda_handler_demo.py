import json
import urllib.parse
import boto3
from transform.dim_currency import dim_currency
from transform.dim_counterparty import dim_counterparty
from transform.dim_staff import dim_staff
from pprint import pprint

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
def dim_sales_order():
    pass

def lambda_handler(event, context=None):

   #Get bucket and key from s3 event object (example above)
   bucket = event['Records'][0]['s3']['bucket']['name']
   key = event['Records'][0]['s3']['object']['key']

   #Get s3 file and table name from event object
   s3 = boto3.client("s3")
   file = json.load(s3.get_object(Bucket=bucket, Key=key)["Body"])
   head, sep, tail = key.partition("/")
   file_date = head
   # print(file_date)
   table = list(file.keys())[0]
   # print(table)

   #Dictionary to define all the functions

   file_function_dict = {
      "sales_order": dim_sales_order,
      "currency": dim_currency,
      "counterparty": dim_counterparty,
      # "design": dim_design,
      # "address": dim_location,
      "staff": dim_staff,     
   }
   file_process_function = file_function_dict[f"{table}"]

   # Use the file to get the right function
   if table == "staff":
       
       address_file = f"{file_date}/department.json"
      #  print(address_file)
       address = json.load(s3.get_object(Bucket=bucket, Key=address_file)["Body"])
      #  print(address)
       counterparty = file_process_function(file, address)
   # run_file = file_process_function(file)
   
   # pprint(address)
   pprint(counterparty)
    


lambda_handler(test_event)

    


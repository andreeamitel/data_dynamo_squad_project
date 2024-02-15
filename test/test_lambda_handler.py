# from src.extract.lambda_handler import lambda_handler
# import pytest
# import boto3
# from datetime import datetime 
# from moto import mock_aws
# from unittest.mock import patch

# @pytest.mark.describe("lambda_handler")
# @pytest.mark.it("Test that a json file gets written to the ingestion bucket in aws")
# @mock_aws
# @patch("src.extract.lambda_handler.datetime")
# def test_write_json_file(mock_time):
#     mock_time.now().isoformat.return_value = "2024-02-14 16:54:36.774180"
#     s3 = boto3.client("s3")
#     s3.create_bucket(Bucket = "ingested-bucket-20240213151611822700000004",
#     CreateBucketConfiguration = {
#         'LocationConstraint': 'eu-west-2',
#     })
#     lambda_handler()
#     result = s3.get_object(Bucket = "ingested-bucket-20240213151611822700000004",
#     Key = "Last_Ingested.json")
#     #need to finish assert
#     print((result["Body"].read()))
#     assert result["Body"].read()=={"last_ingested_time": "2024-02-14 16:54:36.774180", "new_data_found": true}

# @pytest.mark.describe("lambda_handler")
# @pytest.mark.it("Test that a connection has been established to a database - using secretsmanager")
# @patch("src.extract.lambda_handler.Connection")
# @mock_aws
# def test_database_conn(mock_conn):
#     pass

# @pytest.mark.describe("lambda_handler")
# @pytest.mark.it("Test that all internal functions are called")
# @patch("src.extract.lambda_handler.check_for_changes")
# @patch("src.extract.lambda_handler.extract_data")
# @patch("src.extract.lambda_handler.data_conversion")
# def test_functions_are_called(mock_data_conv, mock_extract_data, mock_check_changes):
#     pass

# @pytest.mark.describe("lambda_handler")
# @pytest.mark.it("Integration test - Test that data_conversion gets called with outputs from extract_data and appears in bucket")
# @patch("src.extract.lambda_handler.check_for_changes")
# @patch("src.extract.lambda_handler.extract_data")
# @mock_aws
# def test_data_conversion(mock_extract_data, mock_check_changes):
#     pass

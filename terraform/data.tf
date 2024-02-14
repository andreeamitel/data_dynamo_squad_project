data "aws_caller_identity" "current" {}

data "aws_region" "current" {}

# data "archive_file" "ingest_lambda" {
#   type        = "zip"
# #   change source_file later after creating py file
#   source_file = "../src/reader.py"
#   output_path = "ingest_lambda.zip"
# }
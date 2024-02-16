data "aws_caller_identity" "current" {}

data "aws_region" "current" {}

data "archive_file" "ingest_lambda" {
  type        = "zip"
  source_dir = "../src/extract"
  output_path = "./ingest_lambda.zip"
}
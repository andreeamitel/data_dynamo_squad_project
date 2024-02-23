data "aws_caller_identity" "current" {}

data "aws_region" "current" {}

data "archive_file" "process_layer_zip" {
  type        = "zip"
  source_dir = "./transform/python/"
  output_path = "./layer2.zip"
  excludes = ["__pycache__"]
}

data "archive_file" "process_lambda" {
  type        = "zip"
  source_dir  = "../deployment_code"
  output_path = "./transform_lambda.zip"
  excludes = ["extract", "load"]
}

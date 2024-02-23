data "aws_caller_identity" "current" {}

data "aws_region" "current" {}

data "archive_file" "process_lambda" {
  type        = "zip"
  source_dir  = "../deployment_code"
  output_path = "./transform_lambda.zip"
  excludes    = ["extract", "load"]
}

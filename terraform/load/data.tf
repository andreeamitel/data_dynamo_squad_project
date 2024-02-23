data "aws_caller_identity" "current" {}

data "aws_region" "current" {}

data "archive_file" "load_lambda" {
  type        = "zip"
  source_dir  = "../deployment_code"
  output_path = "./load_lambda.zip"
  excludes    = ["transform", "extract"]
}

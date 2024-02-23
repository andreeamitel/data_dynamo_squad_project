data "aws_caller_identity" "current" {}

data "aws_region" "current" {}

data "archive_file" "ingest_lambda" {
  type        = "zip"
  source_dir  = "../deployment_code"
  output_path = "./ingest_lambda.zip"
  excludes    = ["transform", "load"]
}
# data "archive_file" "layer_zip" {
#   type        = "zip"
#   source_dir = "../../../venv/lib/python3.11/site-packages"
#   output_path = "./layer.zip"
#   excludes = ["boto3", "boto3-1.34.40.dist-info", "botocore-1.34.40.dist-info", "botocore", "pandas", "pandas-2.2.0.dist-info", "pyarrow-15.0.0.dist-info", "moto", "moto-5.0.1.dist-info", "pyarrow", "sympy", "sympy-1.12.dist-info", "numpy", "numpy-1.26.4.dist-info", "numpy.libs"]
# }

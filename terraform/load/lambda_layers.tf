locals {
  layer_zip_path    = "./load_layer.zip"
  layer_name        = "my_load_lambda_requirements_layer"
}

# upload zip file to s3
resource "aws_s3_object" "lambda_layer_zip" {
  bucket     = aws_s3_bucket.code_bucket.id
  key        = "lambda_layers/${local.layer_name}/${local.layer_zip_path}"
  source     = local.layer_zip_path
  depends_on = [data.archive_file.load_lambda_layer] # triggered only if the zip file is created
}

# create lambda layer from s3 object
resource "aws_lambda_layer_version" "my-lambda-layer" {
  s3_bucket           = var.code_buck_id
  s3_key              = aws_s3_object.lambda_layer_zip.key
  layer_name          = local.layer_name
  compatible_runtimes = ["python3.11"]
  skip_destroy        = true
  depends_on          = [aws_s3_object.lambda_layer_zip] # triggered only if the zip file is uploaded to the bucket
}
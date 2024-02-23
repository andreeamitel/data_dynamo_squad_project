locals {
  layer_zip_path    = "./layer3.zip"
  layer_name        = "my_lambda3_requirements_layer"
  requirements_path = "${path.root}/../../../requirements.txt"
}

# create zip file from requirements.txt. Triggers only when the file is updated
resource "null_resource" "lambda_layer" {
  # the command to install python and dependencies to the machine and zips
  provisioner "local-exec" {
    command = <<EOT
      rm -rf python3/python3
      mkdir python/python3
      pip3 install pg8000 -t python/python3
      zip -r layer3.zip python/python3
    EOT
  }
}

# upload zip file to s3
resource "aws_s3_object" "lambda_layer_zip" {
  bucket     = var.code_buck_id
  key        = "lambda_layers/${local.layer_name}/${local.layer_zip_path}"
  source     = local.layer_zip_path
  depends_on = [null_resource.lambda_layer] # triggered only if the zip file is created
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
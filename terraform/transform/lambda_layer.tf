#define variables
locals {
  layer_zip_path = "./layer2.zip"
  layer_name     = "my_lambda2_requirements_layer"
}

# # create zip file from requirements.txt. Triggers only when the file is updated
# resource "null_resource" "lambda_layer" {
#   # the command to install python and dependencies to the machine and zips
#  provisioner "local-exec" {
#     command = <<EOT
#       rm -rf transform/python
#       mkdir transform/python
#       cd transform/python
#       pip3 install pandas 
#       cd ../../
#       zip -r layer2.zip  transform/python/numpy
#       zip -r layer2.zip  transform/python/numpy-1.26.4.dist-info
#       zip -r layer2.zip  transform/python/numpy.libs
#       zip -r layer2.zip  transform/python/pandas
#       zip -r layer2.zip  transform/python/pandas-2.2.0.dist-info
#       zip -r layer2.zip  transform/python/pytz
#       zip -r layer2.zip  transform/python/pytz-2024.1.dist-info
#     EOT
#   }
# }

# upload zip file to s3
resource "aws_s3_object" "lambda_layer_zip" {
  bucket     = var.code_buck_id
  key        = "lambda_layers/${local.layer_name}/${local.layer_zip_path}"
  source     = local.layer_zip_path
  depends_on = [data.archive_file.process_layer_zip] # triggered only if the zip file is created
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

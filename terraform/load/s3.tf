resource "aws_s3_object" "load_lambda_code" {
  bucket = var.code_buck_id
  key    = "lambda_code/load_lambda.zip"
  source = "./load_lambda.zip"
}

resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = var.processed_bucket_id

  lambda_function {
    lambda_function_arn = aws_lambda_function.load_lambda.arn
    events              = ["s3:ObjectCreated:*"]
    filter_suffix       = ".txt"
  }
  depends_on = [aws_lambda_permission.allow_s3]
}

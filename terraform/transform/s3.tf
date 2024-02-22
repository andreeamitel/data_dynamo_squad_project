
resource "aws_s3_bucket" "processed_bucket" {
  bucket_prefix = "${var.bucket_name}-"
}
resource "aws_s3_bucket" "code_bucket-processed" {
  bucket_prefix = "${var.bucket_name}-code-"
}

resource "aws_s3_object" "process_lambda_code" {
  bucket = aws_s3_bucket.code_bucket-processed.id
  key    = "lambda_code/process_lambda.zip"
  source = "./function.zip"

}


resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = var.ingested_bucket_id

  lambda_function {
    lambda_function_arn = aws_lambda_function.process_lambda.arn
    events = ["s3:ObjectCreated:*"]
    filter_suffix = ".txt"
  }
  depends_on = [ aws_lambda_permission.allow_s3 ]
}
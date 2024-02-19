resource "aws_s3_bucket" "processed_bucket" {
  bucket_prefix = "${var.bucket_name}-"
}
resource "aws_s3_bucket" "code_bucket-processed" {
  bucket_prefix = "${var.bucket_name}-"
}

resource "aws_s3_object" "process_lambda_code" {
  bucket = aws_s3_bucket.code_bucket-processed.id
  key    = "lambda_code/process_lambda.zip"
  # source = "${path.module}/process_lambda.zip"
  source = "${path.module}./../dummy_function/function.zip"

}
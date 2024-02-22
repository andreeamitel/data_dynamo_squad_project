
resource "aws_s3_bucket" "processed_bucket" {
  bucket_prefix = "${var.bucket_name}-"
}
resource "aws_s3_bucket" "code_bucket-processed" {
  bucket_prefix = "${var.bucket_name}-code-"
}

resource "aws_s3_object" "process_lambda_code" {
  bucket = aws_s3_bucket.code_bucket-processed.id
  key    = "lambda_code/process_lambda.zip"
  # source = "${path.module}/process_lambda.zip"
  source = "${path.module}/../function.zip"
  # source = "dummy_function/event.zip"

}

# resource "aws_s3_bucket_notification" "bucket_notification" {
#   bucket = "ingested-bucket-20240220192448927000000006"
#   lambda_function {
#     lambda_function_arn = aws_lambda_function.process_lambda.arn
#     events = ["s3:ObjectCreated:*"]
#   }
#   depends_on = [ aws_lambda_permission.allow_s3 ]
# }

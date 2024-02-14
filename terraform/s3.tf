

resource "aws_s3_bucket" "code_bucket" {
  bucket_prefix = "data-dynamo-squad-code-"
}

resource "aws_s3_bucket" "ingested_bucket" {
  bucket_prefix = "ingested-bucket-"
}
#needs to be changed to actual code when complete 

resource "aws_s3_object" "lambda_code" {
  bucket = aws_s3_bucket.code_bucket.id
  key = "lambda_code/function.zip"
  source = "${path.module}/../dummy_function/function.zip"
}


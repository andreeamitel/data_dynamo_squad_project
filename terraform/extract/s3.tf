

resource "aws_s3_bucket" "code_bucket" {
  bucket_prefix = "data-dynamo-squad-code-"
  force_destroy = true
}

resource "aws_s3_bucket" "ingested_bucket" {
  bucket_prefix = "ingested-bucket-"
  force_destroy = true
}
#needs to be changed to actual code when complete 

resource "aws_s3_object" "lambda_code" {
  bucket = aws_s3_bucket.code_bucket.id
  key = "lambda_code/ingest_lambda.zip"
  source = "./ingest_lambda.zip"
}




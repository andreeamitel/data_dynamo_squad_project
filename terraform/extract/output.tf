output "ingest_bucket_id" {
  value = aws_s3_bucket.ingested_bucket.id
}

output "ingest_bucket_arn" {
  value = aws_s3_bucket.ingested_bucket.arn
}

output "code_bucket_id" {
  value = aws_s3_bucket.code_bucket.id
  }
output "code_bucket_arn" {
  value = aws_s3_bucket.code_bucket.arn
  }

output "ingested_lambda_layer" {
  value = aws_lambda_layer_version.my-lambda-layer.arn
}

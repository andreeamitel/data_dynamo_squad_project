output "ingest_bucket_id" {
  value = aws_s3_bucket.ingested_bucket.id
}

output "ingest_bucket_arn" {
  value = aws_s3_bucket.ingested_bucket.arn
}

output "code_bucket_id" {
  value = aws_s3_bucket.code_bucket.id
}


resource "aws_secretsmanager_secret" "processed_bucket2" {
    name = "processed_bucket2"
    recovery_window_in_days = 0
}

resource "aws_secretsmanager_secret_version" "processed_bucket_values" {
  secret_id     = aws_secretsmanager_secret.processed_bucket2.id
  secret_string = aws_s3_bucket.processed_bucket.bucket
}

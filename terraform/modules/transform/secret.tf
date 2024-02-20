
resource "aws_secretsmanager_secret" "processed_bucket" {
    name = "processed_bucket"
    recovery_window_in_days = 0
}

resource "aws_secretsmanager_secret_version" "processed_bucket_values" {
  secret_id     = aws_secretsmanager_secret.processed_bucket.id
  secret_string = aws_s3_bucket.processed_bucket.bucket
}

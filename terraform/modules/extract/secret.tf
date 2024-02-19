resource "aws_secretsmanager_secret" "database_creds_secret" {
    name= "database_creds"
}


# need to input database creds each time run terraform plan and apply, 
# will be set up to auto when workflow set up

resource "aws_secretsmanager_secret_version" "database_creds_values" {
  secret_id     = aws_secretsmanager_secret.database_creds_secret.id
  secret_string = var.database_creds_var
}

resource "aws_secretsmanager_secret" "bucket" {
    name= "bucket"
}

resource "aws_secretsmanager_secret_version" "bucket_values" {
  secret_id     = aws_secretsmanager_secret.bucket.id
  secret_string = aws_s3_bucket.ingested_bucket.bucket
}

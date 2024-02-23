resource "aws_secretsmanager_secret" "database_creds_secret_load" {
  name                    = "load_database_creds"
  recovery_window_in_days = 0
}

resource "aws_secretsmanager_secret_version" "database_creds_values" {
  secret_id     = aws_secretsmanager_secret.database_creds_secret_load.id
  secret_string = var.load_database_creds
}

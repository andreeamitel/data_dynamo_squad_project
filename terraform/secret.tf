resource "aws_secretsmanager_secret" "example_secret" {
    name= "database_secret"

}

resource "aws_secretsmanager_secret_version" "example_secret_value" {
  secret_id     = aws_secretsmanager_secret.example_secret.id
  secret_string = "example-string-to-protect"
}
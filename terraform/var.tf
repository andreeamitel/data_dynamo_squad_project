variable "lambda_name" {
    type = string
    default = "ingest_lambda"
}
#secret for database creds

variable "database_creds_var" {
    type = string
}

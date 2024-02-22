variable "lambda_name" {
    type = string
    default = "ingest_lambda_2"
}
#secret for database creds

variable "database_creds_var" {
    type = string
}

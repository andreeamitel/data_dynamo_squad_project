variable "bucket_name" {
    type = string
    default = "processed-bucket"
}

variable "name_lambda_role" {
    type = string
    default = "lambda-role-tran-"
}

variable "lambda_name" {
    type = string
    default = "process_lambda"
}
variable "ingestion_bucket_name" {
    type = string
    default = "ingested-bucket-20240220192448927000000006"
}
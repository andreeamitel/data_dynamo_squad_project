variable "bucket_name" {
    type = string
    default = "processed-bucket"
}

variable "name_lambda_role" {
    type = string
    default = "lambda-role"
}

variable "lambda_name" {
    type = string
    default = "process_lambda"
}
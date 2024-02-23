variable "bucket_name" {
  type    = string
  default = "processed-bucket"
}

variable "name_lambda_role" {
  type    = string
  default = "lambda-role-tran-"
}

variable "lambda_name" {
  type    = string
  default = "process_lambda2"
}
variable "ingested_bucket_arn" {
  type = string
}

variable "ingested_bucket_id" {
  type = string
}

variable "code_buck_id" {
  type = string
}

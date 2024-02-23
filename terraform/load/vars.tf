variable "processed_bucket_arn" {
  type = string
}

variable "processed_bucket_id" {
  type = string
}

variable "name_lambda_role" {
  type    = string
  default = "lambda-role-load-"
}

variable "code_buck_id" {
  type = string
}

variable "lambda_name" {
  type    = string
  default = "lambda-load-"
}

variable "load_database_creds" {
  type = string

}

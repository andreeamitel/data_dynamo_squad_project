

# provider "aws" {
#     region= "eu-west-2"
# }

terraform {
   backend "s3" {
    bucket = "backend-project-bucket"
    key = "data/tfstate"
    region = "eu-west-2"
   }
}

# module "modules" {
#     source = "./modules"
# }
variable "secret_var" {
  type = string
}
# variable "in_bucket_id" {
#   type = string
#   default = module.extract.ingest_bucket_id
# }
module "extract" {
    source = "./extract" 
    database_creds_var = var.secret_var
}
module "transform" {
    source = "./transform" 
    ingested_bucket_id = module.extract.ingest_bucket_id
    ingested_bucket_arn = module.extract.ingest_bucket_arn
    code_buck_id = module.extract.code_bucket_id
    code_buck_arn = module.extract.code_bucket_arn
}

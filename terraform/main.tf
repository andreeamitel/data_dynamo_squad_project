

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
}



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
module "extract" {
    source = "./extract" 
    database_creds_var = "fake data"
}
module "transform" {
    source = "./transform" 
    ingest_lambda = module.extract.ingest_lambda_arn
}


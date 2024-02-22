

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
}
module "transform" {
    source = "./transform" 
}
variable "database_creds_var" {
    type = string
}

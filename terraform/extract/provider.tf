provider "aws" {
    region= "eu-west-2"
}

# terraform {
#    backend "s3" {
#     bucket = "backend-project-bucket"
#     key = "data/tfstate"
#     region = "eu-west-2"
#    }
# }
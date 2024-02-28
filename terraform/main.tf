terraform {
   backend "s3" {
    bucket = "backend-project-bucket"
    key = "data/tfstate"
    region = "eu-west-2"
   }
}

variable "secret_var" {
}
variable "load_cred_secret" {
  
}
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

module "load" {
  source = "./load" 
  processed_bucket_arn = module.transform.processed_bucket_arn
  processed_bucket_id = module.transform.processed_bucket_id
  code_buck_id = module.extract.code_bucket_id
  code_buck_arn = module.extract.code_bucket_arn
  load_database_creds = var.load_cred_secret
  ingested_lambda_layer = module.extract.ingested_lambda_layer
}

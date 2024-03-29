resource "aws_lambda_function" "process_lambda" {

  role          = aws_iam_role.lambda_process_role.arn
  function_name = var.lambda_name
  filename      = aws_s3_object.process_lambda_code.source
  handler       = "transform/lambda_handler.lambda_handler"
  runtime       = "python3.11"
  layers        = ["arn:aws:lambda:eu-west-2:336392948345:layer:AWSSDKPandas-Python311:7"]
  timeout          = 900
  source_code_hash = data.archive_file.process_lambda.output_base64sha256
}


resource "aws_lambda_permission" "allow_s3" {
  action         = "lambda:InvokeFunction"
  function_name  = aws_lambda_function.process_lambda.function_name
  principal      = "s3.amazonaws.com"
  source_arn     = var.ingested_bucket_arn
  source_account = data.aws_caller_identity.current.account_id
}

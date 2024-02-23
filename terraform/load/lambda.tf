resource "aws_lambda_function" "load_lambda" {

  role          = aws_iam_role.lambda_load_role.arn
  function_name = var.lambda_name
  filename      = aws_s3_object.load_lambda_code.source
  handler       = "event.lambda_handler" #needs changing
  runtime       = "python3.11"
  layers        = [aws_lambda_layer_version.my-lambda-layer.arn]
  timeout          = 30
  source_code_hash = data.archive_file.load_lambda.output_base64sha256
}


resource "aws_lambda_permission" "allow_s3" {
  action         = "lambda:InvokeFunction"
  function_name  = aws_lambda_function.load_lambda.function_name
  principal      = "s3.amazonaws.com"
  source_arn     = var.processed_bucket_arn
  source_account = data.aws_caller_identity.current.account_id
}
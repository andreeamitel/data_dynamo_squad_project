resource "aws_lambda_function" "process_lambda" {

  role          = aws_iam_role.lambda_process_role.arn
  function_name = var.lambda_name
  filename      = aws_s3_object.process_lambda_code.source
  handler       = "transform/lambda_handler.lambda_handler"
  runtime       = "python3.11"
  layers        = [aws_lambda_layer_version.my-lambda-layer.arn]
  timeout          = 30
  source_code_hash = data.archive_file.process_lambda.output_base64sha256
}


resource "aws_lambda_permission" "allow_s3" {
  action         = "lambda:InvokeFunction"
  function_name  = aws_lambda_function.process_lambda.function_name
  principal      = "s3.amazonaws.com"
  source_arn     = var.ingested_bucket_arn
  source_account = data.aws_caller_identity.current.account_id
}

# resource "aws_cloudwatch_event_rule" "tran_scheduler" {
#   name_prefix         = "processing_scheduler-"
#   schedule_expression = "rate(2 minutes)"
# }

# resource "aws_lambda_permission" "allow_tran_scheduler" {
#   action         = "lambda:InvokeFunction"
#   function_name  = aws_lambda_function.process_lambda.function_name
#   principal      = "events.amazonaws.com"
#   source_arn     = aws_cloudwatch_event_rule.tran_scheduler.arn
#   source_account = data.aws_caller_identity.current.account_id

# }

# resource "aws_cloudwatch_event_target" "tran_lambda_target" {
#   rule = aws_cloudwatch_event_rule.tran_scheduler.name
#   arn = aws_lambda_function.process_lambda.arn
# }

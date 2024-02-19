
resource "aws_lambda_function" "ingest_lambda" {
    
  role          = aws_iam_role.lambda_role.arn
  function_name = var.lambda_name
  filename      = aws_s3_object.lambda_code.source
  handler       = "../src/extract/lambda_handler.lambda_handler"
  runtime       = "python3.11"
  layers        = [aws_lambda_layer_version.my-lambda-layer.arn]
}

resource "aws_lambda_permission" "allow_s3" {
  action = "lambda:InvokeFunction"
  function_name = aws_lambda_function.ingest_lambda.function_name
  principal = "s3.amazonaws.com"
  source_arn = aws_s3_bucket.ingested_bucket.arn
  source_account = data.aws_caller_identity.current.account_id
}


resource "aws_cloudwatch_event_rule" "scheduler" {
    name_prefix = "ingestion_scheduler"
    schedule_expression = "rate(2 minutes)"
}

resource "aws_lambda_permission" "allow_scheduler" {
  action = "lambda:InvokeFunction"
  function_name = aws_lambda_function.ingest_lambda.function_name
  principal = "events.amazonaws.com"
  source_arn = aws_cloudwatch_event_rule.scheduler.arn
  source_account = data.aws_caller_identity.current.account_id
}

resource "aws_cloudwatch_event_target" "lambda_target" {
  rule      = aws_cloudwatch_event_rule.scheduler.name
  arn       = aws_lambda_function.ingest_lambda.arn
}


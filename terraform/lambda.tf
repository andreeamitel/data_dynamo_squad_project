
resource "aws_lambda_function" "ingest_lambda" {
    # change role later
role          = aws_iam_role
function_name = var.lambda_name
# change file name
filename      = "ingest_lambda.zip"
handler       = "lambda_handler"
runtime       = "python3.11"
}

# resource "aws_lambda_permission" "allow_s3" {
#   action = "lambda:InvokeFunction"
#   function_name = aws_lambda_function.ingest_lambda.function_name
#   principal = "s3.amazonaws.com"
#   source_arn = aws_s3_bucket.ingested_bucket.arn
#   source_account = data.aws_caller_identity.current.account_id
# }


resource "aws_cloudwatch_event_rule" "scheduler" {
    name_prefix = "mistaker-scheduler-"
    schedule_expression = "rate(1 minute)"
}

resource "aws_lambda_permission" "allow_scheduler" {
  action = "lambda:InvokeFunction"
  function_name = aws_lambda_function.ingest_lambda.function_name
  principal = "events.amazonaws.com"
  source_arn = aws_cloudwatch_event_rule.scheduler.arn
  source_account = data.aws_caller_identity.current.account_id
}
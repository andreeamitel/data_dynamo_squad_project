variable "ingest_lambda" {
  
}

resource "aws_iam_role" "sfn_role" {
  name = "sfn_role"

  assume_role_policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "states.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
POLICY
}
resource "aws_iam_role_policy" "sfn_policy" {
  role = aws_iam_role.sfn_role.id

  policy = <<POLICY
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": "lambda:InvokeFunction",
            "Resource": "*",
            "Effect": "Allow"
        }
    ]
}
POLICY
}
resource "aws_sfn_state_machine" "sfn_state_machine" {
  name     = "my-state-machine"
  role_arn = aws_iam_role.sfn_role.arn
  publish = true

  definition = <<EOF
{
  "Comment": "A test of the Amazon States Language using an AWS Lambda Function",
  "StartAt": "ingest_lambda_2",
  "States": {
    "ingest_lambda_2": {
      "Type": "Task",
      "Resource": "${var.ingest_lambda}",
      "Next": "process_lambda"
    },
    "process_lambda": {
      "Type": "Task",
      "Resource": "${aws_lambda_function.process_lambda.arn}",
      "End": true
    }
  }
}
EOF
}
resource "aws_iam_role" "lambda_role"{
    name_prefix = "${var.name_lambda_role}"
    assume_role_policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
              "sts:AssumeRole"
            ],
            "Principal": {
                "Service": [
                  "lambda.amazonaws.com"
                ]
            }
        }
    ]
}
EOF
}

data "aws_iam_policy_document" "cloudwatch_create" {
  statement {
    actions = [ "logs:CreateLogGroup" ]
    resources = [
      "arn:aws:logs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:*"
    ]
  }
  statement {
    actions = [ "logs:CreateLogStream", "logs:PutLogEvents" ]
    effect= "Allow"
    resources = [
      "arn:aws:logs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:log-group:/aws/lambda/${var.lambda_name}:*"
    ]
  }
}

resource "aws_iam_policy" "cloudwatch_policy" {
    name_prefix = "s3-policy-${var.lambda_name}"
    policy = data.aws_iam_policy_document.cloudwatch_create.json
}
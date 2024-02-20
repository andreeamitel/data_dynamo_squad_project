resource "aws_iam_role" "lambda_process_role" {
  name_prefix        = var.name_lambda_role
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
    actions = ["logs:CreateLogGroup"]
    resources = [
      "arn:aws:logs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:*"
    ]
  }
  statement {
    actions = ["logs:CreateLogStream", "logs:PutLogEvents"]
    effect  = "Allow"
    resources = [
      "arn:aws:logs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:log-group:/aws/lambda/${var.lambda_name}:*"
    ]
  }
}

resource "aws_iam_policy" "cloudwatch_policy" {
  name_prefix = "s3-policy-${var.lambda_name}"
  policy      = data.aws_iam_policy_document.cloudwatch_create.json
}

resource "aws_iam_role_policy_attachment" "lambda_tran_cw_attachment" {
  role       = aws_iam_role.lambda_process_role.name
  policy_arn = aws_iam_policy.cloudwatch_policy.arn
}


data "aws_iam_policy_document" "s3_get_document" {
  statement {
    actions = [
      "s3:GetObject"
    ]
    effect = "Allow"
    resources = [
      "${aws_s3_bucket.processed_bucket.arn}/*",
    ]
  }
}

resource "aws_iam_policy" "s3_tran_get_policy" {
  name_prefix = "s3-tran_get_policy-${var.lambda_name}"
  policy      = data.aws_iam_policy_document.s3_get_document.json

}

resource "aws_iam_role_policy_attachment" "s3_get_attachment" {
  role       = aws_iam_role.lambda_process_role.name
  policy_arn = aws_iam_policy.s3_tran_get_policy.arn
}

data "aws_iam_policy_document" "s3_document_put" {
  statement {
    actions = [
      "s3:PutObject",
      "s3:PutObjectAcl",
    ]
    effect = "Allow"
    resources = [
      "${aws_s3_bucket.processed_bucket.arn}/*",
    ]
  }
}

resource "aws_iam_policy" "s3_tran_put_policy" {
  name_prefix = "s3-tran_put_policy-${var.lambda_name}"
  policy      = data.aws_iam_policy_document.s3_document_put.json

}

resource "aws_iam_role_policy_attachment" "s3_put_attachment" {
  role       = aws_iam_role.lambda_process_role.name
  policy_arn = aws_iam_policy.s3_tran_put_policy.arn
}


data "aws_iam_policy_document" "secretmanager_get_secret_policy" {
  statement {
    actions   = ["secretsmanager:GetSecretValue"]
    effect    = "Allow"
    resources = ["${aws_secretsmanager_secret.processed_bucket.arn}", "arn:aws:secretsmanager:eu-west-2:767397913254:secret:database_creds_test-3hAvo8"]
  }
}

resource "aws_iam_policy" "secretmanager_get_secret" {
  name_prefix = "secretmanger-get-secret-policy-"
  policy      = data.aws_iam_policy_document.secretmanager_get_secret_policy.json
}

resource "aws_iam_role_policy_attachment" "secretmanager_get_secret_attachment" {
  role       = aws_iam_role.lambda_process_role.name
  policy_arn = aws_iam_policy.secretmanager_get_secret.arn
}

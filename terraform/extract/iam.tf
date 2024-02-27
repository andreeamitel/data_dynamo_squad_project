resource "aws_iam_role" "lambda_role" {
  name_prefix        = "role-lambda"
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

data "aws_iam_policy_document" "cloud_watch_create" {
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

resource "aws_iam_policy" "cloud_watch_policy" {
  name_prefix = "s3-policy-${var.lambda_name}"
  policy      = data.aws_iam_policy_document.cloud_watch_create.json
}

resource "aws_iam_role_policy_attachment" "lambda_cw_attachment" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = aws_iam_policy.cloud_watch_policy.arn
}

data "aws_iam_policy_document" "s3_document_get" {
  statement {
    actions = ["s3:GetObject", "s3:*"]
    effect  = "Allow"
    resources = [
      "${aws_s3_bucket.code_bucket.arn}/*",
      "${aws_s3_bucket.ingested_bucket.arn}/*",
      "${aws_s3_bucket.ingested_bucket.arn}"
    ]
  }
}

resource "aws_iam_policy" "s3_get_policy" {
  name_prefix = "s3-policy-${var.lambda_name}"
  policy      = data.aws_iam_policy_document.s3_document_get.json
}


resource "aws_iam_role_policy_attachment" "lambda_s3_read_attachment" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = aws_iam_policy.s3_get_policy.arn
}



data "aws_iam_policy_document" "s3_write_policy" {
  statement {
    actions = [
      "s3:PutObject",
      "s3:PutObjectAcl",
    ]
    effect    = "Allow"
    resources = ["${aws_s3_bucket.ingested_bucket.arn}/*"]
  }
}

resource "aws_iam_policy" "s3_put_policy" {
  name_prefix = "s3-policy-${var.lambda_name}"
  policy      = data.aws_iam_policy_document.s3_write_policy.json
}

resource "aws_iam_role_policy_attachment" "lambda_s3_write_attachment" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = aws_iam_policy.s3_put_policy.arn
}

data "aws_iam_policy_document" "secretmanager_get_secret_policy" {
  statement {
    actions   = ["secretsmanager:GetSecretValue"]
    effect    = "Allow"
    resources = ["${aws_secretsmanager_secret.bucket.arn}", "${aws_secretsmanager_secret.database_creds_secret.arn}", "arn:aws:secretsmanager:eu-west-2:767397913254:secret:database_creds_test-3hAvo8"]
  }
}

resource "aws_iam_policy" "secretmanager_get_secret" {
  name_prefix = "secretmanger-get-secret-policy-"
  policy      = data.aws_iam_policy_document.secretmanager_get_secret_policy.json
}

resource "aws_iam_role_policy_attachment" "secretmanager_get_secret_attachment" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = aws_iam_policy.secretmanager_get_secret.arn
}
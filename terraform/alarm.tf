# need to add into alarm actions sns arn 
# sns arn can be made from deploy.sh
# command: bash deploy.sh {email to send alerts to}



resource "aws_cloudwatch_log_metric_filter" "client_error_alarm" {
  name           = "client_error_metric"
  pattern        = "ClientError"
  log_group_name = "/aws/lambda/ingest_lambda"

  metric_transformation {
    name      = "ClientErrorCount"
    namespace = "errors"
    value     = "1"
  }
}
resource "aws_cloudwatch_metric_alarm" "client_error_alerts" {
  alarm_name                = "client_error_alarm"
  comparison_operator       = "GreaterThanOrEqualToThreshold"
  evaluation_periods        = 1
  metric_name               = aws_cloudwatch_log_metric_filter.client_error_alarm.metric_transformation[0].name
  namespace                 = aws_cloudwatch_log_metric_filter.client_error_alarm.metric_transformation[0].namespace
  period                    = 60
  statistic                 = "Sum"
  threshold                 = 1
  alarm_description         = "This metric monitors any client errors in the lambda handler"
  actions_enabled           = "true"
  alarm_actions             = []
}

resource "aws_cloudwatch_log_metric_filter" "key_error_alarm" {
  name           = "key_error_metric"
  pattern        = "KeyError"
  log_group_name = "/aws/lambda/ingest_lambda"

  metric_transformation {
    name      = "KeyErrorCount"
    namespace = "errors"
    value     = "1"
  }
}
resource "aws_cloudwatch_metric_alarm" "key_error_alerts" {
  alarm_name                = "key_error_alarm"
  comparison_operator       = "GreaterThanOrEqualToThreshold"
  evaluation_periods        = 1
  metric_name               = aws_cloudwatch_log_metric_filter.key_error_alarm.metric_transformation[0].name
  namespace                 = aws_cloudwatch_log_metric_filter.key_error_alarm.metric_transformation[0].namespace
  period                    = 60
  statistic                 = "Sum"
  threshold                 = 1
  alarm_description         = "This metric monitors any key errors in the lambda handler"
  actions_enabled           = "true"
  alarm_actions             = []
}

resource "aws_cloudwatch_log_metric_filter" "database_error_alarm" {
  name           = "database_error_metric"
  pattern        = "DatabaseError"
  log_group_name = "/aws/lambda/ingest_lambda"

  metric_transformation {
    name      = "DatabaseErrorCount"
    namespace = "errors"
    value     = "1"
  }
}
resource "aws_cloudwatch_metric_alarm" "database_error_alerts" {
  alarm_name                = "database_error_alarm"
  comparison_operator       = "GreaterThanOrEqualToThreshold"
  evaluation_periods        = 1
  metric_name               = aws_cloudwatch_log_metric_filter.database_error_alarm.metric_transformation[0].name
  namespace                 = aws_cloudwatch_log_metric_filter.database_error_alarm.metric_transformation[0].namespace
  period                    = 60
  statistic                 = "Sum"
  threshold                 = 1
  alarm_description         = "This metric monitors any database errors in the lambda handler"
  actions_enabled           = "true"
  alarm_actions             = []
}
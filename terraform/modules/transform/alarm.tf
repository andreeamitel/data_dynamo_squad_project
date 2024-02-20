resource "aws_cloudwatch_log_metric_filter" "tran_error_alarm" {
  name           = "tran_client_error_metric"
  pattern        = "ClientError"
  log_group_name = "/aws/lambda/process_lambda"

  metric_transformation {
    name      = "ClientErrorCount"
    namespace = "errors"
    value     = "1"
  }
}


resource "aws_cloudwatch_metric_alarm" "client_error_alerts" {
  alarm_name          = "tran_client_error_metric"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 1
  metric_name         = aws_cloudwatch_log_metric_filter.tran_error_alarm.metric_transformation[0].name
  namespace           = aws_cloudwatch_log_metric_filter.tran_error_alarm.metric_transformation[0].namespace
  period              = 60
  statistic           = "Sum"
  threshold           = 1
  alarm_description   = "This metric monitors any client errors in the processed lambda handler"
  actions_enabled     = "true"
  alarm_actions       = ["arn:aws:sns:eu-west-2:767397913254:error-alerts"]
}



resource "aws_cloudwatch_log_metric_filter" "tran_key_error_alarm" {
  name           = "tran_key_error_metric"
  pattern        = "KeyError"
  log_group_name = "/aws/lambda/process_lambda"

  metric_transformation {
    name      = "KeyErrorCount"
    namespace = "errors"
    value     = "1"
  }
}
resource "aws_cloudwatch_metric_alarm" "key_error_alerts" {
  alarm_name                = "tran_key_error_alarm"
  comparison_operator       = "GreaterThanOrEqualToThreshold"
  evaluation_periods        = 1
  metric_name               = aws_cloudwatch_log_metric_filter.tran_key_error_alarm.metric_transformation[0].name
  namespace                 = aws_cloudwatch_log_metric_filter.tran_key_error_alarm.metric_transformation[0].namespace
  period                    = 60
  statistic                 = "Sum"
  threshold                 = 1
  alarm_description         = "This metric monitors any key errors in the process lambda handler"
  actions_enabled           = "true"
  alarm_actions             = ["arn:aws:sns:eu-west-2:767397913254:error-alerts"]
}


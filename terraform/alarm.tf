resource "aws_cloudwatch_log_metric_filter" "spot_error" {
  name           = "error_metric"
  pattern        = "ERROR"
  log_group_name = "/aws/lambda/ingest_lambda"

  metric_transformation {
    name      = "anyErrorCount"
    namespace = "errors"
    value     = "1"
  }
}
resource "aws_cloudwatch_metric_alarm" "error_alerts" {
  alarm_name                = "any_error_alarm"
  comparison_operator       = "GreaterThanOrEqualToThreshold"
  evaluation_periods        = 1
  metric_name               = aws_cloudwatch_log_metric_filter.spot_error.metric_transformation[0].name
  namespace                 = aws_cloudwatch_log_metric_filter.spot_error.metric_transformation[0].namespace
  period                    = 60
  statistic                 = "Sum"
  threshold                 = 1
  alarm_description         = "This metric monitors any errors in the lambda handler"
  actions_enabled           = "true"
  alarm_actions             = []
}

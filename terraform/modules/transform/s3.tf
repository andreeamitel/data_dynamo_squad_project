resource "aws_s3_bucket" "processed_bucket" {
  bucket_prefix = "${var.bucket_name}-"
}
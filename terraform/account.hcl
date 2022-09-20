# Set account-wide variables
locals {
  account_name   = "production"
  aws_account_id = "333165456247"
  backend_bucket = "cs-infra-prod-terraform-backend"
  dynamodb_table = "cs-infra-prod-terraform-backend-lock"
  test = "test3"
}

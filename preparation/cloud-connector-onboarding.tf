variable "SYSDIG_API_TOKEN" {
  type = string
}

terraform {
   required_providers {
      sysdig = {
         source  = "sysdiglabs/sysdig"
      }
   }
}

provider "sysdig" {
   sysdig_secure_url       = "https://us2.app.sysdig.com"
   sysdig_secure_api_token = var.SYSDIG_API_TOKEN
}

provider "aws" {
   region = "us-east-1"
}

module "secure_for_cloud_aws_single_account_ecs" {
   source           = "sysdiglabs/secure-for-cloud/aws//examples/single-account-ecs"
}


#indicates the version
terraform {
  required_version = ">= 1.0"
  required_providers {
    google = {
      source = "hashicorp/google"
    }
  }
}

#indicates the provider block  as well as the zones you want to use in cofiguration, also download and input the json file in same folder
provider "google" {
  credentials = file("/home/deen/.google/credentials/google_credentials.json")

  project = "dtc-deen"
  region  = "europe-west6"
}

resource "google_storage_bucket" "online-retail11401" {
  name     = "online-retail11401"
  location = "europe-west6"

  uniform_bucket_level_access = true
  storage_class               = "STANDARD"

  versioning {
    enabled = true
  } 

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 30 // days
    }
  }

  force_destroy = true
}


resource "google_bigquery_dataset" "dataset" {
  dataset_id = "all_online_retail"
  project    = "dtc-deen"
  location   = "europe-west6"
}


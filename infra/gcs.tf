
resource "google_storage_bucket" "bucketfred" {
  name          = "fred-etedata2_testtest"
  location      = var.region
  force_destroy = true
  storage_class = "Standard"
  lifecycle_rule {
    condition {
      age = 30
    }
    action {
      type = "Delete"
    }
  }
  uniform_bucket_level_access = true   

}
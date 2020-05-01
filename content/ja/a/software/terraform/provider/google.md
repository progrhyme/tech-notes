---
title: "Google"
linkTitle: "Google"
description: >
  https://www.terraform.io/docs/providers/google/
date: 2020-04-26T23:20:30+09:00
---

## Configuration

[Google Provider Configuration Reference - Terraform by HashiCorp](https://www.terraform.io/docs/providers/google/guides/provider_reference.html)

SYNOPSIS:

```HCL
provider "google" {
  //credentials = "${file("account.json")}"
  project     = "my-project-id"
  region      = "us-central1"
  zone        = "us-central1-c"
  version     = "3.19.0"
}
```

## Resources
### IAM系

Providerリファレンスでは、「Google Cloud Platform Resources」というカテゴリに属する。

- [google_service_account](https://www.terraform.io/docs/providers/google/r/google_service_account.html)
- [google_service_account_key](https://www.terraform.io/docs/providers/google/r/google_service_account_key.html)

### compute系

- [google_compute_backend_bucket](https://www.terraform.io/docs/providers/google/r/compute_backend_bucket.html) ... HTTP(S) LBのバックエンドになるGCSバケット設定
- [google_compute_backend_service](https://www.terraform.io/docs/providers/google/r/compute_backend_service.html) ... GCLBのバックエンドになるサービスの設定
- [google_compute_health_check](https://www.terraform.io/docs/providers/google/r/compute_health_check.html) ... ヘルスチェック
- [google_compute_managed_ssl_certificate](https://www.terraform.io/docs/providers/google/r/compute_managed_ssl_certificate.html) ... β (2020-03-18) HTTPS LBのためのマネージドTLS証明書
- [google_compute_security_policy](https://www.terraform.io/docs/providers/google/r/compute_security_policy.html) ... Cloud Armorのセキュリティポリシー

### storage (GCS) 系

- [google_storage_bucket](https://www.terraform.io/docs/providers/google/r/storage_bucket.html) ... GCS (Cloud Storage) バケット
- [google_storage_bucket_object](https://www.terraform.io/docs/providers/google/r/storage_bucket_object.html) ... GCSオブジェクト。ローカルのファイルからアップロードできる

### google_cloudfunctions_function

https://www.terraform.io/docs/providers/google/r/cloudfunctions_function.html

Cloud Function作成・管理

### google_project_service

https://www.terraform.io/docs/providers/google/r/google_project_service.html

APIサービスの有効化

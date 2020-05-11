---
title: "Google"
linkTitle: "Google"
description: >
  https://www.terraform.io/docs/providers/google/
date: 2020-04-26T23:20:30+09:00
---

## Versions

https://www.terraform.io/docs/providers/google/guides/provider_versions.html

β機能をサポートした [google-beta](https://github.com/terraform-providers/terraform-provider-google-beta) というProviderもある。

「要するに、ふつうの `gcloud` コマンドの代わりに `gcloud beta` コマンドを使うようなもの」

NOTE:

- 両Providerの併用も可能だが、beta -> 無印への移行時には作業が必要

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

- `credentials`
  - GCPのサービスアカウントキー（JSON）のパスまたは内容
  - 環境変数 `GOOGLE_CREDENTIALS` or `GOOGLE_CLOUD_KEYFILE_JSON` or `GCLOUD_KEYFILE_JSON` による指定も可能。
  - 指定がない場合、[Application Default Credentials](https://cloud.google.com/docs/authentication/production)にフォールバックする

See also:

- [Backends#gcs]({{< ref "/a/software/terraform/backend.md" >}}#gcs)

## Data Sources
### compute系

- [google_compute_network](https://www.terraform.io/docs/providers/google/d/datasource_compute_network.html)
- [google_compute_subnetwork](https://www.terraform.io/docs/providers/google/d/datasource_compute_subnetwork.html)


## Resources
### GCP (IAM, API, Billing, Organization)

Providerリファレンスで、「Google Cloud Platform Resources」というカテゴリに属するもの。

- [google_project_service](https://www.terraform.io/docs/providers/google/r/google_project_service.html) ... APIs & Servicesの有効化
- [google_service_account](https://www.terraform.io/docs/providers/google/r/google_service_account.html)
- [google_service_account_key](https://www.terraform.io/docs/providers/google/r/google_service_account_key.html)

Examples:

```HCL
resource "google_service_account" "terraform" {
  account_id   = "terraform"
}

resource "google_service_account_key" "terraform_key" {
  service_account_id = google_service_account.terraform.name
  private_key_type   = "TYPE_GOOGLE_CREDENTIALS_FILE"
}

# ローカルにService Account KeyのJSONを保存する
resource local_file "terraform_key_json" {
  filename             = "./tmp/terraform_service_account_key.json"
  content              = base64decode(google_service_account_key.terraform_key.private_key)
  file_permission      = "0600"
  directory_permission = "0755"
}
```

#### IAM policy for projects

https://www.terraform.io/docs/providers/google/r/google_project_iam.html

- `google_project_iam_policy`
- `google_project_iam_binding` ... role : member = 1 : Nの権限を設定する。Service Accountの権限にも対応
- `google_project_iam_member` ... role : member = 1 : 1の権限を設定する。Service Accountの権限にも対応
- `google_project_iam_audit_config`

### compute系

- [google_compute_backend_bucket](https://www.terraform.io/docs/providers/google/r/compute_backend_bucket.html) ... HTTP(S) LBのバックエンドになるGCSバケット設定
- [google_compute_backend_service](https://www.terraform.io/docs/providers/google/r/compute_backend_service.html) ... GCLBのバックエンドになるサービスの設定
- [google_compute_health_check](https://www.terraform.io/docs/providers/google/r/compute_health_check.html) ... ヘルスチェック
- [google_compute_instance](https://www.terraform.io/docs/providers/google/r/compute_instance.html)
- [google_compute_managed_ssl_certificate](https://www.terraform.io/docs/providers/google/r/compute_managed_ssl_certificate.html) ... β (2020-03-18) HTTPS LBのためのマネージドTLS証明書
- [google_compute_security_policy](https://www.terraform.io/docs/providers/google/r/compute_security_policy.html) ... Cloud Armorのセキュリティポリシー

ネットワーク関係:

- [google_compute_address](https://www.terraform.io/docs/providers/google/r/compute_address.html) ... `EXTERNAL` なアドレスも発行できる。Cloud NATに使うのはこっち
- [google_compute_global_address](https://www.terraform.io/docs/providers/google/r/compute_global_address.html) ... HTTP(S) LBで使うやつ
- [google_compute_network](https://www.terraform.io/docs/providers/google/r/compute_network.html)
- [google_compute_subnetwork](https://www.terraform.io/docs/providers/google/r/compute_subnetwork.html)
- [google_compute_router](https://www.terraform.io/docs/providers/google/r/compute_router.html) ... Cloud Router
- [google_compute_router_nat](https://www.terraform.io/docs/providers/google/r/compute_router_nat.html) ... Cloud NAT w/ Cloud Router

### GKE関連

- [google_container_cluster](https://www.terraform.io/docs/providers/google/r/container_cluster.html)
- [google_container_node_pool](https://www.terraform.io/docs/providers/google/r/container_node_pool.html)

参考:

- [Terraformを用いてVPCネットワークにGKE限定公開クラスタを構成する - Qiita](https://qiita.com/y-uemurax/items/4376e27ccc0b2dcc85f0)

#### Examples

限定公開クラスタ（パブリックエンドポイント有り）

```HCL
resource "google_container_cluster" "experiment" {
  name     = "experiment"
  location = "asia-northeast1"

  private_cluster_config {
    enable_private_nodes    = true
    enable_private_endpoint = false
    master_ipv4_cidr_block  = "172.16.0.0/28"
  }

  ip_allocation_policy {
    # GKE管理のサブネットを作成してもらう
    cluster_ipv4_cidr_block  = ""
    services_ipv4_cidr_block = ""
  }
}
```

### storage (GCS) 系

- [google_storage_bucket](https://www.terraform.io/docs/providers/google/r/storage_bucket.html) ... GCS (Cloud Storage) バケット
- [google_storage_bucket_object](https://www.terraform.io/docs/providers/google/r/storage_bucket_object.html) ... GCSオブジェクト。ローカルのファイルからアップロードできる

### google_cloudfunctions_function

https://www.terraform.io/docs/providers/google/r/cloudfunctions_function.html

Cloud Function作成・管理

### google_project_service

https://www.terraform.io/docs/providers/google/r/google_project_service.html

APIサービスの有効化

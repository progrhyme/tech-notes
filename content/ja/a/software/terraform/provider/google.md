---
title: "Google"
linkTitle: "Google"
description: >
  https://registry.terraform.io/providers/hashicorp/google
date: 2020-04-26T23:20:30+09:00
---

## Versions

https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/provider_versions

β機能をサポートした [google-beta](https://github.com/terraform-providers/terraform-provider-google-beta) というProviderもある。

「要するに、ふつうの `gcloud` コマンドの代わりに `gcloud beta` コマンドを使うようなもの」

NOTE:

- 両Providerの併用も可能だが、beta -> 無印への移行時には作業が必要

## Configuration

[Google Provider Configuration Reference | Guides | hashicorp/google | Terraform Registry](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/provider_reference)

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

- [google_compute_default_service_account](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_default_service_account) ... プロジェクトのデフォルトのサービスアカウントを取得する
- [google_compute_network](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_network)
- [google_compute_subnetwork](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_subnetwork)

## Resources

未分類のもの:

- [google_cloudfunctions_function](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloudfunctions_function) ... Cloud Function作成・管理
- [google_cloud_scheduler_job](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_scheduler_job) ... Cloud Scheduler Job
- [google_redis_instance](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/redis_instance) ... Memorystore (Redis)

### GCP (IAM, API, Billing, Organization)

Providerリファレンスで、「Google Cloud Platform Resources」というカテゴリに属するもの。

- [google_project_service](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_project_service) ... APIs & Servicesの有効化
- [google_service_account](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_service_account)
- [google_service_account_key](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_service_account_key)

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

https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_project_iam

- `google_project_iam_policy`
- `google_project_iam_binding` ... role : member = 1 : Nの権限を設定する。Service Accountの権限にも対応
- `google_project_iam_member` ... role : member = 1 : 1の権限を設定する。Service Accountの権限にも対応
- `google_project_iam_audit_config`

### compute系

- [google_compute_backend_bucket](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_backend_bucket) ... HTTP(S) LBのバックエンドになるGCSバケット設定
- [google_compute_backend_service](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_backend_service) ... GCLBのバックエンドになるサービスの設定
- [google_compute_health_check](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_health_check) ... ヘルスチェック
- [google_compute_instance](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance)
- [google_compute_managed_ssl_certificate](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_managed_ssl_certificate) ... β (2020-03-18) HTTPS LBのためのマネージドTLS証明書
- [google_compute_security_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_security_policy) ... Cloud Armorのセキュリティポリシー

IAM関係:

- https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_iam
  - 基本的には `google_compute_instance_iam_member` で管理すればいいと思う

#### ネットワーク関係

- [google_compute_address](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_address) ... `EXTERNAL` なアドレスも発行できる。Cloud NATに使うのはこっち
- [google_compute_global_address](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_global_address) ... HTTP(S) LBで使うやつ
- [google_compute_network](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network)
- [google_compute_subnetwork](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_subnetwork)
- [google_compute_router](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_router) ... Cloud Router
- [google_compute_router_nat](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_router_nat) ... Cloud NAT w/ Cloud Router

#### インスタンスでcustom machine typeを使う

例:

```HCL
resource "google_compute_instance" "default" {
  machine_type = "custom-6-20480" # 6 vCPU, Mem 20GB
}
```

`google_container_node_pool` などでも同様の指定が行える。

### GKE関連

- [google_container_cluster](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster)
- [google_container_node_pool](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_node_pool)

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

### Pub/Sub

- [google_pubsub_topic](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/pubsub_topic)
- [google_pubsub_subscription](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/pubsub_subscription)

#### Topic/Subscription IAM

- [pubsub_topic_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/pubsub_topic_iam)
  - 以下の3種類のリソースがあり、管理したい粒度に応じていずれかを使う
  - いずれも特定のトピックに対する権限をセットする
  - `google_pubsub_topic_iam_policy` ... 該当トピックに対する全ロール x 全メンバーの権限を含むポリシーを管理する
  - `google_pubsub_topic_iam_binding` ... 特定のロールを持つメンバーセットを管理する
  - `google_pubsub_topic_iam_member` ... 特定のロール x メンバーの組み合わせを1つ1つ管理する
  - たぶん、最も細かい粒度の `google_pubsub_topic_iam_member` を使うのが無難
- [pubsub_subscription_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/pubsub_subscription_iam)
  - topicの方と同様に3種類のリソースを選択的に使う
  - いずれも特定のサブスクリプションに対する権限をセットする
  - `google_pubsub_subscription_iam_policy` ... 該当サブスクリプションに対する全ロール x 全メンバーの権限を含むポリシーを管理する
  - `google_pubsub_subscription_iam_binding` ... 特定のロールを持つメンバーセットを管理する
  - `google_pubsub_subscription_iam_member` ... 特定のロール x メンバーの組み合わせを1つ1つ管理する

参考:

- [アクセス制御 | Cloud Pub/Sub ドキュメント | Google Cloud](https://cloud.google.com/pubsub/docs/access-control?hl=ja)

### Storage (GCS) 系

- [google_storage_bucket](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket) ... GCS (Cloud Storage) バケット
- [google_storage_bucket_object](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket_object) ... GCSオブジェクト。ローカルのファイルからアップロードできる
- [google_storage_notification](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_notification) ... GCSでのイベントをPub/Subに通知する通知リソース

#### IAM for GCS Bucket

https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket_iam

Pub/SubのTopic/Subscription IAMと同じように3種類のリソースが用意されている。

- `google_storage_bucket_iam_policy` ... そのバケットに対するIAM x 権限(Role)をフルコントロールしたい場合に使う
- `google_storage_bucket_iam_binding` ... そのバケットに対して特定のRoleの権限を持つIAMメンバーリストを管理する
- `google_storage_bucket_iam_member` ... 特定の (IAM x Role) の組合せを管理する。既存の他の権限セットとは独立して管理することが可能

特定のIAMアカウントに対して権限を追加したい場合、基本的には `google_storage_bucket_iam_member` を使えばよさそう。

### Cloud Logging

Resources:

- [google_logging_metric](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/logging_metric) ... カスタムログベース指標

### Bigtable関係

IAM管理:

- [bigtable_instance_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigtable_instance_iam) ... インスタンスに対するIAM権限設定
- [bigtable_table_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigtable_table_iam) ... テーブルに対するIAM権限設定
  - `google_bigtable_table_iam_policy`
  - `google_bigtable_table_iam_binding`
  - `google_bigtable_table_iam_member` ... 基本はこれを使えばいいだろう

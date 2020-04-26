---
title: "Terraform"
linkTitle: "Terraform"
description: >
  https://www.terraform.io/
date: 2020-04-26T22:59:20+09:00
---

## Getting Started

- 初心者向けガイド: https://www.terraform.io/guides/
- ドキュメント: https://www.terraform.io/docs/

参考:

- [terraform使い方(超基礎編) - Qiita](https://qiita.com/kohey18/items/38400d8c498baa0a0ed8 "terraform使い方(超基礎編) - Qiita")


## 仕様
### State

https://www.terraform.io/docs/state/

#### Locking

https://www.terraform.io/docs/state/locking.html

[backend](https://www.terraform.io/docs/backends)によってサポートされていれば、排他制御が可能。


## Examples

公式のを見ると良い。

- https://github.com/hashicorp/terraform/tree/master/examples
  - AWS: https://github.com/terraform-providers/terraform-provider-aws/tree/master/examples

## ベストプラクティス

公式: https://github.com/hashicorp/best-practices/tree/master/terraform

| Terraform Version | 記事 |
|-------------------------|--------|
| v0.10 | [Terraform Best Practices in 2017 - Qiita](https://qiita.com/shogomuranushi/items/e2f3ff3cfdcacdd17f99 "Terraform Best Practices in 2017 - Qiita") |
| v0.7.x | [Terraformにおけるディレクトリ構造のベストプラクティス ｜ Developers.IO](https://dev.classmethod.jp/devops/directory-layout-bestpractice-in-terraform/ "Terraformにおけるディレクトリ構造のベストプラクティス ｜ Developers.IO") |

オレオレ:

- [TerraformでWorkspaceを使わずに複数環境をDRYに設定する - Qiita](https://qiita.com/progrhyme/items/766d02e605358ad2930e "TerraformでWorkspaceを使わずに複数環境をDRYに設定する - Qiita") ... Terraform v0.10〜v0.11ぐらい対応

参考:

- [Structuring HashiCorp Terraform Configuration for Production](https://www.hashicorp.com/blog/structuring-hashicorp-terraform-configuration-for-production/) ... 2020-03-27. Workspacesを使わずにディレクトリを分けることのメリットが述べられている。

## How-to
### バージョン固定

[Terraform Settings - Configuration Language - Terraform by HashiCorp](https://www.terraform.io/docs/configuration/terraform.html)

Examples:

```HCL
terraform {
  required_version = ">= 0.12"

  required_providers {
    aws   = ">= 2.8"
    local = "1.2"
  }
}

provider "http" {
  version = "1.2.0"
}
```

- terraformのversion指定はtfenvでも可能

参考:

- [tfupdateでTerraform本体/プロバイダ/モジュールのバージョンアップを自動化する - Qiita](https://qiita.com/minamijoyo/items/1350fb28ae82a3dbb354)


### BackendのS3やGCS等そのものをTerraformで管理

参考:

- [Backend の S3 や DynamoDB 自体を terraform で管理するセットアップ方法 - Qiita](https://qiita.com/saiya_moebius/items/a8f8aa3683c2347d607c)


## Tips
### デバッグ

https://www.terraform.io/docs/internals/debugging.html

#### ログレベルの変更

`TF_LOG` 環境変数に `TRACE, DEBUG, INFO, WARN, ERROR` のいずれかをセットすることで変更できる。

```sh
TF_LOG=DEBUG terraform plan
```

※しかし、どれを指定してもtraceレベルのログが出る気が…(v0.10.x)

### countを使って複数のリソースを作成

Examples:

```Terraform
variable "instance_ips" {
  default = {
    "0" = "10.11.12.100"
    "1" = "10.11.12.101"
    "2" = "10.11.12.102"
  }
}

resource "aws_instance" "app" {
  count = "3"
  private_ip = "${lookup(var.instance_ips, count.index)}"
  # ...
}

variable "rds_roles" {
  default = ["WRITER", "READER"]
}

resource "aws_cloudwatch_metric_alarm" "rds_cpu" {
  count = "2"
  alarm_name = "RDS-${var.rds_roles[count.index]}-CPU"
  :
}
```

参考:

- https://www.terraform.io/docs/configuration/resources.html#using-variables-with-count
- [terraformでautoscalingしているサーバのcloudwatch alarmを自動設定する \- Qiita](https://qiita.com/kanagi/items/095037ba3f72de3f9572)
- [Terraform でループして複数のリソースを作成する - Qiita](https://qiita.com/ringo/items/875f08ec550f0826f0dc "Terraform でループして複数のリソースを作成する - Qiita")

### 変数やoutputでmapを使うと記述量が減って便利

参考:

- [Terraformのoutputでmapを利用する方法 - Qiita](https://qiita.com/shogomuranushi/items/cc387a1233cc7f4e6e60 "Terraformのoutputでmapを利用する方法 - Qiita")


### mapのlistを作る方法

- [A hacky way to create a dynamic list of maps in Terraform](https://gist.github.com/brikis98/f3fe2ae06f996b40b55eebcb74ed9a9e)

#### できない説

- [Cannot pass a list of maps to a resource/data · Issue #7705 · hashicorp/terraform](https://github.com/hashicorp/terraform/issues/7705 "Cannot pass a list of maps to a resource/data · Issue #7705 · hashicorp/terraform")
- [Terraform でループして複数のリソースを作成する - Qiita](https://qiita.com/ringo/items/875f08ec550f0826f0dc "Terraform  でループして複数のリソースを作成する - Qiita")

…が、手元で試したところ(v0.10.x)、下のようにしてlistとして定義・参照することができた。

```terraform
variable "my_complex_data" {
  type = "list"
  default = [
    {
      id = "1"
      name = "taro"
      height = "170"
    },
    {
      id = "2"
      name = "hanako"
      height = "160"
    },
  ]
}

foo_list = "${var.my_complex_data}"
```

## Tools

3rd Partyのツール

### tfenv

https://github.com/Zordrak/tfenv

rbenv, anyenvのようなツールで、複数バージョンのterraformを切り替えて使えるようになるもの。

参考:

- [tfenvでTerraformのバージョン管理をする - Qiita](https://qiita.com/kamatama_41/items/ba59a070d8389aab7694)


## 参考

- [Terraform職人入門: 日々の運用で学んだ知見を淡々とまとめる - Qiita](https://qiita.com/minamijoyo/items/1f57c62bed781ab8f4d7 "Terraform職人入門: 日々の運用で学んだ知見を淡々とまとめる - Qiita")

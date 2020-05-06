---
title: "CLI"
linkTitle: "CLI"
date: 2020-04-29T22:59:42+09:00
weight: 100
---

## Cloud SDK

https://cloud.google.com/sdk/docs?hl=ja

`gcloud`, `gsutil`, `bq` CLIもこれに含まれる。

- プロキシ設定
  - [プロキシ / ファイアウォールの背後で Cloud SDK を使用する場合の構成 | Cloud SDK のドキュメント](https://cloud.google.com/sdk/docs/proxy-settings?hl=ja)

## gcloud

- Getting Started: https://cloud.google.com/sdk/gcloud/?hl=ja
- リファレンス: https://cloud.google.com/sdk/gcloud/reference/?hl=ja

NOTE:

- 新しめの機能の場合、 `gcloud beta ...` や `gcloud alpha ...` にしかコマンドがなかったり、 `beta ...` や `alpha ...` を付けることで結果が変わることがある

### 認証

```sh
## 初期設定(認証込)
gcloud init

## ログイン認証
gcloud auth login
## 現在認証済みのアカウント一覧
gcloud auth list
## サービスアカウントの認証
gcloud auth activate-service-account --key-file <KEYFILE>
## アクセストークンの表示
gcloud auth print-access-token
```

参考:
- [Cloud SDK ツールの承認 | Cloud SDK のドキュメント | Google Cloud](https://cloud.google.com/sdk/docs/authorizing?hl=ja)


### compute

https://cloud.google.com/sdk/gcloud/reference/compute

Examples:

```sh
## ssh
gcloud compute ssh [--project=<PROJECT>] [--zone=<ZONE>] [--internal-ip | --tunnel-through-iap] \
  <INSTANCE> [-- <SSH_ARGS>]

## scp
gcloud compute scp [--project=<PROJECT>] [--zone=<ZONE>] [--internal-ip | --tunnel-through-iap] \
  [--recurse] host:/path/to/dir path/to/local

## 証明書
gcloud compute ssl-certificates

### 一覧表示
gcloud compute ssl-certificates list

## イメージの作成
gcloud compute images create my-image --source-disk my-vm-disk
```

#### instances

VM操作

- https://cloud.google.com/sdk/gcloud/reference/compute/instances
  - [create](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create)

Examples:

```sh
## 一覧
gcloud compute instances list
## 起動
gcloud compute instances start <INSTANCE> --zone=<ZONE>
## 停止
gcloud compute instances stop <INSTANCE> --zone=<ZONE>

## 作成
gcloud compute instances create my-instance \
  --project=my-project --zone=asia-northeast1-b \
  --no-address \ # 外部IPなし
  --custom-vm-type=n1 \ # N1インスタンス
  --custom-cpu=4 --custom-memory=8GB \ # リソースをカスタマイズする場合
  --image-project=another-project --image=my-image # 別プロジェクトのイメージを使う
```

参考:

- [イメージとスナップショットの共有 | Compute Engine ドキュメント | Google Cloud](https://cloud.google.com/compute/docs/images/sharing-images-across-projects?hl=ja)


### config

https://cloud.google.com/sdk/gcloud/reference/config

SYNOPSIS:

```sh
## 設定値一覧表示
gcloud config list
```

参考:

- [gcloud configで複数の設定を持って切り替える - Qiita](https://qiita.com/sky0621/items/597d4de7ed9ba7e31f6d)

#### configurations

https://cloud.google.com/sdk/gcloud/reference/config/configurations

設定プロファイルの管理

SYNOPSIS:

```sh
## プロファイル一覧表示
gcloud config configurations list

## 表示
gcloud config configurations describe プロファイル名
## 作成
gcloud config configurations create プロファイル名
## 削除
gcloud config configurations delete プロファイル名
## 有効化
gcloud config configurations activate プロファイル名
```

参考:

- [SDK 構成の管理 | Cloud SDK のドキュメント | Google Cloud](https://cloud.google.com/sdk/docs/configurations?hl=ja)


#### set

https://cloud.google.com/sdk/gcloud/reference/config/set

Examples:

```sh
gcloud config set project my-project
gcloud config set compute/region asia-northeast1
gcloud config set compute/zone asia-northeast1-a
```

### functions

https://cloud.google.com/sdk/gcloud/reference/functions

Cloud Functionsの操作

#### deploy

https://cloud.google.com/sdk/gcloud/reference/functions/deploy

Cloud Functionのデプロイ（作成・更新）

Example:

```sh
## cloud-buildsイベントをフックに動くFunctionのデプロイ
gcloud functions deploy <Function Name> \
  --trigger-topic cloud-builds \
  --runtime nodejs10 \
  --set-env-vars "FOO=foo,BAR=bar" \
  --project my-project
```


### logging

https://cloud.google.com/sdk/gcloud/reference/logging

NOTE:

- `read`, `list`などのコマンド利用時には serviceusage.services.use 権限が必要

#### read

https://cloud.google.com/sdk/gcloud/reference/logging/read

Examples:

```sh
gcloud logging read --format json
gcloud logging read --limit=10 --order=asc
gcloud logging read 'timestamp>="2020-03-19T05:28:00Z" timestamp<="2020-03-25T05:33:28Z"'
```

※2020-04-20現在、 `tail -f` 相当のオプションはなさそう


### projects

https://cloud.google.com/sdk/gcloud/reference/projects/

SYNOPSIS:

```sh
## プロジェクト一覧
gcloud projects list
```

### 参考

- [よく使うgcloudコマンドたち - Qiita](https://qiita.com/masaaania/items/7a83c5e44e351b4a3a2c)


## gsutil

Cloud Storage用のPython製CLI

- ドキュメント: https://cloud.google.com/storage/docs/gsutil
- コマンドリファレンス: https://cloud.google.com/storage/docs/gsutil/commands/help

### mb

https://cloud.google.com/storage/docs/gsutil/commands/mb

バケット作成

Examples:

```sh
gsutil mb -l asia gs://mybucket
```
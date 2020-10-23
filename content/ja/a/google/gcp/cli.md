---
title: "CLI"
linkTitle: "CLI"
date: 2020-04-29T22:59:42+09:00
weight: 10
---

Quick links:

- [bq](#bq)
- [cbt](#cbt)
- [gcloud](#gcloud)
- [gsutil](#gsutil)

## Cloud SDK

https://cloud.google.com/sdk/docs?hl=ja

`gcloud`, `gsutil`, `bq` CLIもこれに含まれる。

- プロキシ設定
  - [プロキシ / ファイアウォールの背後で Cloud SDK を使用する場合の構成 | Cloud SDK のドキュメント](https://cloud.google.com/sdk/docs/proxy-settings?hl=ja)

### Install

https://cloud.google.com/sdk/install

- インタラクティブインストーラー: https://cloud.google.com/sdk/docs/downloads-interactive
- yum, apt, snapパッケージでの提供がある
  - snap: https://cloud.google.com/sdk/docs/downloads-snap
- Docker Image ... See below
- [旧バージョンアーカイブ](https://cloud.google.com/sdk/docs/downloads-versioned-archives)

### Docker Image

https://cloud.google.com/sdk/docs/downloads-docker

参考:

- [DockerコンテナからGoogle Cloud SDKのコマンドを簡単に実行できるコマンドをつくってみた | cloudpack.media](https://cloudpack.media/50237)
- [Docker で Google Cloud SDK を使う - yt coffee](https://yuku.takahashi.coffee/blog/2019/01/google-cloud-sdk-in-docker)

## bq

BigQuery操作CLI

リファレンス: https://cloud.google.com/bigquery/docs/reference/bq-cli-reference?hl=ja

### cp

- https://cloud.google.com/bigquery/docs/reference/bq-cli-reference?hl=ja#bq_cp
- https://cloud.google.com/bigquery/docs/managing-tables?hl=ja#copy-table

Examples:

```sh
bq --location=LOCATION cp [OPTIONS] \
  project_id:dataset.source_table project_id:dataset.destination_table
```

 Option | デフォルト | 機能
--------|----------|-----
 `-a, --append_table` | `false` | 指定すると元のテーブルがコピーされて既存の宛先テーブルに追加される
 `-f, --force` | `false` | 指定すると宛先テーブルが存在する場合にプロンプト表示なしで上書きされる
 `-n, --no_clobber` | `false` | 指定すると宛先テーブルが存在する場合は上書きしない

### load

ドキュメント:

- https://cloud.google.com/bigquery/docs/reference/bq-cli-reference?hl=ja#bq_load
- [Cloud Storage からの CSV データの読み込み | BigQuery | Google Cloud](https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv?hl=ja)

Examples:

```sh
# TSVファイルをロードする
bq load --source_format=CSV --encoding=UTF-8 --field_delimiter="\t" [dataset].[table] SOURCE [SCHEMA]
# ↑SOURCEはファイルでもGCSバケットでもいい
```

Specs:

- 要素が改行を含むデータを取り込むには、該当要素を `--quote` 文字（デフォルトは `"` ）で囲み、 `--allow_quoted_newlines` （デフォルトfalse）を指定する
  - 更に、該当要素が元々 `"` を含む場合、 `""` でエスケープする必要がある。

参考:

- [bq loadのCSVにダブルクォーテーションや改行を含むときの対処法 | ppoohh 's blog](https://www.ppoohh.info/post-331/)
- [bigqueryでtsvをインポート | ハックノート](https://hacknote.jp/archives/32117/)

### ls

- https://cloud.google.com/bigquery/docs/reference/bq-cli-reference?hl=ja#bq_ls
- https://cloud.google.com/bigquery/docs/managing-jobs?hl=ja#listing_jobs

Examples:

```sh
# 現在のユーザのジョブを表示
bq ls -j myproject
# すべてのユーザのジョブを表示
bq ls -j -a myproject
# 直近10件のジョブを表示
bq ls -j -a -n 10 myproject
```

### mk

- https://cloud.google.com/bigquery/docs/reference/bq-cli-reference?hl=ja#bq_mk
- テーブル作成: https://cloud.google.com/bigquery/docs/tables?hl=ja

Syntax:

```sh
bq mk \
--table \
--expiration integer \
--description description \
--label key:value, key:value \
project_id:dataset.table \
schema
```

- `schema` ... field:data_type,field:data_type という形式のインラインスキーマ定義か、ローカルマシン上のJSONスキーマファイルのパス

### show

- https://cloud.google.com/bigquery/docs/reference/bq-cli-reference?hl=ja#bq_show
- データセットの情報表示: https://cloud.google.com/bigquery/docs/dataset-metadata?hl=ja

```sh
# schemaをJSON形式で表示
bq show --schema --format=prettyjson PROJECT_ID:DATASET.TABLE

# ジョブの詳細情報を取得
bq show --format=prettyjson -j JOB_ID
```

参考:

- [google cloud platform - BigQuery - Where can I find the error stream? - Stack Overflow](https://stackoverflow.com/questions/52100812/bigquery-where-can-i-find-the-error-stream)

## cbt

Bigtable操作CLI

- リファレンス: https://cloud.google.com/bigtable/docs/cbt-reference?hl=ja
- インストール: [cbt ツールの概要 | Cloud Bigtable ドキュメント | Google Cloud](https://cloud.google.com/bigtable/docs/cbt-reference?hl=ja)

## gcloud

- Getting Started: https://cloud.google.com/sdk/gcloud/?hl=ja
- リファレンス: https://cloud.google.com/sdk/gcloud/reference

NOTE:

- 新しめの機能の場合、 `gcloud beta ...` や `gcloud alpha ...` にしかコマンドがなかったり、 `beta ...` や `alpha ...` を付けることで結果が変わることがある

### 認証

See also [#auth](#auth)

```sh
## 初期設定(認証込)
gcloud init
```

参考:
- [Cloud SDK ツールの承認 | Cloud SDK のドキュメント | Google Cloud](https://cloud.google.com/sdk/docs/authorizing?hl=ja)

### 環境変数

 Variable | 用途
----------|-----
 CLOUDSDK_ACTIVE_CONFIG_NAME | 利用するconfigurationを設定する。See [#configurations](#configurations)

### 全体で使えるオプション

リファレンスで「GCLOUD WIDE FLAGS」とされているもの。

https://cloud.google.com/sdk/gcloud/reference に簡単な説明がある。

例:

- `--configuration` ... コマンドを実行するconfiguration. See [#configurations](#configurations)
- `--project` ... コマンドの対象となるプロジェクトをプロジェクトIDで指定する
- `--verbosity=VERBOSITY` ... ログレベルの設定。デフォルトは `warning`. 他に、debug, info, error, critical, noneが設定可能

#### filter

https://cloud.google.com/sdk/gcloud/reference/topic/filters

結果をリストで出力するコマンドに対し、フィルタ条件を記すことができる。

Examples:

```sh
gcloud compute instances list --filter="machineType:f1-micro"
gcloud compute instances list \
  --filter="zone ~ ^us AND -machineType:f1-micro"
gcloud compute instances list --filter="tags.items=my-tag"

gcloud projects list \
  --format="table(projectNumber,projectId,createTime)" \
  --filter="createTime>=2018-01-15"

gcloud config configurations list --filter='IS_ACTIVE=true'
```

#### format

https://cloud.google.com/sdk/gcloud/reference/topic/formats

結果を出力するコマンドに対し、出力フォーマットや、抽出するプロパティ、ヘッダの有無などを指定できる。

Examples:

```sh
# デフォルトのテーブル表示にボックス装飾を付ける
gcloud ... --format='[box]'
# JSON形式
gcloud ... --format=json
# YAML形式
gcloud ... --format=yaml
# ヘッダ無しCSV形式
gcloud ... --format='csv[no-heading]'

# ヘッダ無しCSVで、特定のカラム値だけ取得
gcloud config list --format="csv[no-heading](core.project,core.account)"

# 特定の値だけ取得
gcloud config configurations list --format='value(name)'
gcloud info --format='value(config.paths.global_config_dir)'
```

### auth

https://cloud.google.com/sdk/gcloud/reference/auth

Examples:

```sh
# ログイン認証
gcloud auth login
# 現在認証済みのアカウント一覧
gcloud auth list
# サービスアカウントの認証
gcloud auth activate-service-account --key-file <KEYFILE>
# アクセストークンの表示
gcloud auth print-access-token
```

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

#### regions

https://cloud.google.com/sdk/gcloud/reference/compute/regions

GCEリージョンの表示。

SYNPSIS:

```sh
gcloud compute regions list
gcloud compute regions describe REGION
```

#### ssl-certificates

https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates

証明書の管理。マネージド証明書が作れる。

```sh
# 一覧表示
gcloud compute ssl-certificates list

# 詳細表示
gcloud compute ssl-certificates describe <name>

# 作成
gcloud compute ssl-certificates create <name> --domains=<fqdn1>,...

# 削除
gcloud compute ssl-certificates delete <name>
```

#### zones

https://cloud.google.com/sdk/gcloud/reference/compute/zones

GCEゾーンの表示。

SYNPSIS:

```sh
gcloud compute zones list
gcloud compute zones describe ZONE
```

### config

https://cloud.google.com/sdk/gcloud/reference/config

Subcommands:

- configurations ... See below
- [get-value](https://cloud.google.com/sdk/gcloud/reference/config/get-value)
- [list](https://cloud.google.com/sdk/gcloud/reference/config/list)
- [set](https://cloud.google.com/sdk/gcloud/reference/config/set)

configurationという単位でプロパティ値のセットを管理できる。  
configurations以外のサブコマンドは現在のconfigurationに対する操作を行う。

SYNOPSIS:

```sh
# 設定プロパティ値一覧表示
gcloud config list

# プロパティ値の取得
gcloud config get-value account
gcloud config get-value artifacts/location

# プロパティ値の設定
gcloud config set project my-project
gcloud config set compute/region asia-northeast1
gcloud config set compute/zone asia-northeast1-a
```

参考:

- [gcloud configで複数の設定を持って切り替える - Qiita](https://qiita.com/sky0621/items/597d4de7ed9ba7e31f6d)

#### configurations

https://cloud.google.com/sdk/gcloud/reference/config/configurations

設定プロファイルの管理。各プロファイルでは、プロパティ値のセットを管理することができる。

SYNOPSIS:

```sh
# プロファイル一覧表示
gcloud config configurations list

# 表示
gcloud config configurations describe プロファイル名
# 作成
gcloud config configurations create プロファイル名
# 削除
gcloud config configurations delete プロファイル名
# 有効化
gcloud config configurations activate プロファイル名
```

Tips:

- gcloudコマンドは現在アクティブなconfigurationの設定プロパティをデフォルト値として参照する
- アクティブなconfigurationは `--configuration` 引数か、環境変数 `CLOUDSDK_ACTIVE_CONFIG_NAME` で上書き指定することもできる

参考:

- [SDK 構成の管理 | Cloud SDK のドキュメント | Google Cloud](https://cloud.google.com/sdk/docs/configurations?hl=ja)
- https://cloud.google.com/sdk/gcloud/reference/topic/configurations

### container

https://cloud.google.com/sdk/gcloud/reference/container

GKEなどコンテナサービスに関する操作。

#### clusters

https://cloud.google.com/sdk/gcloud/reference/container/clusters

GKEクラスタの操作。

Examples:

```sh
gcloud container clusters list

# $KUBECONFIG or ~/.kube/config に認証情報を取得
gcloud container clusters get-credentials クラスタ名 [--region=REGION] [--project=PROJECT_ID]
```

##### create

https://cloud.google.com/sdk/gcloud/reference/container/clusters/create

 オプション | 意味
----------|-----
 --enable-master-authorized-networks | Master Authorized Networksの有効化
 --master-authorized-networks=NETWORK,[NETWORK,…] | Master Authorized Networksの設定

###### beta版（2020-05-13更新）

https://cloud.google.com/sdk/gcloud/reference/beta/container/clusters/create

 オプション | 意味
----------|-----
 --release-channel=CHANNEL | rapid, regular, stableのどれか。リリースチャネルの設定。

#### images

Examples:

```sh
# イメージ一覧
gcloud container images list --repository=[HOSTNAME]/[PROJECT-ID]

# イメージのタグ一覧
gcloud container images list-tags [HOSTNAME]/[PROJECT-ID]/[IMAGE]

## 完全なダイジェストを表示
gcloud container images list-tags --format='get(digest)' [HOSTNAME]/[PROJECT-ID]/[IMAGE]

# 既存イメージに別のタグをつける（下記いずれか）
gcloud container images add-tag \
  [HOSTNAME]/[PROJECT-ID]/[IMAGE]:[TAG] \
  [HOSTNAME]/[PROJECT-ID]/[IMAGE]:[NEW_TAG]

gcloud container images add-tag \
  [HOSTNAME]/[PROJECT-ID]/[IMAGE]@[IMAGE_DIGEST] \
  [HOSTNAME]/[PROJECT-ID]/[IMAGE]:[NEW_TAG]
```

Tips:
- `gcloud container images add-tag` コマンドは、別プロジェクトのリポジトリへのイメージのコピーにも使える

関連ドキュメント:
- [Managing images | Container Registry Documentation | Google Cloud](https://cloud.google.com/container-registry/docs/managing)

### endpoints

https://cloud.google.com/sdk/gcloud/reference/endpoints

APIサービスの作成・有効化・管理を行う。

#### services

https://cloud.google.com/sdk/gcloud/reference/endpoints/services

サービスの管理を行う。

Examples:

```sh
gcloud endpoints services list
gcloud endpoints services delete ENDPOINT
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

### info

https://cloud.google.com/sdk/gcloud/reference/info

gcloudのconfigファイルのパスなど環境構成情報を表示する。

Examples:

```sh
gcloud info
# 特定の値を抽出
gcloud info --format='value(config.paths.global_config_dir)'
# ネットワーク接続や隠し属性のチェック
gcloud info --run-diagnostics
# 直近のログを表示
gcloud info --show-log
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

### バケット操作

- [mb](https://cloud.google.com/storage/docs/gsutil/commands/mb)
- [rb](https://cloud.google.com/storage/docs/gsutil/commands/rb)

Examples:

```sh
# バケット作成
gsutil mb -l asia gs://mybucket
# バケット削除
gsutil rb [-f] gs://<bucket_name>
```

### iam

https://cloud.google.com/storage/docs/gsutil/commands/iam

```sh
# bucket/objectのIAM権限を取得
gsutil iam get gs://bucket[/path]
# bucket/objectにIAM権限を設定
gsutil iam set [-afRr] [-e <etag>] file gs://bucket[/path] ...
# bucket/objectにIAM権限を設定。メンバー単位で個々に設定
gsutil iam ch [-fRr] binding ... gs://bucket
```

関連項目:

- [GCS#IAM]({{<ref "gcs.md">}}#iam)

### ls

https://cloud.google.com/storage/docs/gsutil/commands/ls

バケットやオブジェクトのリスト表示。

Examples:

```sh
gsutil ls gs://my-bucket/

# 古いバージョンも含める
gsutil ls -a gs://my-bucket/
```

### rm

https://cloud.google.com/storage/docs/gsutil/commands/rm

オブジェクトの削除。

Examples:

```sh
# subdir/ 直下のオブジェクトを削除
gsutil rm gs://bucket/subdir/*
# subdir/ 下の全てのオブジェクトを削除
gsutil rm gs://bucket/subdir/**
# 上と同じ
gsutil rm -r gs://bucket/subdir/

# 古いバージョンも含めて削除
gsutil rm -a gs://bucket/path/to/object
```

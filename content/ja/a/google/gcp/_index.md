---
title: "Google Cloud Platform"
linkTitle: "GCP"
description: >
  https://cloud.google.com/
date: 2020-04-27T10:39:24+09:00
weight: 200
---

## 障害情報

- https://status.cloud.google.com/
  - RSSもある
- https://twitter.com/gcpstatus でも配信されている

## quota

リソース制限。割当て上限。

### 緩和方法

参考:

- [GCP リソースの割り当てを増加(上限緩和申請) - Qiita](https://qiita.com/mouse2/items/dd136453798804f99de7)

## コスト管理

コスト節約のためのナレッジ:

- 2020-04-21 [クラウドコストの最適化のためのベスト プラクティス | Google Cloud Blog](https://cloud.google.com/blog/ja/products/gcp/best-practices-for-optimizing-your-cloud-costs)

## 監査
### Cloud Audit Logging

https://cloud.google.com/logging/docs/audit/?hl=ja

デフォルトでもある程度ログを取ってくれるが、有効期限がある。  
永久に保存したい場合は、GCSにエクスポートが必要そう。

https://cloud.google.com/logging/quotas?hl=ja#logs_retention_periods

## 組織

AWSのOrganizationみたいなものと思う。  
G Suiteだとドメインに紐づくか。

### フォルダ

フォルダを作って組織内のプロジェクトを階層化できる。  
例えば組織の部門ごとにフォルダを作ると、権限管理など便利。

See [フォルダの作成と管理 | Google Cloud Resource Manager ドキュメント | Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-folders?hl=ja "フォルダの作成と管理  |  Google Cloud Resource Manager ドキュメント  |  Google Cloud")

### プロジェクトを組織に移行

元々組織に紐付いていなかったプロジェクトを組織に紐付けることができる。  
戻すこともできるが、プロジェクト作成者のみ(？)

プロジェクトは組織のポリシーに準じるようになるので、不整合が起こらないようにしないといけない、といった注意点があるようだ。

See [組織に既存のプロジェクトを移行する | Google Cloud Resource Manager ドキュメント | Google Cloud](https://cloud.google.com/resource-manager/docs/migrating-projects-billing?hl=ja "組織に既存のプロジェクトを移行する  |  Google Cloud Resource Manager ドキュメント  |  Google Cloud")

### 制限

組織内に作れるプロジェクト数は上限がある。  
緩和申請もできるみたい。

- [Project quota requests \- Cloud Platform Console ヘルプ](https://support.google.com/cloud/answer/6330231?hl=ja)

## APIとサービス

https://console.cloud.google.com/apis/library

- 一覧の確認には、 `gcloud services list` コマンドを使う

### 認証
ドキュメント:

- [認証の概要 | Google Cloud](https://cloud.google.com/docs/authentication?hl=ja)
- [エンドユーザーとして認証する | Google Cloud](https://cloud.google.com/docs/authentication/end-user?hl=ja) ... OAuth 2.0を使う

### OAuthスコープ

- [OAuth 2.0 Scopes for Google APIs | Google Identity Platform](https://developers.google.com/identity/protocols/oauth2/scopes)
- https://cloud.google.com/sdk/gcloud/reference/compute/instances/create#--scopes ... エイリアス一覧

## 構成管理
### Cloud Deployment Manager

https://cloud.google.com/deployment-manager/

YAMLでPythonテンプレートとJinja2に対応している。

- Documentation: https://cloud.google.com/deployment-manager/docs/
  - [サポートされるリソースタイプ  |  Cloud Deployment Manager のドキュメント  |  Google Cloud](https://cloud.google.com/deployment-manager/docs/configuration/supported-resource-types)

## 開発
### ローカル開発用サーバ

一部のサービスには、自動テストなどでも使えるエミュレータが提供されている:

- [Cloud Datastore](https://cloud.google.com/datastore/docs/tools/datastore-emulator)
- [Cloud Bigtable](https://cloud.google.com/bigtable/docs/emulator?hl=ja)
- [Cloud Pub/Sub](https://cloud.google.com/pubsub/docs/emulator?hl=ja)

## Service Usage

https://cloud.google.com/service-usage/docs/overview?hl=ja

GCPサービスやAPIの表示、管理。

### 権限

https://cloud.google.com/service-usage/docs/access-control

QuotaやBillingの操作をするとき、 `serviceusage.services.use` が要求される。  
例:

- `gcloud logging logs list`

## Services

だいたい子ページを作っているが、雑多なものをここにまとめる。

### Storage Transfer

[概要 | Cloud Storage Transfer Service のドキュメント | Google Cloud](https://cloud.google.com/storage-transfer/docs/overview?hl=ja)

次のことを可能にするサービス:

- 他のクラウド ストレージ プロバイダから、またはオンプレミス ストレージから Cloud Storage バケットにデータを転送またはバックアップします。
- ある Cloud Storage バケットから別の Cloud Storage バケットにデータを転送し、さまざまなユーザー グループやアプリケーションで使用できるようにします。
- データ処理パイプラインまたは分析ワークフローの一部として、データを定期的に移動する。

## Tips
### ラベルの運用

[ラベルの作成と管理 | Resource Manager のドキュメント | Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-labels?hl=ja)

## 参考
- [はじめてのGCP - Qiita](https://qiita.com/smallpalace/items/bc07c00d1583dbe53a79) ... 2018年8月時点だが、ネットワークセキュリティ周りなどそこそこまとまっている

## Child Pages

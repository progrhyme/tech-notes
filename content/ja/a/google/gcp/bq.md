---
title: "BigQuery"
linkTitle: "BigQuery"
description: https://cloud.google.com/bigquery/
date: 2020-06-22T11:57:02+09:00
weight: 45
---

## Documentation

- [割り当てと上限 | BigQuery | Google Cloud](https://cloud.google.com/bigquery/quotas?hl=ja)

### 料金

https://cloud.google.com/bigquery/pricing

- ストレージ:
  - アクティブストレージ ... 2020-04-22現在、GCSのStandard Storageより若干安い
  - 長期保存 ... テーブルに90日編集がなければ↑から50%値引きされる。2020-04-22現在、GCSのNealineと同額

### Quotas

ストリーミング挿入:

 Item | Quota
------|-------
 行の最大サイズ | 1MB

## Concept

- データセット ... プロジェクトに属し、テーブルやビューを管理する最上位のコンテナ
  - データセットの概要 | BigQuery | Google Cloud

## 機能
### Cloud SQL連携

[Cloud SQL 連携クエリ | BigQuery | Google Cloud](https://cloud.google.com/bigquery/docs/cloud-sql-federated-queries?hl=ja)

連携設定を行うことで、Cloud SQL上のデータをリアルタイムに参照するVIEWを作成できる。

## 仕様
### `0000-00-00 00:00:00` は取り扱えない

MySQLサーバで `NO_ZERO_DATE` modeが有効でないと入ってくるデータだが、BQでは扱えない。

関連項目:

- [MySQL#SQL-Mode]({{<ref "/a/software/mysql/_index.md">}}#sql-mode)

## How-to
### Colaboratoryから使う

関連項目:

- [Colaboratory]({{<ref "/a/google/colab.md">}})

参考:

- [ColaboratoryでBigQueryにアクセスする3つの方法 - Qiita](https://qiita.com/Hyperion13fleet/items/a77ca93a61cb39d50138)

## 運用
### 有効期限の設定

https://cloud.google.com/bigquery/docs/updating-datasets?hl=ja#table-expiration

- **テーブルの有効期限** ... テーブル作成時からの日数を設定できる
- **パーティションの有効期限** ... パーティション分割テーブルで、パーティションの有効期限を設定できる

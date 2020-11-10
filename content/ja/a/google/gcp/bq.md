---
title: "BigQuery"
linkTitle: "BigQuery"
description: https://cloud.google.com/bigquery/
date: 2020-06-22T11:57:02+09:00
weight: 45
---

## 関連ページ

- [bq CLI]({{<ref "cli/bq.md">}})

## Documentation

- [割り当てと上限 | BigQuery | Google Cloud](https://cloud.google.com/bigquery/quotas?hl=ja)

### 料金

https://cloud.google.com/bigquery/pricing

- ストレージ:
  - アクティブストレージ ... 2020-04-22現在、GCSのStandard Storageより若干安い
  - 長期保存 ... テーブルに90日編集がなければ↑から50%値引きされる。2020-04-22現在、GCSのNealineと同額

## Concept

- データセット ... プロジェクトに属し、テーブルやビューを管理する最上位のコンテナ
  - データセットの概要 | BigQuery | Google Cloud

## 機能
### Cloud SQL連携

[Cloud SQL 連携クエリ | BigQuery | Google Cloud](https://cloud.google.com/bigquery/docs/cloud-sql-federated-queries?hl=ja)

連携設定を行うことで、Cloud SQL上のデータをリアルタイムに参照するVIEWを作成できる。

### Authorized View (承認済みビュー)

[承認済みビューの作成 | BigQuery | Google Cloud](https://cloud.google.com/bigquery/docs/share-access-views?hl=ja)

> データセットに表示アクセス権を設定する場合、BigQuery では承認済みビューを作成します。承認済みビューを使用すると、元のテーブルへのアクセス権がないユーザーでも、クエリの結果を特定のユーザーやグループと共有できます。ビューの SQL クエリを使用して、ユーザーがクエリを実行できる列（フィールド）を制限することもできます

## 仕様
### `0000-00-00 00:00:00` は取り扱えない

MySQLサーバで `NO_ZERO_DATE` modeが有効でないと入ってくるデータだが、BQでは扱えない。

関連項目:

- [MySQL#SQL-Mode]({{<ref "/a/software/mysql/_index.md">}}#sql-mode)

## Limitations (Quota)

- https://cloud.google.com/bigquery/quotas
- https://cloud.google.com/bigquery/docs/reference/standard-sql/data-manipulation-language#limitations

### ストリーミング挿入

 Item | Quota
------|-------
 行の最大サイズ | 1MB

- ストリーミング（tabledata.insertall メソッド）を使用して直近30分以内にテーブルに書き込まれた行は、UPDATE、DELETE、MERGE ステートメントを使用して変更することはできない

## How-to
### Colaboratoryから使う

関連項目:

- [Colaboratory]({{<ref "/a/google/colab.md">}})

参考:

- [ColaboratoryでBigQueryにアクセスする3つの方法 - Qiita](https://qiita.com/Hyperion13fleet/items/a77ca93a61cb39d50138)

### INFORMATION_SCHEMAによるメタデータの取得

https://cloud.google.com/bigquery/docs/information-schema-tables?hl=ja

Examples:

```sql
-- テーブル情報一覧
SELECT * FROM [[project_id.]dataset_id.]INFORMATION_SCHEMA.TABLES
```

## 運用
### 有効期限の設定

https://cloud.google.com/bigquery/docs/updating-datasets?hl=ja#table-expiration

- **テーブルの有効期限** ... テーブル作成時からの日数を設定できる
- **パーティションの有効期限** ... パーティション分割テーブルで、パーティションの有効期限を設定できる

### 権限管理

- [データセットへのアクセスの制御 | BigQuery | Google Cloud](https://cloud.google.com/bigquery/docs/dataset-access-controls?hl=ja)
- [テーブルおよびビューへのアクセスの制御 | BigQuery | Google Cloud](https://cloud.google.com/bigquery/docs/table-access-controls)
- [BigQuery の列レベルのセキュリティの概要 | Google Cloud](https://cloud.google.com/bigquery/docs/column-level-security-intro?hl=ja)

## 標準SQL

https://cloud.google.com/bigquery/docs/reference/standard-sql/

### 文字列関数

https://cloud.google.com/bigquery/docs/reference/standard-sql/string_functions

Examples:

```sql
-- 結合
CONCAT(value1[, value2, ...])

-- 置換
REGEXP_REPLACE(value, regexp, replacement)
REPLACE(original_value, from_value, to_value)
```

### 日時関数

https://cloud.google.com/bigquery/docs/reference/standard-sql/datetime_functions

Examples:

```sql
-- 現在日時
CURRENT_DATETIME()
CURRENT_DATETIME("Asia/Tokyo")
```

### タイムスタンプ関数

https://cloud.google.com/bigquery/docs/reference/standard-sql/timestamp_functions

Examples:

```sql
-- 現在日時
CURRENT_TIMESTAMP()

-- TIMESTAMP型への変換
TIMESTAMP("2008-12-25 15:30:00+00")
TIMESTAMP("2008-12-25 15:30:00", "Asia/Tokyo")
TIMESTAMP("2008-12-25 15:30:00 UTC")
TIMESTAMP(DATETIME "2008-12-25 15:30:00")
TIMESTAMP(DATE "2008-12-25")

-- タイムスタンプの減算
TIMESTAMP_SUB(<timestamp_expression>, INTERVAL <int64_expression> <date_part>)
-- 10分前
TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 10 MINUTE)
```

### タイムゾーンの指定方法

https://cloud.google.com/bigquery/docs/reference/standard-sql/timestamp_functions?hl=ja#timezone_definitions

タイムゾーン名（例: `Asia/Tokyo` ）か、オフセット（例: `+09` ）を指定する。

### DROP VIEW

https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language?hl=ja#drop_view_statement

ビューの削除。

Syntax:

```sql
DROP VIEW [IF EXISTS] [[project_name.]dataset_name.]view_name
```

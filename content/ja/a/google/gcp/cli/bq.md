---
title: "bq"
linkTitle: "bq"
date: 2020-11-10T09:49:17+09:00
weight: 10
---

BigQuery操作CLI

リファレンス: https://cloud.google.com/bigquery/docs/reference/bq-cli-reference?hl=ja

## 関連ページ

- [BigQuery]({{<ref "/a/google/gcp/bq.md">}})

## cp

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

## load

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

## ls

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

## mk

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

## show

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

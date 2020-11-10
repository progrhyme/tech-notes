---
title: "cbt"
linkTitle: "cbt"
date: 2020-11-10T09:49:20+09:00
weight: 20
---

Bigtable操作CLI

- リファレンス: https://cloud.google.com/bigtable/docs/cbt-reference?hl=ja
- インストール: [cbt ツールの概要 | Cloud Bigtable ドキュメント | Google Cloud](https://cloud.google.com/bigtable/docs/cbt-reference?hl=ja)

## 全般オプション

 option | 意味
--------|-----
 `-project` | プロジェクトID
 `-instance` | インスタンス

## count

テーブル内の行数を数える

Example:

```sh
cbt count <table>
```

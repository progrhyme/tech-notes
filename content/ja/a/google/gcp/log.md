---
title: "Cloud Logging"
linkTitle: "Logging"
description: https://cloud.google.com/logging
date: 2020-06-10T11:41:21+09:00
weight: 300
---

旧Stackdriver Logging

## クエリ

[高度なログクエリ | Stackdriver Logging | Google Cloud](https://cloud.google.com/logging/docs/view/advanced-queries?hl=ja)

```
// 特定のフィールド/エントリが含まれるログ
some_key:*
```

参考:

- [サンプルクエリ | Stackdriver Logging | Google Cloud](https://cloud.google.com/logging/docs/view/advanced-queries?hl=ja)

## Features
### Export

[ログビューアによるエクスポート | Stackdriver Logging | Google Cloud](https://cloud.google.com/logging/docs/export/configure_export_v2?hl=ja)

シンクのエクスポート先:
- Cloud Storage
- Pub/_Sub
- BigQuery

### ログベースメトリクスの作成

[ログベースの指標の概要 | Stackdriver Logging | Google Cloud](https://cloud.google.com/logging/docs/logs-based-metrics/counter-metrics?hl=ja)

MEMO:
- Loggingの検索結果から、Cloud Monitoringのメトリクスを作成できる

### ログの除外（Exclusion）

[ログの除外 | Cloud Logging | Google Cloud](https://cloud.google.com/logging/docs/exclusions?hl=ja)

特定のログの取り込みを除外して、課金額を下げることができる。

Tips:

- 除外される前にエクスポートすることもできる
  - 除外しつつBigQueryにエクスポートして、Loggingの課金なしに、BQからログを利用することが可能
- 完全に除外するのではなく、除外する割合をパーセンテージで設定することも可能。99.9%など、少数値も設定可能

## Specification
### LogSeverity

severityは数値が定義されていて、比較演算子でフィルタできる。

See https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity

 severity | enum
------------|---------
 DEFAULT | 0
 DEBUG | 100
 INFO | 200
 NOTICE | 300
 WARNING | 400
 ERROR | 500
 CRITICAL | 600
 ALERT | 700
 EMERGENCY | 800

## How-to
### 利用量の確認

Logs Ingestionでresource type別のログ利用量を確認できる。

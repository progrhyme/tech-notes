---
title: "Datadog"
linkTitle: "Datadog"
description: https://www.datadoghq.com/
date: 2020-05-14T19:05:18+09:00
weight: 120
---

監視ソリューションをサービスとして提供している。

## 料金

https://www.datadoghq.com/ja/pricing/

参考:

- [Datadogの課金体系について - Qiita](https://qiita.com/t_ume/items/a45fcf5f464beb50d876)
- 2016年の記事: [Datadogの請求書に怯えないためにするべきこと - Qiita](https://qiita.com/selmertsx/items/9dd5af1d6d5d94ce6972)

## Documentation

https://docs.datadoghq.com/

## Status

- https://status.datadoghq.com/
- https://twitter.com/datadogops

## Features

- Dashboards
   - [Querying](https://docs.datadoghq.com/dashboards/querying/)

### Alerting
#### Logs Monitor

https://docs.datadoghq.com/monitors/monitor_types/log/

ログに対して監視を設定できる。

### Log Management
#### Generate Metrics

https://docs.datadoghq.com/logs/logs_to_metrics/

ログからメトリクスを生成できる。

参考:

- [新機能 Metrics from Logs と Log Rehydration™ の紹介 | Datadog](https://www.datadoghq.com/ja/blog/logging-without-limits-new-features/)
- [ログからメトリクスを生成し、過去の傾向の表示や SLO の追跡を実行する。 | Datadog](https://www.datadoghq.com/ja/blog/log-based-metrics/)

## インテグレーション

https://docs.datadoghq.com/integrations/

各種ツール、サービスと連携が可能。

### Google Cloud Platform

https://docs.datadoghq.com/integrations/google_cloud_platform/

#### セットアップ

メトリクスの収集:

1. サービスアカウント作成
   - 権限「Compute Viewer」「Monitoring Viewer」「Cloud Asset Viewer」をつける
   - サービスアカウントキーをJSONで作成
1. 作成したサービスアカウントキーをDatadogのGCPインテグレーションの画面でUpload

ログの収集:

1. Cloud Pub/Sub Topicを作成
1. 上のTopicのSubscriberを作成
   - 配信タイプとして Push を選択し、 `https://gcp-intake.logs.datadoghq.com/v1/input/<DATADOG_API_KEY>/` と入力
1. Cloud LoggingでログをPub/Subエクスポートし、上で作ったTopicを指定する

### Slack

https://docs.datadoghq.com/integrations/slack/

1. Slack側でDatadogインテグレーションを追加し、Webhook URLを取得する
1. Datadog側でSlackインテグレーションを追加
    - 「Configuration」タブで通知先チャネルを選択

Monitorの通知先に設定するには、通知先に `@slack-<チャネル名>` を入れる。

## 事例

- [Datadog Log Management でアプリケーション稼働モニタリング - 一休.com Developers Blog](https://user-first.ikyu.co.jp/entry/application_monitoring_with_datadog_log_management)

---
title: "Cloud Monitoring"
linkTitle: "Monitoring"
description: https://cloud.google.com/monitoring
date: 2020-10-22T09:18:17+09:00
weight: 310
---

旧Stackdriver Monitoring

## Documentation

- https://cloud.google.com/monitoring/docs
- https://cloud.google.com/monitoring/docs/apis ... APIリファレンス
  - https://cloud.google.com/monitoring/api/metrics ... メトリクス一覧
- https://cloud.google.com/monitoring/docs/resources

## アラート

- [アラート ポリシーの条件を指定する | Stackdriver Monitoring | Google Cloud](https://cloud.google.com/monitoring/alerts/ui-conditions-ga?hl=ja)
- [アラート ポリシーの詳細 | Stackdriver Monitoring | Google Cloud](https://cloud.google.com/monitoring/alerts/concepts-indepth?hl=ja)
- [インシデントとイベント | Stackdriver Monitoring | Google Cloud](https://cloud.google.com/monitoring/alerts/incidents-events?hl=ja)

### Limitation

2020-10-22更新。

- 指標データが欠落または遅延していると、ポリシーによってアラートされなくなり、インシデントが閉じられなくなる可能性がある https://cloud.google.com/monitoring/alerts/concepts-indepth?hl=ja#partial-metric-data
- メトリクスデータがない状態を正常とするようなアラートを作ると、エラーが解消しても7日間クローズされなくなる
- インシデントの状態を手動で解決済みに変更することはできない

## 稼働時間チェック (Uptime Checks)

https://cloud.google.com/monitoring/uptime-checks

無料の外形監視ツール。

## エージェント

https://cloud.google.com/monitoring/agent

Cloud Monitoringエージェント。  
GCE等にインストールして使える。

- [Cloud Monitoring エージェントをインストールする | Google Cloud](https://cloud.google.com/monitoring/agent/install-agent?hl=ja)
  - [StatsD プラグイン | Cloud Monitoring | Google Cloud](https://cloud.google.com/monitoring/agent/plugins/statsd?hl=ja)

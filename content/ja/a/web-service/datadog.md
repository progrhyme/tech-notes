---
title: "Datadog"
linkTitle: "Datadog"
description: https://www.datadoghq.com/
date: 2020-05-14T19:05:18+09:00
weight: 120
---

監視ソリューションをサービスとして提供している。

## Documentation

https://docs.datadoghq.com/

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

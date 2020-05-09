---
title: "Container Registry"
linkTitle: "GCR"
description: https://cloud.google.com/container-registry
date: 2020-05-07T16:23:49+09:00
weight: 210
---

Dockerコンテナレジストリ。

## Getting Started

Documentation:

- https://cloud.google.com/container-registry/docs
  - [リソース](https://cloud.google.com/container-registry/docs?hl=ja) ... 料金、クォータ、リリースノートなど

### 認証

dockerコマンドでGCRにアクセスできるようにする:

```sh
gcloud auth configure-docker
```

https://cloud.google.com/container-registry/docs/advanced-authentication

## How-to
### Pub/Sub通知

[Pub/Sub 通知の構成 | Container Registry のドキュメント | Google Cloud](https://cloud.google.com/container-registry/docs/configuring-notifications?hl=ja)

> イメージが push、タグ付け、削除されたときなど、Container Registry リポジトリに変更が加えられた場合、Pub/Sub を使用して通知を受け取ることができます


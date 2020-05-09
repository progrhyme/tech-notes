---
title: "Cloud Load Balancing"
linkTitle: "Load Balancing"
description: >
  https://cloud.google.com/load-balancing
date: 2020-04-27T10:48:40+09:00
weight: 300
---

## Documentation

https://cloud.google.com/load-balancing/docs/

## 概要

- [HTTP(S) 負荷分散のコンセプト | 負荷分散 | Google Cloud](https://cloud.google.com/load-balancing/docs/https/?hl=ja)
- [バックエンド サービスについて | 負荷分散 | Google Cloud](https://cloud.google.com/load-balancing/docs/backend-service?hl=ja)

## Spec

- IP anycast対応
- アーキテクチャ:
  - [グローバル負荷分散によるアプリケーションの処理能力の改善 | アーキテクチャ | Google Cloud](https://cloud.google.com/solutions/about-capacity-optimization-with-global-lb?hl=ja) ... IP anycast, GFE

### SSL証明書

https://cloud.google.com/load-balancing/docs/ssl-certificates

- マネージド証明書
  - Let's Encrypt
  - DV
  - 自動更新
  - ワイルドカードドメインは不可

### 接続ドレイン

[コネクション ドレインの有効化 | 負荷分散 | Google Cloud](https://cloud.google.com/load-balancing/docs/enabling-connection-draining?hl=ja)

コネクションドレインとも表記される。（公式ドキュメント統一してくれ）

> コネクション ドレインとは、VM がインスタンス グループから除外されたときに、既存の進行中リクエストに完了までの時間が確実に与えられるようにするプロセスです。
> 
> コネクション ドレインを有効にするには、バックエンド サービスでコネクション ドレイン タイムアウトを設定します。タイムアウト時間は 1～3,600 秒に設定してください。

デフォルトONでいいんじゃないかと思うのだが、2020-04-27現在は、上記のように設定が必要。

次のLBのバックエンドサービスで使える:

- HTTP(S) ロードバランサ
- TCP プロキシ ロードバランサ
- SSL プロキシ ロードバランサ
- 内部 HTTP(S) ロードバランサ
- 内部 TCP / UDP ロードバランサ

## 外部HTTP(S)負荷分散
### バックエンドバケット

[ロードバランサへの Cloud Storage バケットの追加 | 負荷分散 | Google Cloud](https://cloud.google.com/load-balancing/docs/https/adding-backend-buckets-to-load-balancers?hl=ja)

Cloud Storageバケットをバックエンドに追加し、パスで振り分けることができる。

## Logging

[HTTP(S) 負荷分散のロギングとモニタリング | Google Cloud](https://cloud.google.com/load-balancing/docs/https/https-logging-monitoring?hl=ja)

## Topics
### GCLBとCDNによる動的サイト高速化

[グローバル負荷分散によるアプリケーションの処理能力の改善 | アーキテクチャ | Google Cloud](https://cloud.google.com/solutions/about-capacity-optimization-with-global-lb?hl=ja)にあるように、GCLBを前段に置いたサービスでは、GFEによるネットワーク経路最適化やTLS終端の恩恵を得られる。  
従って、APIの[動的サイト高速化](https://docs.microsoft.com/ja-jp/azure/cdn/cdn-dynamic-site-acceleration)をねらいとしてCDNを入れる意味は薄い。  
特に、全くキャッシュをしない場合、CDNを入れても入れなくてもほとんど変わらない、とGoogle Cloudの中の人が言っていた。（無意味ではないけど、ネットワークのゆらぎぐらいの差らしい）

---
title: "Elasticsearch"
linkTitle: "Elasticsearch"
description: https://www.elastic.co/jp/elasticsearch/
date: 2020-07-10T23:39:27+09:00
weight: 100
---

## Architecture

ノードの種類:

- Master node ... クラスタで1台だけ
- Master-eligible node ... マスター候補。マスターが故障したら、この中から新たなマスターが選ばれる。
- Data node
- Coordinating node
- Coordinating only node

参考:

- [はじめてのElasticsearchクラスタ](https://www.slideshare.net/snuffkin/elasticsearch-107454226)
- [Elasticsearch クラスタ概説](https://gist.github.com/yano3/3f5abc9eba0c1ad6a0508056961b273c)
- [elasticsearchでノード障害が起きたときの動作 #elastic - クリエーションライン株式会社](https://www.creationline.com/blog/15831)

## Kubernetes

スタートガイド:

- [Quickstart | Elastic Cloud on Kubernetes \[1.1\] | Elastic](https://www.elastic.co/guide/en/cloud-on-k8s/current/k8s-quickstart.html)

参考:

- [Elasticsearch on GKEで注意すべき可用性・耐久性のポイント - Qiita](https://qiita.com/ryo-yamaoka/items/0b968112f03672991a5f)

## Releases
### v6.0

Breaking Changes: https://www.elastic.co/guide/en/elasticsearch/reference/6.0/breaking-changes-6.0.html

- 複数のmapping typesを持つindexは作れなくなった。

## Mapping

JSONとかでデータを入れると良い感じにマッピングしてくれる印象。  
Kibanaとか。

参考:

- [Elasticsearch マッピング – Hello! Elasticsearch. – Medium](https://medium.com/hello-elasticsearch/elasticsearch-9a8743746467 "Elasticsearch マッピング – Hello! Elasticsearch. – Medium")

### データ型

https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-types.html

#### 数値型

https://www.elastic.co/guide/en/elasticsearch/reference/current/number.html

- 整数型: byte, short, integer, long
- 実数型: `scaled_float`, `half_float`, `float`, `double`

## 運用
### ヒープダンプでDiskを消費する

ElasticsearchのデフォルトのJVM起動引数に `-XX:+HeapDumpOnOutOfMemoryError` がついているそうで、メモリの少ない環境で動かしていると、Elasticsearchを起動したディレクトリに数GBサイズの `java_pidXXXX.hprof` ファイルが吐かれるようだ。

参考:

- [Elasticsearchをメモリの足りない環境で動かしているとDisk Fullになる。 \- Qiita](https://qiita.com/aya_eiya/items/f0871f58c7eb23c85ee8)

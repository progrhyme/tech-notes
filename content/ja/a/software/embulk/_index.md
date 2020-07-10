---
title: "Embulk"
linkTitle: "Embulk"
description: https://www.embulk.org/
date: 2020-07-01T20:19:41+09:00
weight: 110
---

## About

Treasure Data社発のOSSで、プラガブルなETLフレームワーク的なソフトウェア。

Documentation: https://www.embulk.org/docs/

## Spec

- 内部に独自データ型を持っているようで、Inputプラグインから受け取る際に一度変換が起こる

## Configuration

- YAMLまたは[Liquidテンプレート](https://shopify.github.io/liquid/)。

### Liquidテンプレート

https://www.embulk.org/docs/built-in.html#using-variables

重要:

- Liquidテンプレートを使う場合、 **拡張子は必ず `.yml.liquid` にしなければならない**

機能:

- 環境変数の利用。例: `{{ env.ENV_KEY }}`
- include

### フォーマット

```YAML
in: # Input plugin
  paraser: # Parser plugin
  decoder: # Decoder plugin
out: # Output plugin
  formatter: # Formatter plugin
  encoder: # Encoder plugin
filters: # Filter plugin
exec: # Executor plugin
```

## CLI

```sh
# 実行
embulk run [OPTIONS] config.yml[.liquid]

# プレビュー
embulk preview [OPTIONS] config.yml[.liquid]
```

 Option | 値 | 機能
--------|----|-----
 `-l, --log-level LEVEL` | trace,debug,info,warn,error | ログレベル

## Troubles

遭遇したエラーなどについて書く。  
個別のプラグインの問題は[Plugins]({{<ref "plugin.md">}})に記す。

全体的にエラーがわかりづらいと思う。

参考:

- [大量データの転送にEmbulkを使ってみたら本当に楽だった - VOYAGE GROUP techlog](https://techlog.voyagegroup.com/entry/2017/07/31/173839)

### Setting null to a task field is not allowed

例:

```
Error: org.embulk.config.ConfigException: com.fasterxml.jackson.databind. \
JsonMappingException: Setting null to a task field is not allowed. Use Optional<T> \
(com.google.common.base.Optional) to represent null.
```

どうも、configの設定値が取れなかったときに起こるエラーっぽい。  
よくあるのは、環境変数の設定ミス（一度やらかした）。

- キーが間違っていないか
- exportしているか

などを確認するとよさそう。

### A Buffer detected double release() calls

2020年7月、MySQL -> BigQueryへのETL操作をAWS ECS Fargate上で実行しているときに、50GB以上の大きなテーブルで起こった。

- ログ: https://gist.github.com/progrhyme/a0455ba29e3c590daacdb187d3f8282b

今のところ、ECS Taskのストレージ不足なのでは、という気がしている。  
Fargateのエフェメラルストレージは20GB程度しかないようなので。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">ありがとうございます。Errno::ENOSPCって出ているから、中間データを書き込むためのディスク容量が足りないってことはないですか？</p>&mdash; Hiroyuki Sato (@hiroysato) <a href="https://twitter.com/hiroysato/status/1281580625602834438?ref_src=twsrc%5Etfw">July 10, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

参考:

- [Fargate タスクストレージ - Amazon Elastic Container Service](https://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/fargate-task-storage.html)

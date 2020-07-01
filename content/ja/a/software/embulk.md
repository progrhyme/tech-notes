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

## Plugins
### Input

一覧: https://plugins.embulk.org/#input

- [embulk-input-mysql](https://github.com/embulk/embulk-input-jdbc/tree/master/embulk-input-mysql)

### Output

一覧: https://plugins.embulk.org/#output

- [embulk-output-bigquery](https://github.com/embulk/embulk-output-bigquery)

## Pitfalls

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

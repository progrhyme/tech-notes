---
title: "Cloud Functions"
linkTitle: "Cloud Functions"
description: https://cloud.google.com/functions
date: 2020-05-04T09:26:37+09:00
weight: 110
---

## Getting Started

https://cloud.google.com/functions/docs?hl=ja

## How-to
### ログ出力

https://cloud.google.com/functions/docs/monitoring/logging

Cloud Loggingにログを送ることができる。  
言語によってやり方が異なる。

- 共通: 標準出力/標準エラー出力
- Node.js
  - `console.log()` -> `INFO` ログ
  - `console.error()` -> `ERROR` ログ

参考:
- [Cloud FunctionsのlogをstackdriverにjsonPayloadで送りたい - Qiita](https://qiita.com/Sho2010@github/items/460900d16cdee7f3d2bd)

### VPC接続

- [VPC ネットワークへの接続 | Cloud Functions のドキュメント | Google Cloud](https://cloud.google.com/functions/docs/connecting-vpc?hl=ja)

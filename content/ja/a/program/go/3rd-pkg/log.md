---
title: "ロギング"
linkTitle: "ロギング"
date: 2020-07-07T07:35:30+09:00
weight: 2850
---

## google/logger

- https://github.com/google/logger
- https://pkg.go.dev/github.com/google/logger

クロスプラットフォームでシンプルなロガー。  
ログレベルはinfo, warning, error, fatalの4段階。

## rs/zerolog

- https://github.com/rs/zerolog
- https://pkg.go.dev/github.com/rs/zerolog

高速でシンプルなJSONロガー。

## sirupsen/logrus

- https://github.com/sirupsen/logrus
- https://pkg.go.dev/github.com/sirupsen/logrus

標準のlogパッケージと互換性のあるAPIで、構造化ロギングを提供。

NOTICE:

- 2020-07-07現在、メンテナンスモードに入っており、今後はセキュリティやバグ修正、パフォーマンスに関する対応が中心になるとしている。

## uber-go/zap

- https://github.com/uber-go/zap
- https://pkg.go.dev/github.com/uber-go/zap

とても高速らしいロガー。構造化ログ、ログレベル対応。  
go.uber.orgなライブラリへの依存がある。

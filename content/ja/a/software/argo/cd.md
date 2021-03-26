---
title: "Argo CD"
linkTitle: "Argo CD"
description: https://argoproj.github.io/argo-cd/
date: 2020-05-08T17:20:10+09:00
---

## Features

- [SSO Overview - Argo CD - Declarative GitOps CD for Kubernetes](https://argoproj.github.io/argo-cd/operator-manual/sso/)
  - [dex](https://github.com/dexidp/dex)を使ってOpen ID対応できる
- [Automated Sync Policy - Argo CD - Declarative GitOps CD for Kubernetes](https://argoproj.github.io/argo-cd/user-guide/auto_sync/)
  - Automatic Pruning
    - デフォルトではリソースの削除はやらないが、このオプションをONにすると、削除同期もやってくれる

## Demo

https://cd.apps.argoproj.io/applications

## Specification

- AppProject Custom Resourceはnamespaceバウンドだけど、別namespaceのリソースのデプロイはサポートされている
  - [Issue #696 - Support apps with static namespaces in resources by alexmt · Pull Request #842 · argoproj/argo-cd · GitHub](https://github.com/argoproj/argo-cd/pull/842)

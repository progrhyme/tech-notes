---
title: "ConfigMap"
linkTitle: "ConfigMap"
description: >
  [ConfigMaps - Kubernetes](https://kubernetes.io/docs/concepts/configuration/configmap/)
date: 2020-05-04T22:39:04+09:00
weight: 55
---

See also [Secret]({{< ref "/a/software/k8s/secret.md" >}})

## Overview

[Kubernetes道場 11日目 - ConfigMap / Secretについて - Toku's Blog](https://cstoku.dev/posts/2018/k8sdojo-11/)より

> ConfigMapやSecretはアプリケーションの設定やクレデンシャルをコンテナイメージから分離するために使われる。  
> ConfigMapやSecretをVolumeとして、または環境変数を通してPodに設定やクレデンシャルを渡す。

ConfigMapはSecretと違い、値をencodeせずに平文でYAMLに書くので、普通の設定ファイル的な位置づけ。

> A ConfigMap is an API object used to store non-confidential data in key-value pairs. Pods can consume ConfigMaps as environment variables, command-line arguments, or as configuration files in a volume .

参考:

- [Kubernetes: ConfigMap / Secret の内容を一度に環境変数として読み込む (envFrom) - Qiita](https://qiita.com/tkusumi/items/cf7b096972bfa2810800)

## Getting Started

公式サイトにいくつかのガイドやサンプルがある:

- [Configure a Pod to Use a ConfigMap - Kubernetes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/)
- [Configuring Redis using a ConfigMap | Kubernetes](https://kubernetes.io/docs/tutorials/configuration/configure-redis-using-configmap/)

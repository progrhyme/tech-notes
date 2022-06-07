---
title: "EKS"
linkTitle: "EKS"
date: 2022-06-07T16:43:46+09:00
description: https://aws.amazon.com/eks/
weight: 160
---

## About
Amazon Elastic Kubernetes Service

## 公式ドキュメント

https://docs.aws.amazon.com/ja_jp/eks/index.html

- [ユーザーズガイド](https://docs.aws.amazon.com/ja_jp/eks/latest/userguide/what-is-eks.html)
- [APIリファレンス](https://docs.aws.amazon.com/ja_jp/eks/latest/APIReference/Welcome.html)

## 仕様
### コンテナランタイム

- ランタイムとしてcontainerd, Dockerがサポートされている
- EKS 1.21のデフォルトはDockerとなっている
- EKS 1.20以降ではDockerは非推奨となっている

参考:
- [Amazon EKS が Kubernetes 1.21 のサポートを開始 | Amazon Web Services ブログ](https://aws.amazon.com/jp/blogs/news/amazon-eks-1-21-released/)
- [EKSでdocker非推奨問題に対応しました - Tech Inside Drecom](https://tech.drecom.co.jp/eks-deprecates-docker/)

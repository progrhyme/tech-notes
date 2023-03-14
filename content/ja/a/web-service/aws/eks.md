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

2022-06-08現在の情報。

- ランタイムとしてcontainerd, Dockerがサポートされている
- EKS 1.21のデフォルトはDockerとなっている
- EKS 1.20以降ではDockerは非推奨となっている
- EKS 1.23でDockershimは削除される予定

参考:
- [Amazon EKS now supports Kubernetes 1.22 | Containers](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-kubernetes-1-22/)
- [Amazon EKS が Kubernetes 1.21 のサポートを開始 | Amazon Web Services ブログ](https://aws.amazon.com/jp/blogs/news/amazon-eks-1-21-released/)
- [EKSでdocker非推奨問題に対応しました - Tech Inside Drecom](https://tech.drecom.co.jp/eks-deprecates-docker/)
- [Define Container Runtime - eksctl](https://eksctl.io/usage/container-runtime/)

## How-to
### HPAのスケール条件に外部メトリクスを使う

参考:
- [Scaling Kubernetes deployments with Amazon CloudWatch metrics | AWS Compute Blog](https://aws.amazon.com/jp/blogs/compute/scaling-kubernetes-deployments-with-amazon-cloudwatch-metrics/) ... CloudWatchメトリクスを使う場合のAWS公式ガイド
- [EKSにおけるAutoScalingパターン | じゃあ、したためておきます](https://esakat.github.io/esakat-blog/posts/eks-advent-calender-2020/#%E5%A4%96%E9%83%A8%E3%83%A1%E3%83%88%E3%83%AA%E3%82%AF%E3%82%B9%E3%82%92%E5%88%A9%E7%94%A8%E3%81%97%E3%81%A6%E3%81%AE%E3%82%B9%E3%82%B1%E3%83%BC%E3%83%AA%E3%83%B3%E3%82%B0hpacloudwatchclusterautoscaler)

## ツール
### eksctl

https://eksctl.io/

公式CLI。

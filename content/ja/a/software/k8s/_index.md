---
title: "Kubernetes"
linkTitle: "Kubernetes"
description: >
  https://kubernetes.io/
date: 2020-04-27T10:39:49+09:00
weight: 300
---

関連ページ:

- [Google Cloud > GKE]({{< ref "/a/google/gcp/gke/_index.md" >}})

## Getting Started
### Documentation

- https://kubernetes.io/docs/home/ ... ドキュメント
  - https://kubernetes.io/docs/tutorials/ ... チュートリアル
  - https://kubernetes.io/docs/tasks/ ... How-toガイド
  - [Standardized Glossary - Kubernetes](https://kubernetes.io/docs/reference/glossary/?fundamental=true) ... 用語集

参考:

- [Kubernetes道場 Advent Calendar 2018 - Qiita](https://qiita.com/advent-calendar/2018/k8s-dojo)

### リファレンス

- https://kubernetes.io/docs/reference/
  - APIリファレンス
  - CLIリファレンス
  - etc.

## ベストプラクティス

- [Configuration Best Practices | Kubernetes](https://kubernetes.io/docs/concepts/configuration/overview/)

## ケーススタディ

参考:

- [Kubernetes Failure Stories](https://k8s.af/)

## Versions

- [Kubernetes version and version skew support policy - Kubernetes](https://kubernetes.io/docs/setup/release/version-skew-policy/)

## How-to
### Podの再起動

- K8sはクラスタの状態を宣言型で記述するので、「再起動する」というのを指示するのは難しいようだ
- 下の記事にあるように、Deploymentの定義を変えてapplyするのが良いだろう
- レプリカの数を0にして増やすという手もある

See

- [全ての Pod を一発でリロードさせる方法 - Qiita](https://qiita.com/dtan4/items/9e0ab5dbe8c64ed6dd21)

### 複数クラスタを設定する

- https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/ ... `kubectl config use-context` で複数クラスタを切り替えられるようにする設定チュートリアル

### 機密情報や環境設定の扱い

SecretsやConfigMapを使う。

参考:

- [Kubernetes 上で Credentials を扱う | tellme.tokyo](https://tellme.tokyo/post/2018/08/07/kubernetes-configmaps-secrets/)

### Namespaceの削除

https://kubernetes.io/docs/tasks/administer-cluster/namespaces/#deleting-a-namespace

```sh
kubectl delete namespace my-ns
kubectl delete -f my-ns.yml
```

参考:

- [Kubernetesでnamespaceを作成・変更・削除する方法 - Qiita](https://qiita.com/yusuke_kinoshita/items/d1302cc3ad4657ad3466)
- [\[小ネタ\]Kubernetesで消せないNamespaceが発生した場合の対処方法 | Developers.IO](https://dev.classmethod.jp/articles/k8s-namespace-force-delete/)

### 全リソースオブジェクト取得

`kubectl get all` では一部しか取れない。

こんな感じで行ける。

```sh
kubectl api-resources --verbs=list --namespaced -o name \
  | xargs -n 1 kubectl get --show-kind --ignore-not-found -l <label>=<value> -n <namespace>
```

参考: https://github.com/kubernetes/kubectl/issues/151#issuecomment-402003022

## Topics
### CFS quotaが有効のときCPU limits設定によってコンテナがストールする問題

2018年には起こっていた問題。  
2023-01-17現在の状況は不明。

TL;DR:

- KubeletでCPU CFS quota有効だと問題
  - OS kernelのスケジューラがCFSだったらデフォルト有効だと思う
- デフォルトの `cpu.cfs_period_us` が100ms ... この単位時間でクォータがリセットされる
- マルチコアのマシン上に複数Podがスケジュールされたとき、複数のPodが同時にCPUを使うと、すぐにlimitsに達してスロットルされてしまうことが起こり得る

仕組みについては、下の記事が詳しい:

- [CPU limits and aggressive throttling in Kubernetes - Omio Engineering - Medium](https://medium.com/omio-engineering/cpu-limits-and-aggressive-throttling-in-kubernetes-c5b20bd8a718)

関連リソース:

- https://github.com/kubernetes/kubernetes
  - [CFS quotas can lead to unnecessary throttling · Issue #67577 · kubernetes/kubernetes](https://github.com/kubernetes/kubernetes/issues/67577) ... 2020-11-01にクローズされたが、スレッドが伸びすぎたから閉じたという理由で、必ずしも解決したわけではなさそう（？）
  - [CPU Throttling on Linux kernel 5.4.0-1029-aws · Issue #97445 · kubernetes/kubernetes](https://github.com/kubernetes/kubernetes/issues/97445) ... 2023-01-17現在、オープン
- [Optimizing Kubernetes Resource Requests/Limits for Cost-Efficiency an…](https://www.slideshare.net/try_except_/optimizing-kubernetes-resource-requestslimits-for-costefficiency-and-latency-highload) pp.24-43
- [Control CPU Management Policies on the Node - Kubernetes](https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/)
- [Kubernetesのresource requests, limits - Carpe Diem](https://christina04.hatenablog.com/entry/kubernetes-resource-limits)
- Kubeletの設定:
  - [kubelet - Kubernetes](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/)
  - [Set Kubelet parameters via a config file - Kubernetes](https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/)

### クラスタが大きくなるとどんな問題があるか？

巷では不安定になるとよく言われるが、どのくらいやばいのか、どんな問題が起こり得るのかを考察する。

起こり得る問題:

- Pod Affinityを使っている場合に、スケジューリングが遅くなる。
  - ref. https://kubernetes.io/ja/docs/concepts/configuration/assign-pod-node/  
> Inter-Pod AffinityとAnti-Affinityは、大規模なクラスター上で使用する際にスケジューリングを非常に遅くする恐れのある多くの処理を要します。 そのため、数百台以上のNodeから成るクラスターでは使用することを推奨されません。

#### GKE (Google Kubernetes Engine) の場合

- 内部TCP/UDPロードバランサのバックエンドVMの最大数が250
  - https://cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing?hl=ja#limits

## Child Pages

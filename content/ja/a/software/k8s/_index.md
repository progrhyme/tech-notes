---
title: "Kubernetes"
linkTitle: "Kubernetes"
description: >
  https://kubernetes.io/
date: 2020-04-27T10:39:49+09:00
weight: 300
---

関連ページ:

- [Google Cloud > GKE]({{< ref "/a/gcp/gke.md" >}})

## Getting Started
### Documentation

- https://kubernetes.io/docs/home/ ... ドキュメント
  - https://kubernetes.io/docs/tutorials/ ... チュートリアル
  - https://kubernetes.io/docs/tasks/ ... How-toガイド

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

## Topics
### CFS quotaが有効のときCPU limits設定によってコンテナがストールする問題

2018年には起こっていた問題。  
2020-04-14現在の状況は不明。

TL;DR:

- KubeletでCPU CFS quota有効だと問題
  - OS kernelのスケジューラがCFSだったらデフォルト有効だと思う
- デフォルトの `cpu.cfs_period_us` が100ms ... この単位時間でクォータがリセットされる
- マルチコアのマシン上に複数Podがスケジュールされたとき、複数のPodが同時にCPUを使うと、すぐにlimitsに達してスロットルされてしまうことが起こり得る

仕組みについては、下の記事が詳しい:

- [CPU limits and aggressive throttling in Kubernetes - Omio Engineering - Medium](https://medium.com/omio-engineering/cpu-limits-and-aggressive-throttling-in-kubernetes-c5b20bd8a718)

関連リソース:

- [CFS quotas can lead to unnecessary throttling · Issue #67577 · kubernetes/kubernetes](https://github.com/kubernetes/kubernetes/issues/67577) ... 2020-04-14現在、まだOpen
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

## エコシステム

kubectlと周辺ツールについては[kubectl]({{< ref "/a/software/k8s/kubectl.md" >}})を見よ。

参考:

- [Kubernetesのエコシステムをまとめる - Qiita](https://qiita.com/cvusk/items/100dfb955150ef8964e5) 2018年5月時点

### マニフェスト管理

※ * は当サイト内のページ

- [kustomize]({{<ref "/a/software/k8s/kustomize.md" >}}) *
- [Helm](https://helm.sh/)
- [ksonnet](https://github.com/ksonnet/ksonnet)
  - 2019年2月で更新が止まっている。参考: [Welcoming Heptio Open Source Projects to VMware](https://tanzu.vmware.com/content/blog/welcoming-heptio-open-source-projects-to-vmware)

### テスト用クラスタ構築

- Minikube（See below）
- [Kind](https://kind.sigs.k8s.io/)
  - 参考: [Kind で量産する使い捨て Kubernetes #cicd_test_night / CICD Test Night 5th - Speaker Deck](https://speakerdeck.com/ytaka23/cicd-test-night-5th)

#### Minikube

https://github.com/kubernetes/minikube

ローカルでKubernetesを動かすためのツール。  
Linuxのみだが、ハイパーバイザを噛まさず、ローカルのdocker上に直接クラスタを構築することもできる。

- https://kubernetes.io/docs/getting-started-guides/minikube/ ... 導入ガイド
  - ※先にkubectlをインストールしておくこと

参考:

- [minikubeでローカルKubernetesクラスタを5分でつくる方法 - Qiita](https://qiita.com/mumoshu/items/8f55ee830d8e5c172dd4)
- [minikube でローカルでのテスト用 Kubernetes を構築 – 1Q77](https://blog.1q77.com/2016/10/setup-kubernetes-1-4-using-minikube/)
- [ローカルでkubernetesを動かせるminikubeを試す - 年中アイス](http://reiki4040.hatenablog.com/entry/2017/04/11/221122)

### CI/CD

※ * は当サイト内のページ

- [Argo CD](https://argoproj.github.io/argo-cd/)
- [Concourse](https://concourse-ci.org/)
  - 参考: [Kubernetesを前提としたCI/CDパイプラインの具体例と、本番運用に必要なもの (1/2)：コンテナベースのCI/CD本番事例大解剖（3） - ＠IT](https://www.atmarkit.co.jp/ait/articles/1909/04/news005.html)
- [Jenkins X](https://jenkins-x.io/)
- [Prow](https://github.com/kubernetes/test-infra/tree/master/prow)
  - 参考: [KubernetesベースのCI/CDシステムProwに入門してみた | CyberAgent Developers Blog](https://developers.cyberagent.co.jp/blog/archives/22072/)
- Skaffold（See below）
- [Spinnaker]({{< ref "/a/software/spinnaker/_index.md" >}}) *
- [Tekton](https://tekton.dev/)

参考:

- [Spinnaker vs. Argo CD vs. Tekton vs. Jenkins X: Cloud-Native CI/CD](https://www.inovex.de/blog/spinnaker-vs-argo-cd-vs-tekton-vs-jenkins-x/)

#### Skaffold

開発・本番向けにKubernetesクラスタに継続的デリバリーを実施するコマンドラインツール。

- https://github.com/GoogleContainerTools/skaffold
- https://skaffold.dev/

### その他

- [ksync | Sync files between your local system and a kubernetes cluster.](https://ksync.github.io/ksync/)

## Child Pages

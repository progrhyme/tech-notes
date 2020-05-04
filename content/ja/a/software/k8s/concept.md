---
title: "Concept"
linkTitle: "Concept"
description: >
  全体アーキテクチャーや構成要素について
date: 2020-04-27T10:53:19+09:00
weight: 10
---

## Documentation

https://kubernetes.io/docs/concepts/

## Overview

- Kubernetes Master
  - クラスタ内に１つ存在するマスターノード。ノード上で、[kube-apiserver](https://kubernetes.io/docs/reference/generated/kube-apiserver/), [kube-controller-manager](https://kubernetes.io/docs/reference/generated/kube-controller-manager/), [kube-scheduler](https://kubernetes.io/docs/reference/generated/kube-scheduler/)の3プロセスが動作する。
- マスター以外のノードで動くプロセス:
  - [kubelet](https://kubernetes.io/docs/reference/generated/kubelet/)
  - [kube-proxy](https://kubernetes.io/docs/reference/generated/kube-proxy/)

基本的なオブジェクト（* は本サイト内のページ）:

- [Pod]({{< ref "/a/software/k8s/pod.md" >}}) *
- [Service]({{< ref "/a/software/k8s/service.md" >}}) *
- [Volume](https://kubernetes.io/docs/concepts/storage/volumes/)
- [Namespace]({{< ref "/a/software/k8s/namespace.md" >}}) *
  - Kubernetesでは、複数の仮想的なクラスタを同じ物理クラスタ上に構築することができる。この仮想クラスタのことを **Namespace** と呼ぶ。

より高次の概念として **Controller** と呼ばれるものがある。  
これは基本オブジェクト上に構築され、以下のような便利な機能を提供する:

- [ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/) ... [Replication Controller](https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/)の後継。
- [Deployment]({{< ref "/a/software/k8s/deployment.md" >}}) * ... PodやReplicaSetの状態を宣言的に記述することを可能にする。
- [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) ... v1.8でbeta. Deployment同様Podを管理するが、それぞれのPodを異なる個体と認識する。
- [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) ... ノード上でPodのコピーを動かす。典型的なユースケースとしては、cephやfluentd, collectdなどが挙げられる。
- [Job](https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/) ... Podを実行し、正常に完了するまでをトラッキングする。定められた回数、正常に完了したら、Jobも完了となる。

## Components

https://kubernetes.io/docs/concepts/overview/components/

### Master Components

- [kube-apiserver](https://kubernetes.io/docs/reference/generated/kube-apiserver/)
  - Kubernetesを制御するフロントAPI. 水平スケール可能。参考: [Building High-Availability Clusters | Kubernetes](https://kubernetes.io/docs/admin/high-availability/)
- [etcd](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/) ... クラスタの管理データが保存されるので、バックアップすべし。
- [kube-controller-manager](https://kubernetes.io/docs/reference/generated/kube-controller-manager/)
  - Controllerをバックグラウンドのスレッドで動かす。
  - 個々のControllerは論理的には独立した存在だが、複雑性を避けるため同一のバイナリで単一プロセスとして動作している。
  - 以下のControllerが含まれる:
    - Node Controller
    - Replication Controller
    - Endpoints Controller
    - Service Account & Token Controller
- cloud-controller-manager ... v1.6でalpha. クラウド基盤とやりとりするControllerを動かす。
- [kube-scheduler](https://kubernetes.io/docs/reference/generated/kube-scheduler/) ... 生成されるPodを監視し、Podを動作させるノードを決定する。
- addons ... クラスタの機能を提供するPod群。これらのPodは `kube-system` という **Namespace** に作られる。
  - [DNS](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/)
  - [Web UI (Dashboard)](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)
  - [Container Resource Monitoring](https://kubernetes.io/docs/tasks/debug-application-cluster/resource-usage-monitoring/)
  - [Cluster-level Logging](https://kubernetes.io/docs/concepts/cluster-administration/logging/)


### Node Components

- [kubelet](https://kubernetes.io/docs/reference/generated/kubelet/) ... マスターと通信するエージェントプロセス。
- [kube-proxy](https://kubernetes.io/docs/reference/generated/kube-proxy/) ... ノード上でKubernetes APIによって定義されたサービスを媒介するネットワークプロキシ。
- docker, rkt ... コンテナランタイム
- supervisord ... ノード上でdockerやkubeletを動かし続ける。
- fluentd ... cluster-level loggingを実現する。

## リソース管理
### コンテナやPodへのCPU/メモリの割当て

基本:

- Podは、cpu/memory requests以上の空きリソースを持つノードにスケジュールされる
- コンテナのcpu利用量がlimit値を越えるとスロットルされる = パフォーマンス劣化する
- コンテナのmemory利用量がlimit値を越えるとOOM Killerで殺される。再起動できるときは再起動される
- Podが複数のコンテナで構成される場合、リソース指定値は全コンテナの合計値になる
- requestsを指定しないとデフォルト値になる
- limitsを指定しないとノードで利用可能な最大値になる

Tips:

- コンテナのcpu/memoryのrequestsより大きなlimitsを指定することで、突発的な負荷に耐えられるようになり、かつ、適切に制限をかけられる

ベストプラクティス:

- NamespaceでResourceQuotasやLimitRangeを設定すると良い
  - See [Namespace#resourcequotas]({{< ref "/a/software/k8s/namespace.md" >}}#resourcequotas)

参考:

- [コンテナおよびPodへのCPUリソースの割り当て - Kubernetes](https://kubernetes.io/ja/docs/tasks/configure-pod-container/assign-cpu-resource/)
- [コンテナおよびPodへのメモリーリソースの割り当て - Kubernetes](https://kubernetes.io/ja/docs/tasks/configure-pod-container/assign-memory-resource/)
- [例を交えてKubernetesのリミットとリクエストを理解する | Sysdigブログ - コンテナ・Kubernetes環境向けセキュリティ・モニタリング プラットフォーム](https://www.scsk.jp/sp/sysdig/blog/sysdig_monitor/kubernetes_118.html)
- [Kubernetes best practices: Resource requests and limits | Google Cloud Blog](https://cloud.google.com/blog/products/gcp/kubernetes-best-practices-resource-requests-and-limits)
- [開発者のベスト プラクティス - Azure Kubernetes Service (AKS) でのリソース管理 | Microsoft Docs](https://docs.microsoft.com/ja-jp/azure/aks/developer-best-practices-resource-management)

### Pod Eviction

Documents:

- https://kubernetes.io/docs/tasks/administer-cluster/out-of-resource/

メモ:

- ノードのメモリが不足すると、Podがevictされることがある
- メモリ使用量の大きなPodからeviction対象になる
- memoryのrequets/limitsを適切に設定しておくこと

参考:

- [Kubernetes pod evictedとスケジューリングの問題を理解する | Sysdigブログ - コンテナ・Kubernetes環境向けセキュリティ・モニタリング プラットフォーム](https://www.scsk.jp/sp/sysdig/blog/sysdig_monitor/kubernetes_pod_evicted.html)
- [ノード - Kubernetes](https://kubernetes.io/ja/docs/concepts/architecture/nodes/)

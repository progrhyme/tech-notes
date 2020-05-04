---
title: "Concept"
linkTitle: "Concept"
description: >
  全体アーキテクチャーや構成要素について
date: 2020-04-27T10:53:19+09:00
weight: 30
---

## Documentation

https://kubernetes.io/docs/concepts/

## Overview

- Kubernetes Master
  - クラスタ内に１つ存在するマスターノード。ノード上で、[kube-apiserver](https://kubernetes.io/docs/reference/generated/kube-apiserver/), [kube-controller-manager](https://kubernetes.io/docs/reference/generated/kube-controller-manager/), [kube-scheduler](https://kubernetes.io/docs/reference/generated/kube-scheduler/)の3プロセスが動作する。
- マスター以外のノードで動くプロセス:
  - [kubelet](https://kubernetes.io/docs/reference/generated/kubelet/)
  - [kube-proxy](https://kubernetes.io/docs/reference/generated/kube-proxy/)

基本的なオブジェクト:

- [Pod](https://kubernetes.io/docs/concepts/workloads/pods/pod-overview/)
- [Service](https://kubernetes.io/docs/concepts/services-networking/service/)
- [Volume](https://kubernetes.io/docs/concepts/storage/volumes/)
- [Namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)
  - Kubernetesでは、複数の仮想的なクラスタを同じ物理クラスタ上に構築することができる。この仮想クラスタのことを **Namespace** と呼ぶ。

より高次の概念として **Controller** と呼ばれるものがある。  
これは基本オブジェクト上に構築され、以下のような便利な機能を提供する:

- [ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/) ... [Replication Controller](https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/)の後継。
- [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) ... PodやReplicaSetの状態を宣言的に記述することを可能にする。
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


## Pods

### スケジューリング

[Node上へのPodのスケジューリング - Kubernetes](https://kubernetes.io/ja/docs/concepts/configuration/assign-pod-node/)

NOTE:

- Podが起動できない理由:
  - OutOfMemory, OutOfCpu ... Nodeのリソースが足りない

#### TaintsとTolerations

[Taints and Tolerations - Kubernetes](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/)

[KubernetesのTaintsとTolerationsについて - Qiita](https://qiita.com/sheepland/items/8fedae15e157c102757f)より:

> Node SelectorやNode Affinityが特定のノードに特定のPodをスケジュールするための仕組みに対し、TaintsとTolerationsは特定のノードにPodをスケジュールしないための仕組み

### Podの終了

https://kubernetes.io/docs/concepts/workloads/pods/pod/#termination-of-pods

参考:

- [Kubernetes: 詳解 Pods の終了 - Qiita](https://qiita.com/superbrothers/items/3ac78daba3560ea406b2)
- [KubernetesでRollingUpdateするためのPodの安全な終了 | SIOS Tech. Lab](https://tech-lab.sios.jp/archives/18730)


### CrashLoopBackOff

発生条件:

- memory limits以上を使おうとしてOOMで殺され、繰り返し再起動されるとき
  - 再起動間隔はexponential backoffで延びる

参考:

- [KubernetesのResource RequestsとResource Limitsについて - Qiita](https://qiita.com/sheepland/items/eb0e4c65aaae70ec4e2f)


## Services

- https://kubernetes.io/docs/concepts/services-networking/service/
- https://cloud.google.com/kubernetes-engine/docs/concepts/service
  
Kubernetesクラスタ内では、複数のPodを束ねてServiceにしている。
Serviceを使用すると、メンバーPodのIPアドレスが変更されても、Serviceが存続している間に固定のIPアドレスを取得できる。

- [Label Selector](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors) ... サービスを識別するためのラベルとそのセレクタ。
- **Endpoints** API ... Service内のPodの変更に伴って更新される。

Service定義ファイルのサンプル:

```YAML
kind: Service
apiVersion: v1
metadata:
  name: my-service
spec:
  selector:
    app: MyApp
  ports:
  - protocol: TCP
    port: 80
    targetPort: 9376
```

これはKubernetesクラスタ内で `my-service` という名前でアクセスできる。

参考:

- [Service | Kubernetes Engine のドキュメント | Google Cloud](https://cloud.google.com/kubernetes-engine/docs/concepts/service?hl=ja)
- [Kubernetes道場 9日目 - Serviceについて - Toku's Blog](https://cstoku.dev/posts/2018/k8sdojo-09/)


### Serviceのtype

https://cloud.google.com/kubernetes-engine/docs/concepts/service?hl=ja#types_of_services

- `ClusterIP` （デフォルト） ... クラスタ内で固定IPアドレスを獲得
- `NodePort` ... 指定された1つ以上の `nodePort` 値を利用して、ノードのIPアドレスを通じてアクセス可能になる
- `LoadBalancer` ... ネットワークロードバランサを介したアクセスを提供
- `ExternalName` ... See below
- `Headless`


### ExternalName

https://kubernetes.io/ja/docs/concepts/services-networking/service/#externalname

外部から参照できるDNS名を提供する。  
この機能を使うには、GKEなどのように、KubernetesにDNSコンポーネントが導入されている必要がある。  

Example:

```YAML
apiVersion: v1
kind: Service
metadata:
  name: my-service
  namespace: prod
spec:
  type: ExternalName
  externalName: my.database.example.com
```

## リソース管理
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

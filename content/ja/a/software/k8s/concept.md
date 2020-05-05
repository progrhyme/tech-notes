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

## アーキテクチャー概観

[Kubernetesのコンポーネント - Kubernetes](https://kubernetes.io/ja/docs/concepts/overview/components/)より。

- **クラスタ** ... <u>ノード</u>の集合
  - 少なくとも1つの<u>ワーカーノード</u>と少なくとも1つの<u>マスターノード</u>がある
- **ノード（Node）** ... コンテナ化されたアプリケーションを実行するマシン
  - **マスターノード** ... <u>ワーカーノード</u>とPodを管理。複数台構成によって高可用性を実現できる
  - **ワーカーノード** ... Podを動かす

各ノードで実行され、Kubernetesのクラスタ機能を成り立たせる<u>コンポーネント</u>を以下に記す。

### Master Components

マスターコンポーネントは、クラスターのコントロールプレーンを提供する。  
クラスタのどのマシンでも実行できるが、通常は全てのコンポーネントが同じマシンで起動され、そのマシンにはユーザーのPodをスケジュールしない。

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

## リソースオブジェクト

APIオブジェクトとも呼ばれるようだ。

[Kubernetes API Reference Docs (v1.18 at 2020-04-13)](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.18/)に従い、カテゴライズして記す。

NOTE:

- 以下、「*」は本サイト内のページを表すとする。
- 一旦、v1beta以下は省くか、versionを明記する

### Workloads

- coreグループ:
  - [Container]({{< ref "/a/software/k8s/container.md" >}}) *
  - [Pod]({{< ref "/a/software/k8s/pod.md" >}}) *
  - ReplicationContoller
- appsグループ:
  - [ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/) ... [Replication Controller](https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/)の後継。
  - [Deployment]({{< ref "/a/software/k8s/deployment.md" >}}) * ... PodやReplicaSetの状態を宣言的に記述することを可能にする。
  - [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) ... v1.8でbeta. Deployment同様Podを管理するが、それぞれのPodを異なる個体と認識する。
  - [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) ... ノード上でPodのコピーを動かす。典型的なユースケースとしては、cephやfluentd, collectdなどが挙げられる。
- batchグループ:
  - [Job](https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/) ... Podを実行し、正常に完了するまでをトラッキングする。定められた回数、正常に完了したら、Jobも完了となる。
  - CronJob v1beta1

MEMO: 

- apps, batchグループのオブジェクトを **Controller** と呼ぶことがあったようだ。

### Discovery & LB (Service APIs)

- coreグループ:
  - [Service]({{< ref "/a/software/k8s/service.md" >}}) *
  - Endpoints
- networking.k8s.ioグループ:
  - Ingress v1beta1
  - IngressClass v1beta1
- discovery.k8s.ioグループ:
  - EndpointSlice v1beta1

### Config & Storage

- coreグループ:
  - ConfigMap
  - Secret
  - PersistentVolumeClaim
  - [Volume](https://kubernetes.io/docs/concepts/storage/volumes/)
- storage.k8s.ioグループ:
  - CSIDriver
  - CSINode
  - StorageClass
  - VolumeAttachment

### Metadata

- coreグループ:
  - Event
  - LimitRange
  - PodTemplate
- appsグループ:
  - ControllerRevision
- autoscalingグループ:
  - [HorizontalPodAutoscaler](#horizontal-pod-autoscaler) * ... HPAと略されることが多い
- scheduling.k8s.ioグループ:
  - PriorityClass ... See [Pod Priority and Preemption - Kubernetes#priorityclass](https://kubernetes.io/docs/concepts/configuration/pod-priority-preemption/#priorityclass)
- admissionregistration.k8s.ioグループ:
  - MutatingWebhookConfiguration
  - ValidatingWebhookConfiguration
- apiextensions.k8s.ioグループ:
  - CustomResourceDefinition ... CRDと略されることが多い。K8sの機能拡張によく用いられる
- policyグループ:
  - PodDisruptionBudget v1beta1
  - PodSecurityPolicy v1beta1

### Cluster

- coreグループ:
  - Binding
  - ComponentStatus
  - [Namespace]({{< ref "/a/software/k8s/namespace.md" >}}) * ... Kubernetesでは、複数の仮想的なクラスタを同じ物理クラスタ上に構築することができる。この仮想クラスタのことを **Namespace** と呼ぶ
  - Node
  - PersistentVolume
  - ResourceQuota
  - ServiceAccount
- authentication.k8s.ioグループ:
  - TokenRequest
  - TokenReview
- authorization.k8s.ioグループ:
  - LocalSubjectAccessReview
  - SelfSubjectAccessReview
  - SelfSubjectRulesReview
  - SubjectAccessReview
- rbac.authorization.k8s.ioグループ:
  - ClusterRole
  - ClusterRoleBinding
  - Role
  - RoleBinding
- apiregistration.k8s.ioグループ:
  - APIService
  - AuditSink
- certificates.k8s.ioグループ:
  - CertificateSigningRequest v1beta1
- networking.k8s.ioグループ:
  - NetworkPolicy
- coordination.k8s.ioグループ:
  - Lease

## 認証/認可
### RBAC

https://kubernetes.io/docs/reference/access-authn-authz/rbac/

- Role ... 権限ロール。Namespace単位
- ClusterRole ... クラスタ全体に効く権限ロール
- RoleBinding ... Roleとユーザ/グループの紐付け
- ClusterRoleBinding ... ClusterRoleとユーザ/グループの紐付け

参考:

- [Kubernetes道場 20日目 - Role / RoleBinding / ClusterRole / ClusterRoleBindingについて - Toku's Blog](https://cstoku.dev/posts/2018/k8sdojo-20/)
- [KubernetesのRBACについて - Qiita](https://qiita.com/sheepland/items/67a5bb9b19d8686f389d)

## オートスケール
### Horizontal Pod Autoscaler

- https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/
- https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/

Podの水平オートスケーラー

- v1 ... CPU使用率(requestsの平均)でスケール
- v2
  - https://github.com/kubernetes/community/blob/master/contributors/design-proposals/autoscaling/hpa-v2.md
  - カスタムメトリクス対応
  - 複数メトリクス対応

Example:

```YAML
kind: HorizontalPodAutoscaler
apiVersion: autoscaling/v2alpha1
metadata:
  name: WebFrontend
spec:
  scaleTargetRef:
    kind: ReplicationController
    name: WebFrontend
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      targetAverageUtilization: 80
  - type: Object
    object:
      target:
        kind: Service
        name: Frontend
      metricName: hits-per-second
      targetValue: 1k
```

参考:

- [Configuring a Horizontal Pod Autoscaler - GKE](https://cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling)
- [GKE クラスタの観察 | Stackdriver Monitoring | Google Cloud](https://cloud.google.com/monitoring/kubernetes-engine/observing?hl=ja)
- [GKEでPodとNodeをAutoscaling する - Qiita](https://qiita.com/k-hal/items/5f060fdbafa3d29b3499#hpa)

### Cluster Autoscaler

https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler

- [FAQ.md](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md)

## Storage
### PersistentVolume

https://kubernetes.io/docs/concepts/storage/persistent-volumes/

永続化ボリューム

参考:

- [Kubernetes道場 12日目 - PersistentVolume / PersistentVolumeClaim / StorageClassについて - Toku's Blog](https://cstoku.dev/posts/2018/k8sdojo-12/)

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

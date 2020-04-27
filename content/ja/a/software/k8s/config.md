---
title: "Configuration"
linkTitle: "Configuration"
description: >
  Manifestファイルや環境設定など
date: 2020-04-27T10:53:22+09:00
weight: 20
---

## Best Practices

- [Configuration Best Practices | Kubernetes](https://kubernetes.io/docs/concepts/configuration/overview/)

## kubeconfig

クラスタ認証情報を保存するYAMLファイル。  
`kubectl` の設定ファイル。  
デフォルトのPATHは `$HOME/.kube/config`

参考:

- [Configure Access to Multiple Clusters - Kubernetes](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/)

## Container

### コマンド/引数の定義

See https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#notes

Example:

```YAML
apiVersion: v1
kind: Pod
metadata:
  name: command-demo
  labels:
    purpose: demonstrate-command
spec:
  containers:
  - name: command-demo-container
    image: debian
    command: ["printenv"]
    args: ["HOSTNAME", "KUBERNETES_PORT"]
  restartPolicy: OnFailure
```

### liveness/readiness probes

- [Configure Liveness, Readiness and Startup Probes - Kubernetes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)

ヘルスチェック的なもの。

参考:

- [Kubernetes道場 10日目 - LivenessProbe / ReadinessProbeについて - Toku's Blog](https://cstoku.dev/posts/2018/k8sdojo-10/)


### Lifecycle Hooks

https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/

以下のフックを仕込むことで、コマンド実行などが可能。

- PostStart
- PreStop ... 終了直前に実行される

詳細な仕様はAPIリファレンスを見よ。

設定例:

```YAML
apiVersion: v1
kind: Pod
metadata:
  name: lifecycle-demo
spec:
  containers:
  - name: lifecycle-demo-container
    image: httpd
    lifecycle:
      preStop:
        exec:
          command: ["sh", "-c", "sleep 2; httpd -k graceful-stop; sleep 30"]
  terminationGracePeriodSeconds: 40
```

参考:

- [pod(Kubernetes)のlifecycle.prestopの挙動 - １クール続けるブログ](https://44smkn.hatenadiary.com/entry/2018/08/01/022312)
- [Kubernetes道場 6日目 - Init Container / Lifecycleについて - Toku's Blog](https://cstoku.dev/posts/2018/k8sdojo-06/)

## Pods
### Affinity

- [Node上へのPodのスケジューリング - Kubernetes#AffinityとAnti-Affinity](https://kubernetes.io/ja/docs/concepts/configuration/assign-pod-node/#affinity-%e3%81%a8-anti-affinity)

参考:

- [Kubernetes道場 18日目 - Affinity / Anti-Affinity / Taint / Tolerationについて - Toku's Blog](https://cstoku.dev/posts/2018/k8sdojo-18/#affinity-anti-affinity)
- [KubernetesのNode AffinityとInternal Pod Affinityを使ってPodを高度スケジューリングする - Kekeの日記](https://www.1915keke.com/entry/2018/09/26/163447)
- [KubernetesのNode Affinity, Inter-Pod Affinityについて - Qiita](https://qiita.com/sheepland/items/ed12b3dc4a8f1df7c4ec)


## Deployment

- https://kubernetes.io/ja/docs/concepts/workloads/controllers/deployment/

参考:

- [Kubernetes道場 8日目 - ReplicaSet / Deploymentについて - Toku's Blog](https://cstoku.dev/posts/2018/k8sdojo-08/)


### spec
#### strategy

更新戦略。

Example:

```YAML
spec:
  strategy:
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 25%
    type: RollingUpdate
```

上はデフォルト値。

- type ... `Recreate` を選ぶと既存の全てのPodは新しいPodが作成される前に削除される
- `maxSurge` ... 理想状態のPod数を超えて作成できる最大のPod数/割合。絶対数も指定可能
- `maxUnavailable` ... 更新中に利用不可となる最大のPod数/割合。絶対数も指定可能
  - 本番ではキャパシティが低下しないように `0` にしておいた方が良さそう。

参考:

- [KubernetesのRolling updateを安全に行う - Qiita](https://qiita.com/TakiTake@github/items/bfc977baf4b909b1e118)
- [Zero Downtime Deployment with Kubernetes](https://rahmonov.me/posts/zero-downtime-deployment-with-kubernetes/)


## ConfigMaps & Secrets 

参考:

- [Kubernetes道場 11日目 - ConfigMap / Secretについて - Toku's Blog](https://cstoku.dev/posts/2018/k8sdojo-11/)
- [Kubernetes: ConfigMap / Secret の内容を一度に環境変数として読み込む (envFrom) - Qiita](https://qiita.com/tkusumi/items/cf7b096972bfa2810800)


### ConfigMaps

Secretsと似ているが、こちらは値をencodeせずに平文でYAMLに書くので、普通の設定ファイル的な位置づけ。

公式サイトにいくつかのガイドやサンプルがある:

- [Use ConfigMap Data in Pods | Kubernetes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/)
- [Configure Containers Using a ConfigMap | Kubernetes](https://kubernetes.io/docs/tasks/configure-pod-container/configmap/)
- [Configuring Redis using a ConfigMap | Kubernetes](https://kubernetes.io/docs/tutorials/configuration/configure-redis-using-configmap/)


### Secrets

https://kubernetes.io/docs/concepts/configuration/secret/

パスワードなどテキストをbase64でencodeして保存する。  
暗号化の機能もある？

Podから環境変数として読み込むという使い方をすることが多いようだ。

参考:

- [Kubernetes Secrets の紹介 – データベースのパスワードやその他秘密情報をどこに保存するか？ – ゆびてく](https://ubiteku.oinker.me/2017/03/01/kubernetes-secrets/)


#### Secretsの作成

例1) テキストファイルから作成

```Bash
echo -n 'admin' > ./username.txt
echo -n '1f2d1e2e67df' > ./password.txt

kubectl create secret generic db-user-pass --from-file=./username.txt --from-file=./password.txt
```

例2) 自分で定義ファイル(YAML)を作る

```Bash
echo -n 'admin' | base64
YWRtaW4=
echo -n '1f2d1e2e67df' | base64
MWYyZDFlMmU2N2Rm
```

```YAML
## secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: Opaque
data:
  username: YWRtaW4=
  password: MWYyZDFlMmU2N2Rm
```

```Bash
kubectl apply -f ./secret.yaml
```

## ResourceQuotas

https://kubernetes.io/docs/concepts/policy/resource-quotas/

Example:

```YAML
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-resources
spec:
  hard:
    requests.cpu: "1"
    requests.memory: 1Gi
    limits.cpu: "2"
    limits.memory: 2Gi
```

適用例:

```sh
kubectl create -f ./compute-resources.yaml --namespace=myspace
```

Note:

- ResourceQuotaを設定したnamespaceに属する全Podの合計値が上限になる
- cpu, memory以外も色々ある


## LimitRange

https://kubernetes.io/docs/concepts/policy/limit-range/

Example:

```YAML
apiVersion: v1
kind: LimitRange
metadata:
  name: limit-mem-cpu-per-container
spec:
  limits:
  - max:
      cpu: "800m"
      memory: "1Gi"
    min:
      cpu: "100m"
      memory: "99Mi"
    default:
      cpu: "700m"
      memory: "900Mi"
    defaultRequest:
      cpu: "110m"
      memory: "111Mi"
    type: Container
```

- namespaceに対して設定する
- cpu/memoryのrequests/limitsの下限、上限、デフォルト値を設定できる


## Topics
### CPU/Memoryの割り当て

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


参考:

- [コンテナおよびPodへのCPUリソースの割り当て - Kubernetes](https://kubernetes.io/ja/docs/tasks/configure-pod-container/assign-cpu-resource/)
- [コンテナおよびPodへのメモリーリソースの割り当て - Kubernetes](https://kubernetes.io/ja/docs/tasks/configure-pod-container/assign-memory-resource/)
- [例を交えてKubernetesのリミットとリクエストを理解する | Sysdigブログ - コンテナ・Kubernetes環境向けセキュリティ・モニタリング プラットフォーム](https://www.scsk.jp/sp/sysdig/blog/sysdig_monitor/kubernetes_118.html)
- [Kubernetes best practices: Resource requests and limits | Google Cloud Blog](https://cloud.google.com/blog/products/gcp/kubernetes-best-practices-resource-requests-and-limits)
- [開発者のベスト プラクティス - Azure Kubernetes Service (AKS) でのリソース管理 | Microsoft Docs](https://docs.microsoft.com/ja-jp/azure/aks/developer-best-practices-resource-management)

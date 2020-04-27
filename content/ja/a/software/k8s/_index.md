---
title: "Kubernetes"
linkTitle: "Kubernetes"
description: >
  https://kubernetes.io/
date: 2020-04-27T10:39:49+09:00
weight: 300
---

## Getting Started

- https://kubernetes.io/docs/home/ ... ドキュメント
  - https://kubernetes.io/docs/tutorials/ ... チュートリアル
  - https://kubernetes.io/docs/tasks/ ... How-toガイド

## Documentation

参考:

- [Kubernetes道場 Advent Calendar 2018 - Qiita](https://qiita.com/advent-calendar/2018/k8s-dojo)

## Reference

- https://kubernetes.io/docs/reference/
  - APIリファレンス
  - CLIリファレンス
  - etc.

## Case Study

参考:

- [Kubernetes Failure Stories](https://k8s.af/)

## Versions

- [Kubernetes version and version skew support policy - Kubernetes](https://kubernetes.io/docs/setup/release/version-skew-policy/)

## Features
### PersistentVolume

https://kubernetes.io/docs/concepts/storage/persistent-volumes/

永続化ボリューム

参考:

- [Kubernetes道場 12日目 - PersistentVolume / PersistentVolumeClaim / StorageClassについて - Toku's Blog](https://cstoku.dev/posts/2018/k8sdojo-12/)

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


## Tools
### Minikube

https://github.com/kubernetes/minikube

ローカルでKubernetesを動かすためのツール。  
Linuxのみだが、ハイパーバイザを噛まさず、ローカルのdocker上に直接クラスタを構築することもできる。

- https://kubernetes.io/docs/getting-started-guides/minikube/ ... 導入ガイド
  - ※先にkubectlをインストールしておくこと

参考:

- [minikubeでローカルKubernetesクラスタを5分でつくる方法 - Qiita](https://qiita.com/mumoshu/items/8f55ee830d8e5c172dd4)
- [minikube でローカルでのテスト用 Kubernetes を構築 – 1Q77](https://blog.1q77.com/2016/10/setup-kubernetes-1-4-using-minikube/)
- [ローカルでkubernetesを動かせるminikubeを試す - 年中アイス](http://reiki4040.hatenablog.com/entry/2017/04/11/221122)


### Skaffold

開発・本番向けにKubernetesクラスタに継続的デリバリーを実施するコマンドラインツール。

- https://github.com/GoogleContainerTools/skaffold
- https://skaffold.dev/

## Child Pages

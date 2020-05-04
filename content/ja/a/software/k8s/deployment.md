---
title: "Deployment"
linkTitle: "Deployment"
date: 2020-05-04T21:45:16+09:00
weight: 90
---

https://kubernetes.io/ja/docs/concepts/workloads/controllers/deployment/

> Deployment コントローラーはPodとReplicaSetの宣言的なアップデート機能を提供します。

Example:

```YAML
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  namespace: app
spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 1
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
```

参考:

- [Kubernetes道場 8日目 - ReplicaSet / Deploymentについて - Toku's Blog](https://cstoku.dev/posts/2018/k8sdojo-08/)

## spec
### strategy

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

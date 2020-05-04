---
title: "Pod"
linkTitle: "Pod"
date: 2020-05-04T21:45:01+09:00
weight: 600
---

1つ以上のコンテナを内包する、ワークロードの基本単位。

See also [Container]({{< ref "/a/software/k8s/container.md" >}})

## スケジューリング

[Node上へのPodのスケジューリング - Kubernetes](https://kubernetes.io/ja/docs/concepts/configuration/assign-pod-node/)

NOTE:

- Podが起動できない理由:
  - OutOfMemory, OutOfCpu ... Nodeのリソースが足りない

### Affinity

- [Node上へのPodのスケジューリング - Kubernetes#AffinityとAnti-Affinity](https://kubernetes.io/ja/docs/concepts/configuration/assign-pod-node/#affinity-%e3%81%a8-anti-affinity)

参考:

- [Kubernetes道場 18日目 - Affinity / Anti-Affinity / Taint / Tolerationについて - Toku's Blog](https://cstoku.dev/posts/2018/k8sdojo-18/#affinity-anti-affinity)
- [KubernetesのNode AffinityとInternal Pod Affinityを使ってPodを高度スケジューリングする - Kekeの日記](https://www.1915keke.com/entry/2018/09/26/163447)
- [KubernetesのNode Affinity, Inter-Pod Affinityについて - Qiita](https://qiita.com/sheepland/items/ed12b3dc4a8f1df7c4ec)

### TaintsとTolerations

[Taints and Tolerations - Kubernetes](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/)

[KubernetesのTaintsとTolerationsについて - Qiita](https://qiita.com/sheepland/items/8fedae15e157c102757f)より:

> Node SelectorやNode Affinityが特定のノードに特定のPodをスケジュールするための仕組みに対し、TaintsとTolerationsは特定のノードにPodをスケジュールしないための仕組み

## ライフサイクル

[Podのライフサイクル - Kubernetes](https://kubernetes.io/ja/docs/concepts/workloads/pods/pod-lifecycle/)

See also [Container#lifecycle-hooks]({{< ref "/a/software/k8s/container.md" >}}#lifecycle-hooks)

### Podの終了

https://kubernetes.io/docs/concepts/workloads/pods/pod/#termination-of-pods

参考:

- [Kubernetes: 詳解 Pods の終了 - Qiita](https://qiita.com/superbrothers/items/3ac78daba3560ea406b2)
- [KubernetesでRollingUpdateするためのPodの安全な終了 | SIOS Tech. Lab](https://tech-lab.sios.jp/archives/18730)

## Topics
### CrashLoopBackOff

発生条件:

- memory limits以上を使おうとしてOOMで殺され、繰り返し再起動されるとき
  - 再起動間隔はexponential backoffで延びる

参考:

- [KubernetesのResource RequestsとResource Limitsについて - Qiita](https://qiita.com/sheepland/items/eb0e4c65aaae70ec4e2f)

### Pod Eviction

See [Concept#pod-eviction]({{< ref "/a/software/k8s/concept.md" >}}#pod-eviction)

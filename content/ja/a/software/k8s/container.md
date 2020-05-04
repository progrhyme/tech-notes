---
title: "Container"
linkTitle: "Container"
date: 2020-05-04T22:14:09+09:00
weight: 75
---

Kubernetesにおいて、基本的にコンテナはPod内で定義され、実行される（はず）。

See also [Pod]({{< ref "/a/software/k8s/pod.md" >}})

## CPU/メモリの割当て

考え方やベストプラクティスについては[Concept#コンテナやpodへのcpuメモリの割当て]({{< ref "/a/software/k8s/concept.md" >}}#コンテナやpodへのcpuメモリの割当て)を見よ。

## コマンド/引数の定義

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

## liveness/readiness probes

- [Configure Liveness, Readiness and Startup Probes - Kubernetes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)

ヘルスチェック的なもの。

参考:

- [Kubernetes道場 10日目 - LivenessProbe / ReadinessProbeについて - Toku's Blog](https://cstoku.dev/posts/2018/k8sdojo-10/)

## Lifecycle Hooks

https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/

See also [Pod#ライフサイクル]({{< ref "/a/software/k8s/pod.md" >}}#ライフサイクル)

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

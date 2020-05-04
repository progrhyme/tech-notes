---
title: "Namespace"
linkTitle: "Namespace"
date: 2020-05-04T21:45:30+09:00
weight: 500
---

https://kubernetes.io/docs/tasks/administer-cluster/namespaces/

Kubernetesでは、複数の仮想的なクラスタを同じ物理クラスタ上に構築することができる。この仮想クラスタのことを **Namespace** と呼ぶ。

Example:

```YAML
apiVersion: v1
kind: Namespace
metadata:
  name: myapp
```

参考:

- [Kubernetes道場 15日目 - Namespace / Resource QoS / ResourceQuota / LimitRangeについて - Toku's Blog](https://cstoku.dev/posts/2018/k8sdojo-15/)

## リソース管理

See also [Concept#コンテナやpodへのcpuメモリの割当て]({{< ref "/a/software/k8s/concept.md" >}}#コンテナやpodへのcpuメモリの割当て)

ResourceQuotasやLimitRangeを設定することで、リソース管理をよりいい感じに行えるっぽい。（が、逆に面倒ではないかという気もする。）

### ResourceQuotas

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

### LimitRange

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

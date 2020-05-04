---
title: "Service"
linkTitle: "Service"
date: 2020-05-04T21:45:23+09:00
weight: 750
---

- https://kubernetes.io/docs/concepts/services-networking/service/
- https://cloud.google.com/kubernetes-engine/docs/concepts/service

## Overview

Podの集合で実行されている持続的なワークロードをネットワークサービスとして公開する抽象的な手法。

Serviceを使用すると、メンバーPodのIPアドレスが変更されても、Serviceが存続している間に固定のIPアドレスを取得できる。

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

## 仕様

- [Label Selector](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors) ... サービスを識別するためのラベルとそのセレクタ。
- **Endpoints** API ... Service内のPodの変更に伴って更新される。

## Serviceのtype

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

## 参考記事など

- [Service | Kubernetes Engine のドキュメント | Google Cloud](https://cloud.google.com/kubernetes-engine/docs/concepts/service?hl=ja)
- [Kubernetes道場 9日目 - Serviceについて - Toku's Blog](https://cstoku.dev/posts/2018/k8sdojo-09/)

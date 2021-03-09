---
title: "機能"
linkTitle: "機能"
date: 2021-03-09T16:51:32+09:00
---

## 負荷分散

- https://cloud.google.com/kubernetes-engine/docs/concepts/ingress

### HTTP(S) 負荷分散

Ingressで複数のバックエンドServiceを設定できる。設定例:

```YAML
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: my-ingress
spec:
  rules:
  - http:
      paths:
      - path: /*
        backend:
          serviceName: my-products
          servicePort: 60000
      - path: /discounted
        backend:
          serviceName: my-discounted-products
          servicePort: 80
```

#### Managed SSL certificateを使う

https://cloud.google.com/kubernetes-engine/docs/how-to/managed-certs

- GCPの静的IPを払い出し、対象のDNSレコードに設定する必要がある

See also https://sites.google.com/site/progrhymetechwiki/cloud/gcp/gclb#TOC-SSL-

#### HTTPの無効化

https://cloud.google.com/kubernetes-engine/docs/concepts/ingress?hl=ja#disabling_http

HTTPSのみを使うときはアノテーション `kubernetes.io/ingress.allow-http` の値を `"false"` に設定する。

```YAML
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: my-ingress-2
  annotations:
    kubernetes.io/ingress.allow-http: "false"
spec:
  tls:
  - secretName: my-secret
  ...
```

※2020-03-04現在、K8sのバージョンによっては、マネージドSSL証明書を使う場合は、 `ingress.gcp.kubernetes.io/pre-shared-cert` アノテーションの値に証明書名を入れる必要がある。1.15.x-gke.y の場合は自動でアノテーション付けてくれるっぽい。  
See https://github.com/kubernetes/ingress-gce/issues/1001

## 内部TCP/UDP負荷分散

[内部 TCP / UDP 負荷分散 | Kubernetes Engine のドキュメント | Google Cloud](https://cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing?hl=ja)

2020-03-25現在、β版

- Serviceを `type: LoadBalancer` で作成し、所定のannotationを入れる
- 内部LBが作成される
- Ingressは不要
- Compute InstanceGroupで振り分けされる
  - 2020-03-25現在、ネットワークエンドポイントグループには対応していない
- 同じDeploymentで、内部LBのServiceと外部HTTP(S)負荷分散用の2つのServiceを持つことができる

Example:

```YAML
apiVersion: v1
kind: Service
metadata:
  name: ilb-service
  annotations:
    cloud.google.com/load-balancer-type: "Internal"
  labels:
    app: hello
spec:
  type: LoadBalancer
  selector:
    app: hello
  ports:
  - port: 80
    targetPort: 8080
    protocol: TCP
```

## BackendConfig

https://cloud.google.com/kubernetes-engine/docs/how-to/ingress-features

GKE固有のcustom resource.

BackendConfigによって、HTTP(S) Load Balancingに以下の機能を設定できる:

- [Cloud CDN](https://cloud.google.com/kubernetes-engine/docs/how-to/cdn-backendconfig)
- [Cloud Armor](https://cloud.google.com/kubernetes-engine/docs/how-to/cloud-armor-backendconfig)
- Identity-Aware Proxy (IAP)
- [Timeout, Connection draining timeout, Session affinity, User-defined request headers](https://cloud.google.com/kubernetes-engine/docs/how-to/configure-backend-service)

仕様:

- デフォルトのタイムアウト: 30秒

Example:

- タイムアウトを40秒に設定
- 接続ドレインタイムアウトを60秒に設定

```YAML
apiVersion: cloud.google.com/v1beta1
    kind: BackendConfig
    metadata:
      name: my-bsc-backendconfig
    spec:
      timeoutSec: 40
      connectionDraining:
        drainingTimeoutSec: 60
```

## Workload Identity

[Workload Identity | Kubernetes Engine ドキュメント | Google Cloud](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity?hl=ja)

- GCP Service AccountとK8s Service Accountの紐付け設定をすることができる
- GKE Metadata Serverを有効にしている必要があるようだ

メリット:

- GCP Service Account Keyが不要になる

## Config Connector

[Config Connector の概要 | Config Connector のドキュメント | Google Cloud](https://cloud.google.com/config-connector/docs/overview?hl=ja)

- K8s addon.
- K8sのCRDと関連するコントローラを提供してくれる
- あたかもK8sのリソースかのようにGCPリソースを管理できるようになる

参考:

- 2020-02-05 [もっとGCPが使いやすくなる!? GKE Config Connectorを試してみた！ - google-cloud-jp - Medium](https://medium.com/google-cloud-jp/%E3%82%82%E3%81%A3%E3%81%A8gcp%E3%81%8C%E4%BD%BF%E3%81%84%E3%82%84%E3%81%99%E3%81%8F%E3%81%AA%E3%82%8B-gke-config-connector%E3%82%92%E8%A9%A6%E3%81%97%E3%81%A6%E3%81%BF%E3%81%9F-e1a3370010ea)

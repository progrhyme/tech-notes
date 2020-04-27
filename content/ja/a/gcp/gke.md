---
title: "Google Kubernetes Engine"
linkTitle: "GKE"
description: >
  https://cloud.google.com/kubernetes-engine/
date: 2020-04-27T11:01:49+09:00
---

## Documentation

- https://cloud.google.com/kubernetes-engine/docs/?hl=ja
- https://cloud.google.com/kubernetes-engine/quotas?hl=ja

## ベストプラクティス

- [Best Practices for Operating Containers | Architectures | Google Cloud](https://cloud.google.com/solutions/best-practices-for-operating-containers)
  - Logging, etc.
- [Kubernetes best practices: terminating with grace | Google Cloud Blog](https://cloud.google.com/blog/products/gcp/kubernetes-best-practices-terminating-with-grace)

## 仕様

- [クラスタ オートスケーラー | Kubernetes Engine のドキュメント | Google Cloud](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler?hl=ja)
  - [クラスタの自動スケーリング | Kubernetes Engine のドキュメント | Google Cloud](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler?hl=ja)

### Quota

https://cloud.google.com/kubernetes-engine/quotas

Last updated at 2020-04-13

- GKEクラスタごと
  - クラスタあたりの最大ノード数: 5,000
  - ノードプールあたりの最大ノード数: 1,000
  - ノードあたりの最大ポッド数: 110

### 限定公開クラスタ

Docs:

- [限定公開クラスタの設定 | Kubernetes Engine のドキュメント | Google Cloud](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters?hl=ja)
- https://cloud.google.com/sdk/gcloud/reference/container/clusters/create?hl=ja
- [Example GKE Setup | Cloud NAT | Google Cloud](https://cloud.google.com/nat/docs/gke-example)

要点:

- ノードは内部IPアドレスのみを持つため、インターネットから隔離される
- 限定公開クラスタでは、マスターへのアクセスを制御できる
- LB経由で受信トラフィックを受けられる。また、内部LB経由でVPC内のトラフィックを受けることもできる
- 外と通信したいときは、上記の「Example GKE Setup」にあるように、Cloud NAT + Cloud Routerをセットアップする

Tips:

- (2019-12-02現在) `gcloud container clusters create` コマンドでは `--enable-private-nodes --master-ipv4-cidr <CIDR>` オプションをつける

### 負荷分散

- https://cloud.google.com/kubernetes-engine/docs/concepts/ingress

#### HTTP(S) 負荷分散

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

##### Managed SSL certificateを使う

https://cloud.google.com/kubernetes-engine/docs/how-to/managed-certs

- GCPの静的IPを払い出し、対象のDNSレコードに設定する必要がある

See also https://sites.google.com/site/progrhymetechwiki/cloud/gcp/gclb#TOC-SSL-

##### HTTPの無効化

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

### 内部TCP/UDP負荷分散

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

### BackendConfig（β at 2020-02-20）

https://cloud.google.com/kubernetes-engine/docs/concepts/backendconfig?hl=en

GKE固有のcustom resource.

BackendConfigによって、HTTP(S) Load Balancingに以下の機能を設定できる:

- [Cloud CDN](https://cloud.google.com/kubernetes-engine/docs/how-to/cdn-backendconfig)
- [Cloud Armor](https://cloud.google.com/kubernetes-engine/docs/how-to/cloud-armor-backendconfig)
- Identity-Aware Proxy (IAP)
- [Timeout, Connection draining timeout, Session affinity, User-defined request headers](https://cloud.google.com/kubernetes-engine/docs/how-to/configure-backend-service)

### Horizontal Pod Autoscaler

HPA.

- [水平ポッド自動スケーリング | Kubernetes Engine のドキュメント | Google Cloud](https://cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler?hl=ja)
  - [外部指標によるデプロイの自動スケーリング | Kubernetes Engine のチュートリアル | Google Cloud](https://cloud.google.com/kubernetes-engine/docs/tutorials/external-metrics-autoscaling?hl=ja)
  - [カスタム指標でのデプロイの自動スケーリング | Kubernetes Engine のチュートリアル | Google Cloud](https://cloud.google.com/kubernetes-engine/docs/tutorials/custom-metrics-autoscaling?hl=ja)
  - いずれもCloud Monitoringメトリクスでスケール設定を行う
  - https://github.com/GoogleCloudPlatform/k8s-stackdriver/tree/master/custom-metrics-stackdriver-adapter をクラスタにデプロイする

参考:

- https://sites.google.com/site/progrhymetechwiki/software/k8s#TOC-Horizontal-Pod-Autoscaler
- [Autoscaling K8s HPA with Google HTTP/S Load-Balancer RPS EXTERNAL Stackdriver Metrics](https://blog.doit-intl.com/autoscaling-k8s-hpa-with-google-http-s-load-balancer-rps-stackdriver-metric-92db0a28e1ea)

## How-to
### アップグレード

https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster

Tips:

- [リリースチャネル](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels)を指定することで、自動アップグレードできる

### kubeconfigエントリを生成

```sh
gcloud container clusters get-credentials [CLUSTER_NAME] [--project PROJECT] [--region REGION]
```

↑のコマンドは更に、クラスタをデフォルトのkubectlのcontextに設定する。

参考:

- [kubectl 用のクラスタ アクセスの構成 | Kubernetes Engine のドキュメント | Google Cloud](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl?hl=ja)

### GKEのノードにSSH

- [高度な方法によるインスタンスへの接続 | Compute Engine ドキュメント | Google Cloud](https://cloud.google.com/compute/docs/instances/connecting-advanced#sshbetweeninstances)
- [限定公開クラスターのGKEノードにサクッとSSHする方法 - Qiita](https://qiita.com/inductor/items/bc0ff7d761e0cc7e9394)
- [GKE で k8s クラスタの node に ssh する - Qiita](https://qiita.com/sonots/items/6e2a57af945cf0daedd4)

参考:

- [Insufficient Permission: Request had insufficient authentication scopes. - Course: Google Certified Associate Cloud Engineer 2020](https://acloud.guru/forums/gcp-certified-associate-cloud-engineer/discussion/-Lh3ET0aNrv3FwNbNvh6/Insufficient%20Permission:%20Request%20had%20insufficient%20authentication%20scopes.)

### コンテナネイティブの負荷分散を使う

[コンテナ ネイティブの負荷分散を使用する | Kubernetes Engine のドキュメント | Google Cloud](https://cloud.google.com/kubernetes-engine/docs/how-to/container-native-load-balancing?hl=ja)

- ネットワークエンドポイントグループ(NEG)を作成して、Podに均等にトラフィックを分配できる
- 従来の方式だとインスタンスグループ経由のアクセスで、iptablesを介してPodにアクセスしており、余分なネットワークオーバーヘッドが発生していた

## Topics
### Logging

- [Google Kubernetes Engine の Stackdriver ログを Fluentd でカスタマイズする | ソリューション](https://cloud.google.com/solutions/customizing-stackdriver-logs-fluentd?hl=ja)

## 参考

- [GKE上RailsのアプリケーションログをStackdriver Loggingで運用する方法 - Riki Shimma - Medium](https://medium.com/@rshimma/rails-on-gke-with-stackdriver-logging-63163c72934)

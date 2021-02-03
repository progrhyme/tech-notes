---
title: "Google Kubernetes Engine"
linkTitle: "GKE"
description: >
  https://cloud.google.com/kubernetes-engine/
date: 2020-04-27T11:01:49+09:00
weight: 240
---

関連ページ:

- [Software > Kubernetes]({{< ref "/a/software/k8s/_index.md" >}})

## Getting Started

- [チュートリアル | Kubernetes Engine ドキュメント | Google Cloud](https://cloud.google.com/kubernetes-engine/docs/tutorials?hl=ja)
- [入門ガイド | Kubernetes Engine ドキュメント | Google Cloud](https://cloud.google.com/kubernetes-engine/docs/how-to?hl=ja)

### Documentation

- https://cloud.google.com/kubernetes-engine/docs/?hl=ja
- https://cloud.google.com/kubernetes-engine/quotas?hl=ja

## ベストプラクティス

- [Best Practices for Operating Containers | Architectures | Google Cloud](https://cloud.google.com/solutions/best-practices-for-operating-containers)
  - Logging, etc.
- [Kubernetes best practices: terminating with grace | Google Cloud Blog](https://cloud.google.com/blog/products/gcp/kubernetes-best-practices-terminating-with-grace)

## 機能

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

### BackendConfig（β on 2020-04-27）

https://cloud.google.com/kubernetes-engine/docs/concepts/backendconfig?hl=en

GKE固有のcustom resource.

BackendConfigによって、HTTP(S) Load Balancingに以下の機能を設定できる:

- [Cloud CDN](https://cloud.google.com/kubernetes-engine/docs/how-to/cdn-backendconfig)
- [Cloud Armor](https://cloud.google.com/kubernetes-engine/docs/how-to/cloud-armor-backendconfig)
- Identity-Aware Proxy (IAP)
- [Timeout, Connection draining timeout, Session affinity, User-defined request headers](https://cloud.google.com/kubernetes-engine/docs/how-to/configure-backend-service)

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

### Workload Identity

[Workload Identity | Kubernetes Engine ドキュメント | Google Cloud](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity?hl=ja)

- GCP Service AccountとK8s Service Accountの紐付け設定をすることができる
- GKE Metadata Serverを有効にしている必要があるようだ

メリット:

- GCP Service Account Keyが不要になる

### Config Connector

[Config Connector の概要 | Config Connector のドキュメント | Google Cloud](https://cloud.google.com/config-connector/docs/overview?hl=ja)

- K8s addon.
- K8sのCRDと関連するコントローラを提供してくれる
- あたかもK8sのリソースかのようにGCPリソースを管理できるようになる

参考:

- 2020-02-05 [もっとGCPが使いやすくなる!? GKE Config Connectorを試してみた！ - google-cloud-jp - Medium](https://medium.com/google-cloud-jp/%E3%82%82%E3%81%A3%E3%81%A8gcp%E3%81%8C%E4%BD%BF%E3%81%84%E3%82%84%E3%81%99%E3%81%8F%E3%81%AA%E3%82%8B-gke-config-connector%E3%82%92%E8%A9%A6%E3%81%97%E3%81%A6%E3%81%BF%E3%81%9F-e1a3370010ea)

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

Documents:

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

#### 制限事項

[限定公開クラスタの作成 | Kubernetes Engine ドキュメント | Google Cloud#要件、制約、制限](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters?hl=ja#req_res_lim)


- [エイリアスIP範囲](https://cloud.google.com/vpc/docs/alias-ip?hl=ja)が有効なVPCネイティブクラスタである必要がある
  - See [VPCネイティブクラスタを作成する](#vpcネイティブクラスタを作成する)

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

### コンテナネイティブの負荷分散

[コンテナ ネイティブの負荷分散を使用する | Kubernetes Engine のドキュメント | Google Cloud](https://cloud.google.com/kubernetes-engine/docs/how-to/container-native-load-balancing?hl=ja)

TL;DR:

- ネットワークエンドポイントグループ(NEG)を作成して、Podに均等にトラフィックを分配できる
- 従来の方式だとインスタンスグループ経由のアクセスで、iptablesを介してPodにアクセスしており、余分なネットワークオーバーヘッドが発生していた

[既知の問題](https://cloud.google.com/kubernetes-engine/docs/how-to/container-native-load-balancing#known_issues)（2020-04-27時点）:

- GKEのガベージコレクションが2分間隔なので、LBが完全に削除される前にクラスタが削除された場合、NEGを手動で削除する必要がある
- [Podのreadinessフィードバック](https://cloud.google.com/kubernetes-engine/docs/concepts/container-native-load-balancing#pod_readiness)を<u>使っていない場合</u>、ワークロードをデプロイするときや再起動するときに、ワークロードの更新完了に要する時間よりも、新しいエンドポイントの伝播に要する時間のほうが長くなる場合がある

### VPCネイティブクラスタ

[VPC ネイティブ クラスタを作成する | Kubernetes Engine ドキュメント | Google Cloud](https://cloud.google.com/kubernetes-engine/docs/how-to/alias-ips?hl=ja)

2020-05-04現在、GCPコンソールから作成する場合はデフォルトでVPCネイティブクラスタになるが、REST APIやgcloudコマンドでは[ルートベースクラスタ](https://cloud.google.com/vpc/docs/routes?hl=ja)になるので注意。

2つのやり方がある:

1. 既存のサブネットにクラスタを作成する。アドレス範囲の割り当て方は下の2つ:
   - GKE管理のセカンダリ範囲割り当て
   - ユーザー管理のセカンダリ範囲割り当て
1. クラスタとサブネットを同時に作成する。セカンダリアドレス範囲の割り当てはGKE管理となる

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

### ノードプールを作り直す

マシンタイプやサービスアカウントを変えるときなどには、ノードプールの作り直しが発生する。  
次の要領でやれば良い:

1. 新しいプールを作成
1. ワークロードを新しいプールに移行
1. 古いプールを削除

ドキュメントでは、 [異なるマシンタイプへのワークロードの移行 | Kubernetes Engine のチュートリアル | Google Cloud](https://cloud.google.com/kubernetes-engine/docs/tutorials/migrating-node-pool?hl=ja) の手順に従う形になる。

ただし、この手順に愚直に従うとドレインした瞬間に旧プール上のPodがevictionされ、サービス停止することもあり得るので、常時稼働のワークロードであれば、cordonでノードへのスケジューリングを停止した後、Podをスケールさせて新しいプールにPodが配置された後にドレインした方がよさそう。

### GKEのノードにSSH

- [高度な方法によるインスタンスへの接続 | Compute Engine ドキュメント | Google Cloud](https://cloud.google.com/compute/docs/instances/connecting-advanced#sshbetweeninstances)
- [限定公開クラスターのGKEノードにサクッとSSHする方法 - Qiita](https://qiita.com/inductor/items/bc0ff7d761e0cc7e9394)
- [GKE で k8s クラスタの node に ssh する - Qiita](https://qiita.com/sonots/items/6e2a57af945cf0daedd4)

参考:

- [Insufficient Permission: Request had insufficient authentication scopes. - Course: Google Certified Associate Cloud Engineer 2020](https://acloud.guru/forums/gcp-certified-associate-cloud-engineer/discussion/-Lh3ET0aNrv3FwNbNvh6/Insufficient%20Permission:%20Request%20had%20insufficient%20authentication%20scopes.)

### メンテナンス時間枠と除外枠の設定

[メンテナンスの時間枠と除外の構成 | Kubernetes Engine ドキュメント | Google Cloud](https://cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions?hl=ja)

- クラスタやノードのアップグレードが行われる時間枠を設定可能。  
- （たぶん）最短4時間

### Docker Hubのイメージを使うには？

公開イメージだったら普通に使える。

プライベートなイメージでも認証情報を渡せば普通に使えるんじゃないかな。  

MEMO:

- 日本語の記事だとミラーしたり、GCRにpushしてる例が多い

参考:

- [Google Cloud Kubernetes accessing private Docker Hub hosted images - Stack Overflow](https://stackoverflow.com/questions/50826766/google-cloud-kubernetes-accessing-private-docker-hub-hosted-images)
- [Images - Kubernetes](https://kubernetes.io/docs/concepts/containers/images/)
- [docker hub with kubernetes in GKE](https://gist.github.com/toddlers/bb09002ffdc27fba6b7cef920fda2041)
- [Using Images from a Private Registry on GKE - Engineering Tomorrow’s Systems](https://estl.tech/using-images-from-a-private-registry-on-gke-b3bfb2562b16)
- [hawksnowlog: Google Container Engine に Dockerhub で公開しているイメージをデプロイする方法](https://hawksnowlog.blogspot.com/2017/02/dockerhub-image-deploy-on-gke.html)

### ワークロードを特定のnodepoolで実行する

GKEのノードはnodepoolを表すラベルとして `cloud.google.com/gke-nodepool: <nodepool名>` が設定されている。  
これを用いて、nodeSelector、またはNode Affinityを設定する。

参考:

- [Node上へのPodのスケジューリング | Kubernetes](https://kubernetes.io/ja/docs/concepts/scheduling-eviction/assign-pod-node/)

## Topics
### Logging

- [Google Kubernetes Engine の Stackdriver ログを Fluentd でカスタマイズする | ソリューション](https://cloud.google.com/solutions/customizing-stackdriver-logs-fluentd?hl=ja)

## 参考

- [GKE上RailsのアプリケーションログをStackdriver Loggingで運用する方法 - Riki Shimma - Medium](https://medium.com/@rshimma/rails-on-gke-with-stackdriver-logging-63163c72934)

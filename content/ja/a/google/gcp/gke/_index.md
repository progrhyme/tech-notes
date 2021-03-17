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

## セキュリティ

[クラスタのセキュリティの強化 | Kubernetes Engine ドキュメント | Google Cloud](https://cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster?hl=ja)

### Secretリソースへのアクセスを制限する

いずれか:

1. IAMで `container.secrets.*` の権限を与えない
  - `roles/container.viewer` なら権限なし
1. RBACで権限制御する

参考:
- [【GKE】kubernetesのsecretリソースにアクセスできるユーザーを制限したい](https://zenn.dev/nekoshita/articles/30809412399f70)

### 最小権限のGoogleサービスアカウント

https://cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster?hl=ja#use_least_privilege_sa

- 前提として、Compute Engineのデフォルトサービスアカウントを使わないようにする
- カスタムサービスアカウントには、最低でも以下の権限が必要:
  - monitoring.viewer
  - monitoring.metricWriter
  - logging.logWriter

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

### マルチテナント運用

- [エンタープライズ マルチテナンシーのベスト プラクティス | Kubernetes Engine ドキュメント | Google Cloud](https://cloud.google.com/kubernetes-engine/docs/best-practices/enterprise-multitenancy?hl=ja)

#### ロギング

- [GKE でのマルチテナント ロギング | オペレーション スイート | Google Cloud](https://cloud.google.com/stackdriver/docs/solutions/gke/multi-tenant-logging?hl=ja)

Tips:

- ログシンクを使って、テナントごとにログバケットを分割することができる
  - namespaceによるフィルタを使うことになる

## 参考

- [GKE上RailsのアプリケーションログをStackdriver Loggingで運用する方法 - Riki Shimma - Medium](https://medium.com/@rshimma/rails-on-gke-with-stackdriver-logging-63163c72934)

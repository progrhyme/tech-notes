---
title: "Spinnaker"
linkTitle: "Spinnaker"
description: https://www.spinnaker.io/
date: 2020-05-05T00:24:18+09:00
weight: 650
---

## Documentation

公式サイト: https://www.spinnaker.io/

- [Set up Spinnaker](https://www.spinnaker.io/setup/)
  - [Cloud Providers](https://www.spinnaker.io/setup/install/providers/)
    - [Docker Registry](https://www.spinnaker.io/setup/install/providers/docker-registry/)
    - [Kubernetes v2](https://www.spinnaker.io/setup/install/providers/kubernetes-v2/)
      - [GKE](https://www.spinnaker.io/setup/install/providers/kubernetes-v2/gke/)
- [Guides](https://www.spinnaker.io/guides/)
  - [Tutorials](https://www.spinnaker.io/guides/tutorials/)
    - [Codelabs](https://www.spinnaker.io/guides/tutorials/codelabs/)
      - [Safe Deployments](https://www.spinnaker.io/guides/tutorials/codelabs/safe-deployments/)
- [Reference](https://www.spinnaker.io/reference/)
  - API https://www.spinnaker.io/reference/api/docs.html

## Quickstart

参考:

- https://github.com/spinnaker/spinnaker.github.io/blob/master/downloads/kubernetes/quick-install.yml

## Concepts

- [Overview](https://www.spinnaker.io/concepts/)
  - Application management
    - :
  - Application deployment
    - Pipeline
    - Stage
    - Deployment strategies

## Guides

https://www.spinnaker.io/guides/

### Kubernetes

https://www.spinnaker.io/guides/user/kubernetes-v2/

- [Deploy Kubernetes Manifests](https://www.spinnaker.io/guides/user/kubernetes-v2/deploy-manifest/)
- [Patch Kubernetes Manifests](https://www.spinnaker.io/guides/user/kubernetes-v2/patch-manifest/)
  - K8sのmanifestをpatch更新できる。
  - 参考: [Update API Objects in Place Using kubectl patch - Kubernetes](https://kubernetes.io/docs/tasks/run-application/update-api-object-kubectl-patch/)
- [Rollout Strategies](https://www.spinnaker.io/guides/user/kubernetes-v2/rollout-strategies/)
  - ※ReplicaSetのみ有効 https://www.spinnaker.io/guides/user/kubernetes-v2/traffic-management/#you-must-use-replica-sets
  - Red/Black Rollouts

参考:

- [Introducing Rollout Strategies in the Kubernetes V2 Provider](https://blog.spinnaker.io/introducing-rollout-strategies-in-the-kubernetes-v2-provider-8bbffea109a)

## Reference

https://www.spinnaker.io/reference/

### Artifacts

https://www.spinnaker.io/reference/artifacts/

外部リソースを参照するオブジェクト。

例:

- Dockerイメージ
- GCSやS3内のバイナリ

#### [Artifacts In Kubernetes (Manifest Based)](https://www.spinnaker.io/reference/artifacts/in-kubernetes-v2/)

いくつかのリソースは `vNNN` 形式でSpinnaker内でバージョンが振られる。

## Components

 component | description
-----------------|---------------
Clouddriver | クラウドインフラとのやりとりを司る
Deck | Web UI
Gate | API Gateway
Orca | オーケストレーションエンジン

参考:

- [Authentication - Spinnaker](https://www.spinnaker.io/setup/security/authentication/)
- [Horizontally Scale Spinnaker Services - Spinnaker](https://www.spinnaker.io/setup/productionize/scaling/horizontal-scaling/)

## Spec
### Authentication / 認証

https://www.spinnaker.io/setup/security/authentication/

#### Google Cloud IAPによる認証

参考:

- https://www.spinnaker.io/reference/halyard/commands/#hal-config-security-authn-iap
- [Spinnaker Authentication with Cloud IAP - Damian Myerscough - Medium](https://medium.com/@damianmyerscough/spinnaker-authentication-with-cloud-iap-a7f12ebf18c0)

### Authorization / 認可

- Setup: https://www.spinnaker.io/setup/security/authorization/
  - [Google Groups via G Suite - Spinnaker](https://www.spinnaker.io/setup/security/authorization/google-groups/)
- Architecture: https://www.spinnaker.io/reference/architecture/authz_authn/authorization/

Automated Triggersによって起動するPipelineの場合、以下の2つの方法のいずれかで権限設定する:

- [Service Accounts - Spinnaker](https://www.spinnaker.io/setup/security/authorization/service-accounts/)
- [Pipeline Permissions - Spinnaker](https://www.spinnaker.io/setup/security/authorization/pipeline-permissions/) ... こっちは2020-01-08時点でまだαらしい

#### Service Account

削除

```Bash
curl -X DELETE $FRONT50/serviceAccounts/{サービスアカウントID}
```

参考: https://github.com/spinnaker/front50/blob/a25e184f6afd4dd63a8c8fdb63fe109b378f9991/front50-web/src/main/groovy/com/netflix/spinnaker/front50/controllers/ServiceAccountsController.groovy#L69

### CIツール連携

- https://www.spinnaker.io/setup/ci/
- https://www.spinnaker.io/reference/halyard/commands/#hal-config-ci

2020-01-17現在、Concourse, Jenkins, Google Cloud Build, Travis CI, Werckerに対応しているようだ。

## How-to
### Kubernetesアカウントを追加する

- https://www.spinnaker.io/setup/install/providers/kubernetes-v2/#adding-an-account

参考:

- [Spinnakerでデプロイ先のクラスタを追加する - Qiita](https://qiita.com/Yama-Tomo/items/73c2a7ccf60c22866a04)

### ログレベルの変更

`~/.hal/default/service/settings/${component}.yml` に以下の内容を記述:

```YAML
env:
  JAVA_OPTS: "-Dlogging.level.com.netflix.${コンポーネント名}=DEBUG"
```

参考:
- [Fiat Service Account causes NPE if the Service Account is not a user in LDAP · Issue #3388 · spinnaker/spinnaker](https://github.com/spinnaker/spinnaker/issues/3388)
- [\[SOLVED\] How to change spinnaker's services logging level? - Operations - Spinnaker](https://community.spinnaker.io/t/solved-how-to-change-spinnakers-services-logging-level/458)

## Topics
### Spinnaker Rollout Strategies vs K8s Rolling Update

参考:

- [Spinnaker deployment strategies v. Kubernetes rolling update - Platforms - Spinnaker](https://community.spinnaker.io/t/spinnaker-deployment-strategies-v-kubernetes-rolling-update/180)

## GCP (GKE)

Getting Started:

- https://github.com/GoogleCloudPlatform/spinnaker-for-gcp
- https://cloud.google.com/docs/ci-cd/spinnaker/spinnaker-for-gcp

Advanced:

- [Spinnaker を使用したアプリの管理と複数の GKE クラスタへのデプロイ | ソリューション | Google Cloud](https://cloud.google.com/solutions/managing-and-deploying-apps-to-multiple-gke-clusters-using-spinnaker?hl=ja)

参考:

- [GKE で Spinnaker を構築する - Qiita](https://qiita.com/takasp/items/a74c8acdf3a8851b8da7)

## Child Pages

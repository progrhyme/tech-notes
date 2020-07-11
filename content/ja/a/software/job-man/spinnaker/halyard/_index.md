---
title: "Halyard"
linkTitle: "Halyard"
description: >
  https://www.spinnaker.io/reference/halyard/
date: 2020-05-05T00:27:58+09:00
weight: 200
---

Spinnakerの管理ツール。
daemon + CLI.

## Installation

参考:

- [Install Spinnaker with Halyard on Kubernetes - Oracle Developers - Medium](https://medium.com/oracledevs/install-spinnaker-with-halyard-on-kubernetes-88277bd61d59)

## How-to
### Spinnakerのバージョン更新

```sh
# 利用可能なバージョン一覧
hal version list
# 現在のバージョン表示
hal config version
# バージョン変更
hal config version edit --version $NEW_VERSION
hal deploy apply
```

### 複数のSpinnaker環境を管理する

Halyardでは `Deployment` という単位でconfigを分けることができる。「Deployment」という語はふつうのデプロイという意味やK8s用語としても使われるので、用語としてよくないと思う。 `Environment` とかにしてほしかった気がする（Environmentも何かとかぶりそうだが）。

See https://www.spinnaker.io/reference/halyard/#deployments


新しいDeploymentを作るには下のコマンドを叩く:

```sh
hal config --set-current-deployment $DEPLOYMENT
```

指定した `$DEPLOYMENT` がなければ新規作成される。  
ちなみに、デフォルトの `$DEPLOYMENT` は `default` である。

このコマンドによって新しく作ったDeploymentはまっさらな状態なので、一通りセットアップしなければならない。  
（日記はここで終わっている。）

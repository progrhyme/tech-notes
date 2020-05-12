---
title: "halコマンド"
linkTitle: "hal"
description: >
  リファレンス: https://www.spinnaker.io/reference/halyard/commands/
date: 2020-05-12T12:05:51+09:00
---

リファレンス的に各コマンドの解説を書いていく。

ユースケース別の使い方は[Halyard#How-to]({{< ref "/a/software/spinnaker/halyard/_index.md" >}}#how-to)などを参照すること。

## Global Parameters

 オプション | 意味
----------|------
 `--daemon-endpoint <ADDRESS>` | 指定があればそのdaemonに接続に行く
 `-d, --debug` | daemonの詳細なネットワークトラフィックを出力
 `-l, --log` | CLIのログレベルを設定
 `-h, --help` | ヘルプ表示

## backup

```sh
# バックアップ作成。tarballが出来る
hal backup create
```

## config

```sh
# Spinnakerのコンポーネントのリソース利用量を変更
hal config deploy component-sizing <component> [delete|edit] [parameters]

# IAP認証を有効化
hal config security authn iap enable

# 該当プロバイダのアカウント一覧
hal config provider $PROVIDER account list
# 該当プロバイダの該当アカウントにRBACのロール設定
hal config provider $PROVIDER account edit $ACCOUNT \
  --read-permissions $ROLE1,$ROLE2,... \
  --write-permissions $ROLE1,$ROLE2,...
```

参考:

- https://www.spinnaker.io/setup/security/authorization/#accounts

### canary

Canary analysis settings. kayentaの設定らしい。

Examples:

```sh
hal config canary <integration> account list
hal config canary <integration> account edit ACCOUNT [parameters]
```

Integrations:

- aws, datadog, google, newrelic, prometheus, signalfx

### deploy

Spinnakerのデプロイメントの設定とその表示。

SYNOPSIS:

```sh
# 状態表示
hal config deploy

hal config deploy SUBCOMMAND parameters
```

Subcommands:

- component-sizing, edit, ha

#### component-sizing

各コンポーネントのリソース利用量の設定管理。

Examples:

```sh
hal config deploy component-sizing COMPONENT edit \
  --container-requests-cpu 100m \
  --container-requests-memory 256Mi \
  --container-limits-cpu 200m \
  --container-limits-memory 512Mi \
  --pod-requests-cpu 100m \
  --pod-requests-memory 256Mi \
  --pod-limits-cpu 200m \
  --pod-limits-memory 512Mi \
  --replicas 2
```

Components（一部）:

- clouddriver
- deck
- echo
- fiat
- front50
- gate
- igor
- kayenta
- orca
- rosco

### notification

通知設定の管理。

SYNOPSIS:

```sh
# 設定一覧表示
hal config notification

hal config notification SUBCOMMAND parameters
```

Subcommands:

- github-status
- pubsub
- slack
- twilio

#### slack

Slack通知設定。

SYNOPSIS:

```sh
hal config notification slack enable
hal config notification slack disable
hal config notification slack edit --token $TOKEN
```

### provider

各種クラウドプロバイダなどの設定管理。

Subcommands（一部）:

- appengine
- aws
- azure
- cloudfoundry
- dcos
- docker-registry
- ecs
- google
- kubernetes
- oracle

#### docker-registry

Docker Registryの管理。GCRもこちら

Examples:

```sh
# 状態表示
hal config provider docker-registry

# 有効化・無効化
hal config provider docker-registry enable
hal config provider docker-registry disable

# account管理
hal config provider docker-registry account list
hal config provider docker-registry account get ACCOUNT
hal config provider docker-registry account add ACCOUNT [parameters]
hal config provider docker-registry account delete ACCOUNT [parameters]
hal config provider docker-registry account edit ACCOUNT [parameters]

## GCRをService Account Key認証で追加
hal config provider docker-registry account add asia-gcr-io \
  --address https://asia.gcr.io --username _json_key \
  --password-file path/to/service-account-key.json \
```

NOTE:

- レジストリにリポジトリを追加する場合は `edit` サブコマンドを使う。

例:

```sh
hal config provider docker-registry account edit ACCOUNT --add-repository foo/bar
```

### storage

Persistent storage.

Examples:

```sh
hal config storage <integration> edit [parameters]
```

Integrations:

- azs, gcs, oracle, s3

## deploy

```sh
# Spinnakerの設定変更を適用する
hal deploy apply
# Spinnakerに接続する
hal deploy connect
# 各サービスのログを集める
hal deploy collect-logs
```

---
title: "Pipelines"
linkTitle: "Pipelines"
description: パイプライン設定
date: 2020-05-05T00:28:05+09:00
weight: 700
---

## Documentation

Guides:

- [Managing Pipelines](https://www.spinnaker.io/guides/user/pipeline/managing-pipelines/) ... 作成、実行、無効化、削除、編集、設定の復元、etc.


[Reference](https://www.spinnaker.io/reference/pipeline/):

- [Stages](https://www.spinnaker.io/reference/pipeline/stages/)


## Configuration
### Automated Triggers

パイプラインを外部から実行するためのトリガー設定。

#### Docker Registry

https://www.spinnaker.io/setup/install/providers/docker-registry/ で設定しているリポジトリに新しいイメージがpushされたときに発火する。  
※タグが更新されないと発火しない

参考:

- [Working with Docker Images - Armory Spinnaker Documentation](https://docs.armory.io/spinnaker-user-guides/docker/)
- [Spinnakerのパイプラインによる自動デプロイ - 仮想化通信](https://tech.virtualtech.jp/entry/2018/06/25/180834)


#### Webhooks

https://www.spinnaker.io/guides/user/pipeline/triggers/webhooks/

- `<spinnaker-url>/webhooks/webhook/$key` な任意のURLを発行して、対象のパイプラインのトリガーにできる
- Spinnaker for GCPな環境でも外から叩けるURLが発行できそうだった


### Manual Judgement

Documents:

- [Safe Deployments - Spinnaker](https://www.spinnaker.io/guides/tutorials/codelabs/safe-deployments/)


`Manual Judgement` stageを追加することで、人間による手動判断のプロセスを追加できる。

MEMO:

- `Manual Judgement` stageでは通知を飛ばすことができる。これによってパイプラインの実行権限のある人に判断を促す
- `Manual Judgement` の結果によって処理を分岐させたい場合、続くstageで `Conditional on Expression` にチェックを入れ、条件として `${ #("Manual Judgementのstage名").equals("選択肢")}` を入れる


#### Propagate Authentication

これにチェックを入れると、認証機能によって許可されたユーザにしか判断が下せないようになる。

参考:

- [Authentication and Authorization - Armory Spinnaker Documentation](https://docs.armory.io/spinnaker/authorization/)
- [Lab 5: Deployment Safeguards | workshops](https://www.spinnaker.io/workshops/lab-5.html)

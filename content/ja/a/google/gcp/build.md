---
title: "Cloud Build"
linkTitle: "Build"
description: https://cloud.google.com/cloud-build
date: 2020-06-10T11:39:18+09:00
weight: 40
---

## ビルド構成

https://cloud.google.com/cloud-build/docs/build-config

- docker build -> Dockerfile
- その他の処理 -> ビルド構成ファイル(YAML or JSON)

### ビルド構成ファイル

https://cloud.google.com/cloud-build/docs/build-config?hl=ja#structure_of_a_build_config_file

#### ビルドステップ

https://cloud.google.com/cloud-build/docs/build-config?hl=ja#build_steps

- name ... [クラウドビルダー](https://cloud.google.com/cloud-build/docs/cloud-builders)を指定する
- args ... 引数リスト
- entrypoint ... ビルダーのデフォルトのエントリーポイント（実行コマンド）を上書き可能


## ビルドトリガーによるビルドの自動化

ドキュメント:

- [ビルドトリガーを使用したビルドの自動化 | Cloud Build のドキュメント | Google Cloud](https://cloud.google.com/cloud-build/docs/running-builds/automate-builds?hl=ja)
- [Creating and managing build triggers | Cloud Build Documentation](https://cloud.google.com/build/docs/automating-builds/create-manage-triggers)

MEMO:

- GCSR, GitHub or Bitbucketにソースコードが必要
  - Bitbucketの場合GCSRにミラーリングするか、コンソールからリポジトリ登録時に認証を行う

### トリガー設定

 項目 | 必須？ | 説明
-----|-------|------
Source | Yes | リポジトリとブランチ/タグを選ぶ
Included files | No | 設定されていると、ビルドをトリガーするには最低でもここに含まれるいずれかのファイルの変更が必要
Ignored files | No | 設定されたファイルリストのみの変更はビルドをトリガーしない

Included files / Ignored filesについて:
- あるファイルを両方に指定したら、そのファイルへの変更はビルドをトリガーしない
- 新規ブランチをpushした場合、全ファイルが変更されたとみなされる

## ビルド通知の送信

https://cloud.google.com/cloud-build/docs/send-build-notifications

Cloud Buildでは、ビルドの作成時・動作状態への移行時・完了時などビルド状態の変化時にCloud Pub/Subトピック `cloud-builds` にメッセージを公開する。

他のツール:

- https://github.com/GoogleCloudPlatform/cloud-builders-community/tree/master/slackbot

## 権限管理

サービスアカウントで設定する。

ドキュメント:

- [サービス アカウント権限の設定 | Cloud Build のドキュメント | Google Cloud](https://cloud.google.com/cloud-build/docs/securing-builds/set-service-account-permissions?hl=ja)


## How-to
### ビルド通知をSlackに送信

ドキュメント:
- [サードパーティ サービスの通知の構成 | Cloud Build のドキュメント | Google Cloud](https://cloud.google.com/cloud-build/docs/configure-third-party-notifications?hl=ja#writing_the_cloud_function)

上のようにCloud Functionを書けばよい。

参考:

- [Cloud Buildの進行状況をSlackに通知する - Qiita](https://qiita.com/tnagao3000/items/ff7dd2e89fd8cb42ad5a)

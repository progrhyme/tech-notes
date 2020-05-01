---
title: "Bitbucket"
linkTitle: "Bitbucket"
description: >
  https://bitbucket.org/
date: 2020-04-28T00:22:53+09:00
weight: 100
---

Atlassian社が提供しているソースコードのホスティングサービス。  
JIRAなど他のAtlassian製品との連携が強み（だと思う）。

## 提供形態

- クラウド ... Bitbucket Cloud
- セルフホスト ... オンプレミス
  - Bitbucket Server ... 単一サーバ
  - Bitbucket Datacenter ... クラスタ構成

## Pipelines

付属のCI/CDツール。

[製品ページ](https://www.atlassian.com/ja/software/bitbucket/features/pipelines)

### Documentation

- 日本語: [Pipelines を使用したビルド、テスト、およびデプロイ](https://ja.confluence.atlassian.com/bitbucket/build-test-and-deploy-with-pipelines-792496469.html)
  - [プル リクエストを使用したデプロイ](https://ja.confluence.atlassian.com/bitbucket/deploy-with-pull-requests-856832274.html)
- English: [Build, test, and deploy with Pipelines](https://confluence.atlassian.com/bitbucket/build-test-and-deploy-with-pipelines-792496469.html)
- デモリポジトリ: https://bitbucket.org/bitbucketpipelines/workspace/projects/DOC

### Dockerイメージの利用

[Docker イメージをビルド環境として使用する - アトラシアン製品ドキュメント](https://ja.confluence.atlassian.com/bitbucket/use-docker-images-as-build-environments-792298897.html)

- DockerHubでは認証情報を渡すことでプライベートイメージの利用も可能
- AWSのECRやGCPのGCRも利用可能

### パイプラインの変数

[パイプラインでの変数 - アトラシアン製品ドキュメント](https://ja.confluence.atlassian.com/bitbucket/variables-in-pipelines-794502608.html)

- 「secure」チェックをONにすると、パイプラインの実行ログ上でもマスクされ、表示されなくなる
  - `$MY_SECRET` のように表示される

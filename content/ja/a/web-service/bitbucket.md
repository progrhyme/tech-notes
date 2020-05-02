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

## Documentation

- [Bitbucket Cloud documentation - Atlassian Documentation](https://confluence.atlassian.com/bitbucket)
- 邦訳: [Bitbucket Cloud ドキュメント - アトラシアン製品ドキュメント](https://ja.confluence.atlassian.com/bitbucket/bitbucket-cloud-documentation-221448814.html)
  - [Webhook を管理する - アトラシアン製品ドキュメント](https://ja.confluence.atlassian.com/bitbucket/manage-webhooks-735643732.html)
  - [Bitbucket Cloud で Web サイトを公開する - アトラシアン製品ドキュメント](https://ja.confluence.atlassian.com/bitbucket/publishing-a-website-on-bitbucket-cloud-221449776.html)

## Pipelines

付属のCI/CDツール。

[製品ページ](https://www.atlassian.com/ja/software/bitbucket/features/pipelines)

### Documentation

- [Build, test, and deploy with Pipelines](https://confluence.atlassian.com/bitbucket/build-test-and-deploy-with-pipelines-792496469.html)
- 邦訳: [Pipelines を使用したビルド、テスト、およびデプロイ](https://ja.confluence.atlassian.com/bitbucket/build-test-and-deploy-with-pipelines-792496469.html)
  - [YAML アンカー - アトラシアン製品ドキュメント](https://ja.confluence.atlassian.com/bitbucket/yaml-anchors-960154027.html)
  - [Bitbucket Pipelines の FAQ - アトラシアン製品ドキュメント](https://ja.confluence.atlassian.com/bitbucket/bitbucket-pipelines-faq-827104769.html)
- デモリポジトリ: https://bitbucket.org/bitbucketpipelines/workspace/projects/DOC

### プルリクエストで実行する

ドキュメント: [bitbucket-pipelines.yml の設定 - アトラシアン製品ドキュメント](https://ja.confluence.atlassian.com/bitbucket/configure-bitbucket-pipelines-yml-792298910.html)

`pull-requests` というキーワードによって、PRをトリガーとするパイプライン処理を記述できる。

Example:

```YAML
pipelines:
  pull-requests:
    '**': #this runs as default for any branch not elsewhere defined
      - step:
          script:
            - ...
    feature/*: #any branch with a feature prefix
      - step:
          script:
            - ...
```

参考:

- [プル リクエストを使用したデプロイ](https://ja.confluence.atlassian.com/bitbucket/deploy-with-pull-requests-856832274.html)

### ステップを手動実行する

ドキュメント: [bitbucket-pipelines.yml の設定 - アトラシアン製品ドキュメント](https://ja.confluence.atlassian.com/bitbucket/configure-bitbucket-pipelines-yml-792298910.html)

- `trigger: manual` をつける。  
- ※最初のステップは手動にはできない

Example:

```YAML
pipelines:
  default:
    - step:
        script:
          - ./run-test.sh
    - step:
        trigger: manual
        script:
          - ./deploy.sh
```

Tips:

- パイプライン全体を手動トリガーで実行する場合、customパイプラインを使う

### Dockerイメージの利用

[Docker イメージをビルド環境として使用する - アトラシアン製品ドキュメント](https://ja.confluence.atlassian.com/bitbucket/use-docker-images-as-build-environments-792298897.html)

- DockerHubでは認証情報を渡すことでプライベートイメージの利用も可能
- AWSのECRやGCPのGCRも利用可能

### パイプラインの変数

[パイプラインでの変数 - アトラシアン製品ドキュメント](https://ja.confluence.atlassian.com/bitbucket/variables-in-pipelines-794502608.html)

- 「secure」チェックをONにすると、パイプラインの実行ログ上でもマスクされ、表示されなくなる
  - `$MY_SECRET` のように表示される

### パイプラインをトリガーせずにコミット

コミットメッセージに `[skip ci]` または `[ci skip]` を含める。

[Bitbucket Pipelines の FAQ - アトラシアン製品ドキュメント](https://ja.confluence.atlassian.com/bitbucket/bitbucket-pipelines-faq-827104769.html)

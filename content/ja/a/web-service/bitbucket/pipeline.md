---
title: "Bitbucket Pipelines"
linkTitle: "Pipelines"
description: >
  Cloud版に付属しているCI/CDツール。
  [製品ページ](https://www.atlassian.com/ja/software/bitbucket/features/pipelines)
date: 2020-05-14T14:15:43+09:00
---

## Documentation

- [Build, test, and deploy with Pipelines](https://confluence.atlassian.com/bitbucket/build-test-and-deploy-with-pipelines-792496469.html)
- 邦訳: [Pipelines を使用したビルド、テスト、およびデプロイ](https://ja.confluence.atlassian.com/bitbucket/build-test-and-deploy-with-pipelines-792496469.html)
  - [YAML アンカー](https://ja.confluence.atlassian.com/bitbucket/yaml-anchors-960154027.html)
  - [Bitbucket Pipelines の FAQ](https://ja.confluence.atlassian.com/bitbucket/bitbucket-pipelines-faq-827104769.html)
- デモリポジトリ: https://bitbucket.org/bitbucketpipelines/workspace/projects/DOC

参考:

- [【初心者向け】bitbucket-pipelinesのキーワードとTips - Qiita](https://qiita.com/mochio/items/33584357e924f55f9023)

## Features
### Deployments

Documentation:

- [Bitbucket Deployments - アトラシアン製品ドキュメント](https://ja.confluence.atlassian.com/bitbucket/bitbucket-deployments-940695276.html)
  - [Bitbucket Deployments のセットアップ](https://ja.confluence.atlassian.com/bitbucket/set-up-bitbucket-deployments-968683907.html)
  - [ロールバック](https://ja.confluence.atlassian.com/bitbucket/rollbacks-981147477.html)

NOTE:

- Deployments設定で、デプロイ先環境の管理ができる。
- bitbucket-pipelines.ymlのstep設定で `deployment: Production` などと指定すると、そのstepのビルドがデプロイ先環境と紐付けられる。
- ダッシュボードで履歴が確認できる
- ロールバックもGUIぽちぽちで行ける

## How-to
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

### パイプラインからリポジトリを変更してプッシュする

[リポジトリにプッシュ バックする - アトラシアン製品ドキュメント](https://ja.confluence.atlassian.com/bitbucket/push-back-to-your-repository-962352710.html)

Example:

```YAML
pipelines:
  default:
    - step:
        script:
        - echo "Made a change in build ${BITBUCKET_BUILD_NUMBER}" >> changes.txt
        - git add changes.txt
        - git commit -m "[skip ci] Updating changes.txt with latest build number."
        - git push
```

## Topics
### Server版ではどうすればよいか？

- サーバ版ではBitbucket Pipelinesの提供がない（2020-05-14時点）
  - Cloud版向けのツールらしい。
  - [Pipelines in Bitbucket server - Bitbucket Development / Bitbucket Server - The Atlassian Developer Community](https://community.developer.atlassian.com/t/pipelines-in-bitbucket-server/25636)
    - [Bamboo](https://www.atlassian.com/software/bamboo)のインテグレーションがあるよって言ってる
  - [\[BSERV-9245\] Bitbucket Pipelines for Bitbucket Server - Create and track feature requests for Atlassian products.](https://jira.atlassian.com/browse/BSERV-9245)

Bitbucketサーバ版に対応してそうなCIツール:

- CircleCI

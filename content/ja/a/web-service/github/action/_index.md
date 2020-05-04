---
title: "GitHub Actions"
linkTitle: "Actions（製品）"
description: >
  https://github.com/features/actions
date: 2020-04-26T14:16:09+09:00
---

GitHubのリポジトリに対してCI/CD等のワークフローを自動実行できるサービス。  
[2019年11月に正式リリースされた](https://github.blog/jp/2019-11-14-universe-day-one/)。

※2020-05-03 このページの内容を元に、[Qiitaに投稿した](https://qiita.com/progrhyme/items/56c24b3731deffcd4481)。

## Documentation

https://help.github.com/en/actions

- [Workflow syntax for GitHub Actions - GitHub Help](https://help.github.com/en/actions/reference/workflow-syntax-for-github-actions)
- [Virtual environments for GitHub-hosted runners - GitHub Help](https://help.github.com/en/actions/reference/virtual-environments-for-github-hosted-runners) ... `runs-on` でサポートされている実行環境
- [Context and expression syntax for GitHub Actions - GitHub Help](https://help.github.com/en/actions/reference/context-and-expression-syntax-for-github-actions) ... `${{ <expression> }}` 形式でYAMLに埋め込める式表現とか、 `if: ${{ <expression> }}` によるガード条件について

参考:

- [Github Actionsの使い方メモ - Qiita](https://qiita.com/HeRo/items/935d5e268208d411ab5a)

## 既知の制限事項

2020-05-03更新

- ビルドを手動トリガーするネイティブ機能がない
  - [2020-05-03に調べたログ]({{< ref "20200503.md" >}}#github-actionsには今ビルドを手動トリガーするネイティブ機能はないが同等のことはできる)
  - ※ワークアラウンドは可能
- YAMLアンカーがサポートされていない
  - [Support for YAML anchors - GitHub Community Forum](https://github.community/t5/GitHub-Actions/Support-for-YAML-anchors/td-p/30336)
- デフォルトでは[公式のSlackインテグレーション](https://github.com/integrations/slack#configuration)で、ビルド結果通知を受け取れない。
  - 該当するfeatureがない
  - 3rd Partyのactionを使えば可能。incoming webhookと組み合わせる
  - プルリクエストに紐付いたビルドの結果はわかるようだ

## Getting Started

https://github.com/actions/starter-workflows ... 初心者向けワークフローサンプル集

## Workflowの作成

https://help.github.com/en/actions/configuring-and-managing-workflows/configuring-a-workflow

NOTE:

- プロジェクトの `.github/workflows/` ディレクトリ下にYAMLファイルを作成する
- pushをトリガーにしたり、定期的に実行したりできる
  - See https://help.github.com/en/actions/reference/workflow-syntax-for-github-actions#on

### プルリクエストで実行する

任意のプルリクエストでtestを実行し、masterブランチへのマージでのみdeployを実行する設定例（2ファイル）:

```YAML
# test.yml
name: test
on: pull_request
jobs:
  test:
    runs-on: ubuntu-latest
      steps:
        # tasks for testing
---
# deploy.yml
name: deploy
on:
  pull_request:
    branches:
      - master
    types: [closed]
jobs:
  deploy:
    runs-on: ubuntu-latest
    if: ${{ github.event.pull_request.merged == true }}
      steps:
        # tasks for deployment
```

NOTE:

- デフォルトでは `pull_request` eventでは `types: [opened, synchronize, reopend]` でしか実行されない。 `test` のときはこれになっている。
  - https://help.github.com/en/actions/reference/events-that-trigger-workflows#pull-request-event-pull_request

参考:

- [Solved: Re: Trigger workflow only on pull request MERGE - GitHub Community Forum](https://github.community/t5/GitHub-Actions/Trigger-workflow-only-on-pull-request-MERGE/td-p/43201) ... Solutionは間違ってるので注意

### 対象branchやpathをフィルタする

Example:

```YAML
on:
  push:
    branches:
      - master
      - 'releases/**'
      - '!releases/**-alpha' # alpha版は含めない
    tags:
      - v1
    # file paths to consider in the event. Optional; defaults to all.
    paths:
      - 'test/*'
    paths-ignore:
      - 'docs/**'
```

NOTE:

- `branches` と `branches-ignore` は**併用不可**
- `tags` と `tags-ignore` は**併用不可**
- `paths` と `paths-ignore` は（たぶん）併用可

リファレンス:

- branchやtagについて -> [on\.\<push\|pull_request\>\.\<branches\|tags\>](https://help.github.com/en/actions/reference/workflow-syntax-for-github-actions#onpushpull_requestbranchestags)
- pathについて -> [on\.\<push\|pull_request\>\.paths](https://help.github.com/en/actions/reference/workflow-syntax-for-github-actions#onpushpull_requestpaths)

### 複数の実行環境に対応する

複数のOSプラットフォームや、ランタイムのバージョンに対応する方法。  
下のようなbuild matrixを設定すると良い。

Example:

```YAML
runs-on: ${{ matrix.os }}
strategy:
  matrix:
    os: [ubuntu-16.04, ubuntu-18.04]
    node: [6, 8, 10]
```

### Dockerコンテナ上でビルド実行

`jobs.<job_id>.container` で指定する。

https://help.github.com/en/actions/reference/workflow-syntax-for-github-actions#jobsjob_idcontainer

Examples:

```YAML
jobs:
  my_job:
    container: node:10.16-jessie

---
jobs:
  my_job:
    container:
      image: node:10.16-jessie
      env:
        NODE_ENV: development
      ports:
        - 80
      volumes:
        - my_docker_volume:/volume_mount
      options: --cpus 1
```

[starter-workflows](https://github.com/actions/starter-workflows)にも参考になるサンプルがある。以下は例:

- https://github.com/actions/starter-workflows/blob/master/ci/erlang.yml

### 環境変数を設定する

https://help.github.com/en/actions/reference/workflow-syntax-for-github-actions#env

いくつかの箇所で設定できる。それぞれ適用範囲が異なる。

 設定位置 | 適用範囲
----------|----------
 `env` | for all jobs and steps
 `jobs.<job_id>.env` | for all steps in the job
 `jobs.<job_id>.steps.env` | for the step
 `jobs.<job_id>.container.env` | for the container to run steps in the job

Examples:

```YAML
env:
  SERVER: production

---
jobs:
  my-job:
    name: My Job
    runs-on: ubuntu-latest
    env:
      MY_VAR: Hi there! My name is
    steps:
    - name: Print a greeting
      env:
        FIRST_NAME: Mona
        MIDDLE_NAME: The
        LAST_NAME: Octocat
      run: |
        echo $MY_VAR $FIRST_NAME $MIDDLE_NAME $LAST_NAME.
```

See also [#変数やシークレットの利用](#変数やシークレットの利用)

### jobやstepを特定の条件で実行する

`jobs.<job_id>.if` や `jobs.<job_id>.steps.if` の値に条件式を記述することで、該当のjobやstepを条件が真のときのみ実行することができる。

Examples:

```YAML
jobs:
  deploy:
    # プルリクエストがマージされた時のみ実行
    if: ${{ github.event.pull_request.merged == true }}

    steps:
      - name: Deploy
        # some deploy action

      - name: Notify
        # このstepは常に実行する
        if: ${{ always() }}
        # some notify action
```

NOTE:

- `if: ` に渡す条件式では `${{ }}` は省略可能
- ワークフロー内でタスクが失敗すると、デフォルトでは後続のタスクはスキップされる
  - See [Context and expression syntax for GitHub Actions - GitHub Help#always](https://help.github.com/en/actions/reference/context-and-expression-syntax-for-github-actions#always)

> A job or step will not run when a critical failure prevents the task from running. For example, if getting sources failed.

## 変数やシークレットの利用

Documents:

- https://help.github.com/en/actions/configuring-and-managing-workflows/using-variables-and-secrets-in-a-workflow
  - [Creating and storing encrypted secrets - GitHub Help](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets)
  - [Using environment variables - GitHub Help](https://help.github.com/en/actions/configuring-and-managing-workflows/using-environment-variables)

### GITHUB_TOKENによる認証

[Authenticating with the GITHUB_TOKEN - GitHub Help](https://help.github.com/en/actions/configuring-and-managing-workflows/authenticating-with-the-github_token)

> GitHubは、ワークフローで利用する `GITHUB_TOKEN` シークレットを自動的に生成します。 この `GITHUB_TOKEN` は、ワークフローの実行内での認証に利用できます。

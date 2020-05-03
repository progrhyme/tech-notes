---
title: "Actions（タスク）"
linkTitle: "Actions（タスク）"
date: 2020-04-26T14:28:26+09:00
---

- [Marketplace](https://github.com/marketplace?type=actions) ... 公開されているactionを見つけられる。

## Actionとは

アクションは、ワークフロー内で実行される個々のタスク。

[About actions - GitHub Help](https://help.github.com/en/actions/building-actions/about-actions)

### Actionの形式

https://help.github.com/en/actions/building-actions/about-actions#types-of-actions

Type | Operating system
-----|-----------------
Docker container | Linux
JavaScript | Linux, MacOS, Windows

### ワークフローからの利用

https://help.github.com/en/actions/configuring-and-managing-workflows/configuring-a-workflow#referencing-actions-in-your-workflow

ワークフローからは、次のロケーションのactionが利用できる:

- 公開リポジトリ
- 同リポジトリ内で参照できるもの
- Docker Hubに公開されたDockerイメージ

## 公式Actions

GitHub公式のactionはたぶん https://github.com/actions にあるもの。  

### checkout

https://github.com/actions/checkout

リポジトリをチェックアウトする。  
おそらくほとんどのワークフローから利用される。

Example:

```YAML
- uses: actions/checkout@v2
  with:
    # Number of commits to fetch. 0 indicates all history.
    # Default: 1
    fetch-depth: 0

    # Whether to checkout submodules: `true` to checkout submodules or `recursive` to
    # recursively checkout submodules.
    #
    # Default: false
    submodules: true
```

### setup-node

https://github.com/actions/setup-node/

Node.jsをセットアップ。

Basic:

```YAML
steps:
- uses: actions/checkout@v2
- uses: actions/setup-node@v1
  with:
    node-version: '10.x'
- run: npm install
- run: npm test
```

Matrix Testing:

```YAML
jobs:
  build:
    runs-on: ubuntu-18.04
    strategy:
      matrix:
        node: [ '10.x', '12.x' ]
    name: Node ${{ matrix.node }} sample
    steps:
      - uses: actions/checkout@v2
      - name: Setup node
        uses: actions/setup-node@v1
        with:
          node-version: ${{ matrix.node }}
      - run: npm install
      - run: npm test
```

参考:

- [GitHub ActionsでのNode.jsの利用 - GitHub ヘルプ](https://help.github.com/ja/actions/language-and-framework-guides/using-nodejs-with-github-actions)
- https://github.com/actions/starter-workflows/blob/master/ci/node.js.yml

## 3rd Party Actions

### Slack通知用

- [8398a7/action-slack](https://github.com/8398a7/action-slack) ... メッセージ等のカスタマイズの余地はなさそうだが、必要十分な感ある
- [rtCamp/action-slack-notify](https://github.com/rtCamp/action-slack-notify) ... 通知先チャネルも設定可能で、よさそう

### Deployments作成用

Deploymentsについては See [GitHub#Deployments]({{< ref "/a/web-service/github/_index.md" >}}#deployments)

NOTE:

- 後掲のpeaceiris/actions-gh-pagesのように、内部的にDeploymentを作成するactionもあるようだ。

Actions:

- [bobheadxi/deployments](https://github.com/bobheadxi/deployments)
- [chrnorm/deployment-action](https://github.com/chrnorm/deployment-action)

### hashicorp/terraform-github-actions

https://github.com/hashicorp/terraform-github-actions

terraformを実行するaction

ドキュメント:

- 上のREADME
- https://www.terraform.io/docs/github-actions/

NOTE:

- デフォルト設定でプルリクエストにfmt, validate, plan, applyの結果をコメントしてくれて便利。

#### 例: terraform fmt -> validate -> plan

```YAML
name: terraform plan

on: pull_request

env:
  tf_version: '0.12.24'
  tf_work_dir: '.'
  GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

jobs:
  plan:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2

      - name: terraform fmt
        uses: hashicorp/terraform-github-actions@master
        with:
          tf_actions_version: ${{ env.tf_version }}
          tf_actions_subcommand: fmt
          tf_actions_working_dir: ${{ env.tf_work_dir }}

      - name: terraform init
        uses: hashicorp/terraform-github-actions@master
        with:
          tf_actions_version: ${{ env.tf_version }}
          tf_actions_subcommand: init
          tf_actions_working_dir: ${{ env.tf_work_dir }}

      - name: terraform validate
        uses: hashicorp/terraform-github-actions@master
        with:
          tf_actions_version: ${{ env.tf_version }}
          tf_actions_subcommand: validate
          tf_actions_working_dir: ${{ env.tf_work_dir }}

      - name: terraform plan
        uses: hashicorp/terraform-github-actions@master
        with:
          tf_actions_version: ${{ env.tf_version }}
          tf_actions_subcommand: plan
          tf_actions_working_dir: ${{ env.tf_work_dir }}
```

#### 例: terraform plan -> apply

```YAML
name: terraform apply

on:
  push:
    branches:
      - master
env:
  tf_version: '0.12.24'
  tf_work_dir: '.'
  GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

jobs:
  apply:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2

      - name: terraform init
        uses: hashicorp/terraform-github-actions@master
        with:
          tf_actions_version: ${{ env.tf_version }}
          tf_actions_subcommand: init
          tf_actions_working_dir: ${{ env.tf_work_dir }}

      - name: terraform plan
        id: plan
        uses: hashicorp/terraform-github-actions@master
        with:
          tf_actions_version: ${{ env.tf_version }}
          tf_actions_subcommand: plan
          tf_actions_working_dir: ${{ env.tf_work_dir }}

      - name: terraform apply
        # planの差分がある時のみ実行
        if: ${{ steps.plan.outputs.tf_actions_plan_has_changes == 'true' }}
        uses: hashicorp/terraform-github-actions@master
        with:
          tf_actions_version: ${{ env.tf_version }}
          tf_actions_subcommand: apply
          tf_actions_working_dir: ${{ env.tf_work_dir }}
```

### peaceiris/actions-gh-pages

https://github.com/peaceiris/actions-gh-pages

GitHub Pagesに公開するaction.

Example:

```YAML
- uses: peaceiris/actions-gh-pages@v3
  with:
    github_token: ${{ secrets.GITHUB_TOKEN }}
    publish_dir: ./public
    #publish_branch: master # default: gh-pages
```

### peaceiris/actions-hugo

https://github.com/peaceiris/actions-hugo

ランナー上にHugoをインストールする。

Example:

```YAML
- name: Setup Hugo
  uses: peaceiris/actions-hugo@v2
  with:
    hugo-version: '0.68.3'
    # extended: true

- name: Build
  run: hugo --minify
```

Tips:

- `extended: true` でHugoの拡張版をインストール
- `hugo-version: latest` で最新版を使う

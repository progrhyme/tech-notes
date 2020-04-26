---
title: "GitHub Actions"
linkTitle: "Actions（製品）"
description: >
  https://github.com/features/actions
date: 2020-04-26T14:16:09+09:00
---

CI/CD等のワークフローを自動実行できるサービス。  
[2019年11月に正式リリースされた](https://github.blog/jp/2019-11-14-universe-day-one/)。

## Documentation

https://help.github.com/en/actions

- [Workflow syntax for GitHub Actions - GitHub Help](https://help.github.com/en/actions/reference/workflow-syntax-for-github-actions)

## Getting Started

https://github.com/actions/starter-workflows ... 初心者向けワークフローサンプル集

## Workflowの作成

https://help.github.com/en/actions/configuring-and-managing-workflows/configuring-a-workflow

- プロジェクトの `.github/workflows/` ディレクトリ下にYAMLファイルを作成する
- pushをトリガーにしたり、定期的に実行したりできる
  - See https://help.github.com/en/actions/reference/workflow-syntax-for-github-actions#on

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

リファレンス:

- branchやtagについて -> [on.<push|pull_request>.<branches|tags>](https://help.github.com/en/actions/reference/workflow-syntax-for-github-actions#onpushpull_requestbranchestags)
- pathについて -> [on.<push|pull_request>.paths](https://help.github.com/en/actions/reference/workflow-syntax-for-github-actions#onpushpull_requestpaths)

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

## 変数やシークレットの利用

https://help.github.com/en/actions/configuring-and-managing-workflows/using-variables-and-secrets-in-a-workflow

### GITHUB_TOKENによる認証

[Authenticating with the GITHUB_TOKEN - GitHub Help](https://help.github.com/en/actions/configuring-and-managing-workflows/authenticating-with-the-github_token)

> GitHubは、ワークフローで利用する `GITHUB_TOKEN` シークレットを自動的に生成します。 この `GITHUB_TOKEN` は、ワークフローの実行内での認証に利用できます。

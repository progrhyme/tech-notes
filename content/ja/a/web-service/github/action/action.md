---
title: "Actions（タスク）"
linkTitle: "Actions（タスク）"
date: 2020-04-26T14:28:26+09:00
---

- [Marketplace](https://github.com/marketplace?type=actions) ... 公開されているactionを見つけられる。

## Actionとは

[About actions - GitHub Help](https://help.github.com/en/actions/building-actions/about-actions#types-of-actions)

actionはワークフローで実行される処理（タスク）を再利用可能な形にパッケージしたものである。

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
---
title: "MkDocs"
linkTitle: "MkDocs"
description: https://www.mkdocs.org/
date: 2020-06-20T18:56:31+09:00
weight: 420
---

Python製の静的サイトジェネレータ。  
ページ構成を多段にできないので、あまりスケールできないと思われる。

※mkdocs-materialだと少なくとも2階層にはできる。

## Getting Started

参考:

- [MkDocsによるドキュメント作成 - Qiita](https://qiita.com/mebiusbox2/items/a61d42878266af969e3c)

### Installation

いくつか選択肢がある

- パッケージマネージャー
- `pip install mkdocs`

後述のmkdocs-materialを使うなら、そちらのDockerイメージを使う手も有る。MkDocsも含まれているので。

参考:

- [2020-06-20#MkDocs事始め]({{<ref "20200620.md">}}#mkdocs事始め)

### Quickstart

https://www.mkdocs.org/#getting-started

```sh
# プロジェクト作成
mkdocs new my-project
cd my-project

# Webサーバ起動
mkdocs serve

# サイトのビルド
mkdocs build
```

## Usage
### ページの追加

https://www.mkdocs.org/#adding-pages

1. docs/ 以下にMarkdownファイルを追加
1. config file (mkdocs.yml) で設定

設定例:

```YAML
site_name: MkLorum
nav:
  - Home: index.md
  - About: about.md
theme: readthedocs
```

## Themes

一覧: https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes

Pickup:

- ReadTheDocs ... 組み込み。色んなところで使われている。そつない見た目で、使いやすい
- [ReadTheDocs Dropdown](http://readthedocs.sheets.ch/) ... ReadTheDocsの拡張。ドロップダウンメニュー対応
- [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) ... 非常に人気の高いテーマ

## mkdocs-material

- https://squidfunk.github.io/mkdocs-material/
- https://github.com/squidfunk/mkdocs-material

参考:

- [MkDocs・MaterialのDockerを使ったインストール手順 :: GitHub Pages | Refills](https://syon.github.io/refills/rid/1520345/)

### Installation

いくつか選択肢がある:

- `pip install mkdocs-material`
- `docker pull squidfunk/mkdocs-material`
  - https://hub.docker.com/r/squidfunk/mkdocs-material/
- リポジトリをgit cloneして使う

参考:

- [2020-06-20#mkdocs-materialをDockerで動かす]({{<ref "20200620.md">}}#mkdocs-materialをdockerで動かす)

### Features

- ページタブ（後述）
- [Extensions](https://squidfunk.github.io/mkdocs-material/extensions/admonition/)
  - Markdown拡張
    - CodeHilite ... シンタックスハイライト
    - Admonition ... warn, infoなどのブロック要素
    - Footnotes
    - PyMdown
      - superfences
- [Plugins](https://squidfunk.github.io/mkdocs-material/plugins/search/)

### Configuration

タブ機能を有効にするとページをグループ化できる。

```YAML
theme:
  features:
    - tabs
```

---
title: "Hugo"
linkTitle: "Hugo"
description: >
  https://gohugo.io
date: 2020-04-25T23:38:08+09:00
weight: 280
---

Go言語製の高速な静的サイトジェネレーター。

## Documentation

https://gohugo.io/documentation/

- [Getting Started](https://gohugo.io/getting-started/)
  - [Install](https://gohugo.io/getting-started/installing/)
- [Content Management](https://gohugo.io/content-management/)
  - [Front Matter](https://gohugo.io/content-management/front-matter/) ... ページに対して付けることができるメタデータ
- :

## Getting Started
### Install
#### 拡張版のインストール

通常版では、SASS/SCSSサポートがついていないので、必要であれば明示的に拡張版をインストールしないといけない。

{{% alert title="INFO" %}}
2020-04-27現在、Macの場合は `brew install hugo` で拡張版がインストールされるようだ。
{{% /alert %}}

参考:

- [Themes > Docsy](./themes/docsy/#getting-started)
- [\[Hugo\]Hugoの通常バージョンとExtendedバージョンとの違い\[memo\] | 鈍色スイッチ](https://donsyoku.com/software/hugo-what-is-extended-version.html)

##### バイナリをインストール

[GitHub Releases](https://github.com/gohugoio/hugo/releases)から `_extended` 付きのバイナリを取得する。

##### ソースからインストール

```sh
git clone https://github.com/gohugoio/hugo.git
cd hugo
go install --tags extended
```

##### Linux

Snapの場合:

```sh
snap install hugo --channel=extended
```

### [Quickstart](https://gohugo.io/getting-started/quick-start/)

```sh
# 新しくサイトを作る
hugo new site your-new-site

# テーマを用意する
cd your-new-site
git init
git submodule add https://github.com/budparr/gohugo-theme-ananke.git themes/ananke
echo 'theme = "ananke"' >> config.toml

# コンテンツを作成する
hugo new posts/my-first-post.md

# hugo serverを起動
hugo server -D
## -D を付けることで draft のページも表示される
```

## Configuration

### Table Of Contents

https://gohugo.io/getting-started/configuration-markup/#table-of-contents

※Goldmarkのみ

```toml
[markup]
  [markup.tableOfContents]
    endLevel = 3
    ordered = false
    startLevel = 2
```

## Known Issues

### 完全なページツリーを描画する機能がない

ワークアラウンドでの対応が必要。

[Multi-level sections (tree) · Issue #465 · gohugoio/hugo](https://github.com/gohugoio/hugo/issues/465)

ワークアラウンド例:
- http://vjeantet.github.io/hugo-menu-show/
  - [ソースコード](https://github.com/vjeantet/hugo-menu-show/blob/master/themes/menumenu/layouts/index.html)

参考:

- [サイドバー用のページツリーを表示する（現在表示しているページを考慮した階層表示） | まくまくHugo/Goノート](https://maku77.github.io/hugo/list/sidebar-menu.html)

MEMO:

- [Docsyテーマでのサイドバーの実現方法](https://github.com/google/docsy/blob/master/layouts/partials/sidebar-tree.html)が参考になるかも。

## Child Pages

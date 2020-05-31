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

https://gohugo.io/getting-started/configuration/

参考:

- [Hugoで環境によって設定を変える方法 - Qiita](https://qiita.com/progrhyme/items/b31882398f2ddac924cf) ... 自分で書いた記事

### 設定ファイル

デフォルトでは config.toml → config.yaml → config.json の順で参照される。

- `hugo --config CONFIG` オプションで任意の設定ファイルを指定可能
- `hugo --config a.toml,b.toml` のように、カンマ区切りで複数ファイルを指定することも可能

### ディレクトリ構成

https://gohugo.io/getting-started/configuration/#configuration-directory

- 設定ファイルを `config/` ディレクトリ（`--configDir DIRECTORY` で変更可能）に配置することで複数ファイルに分割できる
- `--environment ENVIRONMENT` オプションと組合せて、設定ファイルを更に高度に組織化することもできる。
  - `config/ENVIRONMENT/` 下の設定がマージされる
- ローカリゼーション対応も可能

Example:

```
├── config
│   ├── _default
│   │   ├── config.toml
│   │   ├── languages.toml
│   │   ├── menus.en.toml
│   │   ├── menus.zh.toml
│   │   └── params.toml
│   ├── production
│   │   ├── config.toml
│   │   └── params.toml
│   └── staging
│       ├── config.toml
│       └── params.toml
```

参考:

- [Hugo を利用していると baseURL など prod環境、dev環境で別の値を利用したい場合があります。 今回は config.toml を分割する方法をまとめます。 - n/a n/a nao](https://nananao-dev.hatenablog.com/entry/hugo-config-separate)

### 環境変数による設定

https://gohugo.io/getting-started/configuration/#configure-with-environment-variables

- トップレベルの設定値は、 `HUGO_TITLE="hoge hoge" hugo` のように上書きできるようだ。 `HUGO_TITLE` で `title` を上書き
- `[params]` の設定値であれば、 `HUGO_PARAMS_` をprefixとして設定すればよいそうだ

NOTE:

- 2020-05-31 おそらくこのやり方では設定ファイルで設定した値の削除/無効化はできないと思われる。Docsyで `HUGO_PARAMS_GCS_ENGINE_ID=""` のようにしても、Googleカスタム検索エンジンを無効化できなかった
  - See [2020-05-31#DocsyでGoogleカスタム検索エンジンを使う]({{<ref "20200531.md">}}#docsyでgoogleカスタム検索エンジンを使う)

## 設定項目
設定ファイルの設定項目について。

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

## Writing Pages

記事の作成・編集で使う基本的な機能などについて書く。

### 画像の挿入

現在は記事の近くに画像を置いて、相対パスで参照できる。

```Markdown
<!-- "\" は除いて書くこと -->
{{\<figure src="image.png" alt="blur">}}
```

See [#figure](#figure)

## Shortcodes

https://gohugo.io/content-management/shortcodes/

便利な機能が `{{\<function ... >}}` という構文のShortcodeという形式で提供されている。

自分で独自のShortcodeを作成することもできる。

### figure

https://gohugo.io/content-management/shortcodes/#figure

HTML5の&lt;figure&gt;要素を作る。

 パラメータ | 意味
------------|------
 src | 画像のURL（パス）。必須
 alt | 画像非表示時の代替テキスト
 title | 画像タイトル

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

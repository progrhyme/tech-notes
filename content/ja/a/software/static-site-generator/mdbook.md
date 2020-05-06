---
title: "mdBook"
linkTitle: "mdBook"
description: https://rust-lang.github.io/mdBook/
date: 2020-05-06T13:52:21+09:00
weight: 400
---

Rust製のGitBookみたいなもの。  
高速でよさそう。

## Documentation

上のサイトがドキュメントを兼ねている。

- [CLI](https://rust-lang.github.io/mdBook/cli/)
  - インストール方法はこちら
  - サブコマンド:
    - [init](https://rust-lang.github.io/mdBook/cli/init.html)
    - [build](https://rust-lang.github.io/mdBook/cli/build.html)
    - [serve](https://rust-lang.github.io/mdBook/cli/serve.html)


## CLI & Quickstart

```sh
# 新しくブックのディレクトリを作り、初期セットアップを行う
mdbook init <your-book-directory>

# デフォルトでHTMLを ./book にビルド
mdbook build [OPTIONS]

# デフォルトで ./book 以下のHTMLを元にHTTPサーバを起動
mdbook serve [OPTIONS]
```

NOTE:

- 2020-05-06現在、 `serve` コマンドはHTML表示のテスト用で、Webサイト用の完全なサーバ機能を目指したものではないとのこと

## MEMO
### 2020-04-29

- config: https://rust-lang.github.io/mdBook/format/config.html
- サイドバーに目次ツリーが表示されているが、 `[output.html.fold]` で挙動を変えられそう。
  - https://github.com/rust-lang/mdBook/pull/1027
- 目次（Table of Contents）は公式サポートないのかも。イシューになってる
  - `{{#toc}}{{/toc}}` で行けるんじゃないのかな？
    - https://rust-lang.github.io/mdBook/format/theme/index-hbs.html#1-toc
    - （2020-05-06追記）愚直に書き足したところ、駄目だった
  - https://github.com/rust-lang/mdBook/issues/153
  - 自作している人がいる
    - https://github.com/badboy/mdbook-toc

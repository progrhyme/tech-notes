---
title: "Rust"
linkTitle: "Rust"
description: https://www.rust-lang.org/
date: 2020-05-24T15:28:59+09:00
weight: 800
---

## About

- https://github.com/rust-lang/rust ... ソースコードもRust

## Getting Started

- https://doc.rust-lang.org/book/
  - 日本語訳: https://doc.rust-jp.rs/

### Documentation

https://www.rust-lang.org/learn ... ランディングページ

- [Edition Guide](https://doc.rust-lang.org/edition-guide/)
- [Standard Library](https://doc.rust-lang.org/std/)
  - See [std Library]({{<ref "std.md">}})
- [Cargo Book](https://doc.rust-lang.org/cargo/)
- [rustc book](https://doc.rust-lang.org/rustc/)
- [Rust Compiler Error Index](https://doc.rust-lang.org/error-index.html)
- [rustdoc book](https://doc.rust-lang.org/rustdoc/)

### Style Guide

- [Rust Style Guide](https://github.com/rust-dev-tools/fmt-rfcs/blob/master/guide/guide.md) ... 2020-05-25現在の正式版はこちらのようだ

古い（と思われる）もの:

- https://doc.rust-lang.org/1.0.0/style/

参考:

- [Outdated documentation on doc.rust-lang.org is exposed to search engines · Issue #695 · rust-lang/www.rust-lang.org](https://github.com/rust-lang/www.rust-lang.org/issues/695)

### 開発環境

2018/8/22現在、VSCode, IntelliJが人気のようだ。  
もちろん、Atomでも開発できそうだし、Eclipseもある。

## Community

https://www.rustaceans.org/

Tips:

- Rustを書く人のことを「Rustacean」という。

## CLI

- rustup ... Rustコンパイラインストール。最新バージョンへのアップデート。クロスコンパイル
- rustc ... Rustコンパイラ

### cargo

Rustのビルドシステム兼パッケージマネージャ。

Examples:

```sh
# バージョン表示
cargo --version

# プロジェクト作成
cargo new <project>
cargo new --bin <project>

cargo check # コンパイル可能かチェック

# コンパイル。バイナリ生成
cargo build
cargo build --release # 最適化込み

cargo run   # バイナリを作らずに直接実行
```

参考:

- [Hello, Cargo! - The Rust Programming Language](https://doc.rust-lang.org/book/2018-edition/ch01-03-hello-cargo.html)

### rustup

Rust toolchain installer.

Examples:

```sh
# ヘルプ表示
rustup help

# Update Rust toolchains and rustup
rustup update
# 更新の有無を確認
rustup check

# ブラウザでローカルにインストールされたドキュメントを開く
rustup doc
```

### rustc

Examples:

```sh
# コンパイル
rustc main.rs

# ヘルプ表示
rustc --[h]elp
## 全コマンドオプションを表示
rustc --help -v

# バージョン表示
rustc --version|-V
```

## Crates

Rustのパッケージ管理システム。  
Rustプログラムの単位でもある。  
`cargo new` するとcrateが作られる。

https://crates.io/ : 公式レジストリっぽい。

参考:

- [Rust のモジュールシステム - Qiita](https://qiita.com/skitaoka/items/753a519d720a1ccebb0d)

### [rand](https://crates.io/crates/rand)

乱数生成

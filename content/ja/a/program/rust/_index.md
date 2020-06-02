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
  - See [std Library]({{<ref "std/_index.md">}})
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

### Play Ground

https://play.rust-lang.org/ ... Web上でコードの動作を試せる環境。

## Learn Rust

Rustをより深く学ぶための教材など。

- [Command Line Book](https://rust-cli.github.io/book/) ... RustでCLIを書くためのチュートリアルと関連トピック

## Community

https://www.rustaceans.org/

Tips:

- Rustを書く人のことを「Rustacean」という。

## CLI

- [cargo]({{<ref "cargo.md">}}#cli)
- rustup ... Rustコンパイラインストール。最新バージョンへのアップデート。クロスコンパイル
- rustc ... Rustコンパイラ

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

## Road to Rustacean

Rustでコードを書く上で知っておくべき基礎的なトピックやHow toについて書く。

### 例外処理

入門ガイド:

- [Nicer error reporting - Command Line Applications in Rust](https://rust-cli.github.io/book/tutorial/errors.html)
- [Resultで回復可能なエラー - The Rust Programming Language](https://doc.rust-jp.rs/book/second-edition/ch09-02-recoverable-errors-with-result.html)

関連項目:

- [言語仕様 > 演算子 > ?]({{<ref "spec.md">}}#heading)
- [std::result]({{<ref "std/_index.md">}}#result-module)
- [Crates > failure]({{<ref "crate.md">}}#failure)

### 標準入出力

入門ガイド:

- [Output for humans and machines - Command Line Applications in Rust](https://rust-cli.github.io/book/tutorial/output.html)

関連項目:

- [std::print]({{<ref "std/_index.md">}}#print)などのマクロファミリー
- [std::fmt]({{<ref "std/fmt.md">}})
- [std::io]({{<ref "std/io.md">}})

### ファイル入出力

関連項目:

- [std::path]({{<ref "std/_index.md">}}#path-module)

### コマンドライン引数

入門ガイド:

- [Parsing command line arguments - Command Line Applications in Rust](https://rust-cli.github.io/book/tutorial/cli-args.html)

関連項目:

- [Crates > clap]({{<ref "crate.md">}}#clap)
- [Crates > structopt]({{<ref "crate.md">}}#structopt)

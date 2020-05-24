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

- https://www.rust-lang.org/documentation.html

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
cargo --version

## プロジェクト作成
cargo new <project>
cargo new --bin <project>

cargo check # コンパイル可能かチェック

## コンパイル。バイナリ生成
cargo build
cargo build --release # 最適化込み

cargo run   # バイナリを作らずに直接実行
```

参考:

- [Hello, Cargo! - The Rust Programming Language](https://doc.rust-lang.org/book/2018-edition/ch01-03-hello-cargo.html)


## Crates

Rustのパッケージ管理システム。  
Rustプログラムの単位でもある。  
`cargo new` するとcrateが作られる。

https://crates.io/ : 公式レジストリっぽい。

参考:

- [Rust のモジュールシステム - Qiita](https://qiita.com/skitaoka/items/753a519d720a1ccebb0d)

### [rand](https://crates.io/crates/rand)

乱数生成

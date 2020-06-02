---
title: "Cargo"
linkTitle: "Cargo"
description: https://github.com/rust-lang/cargo
date: 2020-05-30T09:37:39+09:00
weight: 100
---

## About

https://doc.rust-lang.org/cargo/

CargoはRustのパッケージ管理ツール。
以下の機能を有する:

- 依存パッケージのダウンロード
- コンパイル
- 配布可能なパッケージの作成
- crates.io へのアップロード

## CLI

`cargo`

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

## Cargo.toml (manifest)

https://doc.rust-lang.org/cargo/reference/manifest.html

パッケージのメタデータや依存パッケージを記すマニフェストファイル。

参考:

- [cargo publish する前に埋めておきたい Cargo.toml の項目に関するメモ - Qiita](https://qiita.com/tanakh/items/8cfa328ed652d71b1017)

### Dependency tables

https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html

依存パッケージの情報を示すセクション。

- `[dependencies]` ... 実行時に必要なパッケージ
- `[dev-dependencies]` ... テストやベンチマークなどで必要なパッケージ
- `[build-dependencies]` ... ビルドに必要なパッケージ

Example:

```TOML
[dependencies]
time = "0.1.12"
```

上は `"^0.1.12"` (caret requirement) と同じ扱いになる。  
バージョン固定したい場合、 `"= 0.1.12"` と書く。詳しくは下を見よ。

#### バージョンの指定方法

様々な形式でバージョンを指定することができる。

Caret requirements（キャレット）:

```
^1.2.3  :=  >=1.2.3, <2.0.0
^1.2    :=  >=1.2.0, <2.0.0
^1      :=  >=1.0.0, <2.0.0
^0.2.3  :=  >=0.2.3, <0.3.0
^0.2    :=  >=0.2.0, <0.3.0
^0.0.3  :=  >=0.0.3, <0.0.4
^0.0    :=  >=0.0.0, <0.1.0
^0      :=  >=0.0.0, <1.0.0
```

Tilde requirements（チルダ）:

```
~1.2.3  := >=1.2.3, <1.3.0
~1.2    := >=1.2.0, <1.3.0
~1      := >=1.0.0, <2.0.0
```

Wildcard requirements（ワイルドカード）:

```
*     := >=0.0.0
1.*   := >=1.0.0, <2.0.0
1.2.* := >=1.2.0, <1.3.0
```

Note:

- crates.io では `*` だけの指定はNG

Comparison requirements:

```
>= 1.2.0
> 1
< 2
= 1.2.3
```

Multiple requirements:

- 例: `>= 1.2, < 1.5`

#### パッケージ取得先の指定

Examples:

```TOML
[dependencies]
# 独自レジストリ
some-crate = { version = "1.0", registry = "my-registry" }

# Gitロケーション
rand = { git = "https://github.com/rust-lang-nursery/rand" }
rand = { git = "https://github.com/rust-lang-nursery/rand", branch = "next" }

# ファイルシステム
hello_utils = { path = "hello_utils" }
```

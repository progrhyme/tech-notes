---
title: "シェル"
linkTitle: "シェル"
description: shell
date: 2020-05-10T18:04:56+09:00
simple_list: true
weight: 2000
---

## About

[シェルとは - IT用語辞典 e-Words](http://e-words.jp/w/%E3%82%B7%E3%82%A7%E3%83%AB.html)より:

> シェルとは、コンピュータのOSを構成するソフトウェアの一つで、利用者からの操作の受け付けや、利用者への情報の提示などを担当するもの

shやbashはシェルソフトウェア（シェルプログラムともいう）の例。

## ANSIエスケープシーケンス

ターミナルの出力文字に色や装飾を付けたりできる。

参考:

- [ANSIエスケープシーケンス チートシート - Qiita](https://qiita.com/PruneMazui/items/8a023347772620025ad6#%E5%87%BA%E5%8A%9B%E8%89%B2%E3%81%AE%E5%A4%89%E6%9B%B4)

## fish shell

https://fishshell.com/

> **Finally, a command line shell for the 90s**  
> fish is a smart and user-friendly command line shell for Linux, macOS, and the rest of the family.

使いやすいシェルとして人気のもの。

- C++ 実装
- POSIX **非互換**
- プラグイン機能がある

参考:

- [fish-shell でシェルの海をスイスイ泳いでみた | 株式会社ヌーラボ(Nulab inc.)](https://nulab.com/ja/blog/backlog/fish-shell-tutorial/)
- [fish shellが結構良かった話 - Qiita](https://qiita.com/hennin/items/33758226a0de8c963ddf)
- [シェル芸人のためのfish入門 - Qiita](https://qiita.com/kuwa72/items/f3a90fcd215938f5817e) ... Bashとの違いがわかりやすかった

### Getting Started

Install:

- https://fishshell.com/ の「Go fish」から

Documentation:

- https://fishshell.com/docs/current/
  - [Tutorial — fish-shell 3.1.2 documentation](https://fishshell.com/docs/current/tutorial.html)

### fisher

https://github.com/jorgebucaran/fisher

人気のパッケージ管理ツール。

See also [パッケージ管理#fish]({{<ref "/a/cli/shell/pkg-man.md">}}#fish)

Examples:

```sh
# oh-my-fishのテーマをfisherでインストール
fisher add oh-my-fish/theme-<テーマ名>
```

参考:

- [初心者がShellを知りFish〜Fisherを導入するまで - Qiita](https://qiita.com/nutsinshell/items/5f111184b50f7081c92f)
- [fisher v3 で変わったこと | Hi120kiのメモ](https://hi120ki.github.io/blog/posts/20190123/)

## Child Pages

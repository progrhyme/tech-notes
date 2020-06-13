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

## awesome-shell

https://github.com/alebcay/awesome-shell

> A curated list of awesome command-line frameworks, toolkits, guides and gizmos.

## ANSIエスケープシーケンス

ターミナルの出力文字に色や装飾を付けたりできる。

Examples:

```sh
# 太字
echo -e "Normal \e[1mBold\e[0m"
# 文字色、背景色変更
echo -e "Default \e[43m\e[31mRed text on Yellow background\e[0m"

# 256色対応
# - \e[38;5;文字色番号m
# - \e[48;5;背景色番号m
echo -e "Default \e[48;5;239m\e[38;5;93mPurple text on Gray background\e[0m"
```

コードの例:

 Code | 効果
------|------
 0 | Reset all attributes
 1 | Bold/Bright
 31 | Red text
 32 | Green text
 33 | Yellow text
 34 | Blue text
 35 | Magenta text
 36 | Cyan text

NOTE:

- BashやZshでは `$'\e[...m'` の[ANSI-C Quoting]({{<ref "/a/cli/shell/bash/_index.md">}}#ansi-c-quoting)を使わなければならないケースがあるかも。

参考:

- [ANSIエスケープシーケンス チートシート - Qiita](https://qiita.com/PruneMazui/items/8a023347772620025ad6)
- [bash:tip_colors_and_formatting - FLOZz' MISC](https://misc.flogisoft.com/bash/tip_colors_and_formatting)
- [Zsh#色: 256色対応]({{<ref "/a/cli/shell/zsh/_index.md">}}#色-256色対応)

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

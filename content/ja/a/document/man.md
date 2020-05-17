---
title: "man page"
linkTitle: "man page"
date: 2020-05-17T20:39:04+09:00
---

## はじめに

man pageはUnix系システムで広く使われるマニュアルページのフォーマットである。  
POSIXとLinuxではやや仕様が異なるようだ。

筆者はLinuxに馴染みが深いので、以下は基本的にLinuxについて記す。

参考:

- [POSIX 1003\.1 \- man page for man \(posix section 1P\) \- Unix & Linux Commands](https://www.unix.com/man-page/posix/1P/man/)

## CLI Usage

Examples:

```sh
man ls

## セクション番号を指定する
man 1 printf
man 3 printf
```

## ドキュメント

- http://man7.org/linux/man-pages/man1/man.1.html
- http://man7.org/linux/man-pages/man7/man-pages.7.html

## 仕様
### セクション番号とその意味

1. 実行可能プログラム、またはシェルコマンド
1. システムコール
1. ライブラリ関数
1. スペシャルファイル(/dev/ にある)
1. ファイルの書式や規約
1. ゲーム
1. 雑多なこと(マクロや規約を含む)
1. システム管理コマンド(通常はroot用)
1. カーネルルーチン ※非標準

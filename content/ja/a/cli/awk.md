---
title: "AWK"
linkTitle: "AWK"
date: 2020-06-23T22:49:24+09:00
weight: 10
---

## About

UNIX系OSでテキスト処理用途に用いられる。

プラットフォームによって実装が異なる。
https://en.wikipedia.org/wiki/AWK#Versions_and_implementations を参考に。

## Getting Started

参考:

- [Awk - A Tutorial and Introduction - by Bruce Barnett](https://www.grymoire.com/Unix/Awk.html#uh-0) ... NAWKとGAWKの違いについても述べられている

## Documentation

- [awk - pubs.opengroup.org](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/awk.html) ... POSIX
- [The GNU Awk User’s Guide](https://www.gnu.org/software/gawk/manual/gawk.html) ... gawk
  - 邦訳: [The GNU Awk User's Guide - Table of Contents](http://www.kt.rim.or.jp/~kbk/gawk-30/gawk_toc.html)
- https://linux.die.net/man/1/awk ... gawk

参考:

- [どの環境でも使えるシェルスクリプトを書くためのメモ ver4.60 - Qiita](https://qiita.com/richmikan@github/items/bd4b21cf1fe503ab2e5c#awk%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89)
- [AWK によるテキストのワンライナー処理クックブック集 - Qiita](https://qiita.com/key-amb/items/754a12eda28e7650a47c "AWK によるテキストのワンライナー処理クックブック集 - Qiita") ... 以前に自分でまとめたもの
- [awk | テキストのパターンマッチ処理に長けたスクリプト言語](https://bi.biopapyrus.jp/os/linux/awk.html)
- [AWK リファレンス | UNIX &amp; Linux コマンド・シェルスクリプト リファレンス](https://shellscript.sunone.me/awk.html)

## awkコマンド

```sh
# AWKスクリプトが短いとき
command-output-text | awk '{ AWK SCRIPT }'
awk '{ AWK SCRIPT }' INPUT_FILE1 INPUT_FILE2...

# AWKスクリプトが長いとき
command-output-text | awk -f scirpt.awk
awk -f scirpt.awk INPUT_FILE1 INPUT_FILE2...

# おまけ: AWKスクリプトが実行可能なとき
command-output-text | scirpt.awk
```

 Option | 機能
--------|------
 `-F<c>` | フィールドの区切り文字を `<c>` に変える。例: `-F,` でカンマ区切り
 `-v <KEY>=<VALUE>` | awkスクリプト内で使える変数を設定する。 `-v x=y` を繰り返すことで複数設定可

参考:

- [awkからシェル変数を参照する - Qiita](https://qiita.com/tkykmw/items/1622970830262355a5a3)

## スクリプティング

```awk
#!/usr/bin/awk -f

BEGIN { print "start" }
/<pattern>/ { print } # <pattern>マッチ時に行を出力
NR % 2 == 0 { print } # 偶数行を出力
            { print } # 無条件で出力
END   { print "end" }
```

Tips:

- `#` でコメントを書ける

NOTE:

- シバンに `#!/usr/bin/env awk -f` のように記すことはできない
  - See [CLI#シバン]({{<ref "/a/cli/_index.md">}}#シバン)

## 言語仕様

主にPOSIX仕様について記すが、今のところググった結果を貼り付けたものも混ざっている。

- ユーザ定義関数
  - [awk - POSIX#User-Defined Functions](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/awk.html#tag_20_06_13_15)

### 演算子

参考:

- [Let's AWK - aoki2.si.gunma-u.ac.jp](http://aoki2.si.gunma-u.ac.jp/Hanasi/Algo/letsawk/WhatIsOperator.html)

### 文字列の連結

単純にスペースでつなぐ。

```sh
awk '{print $1 "-" $2 "-" $3}' sample.tsv
```

参考:

- [awkの変数と文字列、正規表現のキホン - Qiita](https://qiita.com/tkykmw/items/89c67530c322baedb002 "awkの変数と文字列、正規表現のキホン - Qiita")

### 条件分岐

```awk
{
  if (a && b || c) {
    # ...
  } else if ($1 ~ /foo/) {
    # ...
  } else {
    # ...
  }
}
```

参考:

- [awkのif文のサンプルコード | ITを使っていこう](https://it-ojisan.tokyo/awk-if/)

### パターンマッチ

```awk
{
  regexp = ".*\.sh$"
  if (/^[abc]+/) { # $0 にマッチ
    # ...
  } else if ($1 ~ regexp) {
    # ...
  } else if (match($2, regexp)) {
    # ...
  }
}
```

### Statements
#### exit

[awk - POSIX#Actions](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/awk.html#tag_20_06_13_09)

ループ処理を中断してENDブロックに飛ぶ。

参考:

- [\[awk\] exit文でawkの実行処理を終了 - Qiita](https://qiita.com/kaw/items/329b524336e1400828b0)

### 文字列関数

[awk - POSIX#String Functions](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/awk.html#tag_20_06_13_13)

Tips:

- 関数引数が `$0` のときは省略できることが多いようだ

#### sub, gsub

```awk
sub(ere, repl[, in])
gsub(ere, repl[, in])
```

文字列置換を行う。  
in中のereという正規表現パターンをreplに置換する。  
repl内では `&` でマッチした文字列を参照できるみたい。  
inを省略した時には `$0` が対象になる。

subは最初に出現したパターンを1回だけ置換。  
gsubは出現した全パターンに置換を適用する。

参考:

- [awkの文字列置換関数gsub()の使い方 | ITを使っていこう](https://it-ojisan.tokyo/awk-gsub/)

## How-to
### ワンライナー

```sh
# マッチする行のみ表示
awk '/abc/' sample.tsv
# awk '/abc/ {print $0}' sample.tsv と同じ。以下同

# 偶数行だけを出力
awk 'NR % 2 == 0' sample.tsv

# N行目以降を出力
awk -v n=5 'NR > n' sample.tsv
```

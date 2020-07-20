---
title: "言語仕様"
linkTitle: "言語仕様"
description: |
  [awk - POSIX](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/awk.html)
date: 2020-07-21T00:20:42+09:00
---

主にPOSIX仕様について記すが、今のところググった結果を貼り付けたものも混ざっている。

## Specs

下に記載のないもの。

- ユーザ定義関数
  - [awk - POSIX#User-Defined Functions](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/awk.html#tag_20_06_13_15)

## 演算子

参考:

- [Let's AWK - aoki2.si.gunma-u.ac.jp](http://aoki2.si.gunma-u.ac.jp/Hanasi/Algo/letsawk/WhatIsOperator.html)

## Patterns

[awk - POSIX#Patterns](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/awk.html#tag_20_06_13_05)

AWKの基本構文である `<pattern> { <action> }` の `<pattern>` について。

種類:

- 単一のパターン
- 2つのパターンを `PATTERN1,PATTERN2` のようにカンマ区切りで記したレンジ
- 特殊パターン: `BEGIN`, `END`

### Expression Patterns

Booleanコンテキストで評価できる任意の表現を利用できる。  
（レコードが）真と評価されればマッチしたと見なされ、アクションが実行される。

Examples:

```AWK
NR < 3      { ... } # 1-2行目にマッチ
NR % 2 == 0 { ... } # 偶数行にマッチ
$2 == 'F'   { ... } # 第2フィールドが 'F' だったらマッチ
```

### Pattern Ranges

2つの評価式をカンマ区切りで記すことでレンジを表現する。

- 1つ目の条件にマッチした後、2つ目の条件にマッチするまでアクションが実行される
- 両端のレコード（1つ目と2つ目の条件に最初にマッチした行）もアクションの対象となる

Examples:

```AWK
NR==2,NR==5 { ... } # 2-5行目にマッチ
NR==3,/^$/  { ... } # 3行目から最初の空行までマッチ
```

## 制御構文

リファレンス:
- [awk#Expressions in awk](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/awk.html#tag_20_06_13_02)
- [awk#Actions](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/awk.html#tag_20_06_13_09)

if, elseのサンプル:

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

その他使える構文:

- for
- while, do ... while

Spec:

- 制御構文（break, continue含む）はC言語に由来している
  - See [Introduction#Concepts Derived from the ISO C Standard](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap01.html#tag_17_01_02)
- 真偽判定:
  - 数値の場合、0は偽、他は真
  - 文字の場合、ヌル文字は偽、他は真
- if, else等で実行される文が単文の場合、中括弧は省略可

参考:

- [awkのif文のサンプルコード | ITを使っていこう](https://it-ojisan.tokyo/awk-if/)

## Actions

[awk - POSIX#Actions](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/awk.html#tag_20_06_13_09)

### next

以降の処理を全て破棄して、次のレコードを処理する。  
他言語でもよくあるループ構文の `next` に似ている。

Examples:

```AWK
NR < 3 { next }  # 1-2行目は処理しない
/^#/   { sub("^# ?", ""); print; next } # "^# ?" を取り除いて出力し、次のレコードへ
       { exit }  # /^#/ にマッチしなくなったら終了
```

### exit

ループ処理を中断してENDブロックに飛ぶ。

参考:

- [\[awk\] exit文でawkの実行処理を終了 - Qiita](https://qiita.com/kaw/items/329b524336e1400828b0)

## 文字列関数

[awk - POSIX#String Functions](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/awk.html#tag_20_06_13_13)

Tips:

- 関数引数が `$0` のときは省略できることが多いようだ

### sub, gsub

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

## 文字列操作
### 文字列の連結

単純にスペースでつなぐ。

```sh
awk '{print $1 "-" $2 "-" $3}' sample.tsv
```

参考:

- [awkの変数と文字列、正規表現のキホン - Qiita](https://qiita.com/tkykmw/items/89c67530c322baedb002 "awkの変数と文字列、正規表現のキホン - Qiita")

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

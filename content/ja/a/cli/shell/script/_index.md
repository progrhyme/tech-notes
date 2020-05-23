---
title: "シェルスクリプト"
linkTitle: "スクリプト"
description: shell scripts
date: 2020-05-04T14:49:53+09:00
weight: 2000
---

関連ページ:

- [Bash > Cookbooks]({{< ref "/a/cli/shell/bash/cookbook.md" >}})

NOTE:

- BashのことはなるべくBashのページに書こうと思うが、調査が甘くてBashじゃないと動かないコードがここに書かれることもあるかもしれない。

## About

シェル上で動作する簡易なプログラミング言語、あるいはそれによって書かれたプログラム。

参考:

- [シェルスクリプトとは - IT用語辞典 e-Words](http://e-words.jp/w/%E3%82%B7%E3%82%A7%E3%83%AB%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%97%E3%83%88.html)

## Getting Started
### リファレンス

- [POSIX 1003.1 - man page for sh (posix section 1p) - Unix & Linux Commands](http://www.unix.com/man-page/posix/1p/sh/)
- [CONTENTS - Shell & Utilities: Detailed TOC | The Open Group](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/contents.html)
  - [Shell Command Language](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18)
- [Shell Command Language (www.unix.org))](http://www.unix.org/whitepapers/shdiffs.html)
  - System V や POSIX の古典的な仕様がまとまってるっぽい雰囲気

### コーディング規約

- [Shell Style Guide](https://google.github.io/styleguide/shell.xml "Shell Style Guide") ... Google の
  - 参考: [Googleの肩に乗ってShellコーディングしちゃおう - Qiita](http://qiita.com/laqiiz/items/5f72ca668f1c58176644 "Googleの肩に乗ってShellコーディングしちゃおう - Qiita")

### 入門サイトなど

- [UNIX & Linux コマンド・シェルスクリプト リファレンス](https://shellscript.sunone.me/)
- [シェルスクリプト入門 書き方のまとめ | Memo on the Web](http://motw.mods.jp/shellscript/tutorial.html)
- [シェルスクリプトの基礎知識まとめ - Qiita](https://qiita.com/katsukii/items/383b241209fe96eae6e7)

## Spec
### パラメータと変数
#### Parameter Expansion

[Shell Command Language#2.6.2 Parameter Expansion](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_06_02)

`${expression}` こういうやつ。最もシンプルなのは `${parameter}` とそのままブレースで囲むだけ。

種類:

- `${#parameter}` ... 文字列の長さを表す

参考:

- [【 文字列の長さを調べる 】 | 日経クロステック（xTECH）](https://xtech.nikkei.com/it/article/COLUMN/20060228/231152/)

### 演算子

NOTE:
- `[ 条件式 ]` は `test 条件式` と同じ。
  - See [test](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/test.html)

ドキュメント:

- [Bash Reference Manual](https://tiswww.case.edu/php/chet/bash/bashref.html#Bash-Conditional-Expressions)

参考:

- [シェルスクリプト（bash）のif文やwhile文で使う演算子について - Qiita](https://qiita.com/egawa_kun/items/196cd354c0d8e4e0fefc)

#### 単項条件演算子

 演算子 | 真の条件
-------|---------
 -v VAR | 変数VARが定義されている。※ `-v $VAR` ではない
 -n $str | $str に長さ1以上の文字列が入っている
 -z $str | $str が空文字
 -x $path | $path が実行可能ファイル
 -L $path | $path がシンボリックリンク
 -S $path | $path がソケット

参考:

- [&lt;Bash, zsh&gt; シェル変数が定義されているかを判定する方法 - ねこゆきのメモ](http://nekoyukimmm.hatenablog.com/entry/2018/01/21/101828)

#### 二項条件演算子

 構文 | 真の条件
-----|---------
 "$str1" = "$str2" | $str1と$str2が等しい
 "$str1" != "$str2" | $str1と$str2が等しくない
 $x -eq $y | 数値$xと$yが等しい
 $x -ne $y | 数値$xと$yが等しくない
 $x -gt $y | 数値$xが$yより大きい
 $x -lt $y | 数値$xが$yより小さい
 $x -ge $y | 数値$xが$y以上
 $x -le $y | 数値$xが$y以下
 $path1 -nt $path2 | $path1 のタイムスタンプが $path2 より新しい
 $path1 -ot $path2 | $path1 のタイムスタンプが $path2 より古い

### ループ

```sh
## 無限ループ
while true; do
  if true; then
    continue # 後続の処理をスキップして次の周回へ
  else
    :
  fi
  :
done

## イテレータでループ
for i in $(get_some_list); do
  :
done
```

参考:

- [【 次の繰り返しに移る「continue」 】 | 日経クロステック（xTECH）](https://xtech.nikkei.com/it/article/COLUMN/20060228/231135/)

### case構文

[Shell Command Language#Case Conditional Construct](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_09_04_05)

構文:

```sh
case 値 in
  パターン1 ) 処理1 ;;
  パターン2 ) 処理2 ;;
  パターン3 ) 処理3 ;;
  …
  パターンn ) 処理n ;;
esac
```

NOTE:

- シェルの[パターンマッチ](#パターンマッチ)を使うこともできる

参考:

- [case 文の使用方法 | UNIX &amp; Linux コマンド・シェルスクリプト リファレンス](https://shellscript.sunone.me/case.html)

### パターンマッチ

[Shell Command Language#2.13. Pattern Matching Notation](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_13)

 パターン | マッチ文字列
----------|--------------
 `?` | 任意のアスキー1字
 `*` | ヌル文字を含む任意の文字列
 `[` | `[...]` で `[]` 内の任意の1字にマッチする

### Parameter Expansion

- https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_06_02

Examples:

```sh
parameter=${parameter:-word}
if [ -z ${var+x} ]; then echo "var is unset"; else echo "var is set to '$var'"; fi
```

参考:

- [shell - How to check if a variable is set in Bash? - Stack Overflow](https://stackoverflow.com/questions/3601515/how-to-check-if-a-variable-is-set-in-bash)

## Built-Ins
### . (dot)

https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_18

### : (colon)

null utility

- https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_16
- Bash: https://tiswww.case.edu/php/chet/bash/bashref.html#Bourne-Shell-Builtins

何もしないコマンド

### return

関数かdot scriptを終了する

https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_24

Examples:

```sh
return 0
# 0以外だと異常終了扱い
return 1

# 引数省略時は最後のコマンドのexit statusになる
return
```

参考:

- [シェルスクリプト return コマンド - Qiita](https://qiita.com/blueskyarea/items/805c0aa4b1cbba11818a)
- https://github.com/progrhyme/experiments/tree/master/bash/source-scripts

### unset

https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_29

Examples:

```sh
# シェル変数または環境変数を削除
unset [-v] FOO
# 関数名を削除
unset -f my_func
```

参考:

- [【 unset 】コマンド――変数や関数を削除する：Linux基本コマンドTips（307） - ＠IT](https://www.atmarkit.co.jp/ait/articles/1905/24/news015.html)
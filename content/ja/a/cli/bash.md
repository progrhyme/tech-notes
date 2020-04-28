---
title: "Bash"
linkTitle: "Bash"
description: >
  [GNU Bash](https://www.gnu.org/software/bash/)
date: 2020-04-28T09:14:42+09:00
weight: 100
---

## Getting Started

入門コンテンツ:

- [Introduction to Bash](http://cs.lmu.edu/~ray/notes/bash/)
- [bash 入門 - se.cite.ehime-u.ac.jp](http://se.cite.ehime-u.ac.jp/~aman/memo/bash/)
- [bash 入門 - rat.cis.k.hosei.ac.jp](https://rat.cis.k.hosei.ac.jp/article/linux/bash_intro.html)

コーディング規約:

- [Shell Style Guide](https://google.github.io/styleguide/shell.xml) ... Google
- [bashコーディング規約参考 - Qiita](https://qiita.com/Bopllq0916/items/eeb1b8e2cfe386c4f64f)

## Documents

### 公式

- [Man page of BASH](http://linuxjm.osdn.jp/html/GNU_bash/man1/bash.1.html "Man page of BASH")
- [Bash Reference Manual](https://tiswww.case.edu/php/chet/bash/bashref.html "Bash Reference Manual")
- CHANGES: https://tiswww.case.edu/php/chet/bash/CHANGES
- リリースノート的なもの: https://tiswww.case.edu/php/chet/bash/NEWS

### 非公式

- [Bash changes [Bash Hackers Wiki]](http://wiki.bash-hackers.org/scripting/bashchanges "Bash changes [Bash Hackers Wiki]")
- ★[Bash scripting](http://iishikawa.s371.xrea.com/note/bash-script.html) ... 便利な Bash の小技いろいろ
- [bash 配列まとめ - Qiita](http://qiita.com/b4b4r07/items/e56a8e3471fb45df2f59)
  - 配列の操作いろいろ

プロンプトについて:

- [PS1とPROMPT_COMMAND, GNU screenでの活用も](http://rcmdnk.github.io/blog/2013/03/21/prompt-command/)


## bashコマンド

Examples:

```bash
bash -n script.sh # シンタックスチェック
```

参考:

- [シェルスクリプトのlint - Qiita](https://qiita.com/dharry/items/f593d96c1b0269182922)

## Features
### リダイレクト

Qiitaにまとめを書いた:

- [Bashの入出力リダイレクトまとめ - Qiita](https://qiita.com/progrhyme/items/e99be732c2e62d4a7641)

参考:

- [bash: 標準出力、標準エラー出力をファイル、画面それぞれに出力する方法 - Qiita](https://qiita.com/laikuaut/items/e1cc312ffc7ec2c872fc)
- [覚えてると案外便利なBashのリダイレクト・パイプの使い方9個 | 俺的備忘録 〜なんかいろいろ〜](https://orebibou.com/2016/02/%E8%A6%9A%E3%81%88%E3%81%A6%E3%82%8B%E3%81%A8%E6%A1%88%E5%A4%96%E4%BE%BF%E5%88%A9%E3%81%AAbash%E3%81%AE%E3%83%AA%E3%83%80%E3%82%A4%E3%83%AC%E3%82%AF%E3%83%88%E3%83%BB%E3%83%91%E3%82%A4%E3%83%97/)

### ヒアドキュメント

※POSIX標準ではないか。少なくともkshでは動かなさそう。

Examples:

```bash
cat << EOS > cat.out
foo
  bar
    baz
EOS

BODY="$(cat << EOS
Dear Ken,

I'm so happy to write this message.
I'll be back soon!
EOS
)"
```

ヒアドキュメントは文字列リテラルではなく、標準入力らしい。

参考:

- [bashのヒアドキュメントを活用する - Qiita](https://qiita.com/take4s5i/items/e207cee4fb04385a9952 "bashのヒアドキュメントを活用する - Qiita")


### 正規表現

POSIXか、EREなのだと思う。

SYNOPSIS:

```bash
if [[ "$str" =~ ^ba*r$ ]]; then
  echo match
end

## マッチしないことの検査
if [[ ! "$str" =~ ^ba*r$ ]]; then
  echo not match
end
```

参考:

- https://sites.google.com/site/progrhymetechwiki/program/regexp
- [case 文の使用方法 | UNIX & Linux コマンド・シェルスクリプト リファレンス](http://shellscript.sunone.me/case.html)
- [[Bash]正規表現マッチした部分文字列を再利用する方法 · DQNEO起業日記](http://dqn.sakusakutto.jp/2013/06/bash_rematch_regexp.html "[Bash]正規表現マッチした部分文字列を再利用する方法 · DQNEO起業日記")
- [bashでif に正規表現を使った文字列マッチ条件分岐 - それマグで！](http://takuya-1st.hatenablog.jp/entry/2016/12/22/175514)

## Cookbooks
### 論理演算

```bash
((2 > 1)) # $? => 0
((1 > 1)) # $? => 1
(($(seq 1 3 | wc -w) > 2)) # $? => 0

if true; then echo ok; fi #=> ok
```

## How-to

### プロンプト(PS1)の変更

カスタマイズしたくなったときに見るページ:
- [bashのプロンプトを変更するには](http://www.atmarkit.co.jp/flinux/rensai/linuxtips/002cngprmpt.html "bashのプロンプトを変更するには")
- [Linuxで、bash プロンプトを素敵で実用的なものに変更する](https://jp.linux.com/news/linuxcom-exclusive/416957-lco20140519 "Linuxで、bash プロンプトを素敵で実用的なものに変更する")


### 文字列削除

以下、 [Bash scripting](http://iishikawa.s371.xrea.com/note/bash-script.html#idm2045339272) より。

- `${var%pattern}` … 後方からパターンの最短マッチを削除
- `${var%%pattern}` … 後方からパターンの最長マッチを削除
- `${var#pattern}` … 前方からパターンの最短マッチを削除
- `${var##pattern}` … 前方からパターンの最長マッチを削除

パスからディレクトリ名やファイル名を取り出すのによく使う。

```bash
fullpath=/a/b/c.txt
echo ${fullpath##*/} # c.txt
echo ${fullpath%/*} # /a/b
filename=d.e.txt
echo ${filename%.*} # d.e
echo ${filename##*.} # txt
```

たぶん、Bash に限らず POSIX で使える。  
下に載ってる。

http://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_06_02

### 文字列置換

- `${var/x/y}` ... `$var` 文字列の `x` を `y` に置換（1回のみ）
- `${var//x/y}` ... `$var` 文字列の `x` を `y` に置換（全てマッチ）

参考: [bashの変数をsplitして配列を作る方法: 小粋空間](http://www.koikikukan.com/archives/2019/05/09-235555.php)


### 文字列の部分切り出し

```bash
$ echo $str
1234567890

$ echo ${str:3:4}
4567
```

参考:

- [シェルスクリプトで部分文字列を切り出す - 理系学生日記](http://kiririmode.hatenablog.jp/entry/20170913/1505228400)


### 複数行のコメントアウト

`:` とヒアドキュメントを組み合わせる。

```sh
: << "__EOCOMMENT__"

コメントアウトしたいコード

__EOCOMMENT__
```

参考:

- [bashで複数行コメントアウトする方法 - Qiita](https://qiita.com/imura81gt/items/a2998147bd7ae8056b26 "bashで複数行コメントアウトする方法 - Qiita")

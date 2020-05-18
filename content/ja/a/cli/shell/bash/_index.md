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

- [Bash prompt basics - LinuxConfig.org](https://linuxconfig.org/bash-prompt-basics)
- [PS1とPROMPT_COMMAND, GNU screenでの活用も](http://rcmdnk.github.io/blog/2013/03/21/prompt-command/)

## bashコマンド

Examples:

```bash
bash -n script.sh # シンタックスチェック
```

参考:

- [シェルスクリプトのlint - Qiita](https://qiita.com/dharry/items/f593d96c1b0269182922)

## Syntax
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

### ANSI-C Quoting

https://tiswww.case.edu/php/chet/bash/bashref.html#ANSI_002dC-Quoting

`$'string'` 形式のもの。ユニコードとかエスケープシーケンスで使える。

Examples:

```sh
echo $'\e[031mThis text will be colored Red.\e[0m'
echo $'\U25c0'
```

## How-to
### プロンプト(PS1)の変更

`PS1` 変数を設定する。

Examples:

```sh
PS1="\[\e[1;34m\][\u@\h \W]\\$ \[\e[m\]"
```

 特殊文字 | 内容
--------|------
 \u | 現在のユーザ名
 \h | ホスト名（ドメイン部除く）
 \w | カレントディレクトリ（ホームディレクトリからの絶対パス）

参考（カスタマイズしたくなったときに見るページ）:

- [bashのプロンプトを変更するには](http://www.atmarkit.co.jp/flinux/rensai/linuxtips/002cngprmpt.html "bashのプロンプトを変更するには")
- [Linuxで、bash プロンプトを素敵で実用的なものに変更する](https://jp.linux.com/news/linuxcom-exclusive/416957-lco20140519 "Linuxで、bash プロンプトを素敵で実用的なものに変更する")
- [BashでPromptの色を変更する方法 - Qiita](https://qiita.com/wildeagle/items/5da17e007e2c284dc5dd)

---
title: "シェルスクリプト"
linkTitle: "スクリプト"
description: shell scripts
date: 2020-05-04T14:49:53+09:00
weight: 2000
---

関連ページ:

- [Bash > Cookbooks]({{< ref "/a/cli/shell/bash/cookbook.md" >}})

## About

シェル上で動作する簡易なプログラミング言語、あるいはそれによって書かれたプログラム。

参考:

- [シェルスクリプトとは - IT用語辞典 e-Words](http://e-words.jp/w/%E3%82%B7%E3%82%A7%E3%83%AB%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%97%E3%83%88.html)

## Getting Started
### リファレンス

- [POSIX 1003.1 - man page for sh (posix section 1p) - Unix & Linux Commands](http://www.unix.com/man-page/posix/1p/sh/)
- [Shell Command Language (www.unix.org))](http://www.unix.org/whitepapers/shdiffs.html)
  - System V や POSIX の古典的な仕様がまとまってるっぽい雰囲気
- [Shell Command Language (pubs.opengroup.org)](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html) ... 上と同じ内容のようだ

### コーディング規約

- [Shell Style Guide](https://google.github.io/styleguide/shell.xml "Shell Style Guide") ... Google の
  - 参考: [Googleの肩に乗ってShellコーディングしちゃおう - Qiita](http://qiita.com/laqiiz/items/5f72ca668f1c58176644 "Googleの肩に乗ってShellコーディングしちゃおう - Qiita")

### 入門サイトなど

- [UNIX & Linux コマンド・シェルスクリプト リファレンス](https://shellscript.sunone.me/)
- [シェルスクリプト入門 書き方のまとめ | Memo on the Web](http://motw.mods.jp/shellscript/tutorial.html)
- [シェルスクリプトの基礎知識まとめ - Qiita](https://qiita.com/katsukii/items/383b241209fe96eae6e7)

## Spec
### 演算子

参考:

- [シェルスクリプト（bash）のif文やwhile文で使う演算子について - Qiita](https://qiita.com/egawa_kun/items/196cd354c0d8e4e0fefc)

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
### `:` (colon)

- https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#colon
- Bash: https://tiswww.case.edu/php/chet/bash/bashref.html#Bourne-Shell-Builtins

何もしないコマンド

## How-to
### ユーザー入力を受け付ける

`read` を使う。

```sh
echo -n "Are you sure? (y/N) "
read answer
if [[ "$answer" != "y" ]]; then
  echo "Canceled."
  exit
fi
```

参考:

- [【Linux】シェルスクリプトでキーボード入力を受付ける方法](https://eng-entrance.com/linux-shellscript-keyboard)

### コマンドの出力結果にタイムスタンプをつける

```sh
do_something | while IFS= read -r line; do echo "$(date) $line"; done
```

参考:

- [linux - How to add a timestamp to bash script log? - Server Fault](https://serverfault.com/questions/310098/how-to-add-a-timestamp-to-bash-script-log "linux - How to add a timestamp to bash script log? - Server Fault")

## Topics
### オプション解析

シェルスクリプトでコマンドラインオプションをどう解析するか。

参考:

- [bash によるオプション解析 - Qiita](http://qiita.com/b4b4r07/items/dcd6be0bb9c9185475bb)
  - getopts, getopt, 自前解析のメリット・デメリット。自前解析推し
- [Example of how to parse options with bash/getopt](https://gist.github.com/cosimo/3760587)

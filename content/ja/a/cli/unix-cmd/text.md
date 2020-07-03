---
title: "テキスト処理"
linkTitle: "テキスト処理"
date: 2020-07-03T16:21:13+09:00
weight: 2400
---

## cut

テキストフィルタツール

```sh
# タブ区切りで1, 3つめのフィールドを取得
cat file.txt | cut -f 1,3
# カンマ区切り
cat file.txt | cut -d, -f 1,3
# バイト単位で10-20バイト目を取得
cat file.txt | cut -b10-20
```

## grep

```bash
## ファイル名だけ表示
grep -l PATTERN [PATH]
```

## head

https://linuxjm.osdn.jp/html/GNU_textutils/man1/head.1.html

```sh
## 先頭1行を表示
head -1 [file...]
## 先頭20行を表示
head -n 20 [file...]

## 先頭256Bを表示
head -c 256 [file...]
## 先頭256KBを表示
head --bytes 256k [file...]
```

## printf(1)

書式を指定して文字列を標準出力に出力。

シェルのビルトイン関数と /usr/bin/printf がある。
違いはよくわからない。

```sh
printf "%s %02d" foo 1
#=> foo 01
env LANG=ja_JP.UTF-8 printf "%'d" 1234567890
#=> 1,234,567,890
```

参考:

- [【 printf 】コマンド――データを整形して表示する：Linux基本コマンドTips（319） - ＠IT](https://www.atmarkit.co.jp/ait/articles/1907/05/news012.html)
- [シェルスクリプトで数字を３桁ごとのカンマ区切りにする](https://blog.cles.jp/item/5819)

## sed

https://linuxjm.osdn.jp/html/GNU_sed/man1/sed.1.html

与えられたテキストに対して、sedスクリプトで指定された文字列置換を行って結果のテキストを表示するストリームエディタ。

macOSとLinuxで挙動が違うので、注意が必要。

Examples:

```sh
# 各行のxを1つyに置換した結果を表示
sed s/x/y/ foo.txt
# 各行のxをすべてyに置換した結果を表示
sed -e s/x/y/g foo.txt
# 全文字をすべてyに置換した結果を表示
cat foo.txt | sed 's/./y/g'
# xをyに、aをbに置換
sed -e s/x/y/ -e s/a/b/ foo.txt
```

 オプション | 効果
----------|------
 --[e]xpression=SCRIPT | 実行するコマンドとしてスクリプトを追加
 --[f]ile=FILE | 実行するコマンドとしてスクリプトファイルを追加
 --[r]egexp-extended | （※Linux）拡張正規表現を使う
 -E | （※macOS）拡張正規表現を使う

※ `-e`, `-f` のどちらの指定もなければ、最初のオプションでない引数がsedスクリプトとして解釈される。

## sort

```bash
## 第2フィールドで数値の降順ソート
cat file | sort -nr -k2
```

参考:

- https://linuxjm.osdn.jp/html/gnumaniak/man1/sort.1.html
- [sort コマンド | コマンドの使い方(Linux) | hydroculのメモ](https://hydrocul.github.io/wiki/commands/sort.html "sort  コマンド | コマンドの使い方(Linux) | hydroculのメモ")

---
title: "Cookbooks"
linkTitle: "Cookbooks"
description: >
  スクリプティングのための応用的なコードスニペット集っぽいもの。
  基本的な文法機能の解説は[シェルスクリプト](../)の方に書く。
date: 2020-05-21T22:21:53+09:00
---

See Also:

- [Bash > Cookbooks]({{< ref "/a/cli/shell/bash/cookbook.md" >}})

## ユーザー入力を受け付ける

`read` を使う。

```sh
echo -n "Are you sure? (y/N) "
read answer
if [ "$answer" != "y" ]; then
  echo "Canceled."
  exit
fi
```

参考:

- [【Linux】シェルスクリプトでキーボード入力を受付ける方法](https://eng-entrance.com/linux-shellscript-keyboard)

## コマンドの出力結果にタイムスタンプをつける

```sh
do_something | while IFS= read -r line; do echo "$(date) $line"; done
```

参考:

- [linux - How to add a timestamp to bash script log? - Server Fault](https://serverfault.com/questions/310098/how-to-add-a-timestamp-to-bash-script-log "linux - How to add a timestamp to bash script log? - Server Fault")

## OSの判別

参考:

- [シェルスクリプトでOSを判別する - Qiita](https://qiita.com/UmedaTakefumi/items/fe02d17264de6c78443d)

## 絵文字を使う

1. 絵文字のユニコードを探す
1. `U+1F3A3` だったら `\U1F3A3` とする

4桁だったら小文字のuで、 `\u2122` としてもいいっぽい。

絵文字を探すには http://www.fileformat.info/info/emoji/list.htm とか https://emojipedia.org/ を使うといい。

参考:

- [シェル上で🍣🍣（Unicode絵文字）を表示させる - Qiita](https://qiita.com/nyango/items/671a14ae2834c045fe27)

## シェル関数が定義されているか調べる

コマンド同様に、 `which function` or `command -v function` で取れる。  
`test -v function` ではNG.

## 数字を3桁ずつカンマ区切りで出力

See [UNIX系コマンド#printf(1)]({{<ref "/a/cli/unix-cmd/_index.md">}}#printf1)

## オプション解析

シェルスクリプトでコマンドラインオプションをどう解析するか。

参考:

- [bash によるオプション解析 - Qiita](http://qiita.com/b4b4r07/items/dcd6be0bb9c9185475bb)
  - getopts, getopt, 自前解析のメリット・デメリット。自前解析推し
- [Example of how to parse options with bash/getopt](https://gist.github.com/cosimo/3760587)

## sourceされたスクリプト内でファイル自身のパスを取得

Bash / Zsh両対応:

```sh
script_dir=$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)
```

参考:

- [bash/zshでsourceされたスクリプト内で、ファイル自身の絶対パスをとるシンプルな記法 - Qiita](https://qiita.com/yudoufu/items/48cb6fb71e5b498b2532)

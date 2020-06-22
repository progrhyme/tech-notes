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

## Documentation Comments

ドキュメントコメントの書き方には標準がない感じ。  
たぶん一番有名なのは[Googleコーディング規約](https://google.github.io/styleguide/shellguide.html#s4.1-file-header)。

「shdoc」や「shelldoc」で検索すると、色んな人が様々なツールを作っている。

使えそうなツール:

 ツール | 実装言語 | 出力形式
--------|----------|----------
 [reconquest/shdoc](https://github.com/reconquest/shdoc) | AWK | Markdown
 [essentialkaos/shdoc](https://github.com/essentialkaos/shdoc) | Go | Text/Markdown/HTML
 [RoverAMD/shelldoc](https://gitlab.com/RoverAMD/shelldoc) | Bash | Markdown
 [shdoc in jmcantrell/bashful](https://github.com/jmcantrell/bashful/blob/master/bin/shdoc) | Bash | Text
 [larsks/shdoc](https://github.com/larsks/shdoc) | Python | 任意 (Jinja2)

参考:

- [2020-05-09#シェルスクリプトのドキュメントコメントをPODで書くのはもうやめていいかな]({{<ref "20200509.md">}}#シェルスクリプトのドキュメントコメントをpodで書くのはもうやめていいかな)

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

## Child Pages

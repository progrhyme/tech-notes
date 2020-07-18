---
title: "シェルスクリプト"
linkTitle: "スクリプト"
description: shell scripts
date: 2020-05-04T14:49:53+09:00
weight: 2000
---

関連ページ:

- [POSIXシェル]({{<ref "/a/cli/shell/posix.md">}})
- [Bash > Cookbooks]({{< ref "/a/cli/shell/bash/cookbook.md" >}})

## About

シェル上で動作する簡易なプログラミング言語、あるいはそれによって書かれたプログラム。

参考:

- [シェルスクリプトとは - IT用語辞典 e-Words](http://e-words.jp/w/%E3%82%B7%E3%82%A7%E3%83%AB%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%97%E3%83%88.html)

## Getting Started
### コーディング規約

- [Shell Style Guide](https://google.github.io/styleguide/shell.xml "Shell Style Guide") ... Google の
  - 参考: [Googleの肩に乗ってShellコーディングしちゃおう - Qiita](http://qiita.com/laqiiz/items/5f72ca668f1c58176644 "Googleの肩に乗ってShellコーディングしちゃおう - Qiita")

### 入門サイトなど

- [UNIX & Linux コマンド・シェルスクリプト リファレンス](https://shellscript.sunone.me/)
- [シェルスクリプト入門 書き方のまとめ | Memo on the Web](http://motw.mods.jp/shellscript/tutorial.html)
- [シェルスクリプトの基礎知識まとめ - Qiita](https://qiita.com/katsukii/items/383b241209fe96eae6e7)

## テスト

シェルスクリプトのテストフレームワークは意外とけっこうある。

 Software | 対応シェル
----------|------------
 [Bats](https://github.com/bats-core/bats-core) | Bash
 [shUnit2](https://github.com/kward/shunit2) | POSIX互換シェル
 [bash_unit](https://github.com/pgrange/bash_unit) | Bash
 [ShellSpec](https://shellspec.info/) | POSIX互換シェル
 [rylnd/shpec](https://github.com/rylnd/shpec) | POSIX準拠シェル
 [progrhyme/shove](https://github.com/progrhyme/shove) | POSIX互換シェル
 [ZUnit](https://zunit.xyz/) | Zsh

参考:

- [dodie/testing-in-bash: Bash test framework comparison 2020](https://github.com/dodie/testing-in-bash)
- [&quot;shove&quot; というシェルスクリプト用のテストツールを作った - weblog of key_amb](https://keyamb.hatenablog.com/entry/shove-release-v0.7)

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

- [シェルスクリプトの説明をコメントで書いてコマンドラインでヘルプとして表示する - Qiita](https://qiita.com/progrhyme/items/073dbf58844caa0e4b5c)
- [2020-05-09#シェルスクリプトのドキュメントコメントをPODで書くのはもうやめていいかな]({{<ref "20200509.md">}}#シェルスクリプトのドキュメントコメントをpodで書くのはもうやめていいかな)

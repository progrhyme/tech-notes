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

- [Bats](https://github.com/bats-core/bats-core)
- [shUnit2](https://github.com/kward/shunit2)
- [bash_unit](https://github.com/pgrange/bash_unit)
- [ShellSpec](https://shellspec.info/)
- [rylnd/shpec](https://github.com/rylnd/shpec)
- [progrhyme/shove](https://github.com/progrhyme/shove)

参考:

- [dodie/testing-in-bash: Bash test framework comparison 2020](https://github.com/dodie/testing-in-bash)
- [&quot;shove&quot; というシェルスクリプト用のテストツールを作った - weblog of key_amb](https://keyamb.hatenablog.com/entry/shove-release-v0.7)

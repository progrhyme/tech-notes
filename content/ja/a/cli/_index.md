---
title: "CommandLine Interface"
linkTitle: "CLI"
description:
  コマンドラインツールなど
date: 2020-04-27T19:34:20+09:00
weight: 400
---

シェルソフトウェアやシェルスクリプトについてもこのセクションで扱う。  
ターミナルソフトウェアについては[Software > ターミナル]({{< ref "/a/software/terminal/_index.md" >}})を見よ。

## リファレンス

- [SS64 Command line reference](https://ss64.com/) ... Linux, macOS etc.
  - macOSのmanはやや古いかも。不備が散見される

## シバン

- 英語表記 ... shebang, shbang
- 日本語 ... シェバンとも

UNIX系OSで、実行スクリプトの先頭に書かれる `#!` で始まる行のこと。  
ここにはふつう、インタプリタの絶対パスを書く。

あるいは、 `env` コマンドを用いた `#!/usr/bin/env bash` のような表記もよく用いられる。

参考:

- [シバン (Unix) - Wikipedia](https://ja.wikipedia.org/wiki/%E3%82%B7%E3%83%90%E3%83%B3_(Unix))
- [Shebang集 - Qiita](https://qiita.com/cielavenir/items/6063c117f25f9188b84c#awk)

### 制約

envコマンドは普通、複数引数を取ることができない。  
例えば、Ubuntu v18で `#!/usr/bin/env awk -f` のようにすると、下のようなエラーが出る:

```sh
$ cat foo.txt | test.awk
/usr/bin/env: `awk -f': そのようなファイルやディレクトリはありません`
```

そのため、引数を渡したくなったら、 `#!/path/to/interpreter ARGS` の形にすることになりそう。

NOTE:

- BSD系OSだと複数引数取れるっぽい

参考:

- [shell - Invoking a script, which has an awk shebang, with parameters (vars) - Stack Overflow](https://stackoverflow.com/questions/1418245/invoking-a-script-which-has-an-awk-shebang-with-parameters-vars)
- [scripting - Shebang line with `#!/usr/bin/env command --argument` fails on Linux - Unix &amp; Linux Stack Exchange](https://unix.stackexchange.com/questions/63979/shebang-line-with-usr-bin-env-command-argument-fails-on-linux)

## direnv

https://github.com/direnv/direnv

Documentation:

- [Installation](https://github.com/direnv/direnv/blob/master/docs/installation.md)
  - macOSはHomebrewを使える
  - Ubuntuはaptかsnapで入れられる
- [Setup](https://github.com/direnv/direnv/blob/master/docs/hook.md)
  - Bash: `eval "$(direnv hook bash)"` をbashrcに書く
  - Zsh: `eval "$(direnv hook zsh)"` をzshrcに書く

## ロギング
### script

参考:

- [scriptコマンドで作業ログを記録 ｜ DevelopersIO](https://dev.classmethod.jp/server-side/os/scriptcommand/)

## How-to
### ターミナルでEOFを入力する方法

- Unix系OS: `Ctrl-D`
- Windows: `Ctrl-Z`

参考:

- [EOFを入力する - にたまごほうれん草アーカイブ](https://nitamago-archive.hatenablog.com/entry/20071230/1198945951)

## 用語
### TTY

[TTY（テレタイプ端末）とは - IT用語辞典 e-Words](http://e-words.jp/w/TTY.html)より:

> 利用者が入力した文字を別の機器に送信したり、別の機器から受信した文字情報を利用者に提示したりする機能を持った端末やソフトウェアのこと

元々はteletypewriterの略。  
Linuxだと `tty` コマンドで標準入出力デバイスの名前を表示できる。

## Child Pages

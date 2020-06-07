---
title: "CommandLine Interface"
linkTitle: "CLI"
description:
  コマンドラインツールなど
date: 2020-04-27T19:34:20+09:00
simple_list: true
weight: 400
---

シェルソフトウェアやシェルスクリプトについてもこのセクションで扱う。  
ターミナルソフトウェアについては[Software > ターミナル]({{< ref "/a/software/terminal/_index.md" >}})を見よ。

## リファレンス

- [SS64 Command line reference](https://ss64.com/) ... Linux, macOS etc.
  - macOSのmanはやや古いかも。不備が散見される

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

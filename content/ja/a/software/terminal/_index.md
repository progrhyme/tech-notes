---
title: "ターミナルソフトウェア"
linkTitle: "ターミナル"
date: 2020-05-13T22:23:41+09:00
weight: 2400
---

端末エミュレータ、ターミナルエミュレータなどとも呼ばれる。

## macOS

- ターミナル.app ... 標準でインストールされている端末アプリ
- [iTerm2]({{<ref "iterm2.md">}})

## Topics
### 色

参考:

- [256 Colors - Cheat Sheet - Xterm, HEX, RGB, HSL](https://jonasjacek.github.io/colors/)
- [TrueColor対応のはなし(端末、シェル、tmux、vim) - Panda Noir](https://www.pandanoir.info/entry/2019/11/02/202146)

#### 環境変数

UNIX系OSで端末の色に関する環境変数:

- `COLORTERM` ... `truecolor` など
- `TERM` ... `xterm-256color` など

NOTE:

- tmuxやscreenを使うと、 `TERM` 設定が書き換えられて色表示がおかしくなることがある

## Child Pages

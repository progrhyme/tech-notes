---
title: "tmux"
linkTitle: "tmux"
description: https://github.com/tmux/tmux/wiki
date: 2020-07-03T11:32:53+09:00
weight: 800
---

## About

OSSのターミナルマルチプレクサ。

- ソースコード: https://github.com/tmux/tmux

## Documentation

- https://man.openbsd.org/tmux.1

## Configuration

デフォルトの設定ファイルパスは `~/.tmux.conf`

```
# ログバッファの上限を上げる。デフォルト 2000
set-option -g history-limit 10000

# 256色対応
set-option -g default-terminal screen-256color
```

参考:
- [screen(だけ)の時代は終わり。tmuxでリモートコンソールを便利に使うTips : アシアルブログ](http://blog.asial.co.jp/881 "screen(だけ)の時代は終わり。tmuxでリモートコンソールを便利に使うTips : アシアルブログ")
- [UNIX/tmux/256色表示対応 - yanor.net/wiki](https://yanor.net/wiki/?UNIX/tmux/256%E8%89%B2%E8%A1%A8%E7%A4%BA%E5%AF%BE%E5%BF%9C)

## CLI

参考:

- tmux基本のコマンド — nato’s memo 1.0 documentation : http://room6933.com/mymemo/tmux/tmux-basic.html

### tmux コマンド

```bash
# セッションのリネーム
tmux rename -t 0 hoge

# 256色表示
tmux -2
```

### 仮想端末操作

| コマンド | 説明 |
|:-------:|:----|
| `<prefix>!` | ペイン分割解除 |

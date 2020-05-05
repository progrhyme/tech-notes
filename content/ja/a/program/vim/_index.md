---
title: "Vim"
linkTitle: "Vim"
description: >
  https://www.vim.org/
  the ubiquitous text editor
date: 2020-04-29T20:37:00+09:00
weight: 900
---

## パッケージ管理

Vim 8から標準機能になった。

https://vim-jp.org/vimdoc-ja/repeat.html#packages

> Vim script のパッケージは1つかそれ以上のプラグインを含むディレクトリである

参考:

- [Vim 8.0 Advent Calendar 6 日目 パッケージ - Qiita](https://qiita.com/thinca/items/cdc0169e3bcc5a55a5ba)

## プラグインマネージャー

サードパーティーのものが色々ある。

- [Vundle](https://github.com/VundleVim/Vundle.vim) ... 一番人気っぽいがここ数年、全然更新されてない（2020-05-05現在）
- [vim-plug](https://github.com/junegunn/vim-plug) ... ミニマリストにオススメっぽい
- [dein.vim](https://github.com/Shougo/dein.vim) ... 闇の力を得たプラグインマネージャー（笑） NeoBundleの後継

参考:

- [Vim におけるプラグイン管理についてまとめてみた - Qiita](https://qiita.com/tanabee/items/e2064c5ce59c85915940)

## Specs
### 正規表現

参考:

- [vim正規表現リファレンス - Qiita](https://qiita.com/kawaz/items/d0708a4ab08e572f38f3)

### オプションのグローバルな値とローカルな値

[Vim: オプションのグローバルな値とローカルな値 - while (“im automaton”);](https://whileimautomaton.net/2008/01/14011600) より。

- ふつうは `set` を使う
- ローカルに設定したい値は `setlocal` を使う。そうでないとグローバル値も変化してしまう
  - 例えば `ftplugin/xxx` でファイルタイプごとの設定をするときに `set` を使ってしまうと、ファイルを開くたびにグローバルの設定値が変化しかねない

## エディタの操作
### 全行の削除

```vim
" 全行削除
%d
```

参考:

- [vim - 全行削除コマンド - IT Notebook](http://makaaso.hatenablog.com/entry/2015/04/24/221955)

### 全行のインデント

```vim
" ファイル全体をインデント
gg=G
```

参考:

- [cl.pocari.org - Vim でインデントを整える](http://cl.pocari.org/2002-12-06-9.html)

### テキスト検索

- ノーマルモードで `/` を打って検索。
- `/\c` で始めると大文字小文字を区別せずに検索

参考:

- [Vim内で検索するときに大文字小文字を気にしない（ignore case）する方法 - Qiita](https://qiita.com/shoma2da/items/23009d4e1a90c5fe5c31)

### タブ文字の入力

`:set expandtab` （ `:set et` ）設定の時でも、 `Ctrl+v Tab` で入力できる。

参考:

- [:set expandtab（:set et）設定の時に、タブ文字を挿入する — 名無しのvim使い](https://nanasi.jp/articles/howto/editing/et-inserttab.html)

### 改行文字の置換（挿入/削除）

```Vim
; 改行を削除
:s/\n//g
; 改行を挿入
:s//\r/g
```

See [vimの置換で改行を(挿入|削除)する - Qiita](https://qiita.com/kiduki/items/df724a7a7ae50e70c08c)

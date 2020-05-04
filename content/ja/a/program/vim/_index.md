---
title: "Vim"
linkTitle: "Vim"
description: >
  https://www.vim.org/
  the ubiquitous text editor
date: 2020-04-29T20:37:00+09:00
weight: 900
---

## Commands

### Basic

```vim
" 全行削除
%d
```

参考:

- [vim - 全行削除コマンド - IT Notebook](http://makaaso.hatenablog.com/entry/2015/04/24/221955)

### Advanced Usage

```vim
" ファイル全体をインデント
gg=G
```

参考:

- [cl.pocari.org - Vim でインデントを整える](http://cl.pocari.org/2002-12-06-9.html)


## Specs
### 検索

- ノーマルモードで `/` を打って検索。
- `/\c` で始めると大文字小文字を区別せずに検索

参考:

- [Vim内で検索するときに大文字小文字を気にしない（ignore case）する方法 - Qiita](https://qiita.com/shoma2da/items/23009d4e1a90c5fe5c31)


### 正規表現

参考:

- [vim正規表現リファレンス - Qiita](https://qiita.com/kawaz/items/d0708a4ab08e572f38f3)


## Topics
### オプションのグローバルな値とローカルな値

[Vim: オプションのグローバルな値とローカルな値 - while (“im automaton”);](https://whileimautomaton.net/2008/01/14011600) より。

- ふつうは `set` を使う
- ローカルに設定したい値は `setlocal` を使う。そうでないとグローバル値も変化してしまう
  - 例えば `ftplugin/xxx` でファイルタイプごとの設定をするときに `set` を使ってしまうと、ファイルを開くたびにグローバルの設定値が変化しかねない


## How-to
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

---
title: "エディタ"
linkTitle: "エディタ"
description: エディタの使い方など
date: 2020-05-05T14:04:38+09:00
weight: 20
---

エディタを起動した後の使い方。  
主にファイル編集に関わる操作。

## 全行の削除

```vim
" 全行削除
%d
```

参考:

- [vim - 全行削除コマンド - IT Notebook](http://makaaso.hatenablog.com/entry/2015/04/24/221955)

## 全行のインデント

```vim
" ファイル全体をインデント
gg=G
```

参考:

- [cl.pocari.org - Vim でインデントを整える](http://cl.pocari.org/2002-12-06-9.html)

## テキスト検索

- ノーマルモードで `/` を打って検索。
- `/\c` で始めると大文字小文字を区別せずに検索

参考:

- [Vim内で検索するときに大文字小文字を気にしない（ignore case）する方法 - Qiita](https://qiita.com/shoma2da/items/23009d4e1a90c5fe5c31)

## タブ文字の入力

`:set expandtab` （ `:set et` ）設定の時でも、 `Ctrl+v Tab` で入力できる。

参考:

- [:set expandtab（:set et）設定の時に、タブ文字を挿入する — 名無しのvim使い](https://nanasi.jp/articles/howto/editing/et-inserttab.html)

## 改行文字の置換（挿入/削除）

```Vim
; 改行を削除
:s/\n//g
; 改行を挿入
:s//\r/g
```

See [vimの置換で改行を(挿入|削除)する - Qiita](https://qiita.com/kiduki/items/df724a7a7ae50e70c08c)

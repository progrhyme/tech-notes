---
title: "vimrc"
linkTitle: "vimrc"
date: 2020-05-05T14:34:07+09:00
weight: 90
---

Vimの設定ファイルであるvimrcについて。

## どのファイルが読み込まれるか

https://vim-jp.org/vimdoc-ja/starting.html#initialization

`vim -u ${file}` で任意の設定ファイルを指定できる。

## filetype

```Vim
"filetype検出の有効化
filetype on

" プラグインやインデントのロードも有効化
filetype plugin indent on

" 拡張子によるfiletype検出の追加の例
autocmd BufNewFile,BufRead *.rb setfiletype ruby
```

参考:

- [Vimメモ : filetypeの確認 - もた日記](https://wonderwall.hatenablog.com/entry/2016/03/20/222308)

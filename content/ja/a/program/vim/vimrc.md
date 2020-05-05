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

## キーマッピング

[map - Vim日本語ドキュメント](https://vim-jp.org/vimdoc-ja/map.html)

### マップコマンド

https://vim-jp.org/vimdoc-ja/map.html#:map-commands

構文:

```Vim
map   {lhs} {rhs} " キー入力 {lhs} を {rhs} に割り当てる
unmap {lhs}       " キー入力 {lhs} のマッピングを削除
```

map, nmapなど（ `noremap` じゃないやつ）:

- マップが使われたときに `{rhs}` が評価され、再マップされる
- マップを入れ子にしたり、再帰的にできる

noremap, nnoremapなど:

- `{rhs}` は再マップされないので、入れ子になったり再帰的になったりしない
- コマンドを再定義するときによく使われる

### マップとモード

https://vim-jp.org/vimdoc-ja/map.html#:map-modes

 コマンド | モード
----------|--------
 `map`, `noremap`, `unmap` | ノーマル、ビジュアル、選択、オペレータ待機
 `nmap`, `nnoremap`, `nunmap` | ノーマル

他に `vmap`, `smap`, `xmap` などある。

「オペレータ待機モード」は、`d`、`y`、`c`などの後で、後続の操作を待機しているとき。

### キーマッピングを確認する方法

[Vimのキーマッピングを確認する - Qiita](https://qiita.com/wakaba260/items/99ea1b8042c98fb7df93)より。

```Vim
" デフォルトキーバインドの一覧
:help index.txt

" 自分で割り当てたキーマップの確認
:map " すべて確認
:imap " インサートモードだけ
:nmap " ノーマルモードだけ
:vmap " ヴィジュアルモードだけ
:verbose nmap " 定義元ファイル情報も表示
```

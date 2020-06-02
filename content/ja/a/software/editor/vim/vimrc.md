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

## colorscheme

カラースキームを設定する。

See also [#highlight](#highlight)

Example:

```Vim
colorscheme elflord
```

デフォルトで使えるもの:

- `ls /usr/share/vim/vim80/colors/` などとする。
- 参考: [デフォルトでインストールされている — 名無しのvim使い](https://nanasi.jp/colorscheme/default_install.html)

みんなが作ったカラースキームが載ってるサイト: http://vimcolors.com/

参考:

- [vimのカラースキームの設定・編集方法（初心者〜上級者） - Qiita](https://qiita.com/sff1019/items/3f73856b78d7fa2731c7)

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

## highlight

https://vim-jp.org/vimdoc-ja/syntax.html#:highlight

特定のグループの文字色を変える。  
`:highlight` で現在の設定を得ることができる。

See also [#colorscheme](#colorscheme)

```Vim
" 構文
" 特定のグループの設定を追加
hi[ghlight] {group-name} {key}={arg}...
" 特定のグループの設定をリセット
hi[ghlight] clear{group-name}

" 例
highlight Search term=bold ctermfg=Black ctermbg=Blue
```

### highlight-args

https://vim-jp.org/vimdoc-ja/syntax.html#highlight-args

`highlight` コマンドに与える `{key}={arg}` の引数の一部を下に示す。

 key | 端末種別 | args
-----|-----|-----
 term | 通常 | bold,italic,underline,reverse,NONEなど。NONEは属性リセット用
 cterm | 色付き | termと同じ
 ctermfg | 色付き | 色名や番号を指定する
 ctermbg | 色付き | ctermfgと同じ

### cterm-colors

https://vim-jp.org/vimdoc-ja/syntax.html#cterm-colors

ctermfgやctermbgの値には0〜15の色番号やBlack, Blueなどの色名を指定できる。

色はVim上で `:so $VIMRUNTIME/syntax/colortest.vim` を実行して確認できる。

参考:

- [Vimの検索単語ハイライト時の背景色の変更方法 | Waza Lab](https://www.wazalab.com/2018/10/01/vim%e3%81%ae%e6%a4%9c%e7%b4%a2%e5%8d%98%e8%aa%9e%e3%83%8f%e3%82%a4%e3%83%a9%e3%82%a4%e3%83%88%e6%99%82%e3%81%ae%e8%83%8c%e6%99%af%e8%89%b2%e3%81%ae%e5%a4%89%e6%9b%b4%e6%96%b9%e6%b3%95/)

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

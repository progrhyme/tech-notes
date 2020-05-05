---
title: "Vim Plugins"
linkTitle: "Plugins"
description: Vimプラグイン
date: 2020-05-05T11:23:51+09:00
---

## Plugins

- [ctrlp.vim](https://github.com/ctrlpvim/ctrlp.vim) ... 高速ファイル検索ツール
  - 参考: [vimのファイル検索プラグインctrlp.vimの設定 – MY ROBOTICS](https://sy-base.com/myrobotics/vim/vim_ctrlp/)
- [yankround.vim](https://github.com/LeafCage/yankround.vim) ... レジスタ履歴を取得・再利用する
- NERDTree ... See below

参考:

- [vim – 強力なおすすめプラグイン – MY ROBOTICS](https://sy-base.com/myrobotics/vim/vim-my-plugins/)

## NERDTree

https://github.com/scrooloose/nerdtree

有名なVimのファイラプラグイン。

### Usage

ツリービューの操作:

 キー | 用途
------|------
 `?` | help表示（トグル）
 `I` | 隠しファイルの表示（トグル）

#### ファイル・ディレクトリを作成

ファイルツリーの任意の位置で `m` を押すとメニューが表示されるので、 `(a)dd a childnode` を選ぶ。  
ディレクトリを作る場合は末尾に `/` を入力すること。  
でないと、空のファイルが作られる。

`Ctrl-C` でメニューを抜けることができた。(Macで)


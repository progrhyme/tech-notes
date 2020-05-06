---
title: "Vim"
linkTitle: "Vim"
description: >
  https://www.vim.org/
  the ubiquitous text editor
date: 2020-04-29T20:37:00+09:00
weight: 900
---

## Getting Started

- エディタの操作 → [エディタ]({{< ref "/a/program/vim/edit.md" >}})
- Vimの設定 → [vimrc]({{< ref "/a/program/vim/vimrc.md" >}})

## Install
### Ubuntuに新しいVimを入れる

2020-05-06現在、Ubuntu 18.04に入っているVimのバージョンが8.0だった。  
より新しいバージョンを使うには、aptで `ppa:jonathonf/vim` のようなリポジトリの追加が必要そう。

参考:

- 2019年12月の記事: [How to Install Vim 8.2 in Ubuntu 18.04, 16.04, 19.10 | UbuntuHandbook](http://ubuntuhandbook.org/index.php/2019/12/install-vim-8-2-ubuntu-18-04-16-04-19-10/)

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
- [dein.vim](#deinvim) ... 闇の力を得たプラグインマネージャー（笑） NeoBundleの後継

参考:

- [Vim におけるプラグイン管理についてまとめてみた - Qiita](https://qiita.com/tanabee/items/e2064c5ce59c85915940)

### dein.vim

https://github.com/Shougo/dein.vim

ヘルプ:

- https://github.com/Shougo/dein.vim/blob/master/doc/dein.txt
- `:help dein`

参考:

- [NeoVim、そしてdein.vimへ - Qiita](https://qiita.com/okamos/items/2259d5c770d51b88d75b)
- [\[dein.vim\] hook の便利な使い方 - Qiita](https://qiita.com/delphinus/items/cd221a450fd23506e81a)

## Specs
### 正規表現

参考:

- [vim正規表現リファレンス - Qiita](https://qiita.com/kawaz/items/d0708a4ab08e572f38f3)

### オプションのグローバルな値とローカルな値

[Vim: オプションのグローバルな値とローカルな値 - while (“im automaton”);](https://whileimautomaton.net/2008/01/14011600) より。

- ふつうは `set` を使う
- ローカルに設定したい値は `setlocal` を使う。そうでないとグローバル値も変化してしまう
  - 例えば `ftplugin/xxx` でファイルタイプごとの設定をするときに `set` を使ってしまうと、ファイルを開くたびにグローバルの設定値が変化しかねない

## How-to

参考:

- [Vimメモ : filetypeの確認 - もた日記](https://wonderwall.hatenablog.com/entry/2016/03/20/222308)

### 現在編集してるファイルのfiletypeを確認

エディタ上でどちらかを実行

```Vim
:set filetype?
:echo &filetype
```

### filetype一覧の確認

エディタ上で以下を実行:

```Vim
:echo glob($VIMRUNTIME . '/ftplugin/*.vim')
:echo glob($VIMRUNTIME . '/indent/*.vim')
:echo glob($VIMRUNTIME . '/syntax/*.vim')

" 拡張子との関係を一覧
:autocmd filetypedetect
```

## 関連プロジェクト

- [Neovim](https://neovim.io/)
  - Vimのメンテナンシビリティと拡張性を高め、モダン化するプロジェクト
  - 参考:
    - [Neovimがどういうプロジェクトなのかまとめ - Qiita](https://qiita.com/lighttiger2505/items/440c32e40082dc310c1e)
    - [neovim とは何か？ | Vim入門](https://vim.blue/what-is-neovim/)

## Child Pages
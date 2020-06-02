---
title: "Vim Plugins"
linkTitle: "Plugins"
description: Vimプラグイン
date: 2020-05-05T11:23:51+09:00
weight: 600
---

## Plugins

次節以降で紹介していないもの:

- [ervandew/supertab](https://github.com/ervandew/supertab) ... タブ補完を可能にしてくれる
  - 補完リストのスクロールを上から下にしたい場合、vimrcに  
  `let g:SuperTabDefaultCompletionType = "<c-n>"`  
  を設定する
- [cespare/vim-toml](https://github.com/cespare/vim-toml) ... TOMLのシンタックスハイライト
- [kana/vim-operator-user](https://github.com/kana/vim-operator-user) ... 後掲のvim-operator-replaceなどが依存している
  - ドキュメント: [Vim: operator-user - Define your own operator easily](http://kana.github.io/config/vim/operator-user.html)

参考:

- [vim – 強力なおすすめプラグイン – MY ROBOTICS](https://sy-base.com/myrobotics/vim/vim-my-plugins/)
- [僕がVimで愛用しているプラグイン30連発 | 東京のWeb制作会社LIG](https://liginc.co.jp/469142)

## ctrlp.vim

https://github.com/ctrlpvim/ctrlp.vim

ディレクトリ下のファイルからファイル名をインクリメンタル検索して開いたり、バッファ一覧から検索したり、開いてるバッファの該当行を探してジャンプしたりできる。

vimrc設定例:

```Vim
" <C-p>で実行するフィーチャーをCtrlPMixedに変更
"  カレントディレクトリ下のファイル検索 + バッファ一覧 + 最後に開いたファイルリスト
let g:ctrlp_cmd = 'CtrlPMixed'
" <C-p>で実行するコマンドを変更
"  git下じゃないときはvimのglobとかにフォールバックしてくれる
let g:ctrlp_user_command =
  \ ['.git', 'cd %s && git ls-files -co --exclude-standard']
nnoremap <Leader>/ <ESC>:CtrlPLine<Return>
```

参考:

- [ctrlp.vimの使い方まとめ - Qiita](https://qiita.com/oahiroaki/items/d71337fb9d28303a54a8)
- [vimのファイル検索プラグインctrlp.vimの設定 – MY ROBOTICS](https://sy-base.com/myrobotics/vim/vim_ctrlp/)

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

## vim-operator-replace

https://github.com/kana/vim-operator-replace

ドキュメント:

- [Vim: operator-replace - Operator to replace text with register content](http://kana.github.io/config/vim/operator-replace.html)

ヤンクしているテキストでカーソル下のテキストを置き換える。

vimrc設定例:

```Vim
nmap <Space> <Plug>(operator-replace)
```

※ドキュメントでは `map` になっているが、 `nmap` でも動いた。

下のようなテキストを編集する:

```
foo
bar
baz
```

3行とも `foo` にしたいときは次のように操作すればいい:

1. カーソルを先頭行 `f` 位置に置き、「ye」とタイプして `foo` をヤンク
1. 「j」を押して2行目の行頭にカーソルを移動し、「<Space>e」とタイプする
1. 「j^」とタイプして3行目の行頭に移動し、「.」をタイプする

（参考記事の通りにやるのは難しかった。。）

参考:

- [vim-operator-replaceでコピペを簡単に - 僕のYak Shavingは終わらない](http://kazuph.hateblo.jp/entry/2013/01/04/005030)

## yankround.vim

https://github.com/LeafCage/yankround.vim

レジスタ履歴を取得・再利用する。

vimrc設定例:

```Vim
nmap p <Plug>(yankround-p)
xmap p <Plug>(yankround-p)
nmap P <Plug>(yankround-P)
nmap gp <Plug>(yankround-gp)
xmap gp <Plug>(yankround-gp)
nmap gP <Plug>(yankround-gP)
nmap <C-p> <Plug>(yankround-prev)
nmap <C-n> <Plug>(yankround-next)
nnoremap <Leader>y <ESC>:Unite yankround<Return>
```

`p` や `P` でヤンクを貼り付けた後、 `<C-p>` や `<C-n>` で順に操作して選べる。

`:Unite yankround` でUniteの小画面を開いてレジスタを一覧できる。
この小画面内で `d` でレジスタを消したり、 `x` で素早く対象を選んだりできる。（Unite全然使い倒してない）

ctrlp.vimと組み合わせると `:CtrlPYankRound` というコマンドが使えるようになって、これもレジスタを一覧できるのだけど、レジスタの内容でインクリメンタル検索できないので、 `:Unite yankround` の方が使いやすい。  
（GitHubにイシューが挙がっている。）

参考:

- [vimの便利なPlugin（その26）yankround | 技術者魂](http://engineerspirit.com/2017/07/01/post-1427/)

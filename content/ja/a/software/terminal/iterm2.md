---
title: "iTerm2"
linkTitle: "iTerm2"
description: https://iterm2.com/
date: 2020-05-16T14:18:31+09:00
---

## About

macOSで人気の端末アプリ。  
ターミナル.app より細かい設定が色々できるらしい。

起動アプリ名は「iTerm.app」

## Getting Started

- [Downloads](https://www.iterm2.com/downloads.html) <- インストールはここから
- [Documentation](https://www.iterm2.com/documentation.html)

## Keyboard Shortcuts

 Key | Function
-----|----------
 `⌘D` | 画面を左右に分割
 `⌘⇧D` | 画面を上下に分割
 `⌘]` | 画面分割時に次のペインに移動
 `⌘[` | 画面分割時に前のペインに移動
 `⌥⌘E` | Expose All Tabs
 `⌘⇧B` | Toolbeltの表示/非表示
 `⌘;` | コマンド自動補完のポップアップを呼び出す
 `⌘⇧;` | （Shell Integration）コマンド履歴を呼び出す
 `⌥⌘/` | 最近のディレクトリを呼び出す
 `⌘F` | テキスト検索

参考:

- [MacのターミナルアプリはiTerm2で決まり!!オススメの設定と基本的な機能まとめ – Webrandum](https://webrandum.net/iterm2/)

## Configuration

参考:

- [2020-05-16#MacBookにiTerm2を入れて設定してみた]({{<ref "20200516.md">}}#macbookにiterm2を入れて設定してみた)

### 背景画像の設定

`Profiles > Window > Background Image` で「Enabled」にチェックを入れると、ローカルのファイルシステムにある画像を選べる。

参考:

- [iTerm2を使いこなす - おしゃれな気分でプログラミング](http://neko-mac.blogspot.com/2015/02/iterm2.html)

## Usage
### テキスト検索モード

`⌘F` で入れる。

- マウス操作せず、 `TAB`, `⇧TAB` キーで選択範囲を広げられる。
- `⌥ENTER` で現在選択されているテキストをペースト

## Features

https://iterm2.com/features.html

- Toolbelt ... もう1つの作業スペース。 `⌘⇧B` で表示できる。
- [tmux Integration](https://www.iterm2.com/documentation-tmux-integration.html)

### シェル変数

後掲の[Shell Integration](#shell-integration)を有効にしないと使えないものもあるかもしれない。

 Name | Type | 意味
------|------|-----
 ITERM_PROFILE | 環境変数 | 現在の設定プロファイル。例: `Default`
 ITERM_SESSION_ID | 環境変数 | 

参考:

- [iTerm2 のカレントのプロファイルは $ITERM_PROFILE で取得できる。 - 全力で怠けたい](https://ebc-2in2crc.hatenablog.jp/entry/2019/08/31/170022)

### Shell Integration

https://www.iterm2.com/documentation-shell-integration.html

シェルと連携して機能強化できる。  
tmuxと一緒には使えないそうだ。

機能:

- Auto Command Completion ... メニューバーから `View > Auto Command Completion` で有効化できる

NOTE:

- Auto Command Completionのツールチップ表示中は、タブキーによるシェルの補完や [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions) による補完は効かない。 `Esc` キーでAuto Command Completionを解除できる

参考:

- [2020-05-16#MacBookにiTerm2を入れて設定してみた]({{<ref "20200516.md">}}#macbookにiterm2を入れて設定してみた)

## How-to
### SSH接続時に背景を変更する

背景色のみを変えることもできるが、リモート接続用の設定プロファイルを（複数）用意し、接続先によって切り替えるということも可能。

某現場では `gcloud compute ssh` を使うことが多いので、下のようなスクリプトを作り、 `gcloud-ssh` とaliasした。

```sh
#!/usr/bin/env bash

set -eu

NEW_ITERM_PROFILE=${NEW_ITERM_PROFILE:-remote}
original_profile=$ITERM_PROFILE

# Restore profile in any case
trap "echo -ne \"\033]1337;SetProfile=${original_profile}\a\"" EXIT

# Set given profile
echo -ne "\033]1337;SetProfile=${NEW_ITERM_PROFILE}\a"

gcloud compute ssh "$@"

echo -ne "\033]1337;SetProfile=${original_profile}\a"

exit
```

NOTE:

- 最初 `INT` でtrapしていたけど、gcloudコマンドが途中でコケたときにtrapできなかったので、 `EXIT` にした

参考:

- [iTerm2でSSHログイン先別にプロファイルを自動的に切替えて事故防止する方法 | Developers.IO](https://dev.classmethod.jp/articles/iterm2-ssh-change-profile/)
- [\[macOS\] SSHログインしたときだけターミナルの背景色を変えたい (iTerm2) | Developers.IO](https://dev.classmethod.jp/articles/do-ssh-and-change-bg-color-iterm2/)

## 参考記事

- [iTerm2のおすすめ設定〜ターミナル作業を効率化する〜 - Qiita](https://qiita.com/ruwatana/items/8d9c174250061721ad11)
- [俺よりiTerm使いこなしてるやつおる？ - ハイパーマッスルエンジニアになりたい](https://www.rasukarusan.com/entry/2019/04/13/180443)

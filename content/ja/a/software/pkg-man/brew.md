---
title: "Homebrew"
linkTitle: "Homebrew"
description: https://brew.sh/
date: 2020-05-04T17:19:03+09:00
weight: 200
---

かねてからmacOSでユーザーランドで動くパッケージ管理ソフトとして開発者に親しまれてきたツールだが、2019年にLinuxにも正式に対応した。

関連ページ:

- [OS > macOS]({{<ref "/a/os/mac/_index.md">}})

## Getting Started

- インストール ... https://brew.sh/ に従う

## macOS

- デフォルトで `/usr/local` にインストールされる

## Linux

https://docs.brew.sh/Homebrew-on-Linux

- デフォルトで `/home/linuxbrew/.linuxbrew` にインストールされる

参考:

- [UbuntuにHomebrewを入れてHomebrew Bundleでパッケージ管理することにした - progrhyme's tech blog](https://tech-progrhyme.hatenablog.com/entry/2020/04/29/222302)

## Documentation

https://docs.brew.sh/

## brewコマンド
### create

Formulaの雛形を作成する。

```sh
brew create [Options] URL

# 例
brew create https://github.com/progrhyme/shelp/archive/v0.5.0.tar.gz
## カスタムのTapを指定し、Golang向けの雛形を作る
brew create --go --tap progrhyme/taps -v https://github.com/progrhyme/shelp/archive/v0.5.0.tar.gz
```

 Option | 機能
--------|------
 -v, --verbose | 冗長ログを表示

## Contribution

ガイド:

- [How To Open a Homebrew Pull Request — Homebrew Documentation](https://docs.brew.sh/How-To-Open-a-Homebrew-Pull-Request)

メモ:

- 基本的には、ふつうにGitHubでforkして、featureブランチを作成してPull Requestを送る
- ローカルでHomebrewを展開したディレクトリが作業ツリーになる。そこで自分のforkしたリポジトリもremoteに追加する
- ローカルでtestを行ってからPRを送るべし

### Formulaの作成・更新

- https://docs.brew.sh/Formula-Cookbook
- https://docs.brew.sh/Acceptable-Formulae
- [Homebrew/homebrew-core/CONTRIBUTING.md](https://github.com/Homebrew/homebrew-core/blob/master/CONTRIBUTING.md)
- RubyDoc https://rubydoc.brew.sh/Formula

NOTE:

- homebrew-coreに取り込まれるには、ある程度ツールのレピュテーションが必要らしい。参考記事参照。GitHubリポジトリの場合、 `<20 forks, <20 watchers and <50 stars` だとNGだとか
  - そんなときはbrew tapを使う方式にすればいいっぽい

参考:

- https://github.com/syhw/homebrew/blob/master/Library/Contributions/example-formula.rb ... 最初に作るときに参考にしたのだが、実は非公式で、しかもだいぶ古い。2020-06-15現在は、公式にはこういう便利な雛形はなさそう（または、まだ私が見つけてない）
- [自作ツールをHomebrewに登録したい人生だった - 生涯未熟](https://syossan.hateblo.jp/entry/2018/01/24/192104)

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">ユーザーがつくまではしばらく brew tap にしておくのがよさそうですね。</p>&mdash; Kazuhiro Sera (瀬良) (@seratch_ja) <a href="https://twitter.com/seratch_ja/status/1272188680526942208?ref_src=twsrc%5Etfw">June 14, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

### Formulaの書き方

Tips:

- `sha256` の値はLinuxだと `sha256sum` コマンドで求められる
  - または、空欄にしておいて `brew fetch --force` すると正しい値を表示してくれるそうだ
- `bottle do ... end` ブロックは、botが自動で足してくれるらしい。

### Linuxbrew

https://github.com/Homebrew/linuxbrew-core/blob/master/CONTRIBUTING.md

2020-06-15現在、Linuxbrewは1日に1回はHomebrewをマージしてるから、Formulaの追加や更新はHomebrew側にした方がいいって書いてある。

## Tap

- 公式ドキュメント: https://github.com/Homebrew/brew/blob/master/docs/Taps.md
- 非公式和訳: [brew tapとは - Qiita](https://qiita.com/saa/items/85ed5e914d424fbf9fd6)

メモ:

- Third-Party Repositoriesのことだそうだ。
- 非公式のツールをbrew管理にできる仕組み。

参考:

- [Homebrewで自作ツールを簡単にインストール可能にする | おそらくはそれさえも平凡な日々](https://songmu.jp/riji/entry/2019-02-22-maltmill.html)
- [2020-06-15#maltmillを使いたかったが動かなかった]({{<ref "20200615.md">}}#maltmillを使いたかったが動かなかった)

## Ruby API

https://rubydoc.brew.sh/

### Formula

https://rubydoc.brew.sh/Formula.html

#### bin.install

https://docs.brew.sh/Formula-Cookbook#bininstall-foo

任意のファイルを `bin/` に移して、実行ビットを立てる（`chmod 0555`）。

Examples:

```Ruby
def install
  # fooをインストール
  bin.install 'foo'
  # bar.pyをbarにリネームしてインストール
  bin.install 'bar.py' => 'bar'
end
```

#### .on_linux

https://rubydoc.brew.sh/Formula.html#on_linux-class_method

Linuxでのみ実行されるブロックを作る。

```Ruby
on_linux do
  depends_on "linux_only_dep"
end
```

#### .on_macos

macOSでのみ実行されるブロックを作る。

```Ruby
on_macos do
  depends_on "mac_only_dep"
end
```

### OS

https://rubydoc.brew.sh/OS.html

Examples:

```Ruby
if OS.mac?
  # for macOS installation
elsif OS.linux?
  # for Linuxbrew installation
end
```

## Homebrew Bundle

https://github.com/Homebrew/homebrew-bundle

Rubyのbundlerのように、brewでインストールするパッケージをBrewfileという構成ファイルにまとめる。

オプションなしで実行した場合、カレントディレクトリの `Brewfile` を参照する。

SYNOPSIS:

```sh
# Brewfileに基づいてパッケージインストール
brew bundle [install] [OPTIONS]
# Brewfileに入ってないパッケージを削除する
brew bundle cleanup [--force] [OPTIONS]
# インストールされているパッケージリストをBrewfileに書き出す
brew bundle dump [OPTIONS]
```

オプション:

 オプション | 意味
------------|------
 `--global` | `~/.Brewfile` を見に行く
 `--file <File>` | Brewfileを指定する

参考:

- [Macでのアプリケーションインストールの自動化 - 理系学生日記](https://kiririmode.hatenablog.jp/entry/20200103/1578033722)

### Brewfile

Example:

```Ruby
tap "homebrew/bundle"
tap "homebrew/core"

# macOSでcaskを使う
tap "homebrew/cask"
cask_args appdir: "/Applications"
cask "google-chrome"

brew "bash"
brew "zsh"
brew "git"
brew "vim"
brew "tmux"
brew "direnv"
brew "jq"
brew "the_silver_searcher"
brew "coreutils"
```

NOTE:

- RubyのDSLなので普通に `# ...` でコメントが書けるらしい
  - [Allow comments in Brewfile · Issue #146 · Homebrew/homebrew-bundle](https://github.com/Homebrew/homebrew-bundle/issues/146)

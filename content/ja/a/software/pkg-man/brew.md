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

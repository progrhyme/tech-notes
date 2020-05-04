---
title: "Homebrew"
linkTitle: "Homebrew"
description: https://brew.sh/
date: 2020-05-04T17:19:03+09:00
weight: 200
---

かねてからmacOSでユーザーランドで動くパッケージ管理ソフトとして開発者に親しまれてきたツールだが、2019年にLinuxにも正式に対応した。

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

SYNOPSIS:

```sh
# Brewfileに基づいてパッケージインストール
brew bundle [install] [OPTIONS]
# Brewfileに入ってないパッケージを削除する
brew bundle cleanup [--force] [OPTIONS]
```

オプション:

 オプション | 意味
------------|------
 `--global` | `~/.Brewfile` を見に行く

参考:

- [Macでのアプリケーションインストールの自動化 - 理系学生日記](https://kiririmode.hatenablog.jp/entry/20200103/1578033722)

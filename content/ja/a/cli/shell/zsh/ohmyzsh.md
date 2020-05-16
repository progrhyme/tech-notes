---
title: "Oh My Zsh"
linkTitle: "Oh My Zsh"
description: https://ohmyz.sh/
date: 2020-05-16T09:12:08+09:00
---

## About
OSSのZshコンフィグレーションフレームワーク。

- ソースコード: https://github.com/ohmyzsh/ohmyzsh

## Getting Started

- Install ... ソースコードのREADME.mdの通り。
- Documents: [GitHub Wiki](https://github.com/ohmyzsh/ohmyzsh/wiki)
  - [Themes](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes)
  - [Plugins](https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins)

## Usage
### Update

https://github.com/ohmyzsh/ohmyzsh#getting-updates

2, 3週間に1回ぐらいシェル上でアップグレードのチェックが掛かるらしい。  
または、 `upgrade_oh_my_zsh` を実行すると手動アップデートが可能。

## Custom Plugins

サードパーティー製のプラグイン。

`$ZSH_CUSTOM` or `${oh-my-zshのインストールディレクトリ}/custom` 以下に配置すればよさそう。

### zsh-autosuggestions

https://github.com/zsh-users/zsh-autosuggestions

fishみたいにhistoryから自動補完を効かせてくれるやつ。

参考:

- [2020-05-16#zsh-autosuggestionsをインストールして設定]({{<ref "20200516.md">}}#zsh-autosuggestionsをインストールして設定)

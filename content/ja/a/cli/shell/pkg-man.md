---
title: "Package Managers"
linkTitle: "パッケージ管理"
date: 2020-05-18T23:21:41+09:00
weight: 2600
---

シェルスクリプトのパッケージ管理ツールについて。  
たまに調べるのでこのページにまとめる。

## 汎用

- [basherpm/basher](https://github.com/basherpm/basher) ... clenvと似てる。複数環境切替えなんて機能はもちろんない
- [rossmacarthur/sheldon](https://github.com/rossmacarthur/sheldon) ... Rust製。Zshに向いてそう。なんでもできそう
- [rerun](https://github.com/rerun/rerun) ... フレームワーク色がある
- [progrhyme/clenv](https://github.com/progrhyme/clenv) ... 拙作。未完

参考:

- [シェルスクリプトのパッケージマネージャー「basher」の機能概要と使い方 - Qiita](https://qiita.com/progrhyme/items/3a31282dfd0512a402cc) ... 2020年に書いたbasherの紹介記事
- [A Package Manager For Shell Scripts - Juan Ibiapina](https://juanibiapina.github.io/articles/basher-a-package-manager-for-shell-scripts/) ... basherの作者による紹介記事
- [&quot;clenv&quot; というシェルスクリプトのパッケージ管理ツールのようなものを作った - weblog of key_amb](https://keyamb.hatenablog.com/entry/clenv-release-v0.1)

## Bash

- [bpkg](https://www.bpkg.sh/)
- [ash-shell/ash](https://github.com/ash-shell/ash) ... フレームワークだそうだ

参考:

- [bash package manager: bpkgの紹介 - Qiita](https://qiita.com/Cj-bc/items/3ce2d9e451f3a06a4b4d)

## Zsh

- [Oh My Zsh]({{<ref "/a/cli/shell/zsh/ohmyzsh.md">}}) ... プラグインマネージャーというよりはフレームワークなのかな
- [zsh-users/antigen](https://github.com/zsh-users/antigen)
- [zplug](https://github.com/zplug/zplug)
- zplugin
- [tarjoilija/zgen](https://github.com/tarjoilija/zgen)
- antibody

参考:

- [おい、Antigen もいいけど zplug 使えよ - Qiita](https://qiita.com/b4b4r07/items/cd326cd31e01955b788b) ... b4b4r07氏のエントリ
- [もっと便利になれる zsh プラグインによる CLI ライフ - Qiita](https://qiita.com/b4b4r07/items/f37aadef0b3f740e8c14) ... b4b4r07氏のエントリ
- [A comparison of all the ZSH plugin mangers I used : zsh](https://www.reddit.com/r/zsh/comments/ak0vgi/a_comparison_of_all_the_zsh_plugin_mangers_i_used/)

## fish

- [jorgebucaran/fisher](https://github.com/jorgebucaran/fisher) ... これが人気っぽい
- [oh-my-fish](https://github.com/oh-my-fish/oh-my-fish) ... fisher以前はこれが人気だったっぽい。fishで使えるテーマがたくさんある
  - https://github.com/oh-my-fish/oh-my-fish/blob/master/docs/Themes.md ... 利用可能なテーマ一覧。

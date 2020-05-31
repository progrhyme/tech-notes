---
title: "dotfiles"
linkTitle: "dotfiles"
date: 2020-05-31T21:52:18+09:00
weight: 150
---

dotfilesは、主にコンピュータ上で、ユーザーの$HOMEディレクトリ下に置かれる `.` で始まるファイル類を表す。

## サイト

https://dotfiles.github.io/

> Your unofficial guide to dotfiles on GitHub.

- https://dotfiles.github.io/utilities/ ... dotfilesの管理ツールがたくさん紹介されている。

## まとめページ

https://github.com/webpro/awesome-dotfiles

dotfiles.github.io と同様だが、各種ツールなどが紹介されている。

## Tools

- [ubnt-intrepid/dot: Yet another management tool for dotfiles](https://github.com/ubnt-intrepid/dot) ... Rust製
- [rhysd/dotfiles: dotfiles symbolic links management CLI](https://github.com/rhysd/dotfiles) ... Golang製
- [FooSoft/homemaker: Efficiently manage your dot-file configuration settings.](https://github.com/FooSoft/homemaker) ... Golang製

### jaagr/dots

https://github.com/jaagr/dots

`alias dots='git --git-dir=$HOME/.dots.git/ --work-tree=$HOME'` これだけでやってる。  
`git` コマンドしか使わない。  
賢い。

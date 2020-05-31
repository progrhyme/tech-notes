---
title: "Snap"
linkTitle: "Snap"
description: https://snapcraft.io/
date: 2020-05-31T10:18:26+09:00
weight: 800
---

## About

Ubuntuの開発元であるCanonical社が作った、Linux向けのパッケージマネージャー。
ディストリビューションに依存しない。

参考:

- https://en.wikipedia.org/wiki/Snap_(package_manager)
- https://ja.wikipedia.org/wiki/Snappy

## snapコマンド

[Ubuntu Manpage: snap - Tool to interact with snaps](http://manpages.ubuntu.com/manpages/bionic/man1/snap.1.html)

ガイド:

- [Getting started | Snapcraft documentation](https://snapcraft.io/docs/getting-started)

Examples:

```sh
# インストール
sudo snap install $pkg
sudo snap install --channel=$channel $pkg

# インストールされたパッケージ一覧
snap list

# アンインストール
sudo snap remove $pkg

# パッケージを探す
snap find "<package name>"

# パッケージの情報（channel等）を確認
snap info $pkg
## 利用できるリビジョンを一覧
snap list --all $pkg

# パッケージの更新
sudo snap refresh $pkg
## channel変更も可能
sudo snap refresh --channel=$channel $pkg

# バージョン表示
snap version
```

## Snapcraft

Wikipediaによればビルドツールらしいが、レジストリの役割もあるのかな。  
ストアもある。 https://snapcraft.io/store

## Topics
### Snap or Snappy?

元々は「Snappy」という名前だったっぽくて、2020-05-31現在でも「Snappy」という記述がそこかしこで見られる。

参考:

- 2018-04-11のQA [Snap or Snappy? - other - snapcraft.io](https://forum.snapcraft.io/t/snap-or-snappy/4944)

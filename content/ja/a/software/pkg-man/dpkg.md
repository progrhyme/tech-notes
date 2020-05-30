---
title: "dpkg"
linkTitle: "dpkg"
description: Debian系のLinuxで使われるパッケージマネージャー
date: 2020-05-04T17:18:57+09:00
weight: 150
---

ハイレベルのインタフェースとして **apt**, **apt-get**, **aptitude** がある。  
昔からあるのがaptitudeで、最近あまり使われてない気がするが、2017年11月18日現在、これにしかない機能もあるそうだ。  
aptは最先端のようだが、すべてaptで賄えるというわけではまだなさそう。

dpkg <=> aptの関係は、RHEL系におけるrpm <=> yumの関係と似ている。

つまり、dpkgは低レベルのインタフェースであり、aptは内部的にdpkgを使っている。  
…というようなことが [Debian系のファイル管理コマンドもまとめてみた | tkd55](http://www.tkd55.net/?p=816) に書いてあった。

参考:

- https://sites.google.com/site/progrhymetechwiki/home/memo/2016/20160604#TOC-apt-

## ドキュメント

- [Debian 管理者ハンドブック](https://debian-handbook.info/browse/ja-JP/stable/)
  - [6.2. aptitude、apt-get、apt コマンド](https://debian-handbook.info/browse/ja-JP/stable/sect.apt-get.html)
- [dpkg(1): package manager for Debian - Linux man page](https://linux.die.net/man/1/dpkg)
- [man apt (8): コマンドラインインターフェイス](http://ja.manpages.org/apt/8)
- [apt-get(8) - Linux man page](https://linux.die.net/man/8/apt-get)
- [aptitude(8) - Linux man page](https://linux.die.net/man/8/aptitude)

## コマンド

```sh
# パッケージリストの更新
apt update

# パッケージの更新
## 更新可能なパッケージの一覧
apt list --upgradable

## 最低限可能なアップグレードを行う
apt upgrade
apt-get upgrade
aptitude safe-upgrade

# パッケージの検索
apt search $QUERY
apt-cache search $QUERY

# パッケージの削除
apt remove $PACKAGE...
apt-get remove $PACKAGE...

## 不要なパッケージを削除 ... 依存関係でインストールされたが、使われなくなったもの
apt autoremove

# インストールされたパッケージの一覧
dpkg -l

# パッケージがインストールされているか調べる
dpkg -l $PACKAGE
dpkg-query -l $PACKAGE

# インストールされたパッケージに含まれるファイルリストを表示
dpkg-query -L $PACKAGE
```

### インストール

```sh
apt install $PACKAGE...
apt-get install $PACKAGE...

# バージョン指定
apt-get install ${PACKAGE}=${VERSION}...

# .debパッケージファイルをインストール
dpkg -i foo.deb
```

参考:

- [apt-getでversionを指定してインストールする方法 - Qiita](https://qiita.com/isaoshimizu/items/e9c7fdc8efad66422cae)

### 参考

- [Debian系のファイル管理コマンドもまとめてみた | tkd55](http://www.tkd55.net/?p=816)
- [aptとdpkg - intrinsic feeling](http://d.hatena.ne.jp/bluerepliroid/20071205/1197288679)
- [aptコマンドチートシート - Qiita](https://qiita.com/SUZUKI_Masaya/items/1fd9489e631c78e5b007)
- [rpm、deb、depot、msiパッケージの展開と一覧表示コマンドまとめ | マイナビニュース](https://news.mynavi.jp/article/20100420-a053/)

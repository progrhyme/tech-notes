---
title: "Install"
linkTitle: "インストール"
date: 2020-04-26T19:02:34+09:00
weight: 10
---

## Ubuntu

https://github.com/golang/go/wiki/Ubuntu

2018年以前ぐらいまではtarballからインストールしていたと思うが、2020-04-26現在は、apt installが可能になっている。

以下は最新版をインストールする手順:

```sh
sudo add-apt-repository ppa:longsleep/golang-backports
sudo apt update
sudo apt install golang-go
```

## How-to
### 複数バージョンのGoをインストール

https://golang.org/doc/install#extra_versions に公式のガイドがある。

```sh
$ go get golang.org/dl/go1.10.7
$ go1.10.7 download
$ go1.10.7 version
go version go1.10.7 linux/amd64
```

参考:

- サードパーティーのツールもある。goenvとか

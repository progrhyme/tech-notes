---
title: "Install"
linkTitle: "インストール"
date: 2020-04-26T19:02:34+09:00
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

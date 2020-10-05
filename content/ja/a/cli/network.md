---
title: "ネットワーク関係のCLI"
linkTitle: "ネットワーク系"
date: 2020-05-11T23:30:10+09:00
weight: 2500
---

ネットワーク関係のUnixコマンドやCLIツールについて、ここに記す。

## dig

https://linuxjm.osdn.jp/html/bind/man1/dig.1.html

DNSクエリを送信し、結果を得る。

構文:

```bash
dig [@ server ] domain [Aq query-type ] [Aq query-class ] 
  [+ Aq query-option ] [-Aq dig-option ] [%comment ]
```

- `@server` ... ネームサーバを指定

query-option:

| Option | 意味 |
|----------|--------|
| `+short` | 結果のIPやホスト名だけを返す |
| `+trace` | ルートDNSから問合せ |

参考:

- [digコマンドで覚えておきたい使い方11個 \| 俺的備忘録 〜なんかいろいろ〜](https://orebibou.com/2016/11/dig%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E3%81%A7%E8%A6%9A%E3%81%88%E3%81%A6%E3%81%8A%E3%81%8D%E3%81%9F%E3%81%84%E4%BD%BF%E3%81%84%E6%96%B911%E5%80%8B/)
- [digコマンド 使い方 オプション DNS BIND](http://www.geocities.jp/yasasikukaitou/dig.html)

## lsof

ファイルディスクリプタを表示するコマンドだが、ネットワークソケットの表示にも使える。

Examples:

```sh
# ネットワークコネクションを表示
lsof -i -P
```

参考:

- [lsof, netstat コマンド - Qiita](https://qiita.com/sinsengumi/items/b9e0c1fde8075f9153e1)

## mtr

デフォルトは ICMP を使う。

オプション:

| Option | 意味 |
|--------|------|
| `-T,--tcp` | TCP SYN を使う |
| `-u` | UDP を使う |
| `-P,--port <port>` | UDP/TCP で port を指定する。 |
| `-v,--version` | バージョン表示。 |

※古いバージョンだとオプション効かないかも。man とか見て。

## ss

netstatとまあまあ同じ感じで使える。  
netstatより推奨っぽいが、作りがバギーという噂もどこかで。。

Examples:

```sh
# LISTENしているポート
ss -l

# TCP, UDPとも名前解決せずに全ての接続を表示
ss -antu
```

参考:

- [Linuxでプロセスが何のポート使っているかを調べる - Qiita](https://qiita.com/sonoshou/items/cc2b740147ba1b8da1f3)

## traceroute

デフォルトは UDP を使う。

オプション:

| Option | 意味 |
|--------|-----|
| `-I` | ICMP を使う。 |
| `-T` | TCP を使う。 |
| `-p <port>` | UDP/TCP で port を指定する。 |
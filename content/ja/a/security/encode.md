---
title: "データの符号化"
linkTitle: "符号化"
date: 2020-07-05T13:18:50+09:00
---

データの符号化について。  
暗号化を含めるかは未定。

## CRC

データ転送時の誤り検出によく用いられているようだ。

参考:

- [巡回冗長検査 - Wikipedia](https://ja.wikipedia.org/wiki/%E5%B7%A1%E5%9B%9E%E5%86%97%E9%95%B7%E6%A4%9C%E6%9F%BB)

### バリエーション

生成多項式の長さなどによっていくつかバリエーションがある。  
よく用いられるのはIEEE 802.3の「CRC-32」で、イーサネットやZIPやPNGなどで使われている。

Linuxでは `crc32` というPerlスクリプトが比較的手軽に利用できる。

NOTICE:

- GNU coreutilsの[cksum]({{<ref "/a/cli/unix-cmd/_index.md">}}#cksum)はCRC-32とは実装が異なる

参考:

- [まさおのブログ (表): Ubuntu で CRC32](http://masaoo.blogspot.com/2012/03/ubuntu-crc32.html)

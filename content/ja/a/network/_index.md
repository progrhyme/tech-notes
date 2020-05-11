---
title: "ネットワーク"
linkTitle: "ネットワーク"
date: 2020-05-12T00:11:45+09:00
weight: 820
---

このセクションでは、ネットワークプロトコルやネットワーク通信、その技術に関する話題を扱う。

## インターネット
### 通信の流れ

参考:

- [ネットワーク入門サイト - 全体の通信の流れ](https://beginners-network.com/nagare.html)

## ルーティング

参考:

- [インターネット10分講座：経路制御 - JPNIC](https://www.nic.ad.jp/ja/newsletter/No38/0800.html)

### AS

Autonomous System. 共通のポリシーや同じ管理下で運用されるルータやネットワークの集合。  
インターネットはASの集合。

- **AS番号** ... ASを識別するための番号。かつては2バイトだったが、AS番号の枯渇懸念のため、4バイトに拡張された。

参考:

- [インターネット用語1分解説～4バイトAS番号とは～ - JPNIC](https://www.nic.ad.jp/ja/basics/terms/as4bytes.html)
- [BGPの仕組みと役割を理解する：IPルーティング入門（2） - ＠IT](http://www.atmarkit.co.jp/ait/articles/0112/06/news002.html)

## トンネリング

あるネットワークの上に仮想のネットワークを作り、物理的/論理的に離れたモノの間で通信を成立させる技術。  
パケットのカプセル化によって実現されるものが多い。

様々なトンネリング技術:

- PPPoE (PPP over Ethernet)
- IP-in-IP
  - [RFC 1853](https://tools.ietf.org/html/rfc1853) で標準化されている。
  - IPv4 over IPv4, IPv4 over IPv6, IPv6 over IPv4, IPv6 over IPv6 の4種類がある。
  - 参考:
    - [IPIPトンネリング](http://www.rtpro.yamaha.co.jp/RT/docs/ipip/index.html)
- GRE
  - [RFC 2784](https://tools.ietf.org/html/rfc2784)で標準化されている。
  - IPトンネル内でパケットをカプセル化
  - 暗号化機能は持たないため、データも暗号化したい場合、IPsecを併用する。
  - 参考:
    - [GRE（Generic Routing Encapsulation）とは](http://www.infraexpert.com/study/rp8gre.htm)
- TUN
- TAP
- L2TP (Layer 2 Tunneling Protocol)
  - 参考:
    - https://ja.wikipedia.org/wiki/Layer_2_Tunneling_Protocol
- VXLAN
  - L3ネットワーク上に論理的なL2ネットワークを構築する。
  - 24bitのVXLAN IDによって、最大で約1600万のネットワークを構成可能
  - UDP/IPでカプセル化
  - 参考:
    - [VXLANとは](http://www.infraexpert.com/study/virtual3.html)
- VLANトンネリング
  - See https://sites.google.com/site/progrhymetechwiki/network/vlan
- SSHポートフォワーディング(トンネリング)
  - 参考:
    - [SSHポートフォワード（トンネリング）を使って、遠隔地からLAN内のコンピュータにログインする - ククログ(2014-09-12)](http://www.clear-code.com/blog/2014/9/12.html)
    - [sshポートフォワーディング - Qiita](https://qiita.com/mechamogera/items/b1bb9130273deb9426f5)

トンネリング技術により実現されるモノ:

- VPN

参考:

- [トンネリング - Wikipedia](https://ja.wikipedia.org/wiki/%E3%83%88%E3%83%B3%E3%83%8D%E3%83%AA%E3%83%B3%E3%82%B0)
- [TUN/TAP - Wikipedia](https://ja.wikipedia.org/wiki/TUN/TAP)
- [AWS Solutions Architect ブログ: AWSでも役に立つトンネリング技術入門](http://aws.typepad.com/sajp/2014/03/aws_tunneling.html)

## 帯域制御

- **トラフィックシェーピング** ... トラフィック（通信量）を制御し、パケットを遅延させることで通信性能を最適化/保証し、レイテンシを低減し、帯域幅を確保すること。パケットシェーピングとも言う。

参考:

- [トラフィックシェーピング - Wikipedia](https://ja.wikipedia.org/wiki/%E3%83%88%E3%83%A9%E3%83%95%E3%82%A3%E3%83%83%E3%82%AF%E3%82%B7%E3%82%A7%E3%83%BC%E3%83%94%E3%83%B3%E3%82%B0)

---
title: "Domain Name System"
linkTitle: "DNS"
date: 2020-05-12T00:12:14+09:00
---

DNSプロトコルやDNSサーバなどに関して。

## Getting Started

入門コンテンツ:

- [インターネット10分講座 DNS - JPNIC](https://www.nic.ad.jp/ja/newsletter/No22/080.html)

## Glossary
### スタブとフォワード

- スタブゾーン, 条件付きフォワーダ
- いずれも別のサーバに問合せを転送することができる。
- フォワード
  - 問合せを外部に転送
  - DNS キャッシュサーバを指定する
  - 外部へ問合せするDNSキャッシュサーバをまとめられる
- スタブ
  - その zone をホストする DNS コンテンツサーバを指定
  - サブドメインを委任するときとか
  - 子ゾーンをスタブゾーンとする
  - 親ゾーンでは子ゾーンをホストするすべての DNS サーバを認識するようにする

参考:

- [スタブ ゾーンと条件付きフォワーダとの違い](https://msdn.microsoft.com/ja-jp/library/cc780434(v=ws.10).aspx)
- [実用 BIND 9で作るDNSサーバ（6）：サブドメインの運用と委任 (3/3) - ＠IT](http://www.atmarkit.co.jp/ait/articles/0306/03/news002_3.html)
- [unbound.conf(5) – 日本Unboundユーザー会](http://unbound.jp/unbound/unbound-conf/)

## レコード

https://tools.ietf.org/html/rfc1035

- NS
- A
- CNAME
- MX
- TXT
- SOA
- :

参考:

- [DNSレコードタイプの一覧 \- Wikipedia](https://ja.wikipedia.org/wiki/DNS%E3%83%AC%E3%82%B3%E3%83%BC%E3%83%89%E3%82%BF%E3%82%A4%E3%83%97%E3%81%AE%E4%B8%80%E8%A6%A7)
- [DNSレコードの登録ルール（バリデーションルール）](http://manual.iij.jp/dns/help/1481516.html)

### TXT

https://tools.ietf.org/html/rfc1464

Example:

```
example.jp. IN TXT "exampleA" "exampleB"
```

仕様:

- `"` で括ってエントリを値を記述する。
- `"` で括った1エントリについて
  - 文字数は最大255文字。`"` も含めると最大257文字
- エントリを複数記述できる。エントリ間に半角スペースを入れる。
- TXTレコードの右辺全体に記述できる文字数は最大1,024文字

## DNSSEC

DNSのセキュリティを高める技術の1つで、主にキャッシュポイズニングを防げるっぽい。

参考:

- [インターネット10分講座：DNSSEC - JPNIC](https://www.nic.ad.jp/ja/newsletter/No43/0800.html)

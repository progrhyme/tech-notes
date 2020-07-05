---
title: "セキュリティ"
linkTitle: "セキュリティ"
date: 2020-07-05T13:13:35+09:00
weight: 860
---

## 分野

IPA情報セキュリティスキルマップによると、以下の16の大項目に分類されている。

1. 情報セキュリティマネジメント
2. ネットワークインフラセキュリティ
3. アプリケーションセキュリティ
  - Web, 電子メール, DNS
4. OSセキュリティ
  - Unix, Windows, Trusted OS
5. ファイアウォール
6. 侵入検知システム
7. ウイルス
8. セキュアプログラミング技法
9. セキュリティ運用
10. セキュリティプロトコル
11. 認証
12. PKI
13. 暗号
14. 電子署名
15. 不正アクセス手法
16. 法令・規格

参考:

- [情報セキュリティ専門家の育成：IPA 独立行政法人 情報処理推進機構](https://www.ipa.go.jp/security/manager/edu/training/expert.html)
- [セキュリティ知識分野（SecBoK）人材スキルマップ2017年版](https://www.jnsa.org/result/2017/skillmap/index.html)

## 組織
### パブリック

- CIS - https://www.cisecurity.org/

### 内部組織

- CSIRT
- PSIRT
- SOC ... Security Operation Center. ファイアウォールやIDS, ネットワーク等のログを定常的に監視し、インシデントを発見・特定・報告する。CSIRTと比べ、インシデントの検知に重きが置かれる。

参考:

- [インターネット用語1分解説～SOCとは～ - JPNIC](https://www.nic.ad.jp/ja/basics/terms/soc.html)

## CVSS
共通脆弱性評価システム（Common Vulnerability Scoring System）。

- [共通脆弱性評価システムCVSS概説：IPA 独立行政法人 情報処理推進機構](https://www.ipa.go.jp/security/vuln/CVSS.html)

脆弱性の深刻度（出典: ↓参考リンク）:

 深刻度 | スコア
----------|-----------
 緊急 | 9.0 - 10.0
 重要 | 7.0 - 8.9
 警告 | 4.0 - 6.9
 注意 | 0.1 - 3.9

参考:

- [CVSSとはなんぞや？ 計算方法とスコアの見方を解説します \| 株式会社レオンテクノロジーはWebサイトを守るセキュリティ会社です](https://www.leon-tec.co.jp/blog/yoshida/7689/)

## Linux

参考:

- [【初心者向け基本解説】Linuxのウィルスとその対策方法](https://eng-entrance.com/linux-virus)

## Mac OS

- https://www.munki.org/
  - Managed Software Centerなどをオープンソースで開発するプロジェクト
  - SlackやGoogle Groupがある

## Feeds

参考:

- [【随時更新】セキュリティに関する情報源を整理してみた - トリコロールな猫/セキュリティ](http://security.nekotricolor.com/entry/my-news-source-about-information-security "【随時更新】セキュリティに関する情報源を整理してみた - トリコロールな猫/セキュリティ")
- [購読しているセキュリティ関連メーリングリスト情報 - Qiita](https://qiita.com/harukasan/items/4f11dce5db8cd62b7126 "購読しているセキュリティ関連メーリングリスト情報 - Qiita")

## Keywords

- ITIL
- ISMS
- RFC ... ITILの文脈では、Request For Changeの略で、何らかの変更要求やその文書を表す。

参考:

- [Information Technology Infrastructure Library - Wikipedia](https://ja.wikipedia.org/wiki/Information_Technology_Infrastructure_Library)
- [ITILとは - itSMF Japanオフィシャルサイト](http://www.itsmf-japan.org/aboutus/itil.html)
- [情報セキュリティマネジメントシステム - Wikipedia](https://ja.wikipedia.org/wiki/%E6%83%85%E5%A0%B1%E3%82%BB%E3%82%AD%E3%83%A5%E3%83%AA%E3%83%86%E3%82%A3%E3%83%9E%E3%83%8D%E3%82%B8%E3%83%A1%E3%83%B3%E3%83%88%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0)
- [情報セキュリティマネジメントシステム(ISMS)とは](https://isms.jp/isms/)
- [RFC（あーるえふしー） \- ITmedia エンタープライズ](http://www.itmedia.co.jp/im/articles/0908/25/news114.html)

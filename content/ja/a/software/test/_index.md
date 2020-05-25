---
title: "Software Test"
linkTitle: "テスト"
date: 2020-05-23T17:38:12+09:00
weight: 2500
---

Software Test Engineeringまで入るかも。  
一旦、負荷テストもここに入れる。

## 負荷テストツール

どんなものがあるかメモ:

- ab
- JMeter
- Gatling
- [Locust]({{<ref "locust.md">}})

## Topics
### スタブとモックの違い

どっちがどっちかいつもよくわからなくなる。

スタブの定義らしきもの:

- テスト対象モジュールが依存するモジュールの代用品として動作し、決められた動きをするもの

モックの定義らしきもの:

- テスト対象モジュール、またはスタブが利用するモジュールの代用品として動作し、どのような使われ方をしたかをチェックするもの
  - 例えばどのメソッドが何回呼ばれたか、とか

参考:

- [スタブとモックの違い - Qiita](https://qiita.com/k5trismegistus/items/10ce381d29ab62ca0ea6)
- [自動テストのスタブ・スパイ・モックの違い | gotohayato.com](https://gotohayato.com/content/483/)
- [スタブとは何？ Weblio辞書](https://www.weblio.jp/content/%E3%82%B9%E3%82%BF%E3%83%96)
- [モックアップとは何？ Weblio辞書](https://www.weblio.jp/content/%E3%83%A2%E3%83%83%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97)

MEMO:

- 2020-05-23 旧Wikiに載せていたリンクは切れてしまっていた。

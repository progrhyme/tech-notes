---
title: "Google Sheets"
linkTitle: "Sheets"
description: Googleスプレッドシート
date: 2020-05-09T09:38:09+09:00
weight: 850
---

## 関数

[Google スプレッドシートの関数リスト - ドキュメント エディタ ヘルプ](https://support.google.com/docs/table/25273?hl=ja)

### SUMIFS

https://support.google.com/docs/answer/3238496?hl=ja

SUMIFの条件部を複数指定できるバージョン。

Format: `SUMIFS(合計範囲, 条件範囲1, 条件1, [条件範囲2, 条件2, ...])`

## How-to
### 日時の差を計算

- [DATEDIF](https://support.google.com/docs/answer/6055612?hl=ja) ... 日付、月数、年数に対応

```
=(B2-A2) * 86400  // 秒数
```

参考:

- [2 つの時刻の差を計算する - Excel](https://support.office.com/ja-jp/article/2-%e3%81%a4%e3%81%ae%e6%99%82%e5%88%bb%e3%81%ae%e5%b7%ae%e3%82%92%e8%a8%88%e7%ae%97%e3%81%99%e3%82%8b-e1c78778-749b-49a3-b13e-737715505ff6)

### 数値によって分類する

LOOKUP系の関数（ `[VH]LOOKUP` ）の最後の引数に `true` を与えると、「検索値以下で最も近い値」を取り出すことができる。  
これによって、「点数によってランクを付ける」といったことが可能。

例:

 \ | A | B
---|---|---
 **1** | 下限値 | 等級
 **2** |  0 | D
 **3** | 26 | C
 **4** | 51 | B
 **5** | 76 | A

上のような表があり、 `=VLOOKUP(検索値, $A$2:$B$5, 2, TRUE)` とやると、次のようになる:

- 検索値が `(-∞, 0)` => `#N/A`
- 検索値が `[0, 26)` => D
- 検索値が `[26, 51)` => C
- 検索値が `[51, 76)` => B
- 検索値が `[76, ∞)` => A

参考:

- [ExcelのVLOOKUP関数で「○以上△未満」の条件で表を検索する方法 | できるネット](https://dekiru.net/article/12612/)

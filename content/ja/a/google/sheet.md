---
title: "Google Sheets"
linkTitle: "Sheets"
description: Googleスプレッドシート
date: 2020-05-09T09:38:09+09:00
weight: 850
---

## 関数

[Google スプレッドシートの関数リスト - ドキュメント エディタ ヘルプ](https://support.google.com/docs/table/25273?hl=ja)

### ADDRESS

https://support.google.com/docs/answer/3093308?hl=ja

セル参照を文字列として返す。

Format: `ADDRESS(行, 列, [絶対相対モード], [A1表記の使用], [シート])`

- **絶対相対モード** （省略可 - デフォルトは 1） ... 行/列の絶対参照であるかどうかを指定します。行と列の絶対参照（例: $A$1）である場合は 1、行の絶対参照で列の相対参照（例: A$1）である場合は 2、行の相対参照で列の絶対参照（例: $A1）である場合は 3、行と列の相対参照（例: A1）である場合は 4
- **A1表記の使用** （省略可 - デフォルトは TRUE） ... A1 型表記を使用するか（TRUE）、R1C1 型表示を使用するか（FALSE）を指定する

Examples:

```
ADDRESS(1,2)
ADDRESS(1,2,4,FALSE)
ADDRESS(1,2,,,"シート2")
```

### MATCH

https://support.google.com/docs/answer/3093378?hl=ja

指定した値と一致する範囲内のアイテムの相対的な位置を返します。

Format: `MATCH(検索キー, 範囲, 検索の種類)`

- **検索の種類** （省略可 - デフォルトは 1） ... 検索の方法
  - 1（デフォルト） ... MATCH 関数は範囲が昇順で並べ替えられていると想定し、検索キー以下の最も大きい値を返す
  - 0  ... 完全一致を示し、範囲が並べ替えられていない場合に必須の値
  - -1  ... MATCH 関数は範囲が降順で並べ替えられていると想定し、検索キー以上の最も小さい値を返す

Examples:

```
MATCH("日曜日",A2:A9,0)
MATCH(DATE(2012,1,1),A2:F2)
```

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

### UNIX時間を日時に変換

UNIX時間 `1606057200` がセルA1に入っているとする。

- 日付: `=(A1/86400) + date(1970,1,1)` => `2020/11/23`
- 時刻: `=TEXT(A1/86400, "hh:mm:ss"` => `00:00:00`

参考:

- [スプレッドシートでUNIX timeを日時に変換する方法 - Qiita](https://qiita.com/narikei/items/6678799d2d6acc29c8c1)

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

---
title: "データ型"
linkTitle: "データ型"
date: 2020-08-21T17:34:53+09:00
---

## 組み込み型

https://docs.python.org/ja/3/library/stdtypes.html

- int
  - bool
    - `True == 1`
    - `False == 0`

参考:

- [Pythonの真偽値bool型（True, False）と他の型との変換・判定 | note.nkmk.me](https://note.nkmk.me/python-bool-true-false-usage/)

## 真偽値

https://docs.python.org/ja/3/library/stdtypes.html?#truth-value-testing

- オブジェクトはデフォルトでは真
- 次の場合は偽:
  - `__bool__()` メソッドが `False` を返す
  - `__len__()` メソッドが `0` を返す

偽と判定されるもの:

- `None`, `False`
- 数値型のゼロ: `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0, 1)`
- 空のシーケンス: `''`, `()`, `[]`, `{}`, `set()`, `range(0)`

Tips:

- 組み込み関数 `bool()` を使うと他の型のオブジェクトを `True` or `False` に変換できる

参考:

- [Pythonの真偽値bool型（True, False）と他の型との変換・判定 | note.nkmk.me](https://note.nkmk.me/python-bool-true-false-usage/)

## シーケンス型 - list, tuple, range

ミュータブルなものとイミュータブルなものがある。tupleオブジェクトはイミュータブルらしい。

共通の演算:

- `len(s)` ... 長さ

### ミュータブル

listオブジェクトとか。

演算:

- `s.append(x)` ... 要素追加

参考:

- [リスト \- 作成、取り出し、置換、追加、検索、削除、要素数 \- ひきメモ](http://d.hatena.ne.jp/yumimue/20071205/1196839438)
- [Python: リストの要素の追加と削除、取出し – append\(\)、extend\(\)、pop\(\)、remove\(\)メソッド](http://www.yukun.info/blog/2008/06/python-list2.html)

## マッピング型 - dict

https://docs.python.org/ja/3/library/stdtypes.html?highlight=dict#mapping-types-dict

ミュータブルなオブジェクト。  
hashableな値を任意のオブジェクトに対応付ける。

SYNOPSIS:

```Python
# 生成
d = {'foo': 1, 'bar': 'BAR', 'baz': {'x': True}}

# 演算
len(d)
d[key]
d[key] = value
del d[key]
key in d
key not in d
iter(d)
clear() # 全てのエントリを削除
copy() # shallow copy
get(key[, default])
```

### ループ処理

Examples:

```Python
d = {'key1': 1, 'key2': 2, 'key3': 3}

for key in d:
  print(key)

for key in d.keys():
  print(key)

for val in d.values():
  print(val)

for key, val in d.items():
  print(key, val)

# タプル
for tup in d.items():
  print(tup) #=> ('key1', 1)
```

参考:

- [Pythonの辞書（dict）のforループ処理（keys, values, items） | note.nkmk.me](https://note.nkmk.me/python-dict-keys-values-items/)

## ヌル - None

`None` オブジェクト

## バイトオブジェクト - bytes, bytearray

https://docs.python.org/ja/3/library/stdtypes.html#bytes-objects

- bytes ... 不変型。リテラル: `b'...'`
- bytearray ... 可変型。リテラル構文はないので、コンストラクタで生成する

### replace

https://docs.python.org/ja/3/library/stdtypes.html#bytes.replace

```Python
bytes.replace(old, new[, count])
bytearray.replace(old, new[, count])
```

oldをnewにすべて置換する。countがある場合、先頭からcount個数分だけ置換する。

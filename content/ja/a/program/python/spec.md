---
title: "言語仕様"
linkTitle: "言語仕様"
date: 2020-07-20T23:15:40+09:00
---

## データ型

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

## 演算子
### 三項演算子

Syntax:

```Python
(変数) = (条件がTrueのときの値) if (条件) else (条件がFalseのときの値)
```

Example:

```Python
x = "OK" if n == 10 else "NG"
```

参考:

- [三項演算子(Python) - Qiita](https://qiita.com/howmuch515/items/bf6d21f603d9736fb4a5)

## 制御構文
### 条件分岐

```Python
if 条件1:
    xxx
    :
elif 条件2:
    yyy
    :
else:
    zzz
    :
```

参考:

- [if文を使った条件分岐 | Python入門](https://www.javadrive.jp/python/if/index1.html)

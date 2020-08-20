---
title: "言語仕様"
linkTitle: "言語仕様"
date: 2020-07-20T23:15:40+09:00
weight: 20
---

## はじめに

基本的にPython3の仕様のみを書く。  
ただし、ぐぐった結果とかを貼っているものはPython2のことがあるかもしれない。  

ドキュメント:

- https://docs.python.org/ja/3/
  - 言語仕様: https://docs.python.org/ja/3/reference/


## モジュール検索パス

https://docs.python.org/ja/3/tutorial/modules.html#the-module-search-path

[sys.path](https://docs.python.org/ja/3/library/sys.html#sys.path) のリストから探す。sys.path は以下で初期化される:

- カレントディレクトリ（あるいは入力されたスクリプトのあるディレクトリ）
- 環境変数 [PYTHONPATH](https://docs.python.org/ja/3/using/cmdline.html#envvar-PYTHONPATH)
- インストールごとのデフォルト

参考:

- [Pythonでimportの対象ディレクトリのパスを確認・追加（sys.pathなど） | note.nkmk.me](https://note.nkmk.me/python-import-module-search-path/)

## コメント

複数行のコメントは `"""` または `'''` で書く。

```python
def foo():
  """
  コメント1
  コメント2
  """
  print 'foo'
```

参考:

- [python > 複数行のコメント > indentに気をつける \- Qiita](https://qiita.com/7of9/items/5fb6d57ccb0ce9a47dd6)

## データ型

組み込み型: https://docs.python.org/ja/3/library/stdtypes.html

- int
  - bool
    - `True == 1`
    - `False == 0`

参考:

- [Pythonの真偽値bool型（True, False）と他の型との変換・判定 | note.nkmk.me](https://note.nkmk.me/python-bool-true-false-usage/)

### 真偽値

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

### シーケンス型 - list, tuple, range

ミュータブルなものとイミュータブルなものがある。tupleオブジェクトはイミュータブルらしい。

共通の演算:

- `len(s)` ... 長さ

#### ミュータブル

listオブジェクトとか。

演算:

- `s.append(x)` ... 要素追加

参考:

- [リスト \- 作成、取り出し、置換、追加、検索、削除、要素数 \- ひきメモ](http://d.hatena.ne.jp/yumimue/20071205/1196839438)
- [Python: リストの要素の追加と削除、取出し – append\(\)、extend\(\)、pop\(\)、remove\(\)メソッド](http://www.yukun.info/blog/2008/06/python-list2.html)

### マッピング型 - dict

https://docs.python.org/ja/3/library/stdtypes.html?highlight=dict#mapping-types-dict

ミュータブルなオブジェクト。  
hashableな値を任意のオブジェクトに対応付ける。

SYNOPSIS:

```python
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

### ヌル - None

`None` オブジェクト

## 演算子
### 二項演算子

[6. 式 (expression) — Python 3 ドキュメント](https://docs.python.org/ja/3/reference/expressions.html)

- `@` ... 行列の乗算

### 累算代入演算子

https://docs.python.org/ja/3/reference/simple_stmts.html#augmented-assignment-statements

Examples:

```Python
x += 1
x %= 3  # 剰余
x //= 5 # 切り捨て除算
```

NOTE:

- Rubyの `||=` 相当はない

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

https://docs.python.org/ja/3/tutorial/controlflow.html#if-statements

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

### ループ

```python
for i in range(1, 5):
  print(i)

list = ['a', 'b', 'c']
for elm in list:
  print(elm)
```

参考:

- [Python基礎講座\(9 反復\) \- Qiita](https://qiita.com/Usek/items/3a2f2529e2e7a0dd2542)

## クラス

https://docs.python.org/ja/3/tutorial/classes.html

## 例外処理

https://docs.python.jp/3/tutorial/errors.html

Examples:

```Python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
```


## 書式付き文字列

```python
'Hello, {}!'.format('world')
```

参考:

- [Python3での文字列フォーマットまとめ　旧型で生きるか、新型で生きるか \- Qiita](https://qiita.com/u_kan/items/2a7b4201beb0d467e5b8)

## ジェネレータ

反復可能なオブジェクト

- ジェネレータ関数 ... `yield` を使う
- ジェネレータ式

参考:

- [ジェネレータ (yield) | Python-izm](https://www.python-izm.com/advanced/generator/)

## 組み込み関数

https://docs.python.jp/3/library/functions.html

### list()

https://docs.python.jp/3/library/functions.html#func-list

Example:

```python
list(somedict.keys()) #=> dictのキーをリスト化
```

参考:

- [How to return dictionary keys as a list in Python? \- Stack Overflow](https://stackoverflow.com/questions/16819222/how-to-return-dictionary-keys-as-a-list-in-python)

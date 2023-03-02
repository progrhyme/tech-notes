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

## import

リファレンス:
- インポートシステム https://docs.python.org/ja/3/reference/import.html

### import文

https://docs.python.org/ja/3/reference/simple_stmts.html#import

例:

```Python
import a
from b import foo
from c import bar as baz, quz
```

参考:

- [Python, importの使い方（from, as, PEP8の推奨スタイル, 注意点など） | note.nkmk.me](https://note.nkmk.me/python-import-usage/)


### モジュール検索パス

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

## リテラル

https://docs.python.org/ja/3/reference/lexical_analysis.html#literals

### 文字列

Examples:

```Python
'foo'
"foo"
```

See also:

- [データ型 > テキストシーケンス型(str)]({{<ref types.md>}}#テキストシーケンス型---str)

参考:

- [Python | 文字列リテラルを記述する](https://www.javadrive.jp/python/string/index1.html)

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

### `*`, `**` 展開

- リストやタプルには `*`、dictには `**` を付けることで展開して、関数の引数にすることができる。

参考:
- [Pythonで関数の引数にリスト、タプル、辞書を展開して渡す | note.nkmk.me](https://note.nkmk.me/python-argument-expand/)

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

## 関数
### return

https://docs.python.org/ja/3/reference/simple_stmts.html#the-return-statement

構文:

```
return_stmt ::=  "return" [expression_list]
```

NOTE:

- 多値を返すこともできる

Examples:

```Python
def test():
    return 'abc', 100

a, b = test()
```

参考:

- [Pythonの関数で複数の戻り値を返す方法 | note.nkmk.me](https://note.nkmk.me/python-function-return-multiple-values/)

### decorator (デコレータ)

https://docs.python.org/ja/3/reference/compound_stmts.html#function-definitions

ある関数に対して、前処理や後処理などを追加したりできるシンタックスシュガー。

例:

```Python
@f1(arg)
@f2
def func(): pass
```

`@f1` や `@f2` がデコレータであり、 `func()` に対してネストして適用される。

上のコードはだいたい次と等価:

```Python
def func(): pass
func = f1(arg)(f2(func))
```

参考:

- [Pythonのデコレータについて - Qiita](https://qiita.com/mtb_beta/items/d257519b018b8cd0cc2e)

関連項目

- [memo/20230303/#排他制御のデコレータ]({{< ref "/a/memo/20230303.md" >}}#pythonで排他制御を実現するデコレータ)

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
except IOError as err:
    # 例外の連鎖/変換
    raise RuntimeError('Failed to open or read file!') from err
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
else:
    print("No error.")
finally:
    f.close()
```

参考:

- [Pythonの例外処理（try, except, else, finally） | note.nkmk.me](https://note.nkmk.me/python-try-except-else-finally/)

## 書式付き文字列

```python
a = "foo"
b = 123

'Hello, {}!'.format('world')

# f文字列 ... Python 3.6以上
print(f"{a} has {b} apples")
```

参考:

- [Python3での文字列フォーマットまとめ　旧型で生きるか、新型で生きるか \- Qiita](https://qiita.com/u_kan/items/2a7b4201beb0d467e5b8)
- [Pythonのf文字列（フォーマット済み文字列リテラル）の使い方 | note.nkmk.me](https://note.nkmk.me/python-f-strings/)

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

## トピック
### アンダースコア(`_`)

`_` の使い方:

1. 返り値を無視する
1. 関数や変数の役割を変える
1. 数字を読みやすくする

Examples:

```Python
a, _, c = (1, 2, 3)
# 先頭に１つの「_」で規約としてプライベート化する
# 「weak internal use」と呼ばれる
_foo = 'foo'
def _bar():
    return 'bar'

class Sample:
    # 普通のメソッドとして呼べなくなる
    # 疑似private関数
    def __foo():
        return 'foo'

n = 1_000_000 # 1000000 と同じ
```

参考:

- [Pythonのアンダースコア( _ )を使いこなそう！. Pythonを上手そうに見させる手品の一つ「アンダースコア」の4種類の使い方を説… | by Neil Wu | LSC PSD | Medium](https://medium.com/lsc-psd/pythonic%E8%89%B2%E3%80%85-python%E3%81%AE%E3%82%A2%E3%83%B3%E3%83%80%E3%83%BC%E3%82%B9%E3%82%B3%E3%82%A2-%E3%82%92%E4%BD%BF%E3%81%84%E3%81%93%E3%81%AA%E3%81%9D%E3%81%86-3c132842eeef)

---
title: "道場"
linkTitle: "道場"
date: 2020-08-20T16:32:43+09:00
weight: 30
---

Road to Pythonian.  
Pythonianを名乗るための基礎的なトピックを並べる予定。

## 値と変数
### 定数を使う

- 言語仕様上は定数はない
- 定数として扱う場合、 `FOO_VALUE` のように変数名を大文字 + アンダースコアで表すのが標準規約
- 定数を扱うためのクラスを作るテクニックがある

参考:

- [Python で定数を定義する | まくまくPythonノート](https://maku77.github.io/python/syntax/const.html)

## データ型
### 型変換

参考:

- [Python 3 で16進数とバイト列の相互変換 - Qiita](https://qiita.com/masakielastic/items/21ba9f68ef6c4fd7692d)

#### 整数 <=> 16進数文字列

```Python
# 整数 => 16進数文字列
format(0xabcd, 'x')     #=> 'abcd'
'{:02x}'.format(0xabcd) #=> 'abcd'
'%02x' % 0xabcd         #=> 'abcd'
hex(0xabcd)             #=> '0xabcd'

# 16進数文字列 => 整数
int('0xabcd', 16) #=> 43981
int('abcd', 16)   #=> 43981
```

#### 文字列 <=> 16進数文字列

```Python
# 文字列 => 16進数文字列
import binascii
binascii.hexlify(b'Hello') # => b'48656c6c6f'
binascii.b2a_hex(b'Hello') # => b'48656c6c6f'
binascii.hexlify(u'こんにちは'.encode('utf-8')) # => b'e38193e38293e381abe381a1e381af'
binascii.b2a_hex(u'こんにちは'.encode('utf-8')) # => b'e38193e38293e381abe381a1e381af'

import codecs
codecs.encode(b'Hello', 'hex_codec') # => b'48656c6c6f'
codecs.encode(u'こんにちは'.encode('utf-8'), 'hex_codec') # => b'e38193e38293e381abe381a1e381af'

# 16進数文字列 => 文字列
import binascii
binascii.unhexlify(b'48656c6c6f') # => b'Hello'
binascii.a2b_hex(b'48656c6c6f')   # => b'Hello'
binascii.unhexlify(b'e38193e38293e381abe381a1e381af').decode('utf-8') # => 'こんにちは'
binascii.a2b_hex(b'e38193e38293e381abe381a1e381af').decode('utf-8') # => 'こんにちは'

import codecs
codecs.decode(b'48656c6c6f', 'hex_codec') # => b'Hello'
codecs.decode(b'e38193e38293e381abe381a1e381af', 'hex_codec').decode('utf-8') # => 'こんにちは'
```

参考: [16進文字列と文字列の変換 - Qiita](https://qiita.com/atsaki/items/6120cad2e3c448d774bf)

#### 16進数文字列 <=> バイト列

```Python
import binascii
import codecs

# 16進数文字列 => バイト列
bytes.fromhex('abcd')        #=> b'\xab\xcd'
binascii.unhexlify('abcd')   # 同上
codecs.decode('abcd', 'hex') # 同上

# バイト列 => 16進数文字列
b'\xab\xcd'.hex()                           #=> 'abcd'
str(binascii.hexlify(b'\xab\xcd'), 'utf-8') # 同上
codecs.encode(b'\xab\xcd', 'hex')           #=> b'abcd'
str(b'abcd', 'utf-8')                       #=> 'abcd'
```

## 文字列処理
### 文字列検索 `in`, `not in`

```python
word = 'abcde'
'abc' in word #=> True
'x' in word #=> False

'abc' not in word #=> False
'x' not in word #=> True
```

参考:

- [Python3の文字列操作 \- Qiita](https://qiita.com/Kenta-Han/items/e64035e9c3e4ef08e394)

### 正規表現

See [library#re]({{<ref "library.md#">}}#re)

Examples:

```python
import re

# マッチ
content = r'Hello, Python. 123, end.'
pattern = 'Hel'

## compileしない
### re.match ... 先頭からぴったり一致する必要がある
match_result = re.match(pattern, content)
### re.search ... 存在すればOK
search_result = re.search(pattern, content)

## compileしてマッチ
repatter = re.compile(pattern)
match_result = repatter.match(content)

# 置換
re.sub('^H\w+', 'Good morning', 'Hello, world.')
## 大文字小文字を無視
re.sub('test', 'xxxx', 'Testing', flags=re.IGNORECASE)
```

参考:

- [分かりやすいpythonの正規表現の例 - Qiita](https://qiita.com/luohao0404/items/7135b2b96f9b0b196bf3)
- [Pythonで文字列を置換（replace, translate, re.sub, re.subn） | note.nkmk.me](https://note.nkmk.me/python-str-replace-translate-re-sub/)
- [python — re.compileせずに大文字と小文字を区別しない正規表現？](https://www.it-swarm.dev/ja/python/recompile%E3%81%9B%E3%81%9A%E3%81%AB%E5%A4%A7%E6%96%87%E5%AD%97%E3%81%A8%E5%B0%8F%E6%96%87%E5%AD%97%E3%82%92%E5%8C%BA%E5%88%A5%E3%81%97%E3%81%AA%E3%81%84%E6%AD%A3%E8%A6%8F%E8%A1%A8%E7%8F%BE%EF%BC%9F/958186732/)

## ライブラリの利用
### 外部ファイルの関数を利用

```Python
# mymodule.py
def foo(a, b):
    return a + b

# main.py
import mymodule
c = mymodule.foo(5, 10)
print(c)
```

参考:

- [Python で別ファイルに書いた関数を呼び出す方法 - Python の関数 - Python の基本 - Python 入門](https://python.keicode.com/lang/functions-call-function-defined-in-another-file.php)

## 例外処理

例外オブジェクトを文字列として扱うには、 `str(e)` のようにする。

参考:

- [python - Convert exception error to string - Stack Overflow](https://stackoverflow.com/questions/37684153/convert-exception-error-to-string)

## テスト
### 構文チェック

```sh
python -m py_compile foo.py
```

参考:

- [Pythonのシンタックスチェックに使えるコマンド - すっさんぽ](https://sussan-po.com/2017/10/23/python-syntax-check/)

## オブジェクト指向

```Python
# クラス名の取得
obj.__class__.__name__
```

参考:

- [オブジェクトのクラス名を文字列で取得する – Pythonプログラミング物語](https://pcl.solima.net/pyblog/archives/949)

## ロギング
### 変数のダンプ

クラスのインスタンスなど、 `__dict__` attributeを持つオブジェクトであれば `vars` 関数で1階層のダンプができる:

```Python
class MyClass:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

mc = MyClass(10, 20)
print(vars(mc)) #=> {'val1': 10, 'val2': 20}
```

参考:

- [Pythonでインスタンスの状態をダンプするにはvars()を使う - minus9d's diary](https://minus9d.hatenablog.com/entry/2015/08/02/204226)

## for文による射影操作

Examples:

```Python
keys = [1,2,3,4,5,6,7,8]
newkeys = [(k*2) for k in keys if k % 2 == 0]
```

参考:

- [Python3でforループ式をワンライナーで記述する - みずりゅの自由帳](https://mzryuka.hatenablog.jp/entry/2018/11/17/115720)

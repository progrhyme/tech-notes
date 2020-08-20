---
title: "道場"
linkTitle: "道場"
date: 2020-08-20T16:32:43+09:00
weight: 30
---

Road to Pythonian.  
Pythonianを名乗るための基礎的なトピックを並べる予定。

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
content = r'hellow python, 123, end.' 
pattern = 'hel'

## compileしない
result = re.match(pattern, content)
## compileしてマッチ
repatter = re.compile(pattern)
result = repatter.match(content)

# 置換
re.sub('^H\w+', 'Good morning', 'Hello, world.')
## 大文字小文字を無視
re.sub('test', 'xxxx', 'Testing', flags=re.IGNORECASE)
```

参考:

- [分かりやすいpythonの正規表現の例 - Qiita](https://qiita.com/luohao0404/items/7135b2b96f9b0b196bf3)
- [Pythonで文字列を置換（replace, translate, re.sub, re.subn） | note.nkmk.me](https://note.nkmk.me/python-str-replace-translate-re-sub/)
- [python — re.compileせずに大文字と小文字を区別しない正規表現？](https://www.it-swarm.dev/ja/python/recompile%E3%81%9B%E3%81%9A%E3%81%AB%E5%A4%A7%E6%96%87%E5%AD%97%E3%81%A8%E5%B0%8F%E6%96%87%E5%AD%97%E3%82%92%E5%8C%BA%E5%88%A5%E3%81%97%E3%81%AA%E3%81%84%E6%AD%A3%E8%A6%8F%E8%A1%A8%E7%8F%BE%EF%BC%9F/958186732/)

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

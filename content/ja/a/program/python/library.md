---
title: "標準ライブラリ"
linkTitle: "std-lib"
description: https://docs.python.org/ja/3/library/
weight: 100
date: 2020-06-20T20:27:53+09:00
---

※基本、Python3前提。

## dataclasses

https://docs.python.org/ja/3/library/dataclasses.html

データクラス

`__init__()` や `__repr__()` のような[特殊メソッド](https://docs.python.org/ja/3/glossary.html#term-special-method)を生成し、ユーザー定義のクラスに自動的に追加するデコレータや関数を提供する。

Example:

```Python
from dataclasses import dataclass

@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
```

この場合、下のような `__init__()` が追加される:

```Python
def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
    self.name = name
    self.unit_price = unit_price
    self.quantity_on_hand = quantity_on_hand
```

### @dataclasses.dataclass

```Python
@dataclasses.dataclass(*, init=True, repr=True, eq=True, order=False,
unsafe_hash=False, frozen=False, match_args=True, kw_only=False, slots=False)
```

引数解説（一部）

 引数 | デフォルト | 意味（`True`のとき）
------|-----------|-----
 `init` | `True` | `__init__()` メソッド生成
 `repr` | `True` | `__repr__()` メソッド生成
 `frozen` | `False` | フィールドへの代入は例外を発生させる。インスタンスは読み取り専用を模倣する

## datetime

https://docs.python.org/ja/3/library/datetime.html

日付、時刻モジュール。

### datetime.timedelta

https://docs.python.org/ja/3/library/datetime.html#timedelta-objects

経過時間、即ち、2つの時刻の差を表す。

Example:

```Python
>>> from datetime import timedelta
>>> delta = timedelta(
...     days=50,
...     seconds=27,
...     microseconds=10,
...     milliseconds=29000,
...     minutes=5,
...     hours=8,
...     weeks=2
... )
>>> # Only days, seconds, and microseconds remain
>>> delta
datetime.timedelta(days=64, seconds=29156, microseconds=10)
```


## os

https://docs.python.org/ja/3/library/os.html

ファイル名、コマンドライン引数、環境変数など

### os.getenv

https://docs.python.org/ja/3/library/os.html#os.getenv

```Python
os.getenv(key, default=None)
```

- 環境変数keyが存在すればその値を返し、存在しなければdefaultを返す
- key, default, 返り値は文字列

## os.path

https://docs.python.org/ja/3/library/os.path.html

パス名操作

```Python
>>> os.path.join('/', 'usr', 'local', 'bin')
'/usr/local/bin'
```

## pprint

https://docs.python.org/ja/3/library/pprint.html

Rubyの `pp` 的なもの。

## re

https://docs.python.org/ja/3/library/re.html

正規表現操作モジュール。

See also [道場#正規表現]({{<ref "dojo.md">}}#正規表現)

### フラグ

RegexFlagのインスタンス（Python v3.6〜）

 flag | 機能
------|-----
 re.I, re.IGNORECASE | 大文字・小文字を区別しない

## urllib.request

https://docs.python.org/ja/3/library/urllib.request.html

HTTPリクエストを送る。

使い方: https://docs.python.jp/3.6/howto/urllib2.html

## sys

https://docs.python.org/ja/3/library/sys.html

常に利用可能

### sys.exit

https://docs.python.org/ja/3/library/sys.html#sys.exit

```Python
sys.exit([arg])
```

Pythonを終了する。

引数(arg):
- 整数: 終了コード
  - 0 (デフォルト) ... 正常終了
  - 1-127 ... 異常終了
- 他の型のオブジェクト
  - オブジェクトがstderrに出力され、終了コードは1になる

## venv

https://docs.python.org/ja/3/library/venv.html

```sh
# 仮想環境の作成
python3 -m venv path/to/new_environment

# 仮想環境の利用
source path/to/new_environment/bin/activate

## module install
pip install <some_modules>

## installしたモジュールの表示
pip freeze

## 仮想環境の利用を終了
deactivate
```

参考:

- [venv: Python 仮想環境管理 - Qiita](https://qiita.com/fiftystorm36/items/b2fd47cf32c7694adc2e)

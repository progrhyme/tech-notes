---
title: "標準ライブラリ"
linkTitle: "library"
description: https://docs.python.org/ja/3/library/
date: 2020-06-20T20:27:53+09:00
---

※基本、Python3前提。

## os

https://docs.python.org/ja/3/library/os.html

ファイル名、コマンドライン引数、環境変数など

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

## urllib.request

https://docs.python.org/ja/3/library/urllib.request.html

HTTPリクエストを送る。

使い方: https://docs.python.jp/3.6/howto/urllib2.html

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

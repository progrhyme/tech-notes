---
title: "Python"
linkTitle: "Python"
description: https://www.python.org/
date: 2020-06-20T20:23:39+09:00
weight: 720
---

## はじめに

断りない限りPython3を前提とする。  
ただし、ぐぐった結果とかを貼っているものはPython2のことがあり得る。  
特にPython3に関する話題は「Python3」に書く。

## About

- 日本語サイト: https://www.python.jp/

## Getting Started

- ドキュメント: https://docs.python.org/ja/3/
  - 言語仕様: https://docs.python.org/ja/3/reference/
- コーディング規約(邦訳): http://pep8-ja.readthedocs.io/ja/latest/

## 様々なPython

- CPython ... 標準のC言語によるPython実装
- Cython http://cython.org/
- PyPy https://pypy.org/
  - PythonでPythonを実装したもの
- Boost.Python
  - https://www.boost.org/doc/libs/1_68_0/libs/python/doc/html/index.html

参考:

- [Cython から C\+\+ を使う — Cython 0\.17\.1 documentation](http://omake.accense.com/static/doc-ja/cython/src/userguide/wrapping_CPlusPlus.html)
- [Pythonで高速化処理！numbaとCythonの実行速度を比較してみた。 \- これで無理なら諦めて！世界一やさしいデータ分析教室](http://www.randpy.tokyo/entry/numba_cython)

## 開発環境
### Visual Studio Code
#### venvを使う

関係しそうな設定値が2つある。

 キー | 意味
-----|------
 python.venvFolders | ホームディレクトリ内で仮想環境を格納するフォルダのリスト
 python.venvPath | 仮想環境を格納するフォルダへのパス

どっちを指定すればいいのかわからん。。  
プロジェクトごとにvenvを作るような場合は venvFoldersに `.venv` を入れておけばいいのかな？

ある環境では `~/my/venv/` の下にまとめていたので、次のように設定した:

```JSON
"python.venvPath": "~/my/venv"
```

これで問題なさそう。  
VS CodeのWindowをリロードすると、Pythonインタプリタのリストにvenvのリストが出てくるようになった。

参考:

- [\[VS Code\] デフォルトで読み込む venv/virtualenv 環境のパス - てくなべ (tekunabe)](https://tekunabe.hatenablog.jp/entry/2018/12/28/vscode_venv_default_rolad)
- Windows: [【vscode】環境構築 #1-venvで仮想環境作成-【Python】 | ハチアンアーカイブズ](https://hachian.com/2019/09/19/vscode_venv/)

## How-to
### 文字列処理
#### 文字列検索 `in`, `not in`

```python
word = 'abcde'
'abc' in word #=> True
'x' in word #=> False

'abc' not in word #=> False
'x' not in word #=> True
```

参考:

- [Python3の文字列操作 \- Qiita](https://qiita.com/Kenta-Han/items/e64035e9c3e4ef08e394)

## Python3
### Python2との違い
#### 書式付き文字列

```python
## Python2
'Hello, %s!' % 'world'

## Python3
'Hello, {}!'.format('world')
```

参考:

- [Python3での文字列フォーマットまとめ　旧型で生きるか、新型で生きるか \- Qiita](https://qiita.com/u_kan/items/2a7b4201beb0d467e5b8)

#### print関数に括弧が必要

```python
## Python2
print 'Hello, world!'

## Python3
print('Hello, world!')
```

参考:

- [SyntaxError: Missing parentheses in call to 'print' と言われました \- Qiita](https://qiita.com/pugiemonn/items/94ac57ba1b7b03548efe)

### 2to3

- [26.7. 2to3 - Python 2 から 3 への自動コード変換 — Python 3.6.3 ドキュメント](https://docs.python.jp/3/library/2to3.html "26.7. 2to3 - Python 2 から 3 への自動コード変換 — Python 3.6.3 ドキュメント")

やるべきこと:

- `dict.has_key(key)` => `key in dict` に変換。

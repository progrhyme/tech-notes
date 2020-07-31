---
title: "パッケージ管理"
linkTitle: "パッケージ管理"
date: 2020-07-31T16:39:19+09:00
weight: 50
---

## pip

標準のパッケージマネージャー。

- [Reference Guide — pip 9\.0\.1 documentation](https://pip.pypa.io/en/stable/reference/)

### コマンド

Examples:

```sh
# パッケージのインストール
pip install PACKAGE

# パッケージの更新
## 最新に更新
pip install -U|--upgrade PACKAGE
### pip自体を最新に更新
pip install -U pip
## バージョン指定。ダウングレードも可
pip install urllib3==1.13.1

# パッケージリストを記したファイルに従ってパッケージ群をインストール
pip install -r requirements.txt

# インストールされたパッケージ一覧
pip list
## 更新可能なパッケージリスト
pip list -o
```

参考:

- [pipでアップデートするときのコマンド pip update - Qiita](https://qiita.com/HyunwookPark/items/242a8ceea656416b6da8)
- [Python Tips：pip そのものをアップデートしたい \- Life with Python](https://www.lifewithpython.com/2015/07/pip-upgrade-itself.html)

### Config file

https://pip.pypa.io/en/stable/user_guide/#config-file

- `$HOME/.pip/pip.conf` ... レガシーだが、今でもUnix/Macで有効。

参考:

- [pip\.confを作成してpip listの警告を消す \| Python / note\.nkmk\.me](https://note.nkmk.me/python-pip-list-deprecation-warning/)

### How-to
#### インストール済みのパッケージを一括更新

```sh
pip list -o | awk 'NR>2{print $1}' | xargs -t pip install -U
```

## Pipenv

python.org公式のパッケージツール。  
RubyのBundlerっぽい雰囲気。

公式:

- https://github.com/pypa/pipenv
- https://docs.pipenv.org/
  - 邦訳: http://pipenv-ja.readthedocs.io/ja/translate-ja/

参考:

- [pyenv と pipenv による python 環境 - Qiita](https://qiita.com/euxn23/items/fdd79bad28ccc0476a36)


### Install

https://pipenv-ja.readthedocs.io/ja/translate-ja/install.html#installing-pipenv

```sh
## Mac
brew install pipenv

## Fedora
sudo dnf install pipenv

## Python (pip)
pip install --user pipenv
```

## PyPI

https://pypi.python.org/pypi

the Python Package Index.  
RubyのRubyGems相当。

### .pypirc

アップロード先PyPIのサーバ情報や認証情報を記す設定ファイル

参考:

- [pypiへの登録方法 \- Qiita](https://qiita.com/nittyan/items/6dce0ab5598dda7f8f55)

## 3rd Party Tools
### pip-tools

https://github.com/jazzband/pip-tools
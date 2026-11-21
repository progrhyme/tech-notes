---
date: '2020-06-22T14:58:14+09:00'
description: https://pypi.org/
---

# 3rd-Party Packages

サードパーティー製のパッケージ。

## APScheduler

- https://pypi.org/project/APScheduler/
- https://github.com/agronholm/apscheduler

ジョブスケジューリングを可能にするライブラリ。

参考:

- [APSchedulerの使い方（初心者向け） - プログラミング原人の進化論](https://programgenjin.hatenablog.com/entry/2019/04/01/093005)

## Flask

- https://pypi.org/project/Flask/
- https://palletsprojects.com/p/flask/

### エンドポイントリストの取得

参考:

- [python - Get list of all routes defined in the Flask app - Stack Overflow](https://stackoverflow.com/questions/13317536/get-list-of-all-routes-defined-in-the-flask-app)
- [python - Display links to new webpages created - Stack Overflow](https://stackoverflow.com/questions/13151161/display-links-to-new-webpages-created/13161594#13161594)

## gunicorn

- https://pypi.org/project/gunicorn/
- https://gunicorn.org/

Documentation:

- https://docs.gunicorn.org/

参考:

- [Gunicorn を使用した Python アプリケーションのデプロイ | Heroku Dev Center](https://devcenter.heroku.com/ja/articles/python-gunicorn)

### 設定値

https://docs.gunicorn.org/en/latest/settings.html

 項目 | コマンドオプション | default | 説明
-----|-----------------|---------|-------
 timeout | `-t <INT>` `--timeout <INT>` | 30 | この時間に何の処理もしていない場合、ワーカーが再起動される。0を指定すると無限大

## pytest

Documentation: https://docs.pytest.org/

著名なテストフレームワーク。

Tips:

- [pytestのmarkを使って一部のテストをデフォルトで実行しない方法 - Qiita](https://qiita.com/yattom/items/dbee14d45a8fb936e2d0)

## Python-Markdown

Documentation: https://python-markdown.github.io/

PythonのMarkdownパーサ。MkDocs や [Zensical](../../software/static-site-generator/zensical.md) が使っている。
Extensions: https://python-markdown.github.io/extensions/

CommonMark(Hugo の goldmark や GitHub など)とは解釈が違うところがあり、そちら向けに書いた Markdown をそのまま使うと、リストが崩れる。
リストまわりの主な制約:

- リストの入れ子は、4スペース単位で字下げする。
    - 2スペースや、親項目の内容に揃えた3スペース(`1. ` の下に3スペース)では、入れ子にならない。
    - 項目の内側に書くコードブロックや段落も、同じ4スペース単位で字下げする。
- 段落の直後にリストを書くときは、空行を1行挟む。空行がないと、リストとして認識されない。

```markdown
参考:
- 項目       ← 空行がないので、リストにならない
```

- 同じ階層で、箇条書き(`-`)と番号付き(`1.`)を続けて書くと、間に空行を挟んでも1つのリストに連結される。分けたいときは、HTMLコメントを挟む。

```markdown
1. 番号付き

<!-- -->

- 箇条書き
```

検証には、変換前を CommonMark、変換後を Python-Markdown でレンダリングして、`ul`/`ol`/`li` の構造を比較すると良い。

参考: [2026-11-21 のメモ](../../memo/2026/20261121.md)

## requests

Documentation:

- 英語: [Requests: HTTP for Humans™ — Requests 2.23.0 documentation](https://requests.readthedocs.io/en/master/)
- 日本語: [Requests: 人間のためのHTTP — requests-docs-ja 1.0.4 documentation](http://requests-docs-ja.readthedocs.org/en/latest/) ... 古いのであまり読まない方がよさそう

### カスタムヘッダを付ける

https://requests.readthedocs.io/en/latest/user/quickstart/#custom-headers

dict型の `header` パラメータを渡せばいい。

```Python
>>> url = 'https://api.github.com/some/endpoint'
>>> headers = {'user-agent': 'my-app/0.0.1'}

>>> r = requests.get(url, headers=headers)
```

## retry

https://github.com/invl/retry

デコレータを付けるだけで簡単に関数にリトライを実装できる。

Examples:

```Python
# 最大4回トライする（4回実行してすべてエラーだったらエラーとする）
# トライの間隔は、5秒から始めて、10秒、20秒と2倍ずつ増やしていく
@retry(tries=4, delay=5, backoff=2)
def crawl_url(url):
    print ("crawling...")
    f = urllib.request.urlopen(url)
    return f.read()
```

参考:

- [Tech Tips: 便利なPythonライブラリ（５）retry](http://techtipshoge.blogspot.com/2016/04/pythonretry.html)

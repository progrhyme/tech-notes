---
title: "jq"
linkTitle: "jq"
description: https://stedolan.github.io/jq/
date: 2020-05-07T11:44:41+09:00
weight: 300
---

JSONにクエリしてフィルタできるCLIツール。

## Documents

- https://stedolan.github.io/jq/tutorial/
- https://stedolan.github.io/jq/manual/

## チートシート

```sh
# オブジェクトの特定キーの要素を抽出
cat foo.json | jq '.some_key'

# 配列の特定要素を抽出
cat foo.json | jq '.[0]'

# 配列の個々のオブジェクトの特定キーを抽出
cat foo.json | jq '.[] | .some_key'

# 配列の個々のオブジェクトからいくつかの要素を選んでそれぞれ配列に格納
cat foo.json | jq '.[] | [.keyA, .keyB, .keyC.keyAinC]'

# CSV形式で出力
cat foo.json | jq '.[] | [.keyA, .keyB, .keyC] | @csv'

# 配列の個々のオブジェクトからいくつかの要素を選んで新たなオブジェクトを作り、それぞれ出力
cat foo.json | jq '.[] | {a: .keyA, b: .keyB, ca: .keyC.keyAinC}'

# 配列の要素を特定のフィールドの値でフィルタ
cat foo.json | jq '.[] | select(.keyA == "foo")'
```

参考:

- [jq チートシート - Qoosky](https://www.qoosky.io/techs/1ee07c140f)
- [jq コマンドで JSON を CSV に変換する - VELTRA Engineering - Medium](https://medium.com/veltra-engineering/jq-supports-json-to-csv-fb5c951a9575)
- [jq で 条件にマッチするオブジェクトを取り出す where 句的なこと - それマグで！](https://takuya-1st.hatenablog.jp/entry/2016/12/26/180057)

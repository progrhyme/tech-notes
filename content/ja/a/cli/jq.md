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

# 配列の個々のオブジェクトからいくつかの要素を選んで新たなオブジェクトを作り、それぞれ出力
cat foo.json | jq '.[] | {a: .keyA, b: .keyB, ca: .keyC.keyAinC}'
```

参考:

- [jq チートシート - Qoosky](https://www.qoosky.io/techs/1ee07c140f)

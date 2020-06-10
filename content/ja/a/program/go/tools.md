---
title: "tools"
linkTitle: "tools"
description: https://pkg.go.dev/golang.org/x/tools
date: 2020-05-31T16:18:38+09:00
weight: 820
---

## About

Go言語による開発を支援する様々な公式ツール

- https://github.com/golang/tools Mirror

See Also:

- [エコシステム]({{<ref "ecosystem/_index.md">}})

## cmd/goimports

https://pkg.go.dev/golang.org/x/tools/cmd/goimports

Install:

```bash
go get golang.org/x/tools/cmd/goimports
```

`goimports` というコマンドが入る。  
`go fmt` のときに使われてないpkgの `import` 文を削除してくれる。

Goglandだと `Settings > Go > On Save > On save run` で設定できる。

参考:

- [goのimportを自動的に追加/削除してくれる「goimports」を試してみた - Misc Notes](http://y0m0r.hateblo.jp/entry/20140112/1389501259 "goのimportを自動的に追加/削除してくれる「goimports」を試してみた - Misc Notes")
- [Gogland で保存時に go fmt を走らせる - Qiita](http://qiita.com/kuro_milk/items/6adbf544dcb333d0f472 "Gogland で保存時に go fmt を走らせる - Qiita")

## cmd/present

https://godoc.org/golang.org/x/tools/cmd/present

プレゼンテーションを表示するWebサーバを起動する。

## present

https://godoc.org/golang.org/x/tools/present

プレゼンテーションのファイル・フォーマットを規定する。

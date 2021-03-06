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

## cmd/godoc

https://pkg.go.dev/golang.org/x/tools/cmd/godoc

godoc.org でも使われているWebサーバ。  
ローカルで起動してGoDocをブラウザで閲覧できる。  
（そういえば pkg.go.dev の中はどうなってるんだろう）

NOTE:

- `go doc` とは別のツール

参考:

- [チョットできるGoプログラマーになるための詳解GoDoc - Qiita](https://qiita.com/shibukawa/items/8c70fdd1972fad76a5ce)

### Usage

Examples:

```sh
godoc -goroot $HOME/go [OPTIONS]
GOROOT=$HOME/go godoc -analysis type
# ヘルプ
godoc -help
```

 Option | 説明
--------|------
 -http=ADDR | サーバアドレスを指定する。デフォルトは `localhost:6060`
 -index | 検索を有効にする

NOTE:

- 2020-07-08現在、 `GOROOT` 環境変数 or `-goroot` オプションがないとエラーになる

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

## cmd/gorename

https://pkg.go.dev/golang.org/x/tools/cmd/gorename

リファクタリングツール。  
関数名、変数名などを一括変更できる。

Examples:

```sh
gorename -from '"github.com/progrhyme/shelp/internal/cli".installCmd.name' -to op -v
```

 Option | 機能
--------|------
 -d | rewriteせずにdiffを表示
 -v | 冗長ログ表示

NOTE:

- exportされた名前を対象にすると、 GOPATH 下の全パッケージがスキャンされ、非常に時間がかかることがある
  - 解決するためのラッパースクリプトを書いた。↓のQiita記事参照

参考:

- [Big Sky :: golang のリファクタリングには gofmt ではなく、gorename を使おう。](https://mattn.kaoriya.net/software/lang/go/20150113141338.htm)
- [gorenameでexportした変数名でも短時間でリネームするためのシェルスクリプトを書いた - Qiita](https://qiita.com/progrhyme/items/526a2861b5b06a879dc8)

## cmd/present

https://godoc.org/golang.org/x/tools/cmd/present

プレゼンテーションを表示するWebサーバを起動する。

## present

https://godoc.org/golang.org/x/tools/present

プレゼンテーションのファイル・フォーマットを規定する。

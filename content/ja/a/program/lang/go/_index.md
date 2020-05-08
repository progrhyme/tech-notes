---
title: "Go"
linkTitle: "Golang"
description: >
  Go言語 https://golang.org
date: 2020-04-26T08:01:51+09:00
weight: 200
---

## Getting Started

### ドキュメント

- https://golang.org/doc/
  - https://golang.org/doc/effective_go.html
- http://golang-jp.org/ ... golang.orgの日本語訳プロジェクト

#### 3rd Party がまとめた資料

- [GoのためのGo](https://motemen.github.io/go-for-go-book/)
- [Go Language Programs, Tutorial, Articles and Examples](http://www.golangprograms.com/ "Go Language Programs, Tutorial, Articles and Examples")

### Play Ground

Sandbox https://play.golang.org/

### 記事

- [6年間におけるGoのベストプラクティス | プログラミング | POSTD](http://postd.cc/go-best-practices-2016/ "6年間におけるGoのベストプラクティス | プログラミング | POSTD")

## 開発ツール

### goimports

https://godoc.org/golang.org/x/tools/cmd/goimports

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


## ビルトイン関数
### append

https://golang.org/pkg/builtin/#append

`func append(slice []Type, elems ...Type) []Type`

sliceに要素、またはsliceを結合し、新たなsliceを返す。

```go
slice = append(slice, elem1, elem2)
slice = append(slice, anotherSlice...)
```

## Topics

### vendoring

アプリケーションなどで、依存パッケージを管理する仕組み。  
Go 1.6から正式にサポートされた。  
Go 1.5ではexperimental扱いで、有効化するには環境変数 `GO15VENDOREXPERIMENT` を設定してコンパイルする必要がある。

vendoringのためのツールとして、glideやgomなどがある。

参考:

- [今更だけどGoのVendoringについて思いをはせる - Qiita](http://qiita.com/okamos/items/587a5693a3ae9cae9b88 "今更だけどGoのVendoringについて思いをはせる - Qiita")
- [go vendoring - 隙あらば寝る](http://yoru9zine.hatenablog.com/entry/2016/02/02/054922 "go vendoring - 隙あらば寝る")
- [Glide で Go 言語のパッケージ管理と vendoring - Librabuch](https://librabuch.jp/blog/2016/04/go-lang-vendoring-glide/ "Glide で Go 言語のパッケージ管理と vendoring - Librabuch")

### enum

Goにはenumがない。  
intの独自型を定義するのがイディオムになっている。

```go
type Fruit int

const (
    Apple Fruit = iota
    Orange
    Banana
)

var myFruit Fruit
```

この独自型に対して `String()` メソッドを実装しておくと、名前が引けて便利:

```go
func (f Fruit) String() string {
    switch f {
    case Apple:
        return "Apple"
    case Orange:
        return "Orange"
    case Banana:
        return "Banana"
    default:
        return "Unknown"
    }
}
```

`golang.org/x/tools/cmd/stringer` で `String()` メソッドを含むコードを自動生成することもできる。

参考:

- [GoのEnumイディオム - Qiita](http://qiita.com/awakia/items/c81c7816b9aea5422250 "GoのEnumイディオム - Qiita")
- [Big Sky :: Re: GoLangでJavaのenumっぽいライブラリ作った話](https://mattn.kaoriya.net/software/lang/go/20141208093852.htm "Big Sky :: Re: GoLangでJavaのenumっぽいライブラリ作った話")
- [Ten Useful Techniques in Go – Fatih Arslan](https://arslan.io/2015/10/08/ten-useful-techniques-in-go/ "Ten Useful Techniques in Go – Fatih Arslan")
- https://godoc.org/golang.org/x/tools/cmd/stringer

### build

https://golang.org/pkg/go/build/

`Build Constraints` という機能は「build tag」としても知られている。  
こんなの:

```go
// (A)
// +build foo

// (B)
// +build !foo
```

(A) `go build -tags=foo` でビルドされる。  
(B) `go build` でビルドされる。

参考:

- [go build -tagsを使ってRelease/Debugを切り替える - flyhigh](http://shinpei.github.io/blog/2014/10/07/use-build-constrains-or-build-tag-in-golang/ "go build -tagsを使ってRelease/Debugを切り替える - flyhigh")

### プロファイリング

- [runtime/pprof](https://golang.org/pkg/runtime/pprof/ "pprof - The Go Programming Language")という標準pkgを使うのが基本な感じ。
  - その内 [標準パッケージ - progrhyme's Tech Wiki](https://sites.google.com/site/progrhymetechwiki/programming/go/std-pkg "標準パッケージ - progrhyme's Tech Wiki") に書くと思う。
- runtimeのデバッグに役立つ環境変数の話:
  - [GODEBUG | Dave Cheney](https://dave.cheney.net/tag/godebug "GODEBUG | Dave Cheney")

参考:

- [Profiling Go Programs - The Go Blog](https://blog.golang.org/profiling-go-programs "Profiling Go Programs - The Go Blog") ... pprof
- [golangで書かれたプログラムのメモリ使用状況を見る - hakobe-blog ♨](http://hakobe932.hatenablog.com/entry/2014/04/10/010619 "golangで書かれたプログラムのメモリ使用状況を見る - hakobe-blog ♨") ... pprof, net/http/pprof
- [golang profiling の基礎](https://www.slideshare.net/yuichironakazawa2/golang-profiling-77163552 "golang profiling の基礎") ... pprof他
- [golangパフォーマンス3: mapとGC - Qiita](http://qiita.com/oywc410/items/ad8baee00f039705a5c0 "golangパフォーマンス3: mapとGC - Qiita")

## Child Pages

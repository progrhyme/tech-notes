---
title: "Go"
linkTitle: "Golang"
description: >
  Go言語 https://golang.org
date: 2020-04-26T08:01:51+09:00
weight: 200
---

## Getting Started

- [A Tour of Go](https://tour.golang.org/) ... Web上でコードを動かしてGoプログラミングを体験できるチュートリアル
- https://go.dev/ ... Gopher向けのポータルみたいなサイト

### Play Ground

https://play.golang.org/

Web上で動作するSandbox環境。

## Documentation

- https://golang.org/doc/
  - https://golang.org/doc/effective_go.html
- http://golang-jp.org/ ... golang.orgの日本語訳プロジェクト

## Goを学ぶ

https://learn.go.dev/ に教材がたくさん転がっている。

- [Go by Example](https://gobyexample.com/) ... 言語仕様や標準パッケージの使い方がハンズオンで学べる
  - 邦訳: [Go by Example](https://oohira.github.io/gobyexample-jp/)
- [CodeReviewComments · golang/go Wiki](https://github.com/golang/go/wiki/CodeReviewComments) ... Goらしい書き方を学べる
  - 邦訳: [Go Codereview Comments](https://knsh14.github.io/translations/go-codereview-comments/)
- [The Go Programming Language Blog](https://blog.golang.org/) / 公式ブログ

非公式サイト:

- [GoのためのGo](https://motemen.github.io/go-for-go-book/) ... オンライン教本 by motemen氏
- [Go Language Programs, Tutorial, Articles and Examples](http://www.golangprograms.com/ "Go Language Programs, Tutorial, Articles and Examples")

### 記事

- 2016年 [6年間におけるGoのベストプラクティス | プログラミング | POSTD](http://postd.cc/go-best-practices-2016/ "6年間におけるGoのベストプラクティス | プログラミング | POSTD")

## Programming Tips

コーディングする上で知っておくと便利なTips.

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

## Topics
### ディレクトリ構成

https://github.com/golang-standards/project-layout

unofficialだけど、上が最も有名そう。

解説記事:

- [Goの標準プロジェクトレイアウトを読み解く - Tech Do | メディアドゥの技術ブログ](https://techdo.mediado.jp/entry/2019/01/18/112503)
  - 実例となるリポジトリへのリンクもある

『みんなのGo言語』で紹介されていたサンプルはちょっと違う。  
例えば、下の記事で紹介されている:

- [Goパッケージの配置ルールとディレクトリ構成 | Hodalog](https://hodalog.com/golang-standard-project-layout/)

具体的には、 `pkg/` がない。  
[Songmu/ghg](https://github.com/Songmu/ghg)などもそうなっている。  
まあ別にルートディレクトリがごちゃっとならないなら `pkg/` を切らなくてもいいのでは、という気がする。

参考:

- [Goのパッケージ構成の失敗遍歴と現状確認 - timakin - Medium](https://medium.com/@timakin/go%E3%81%AE%E3%83%91%E3%83%83%E3%82%B1%E3%83%BC%E3%82%B8%E6%A7%8B%E6%88%90%E3%81%AE%E5%A4%B1%E6%95%97%E9%81%8D%E6%AD%B4%E3%81%A8%E7%8F%BE%E7%8A%B6%E7%A2%BA%E8%AA%8D-fc6a4369337)

#### CLI

小さいCLIで、ライブラリとして提供しないものは、下のような感じでもよさそう:

```
.
├── internal
│   ├── bar
│   └── foo
└── main.go
```

https://golang.org/src/cmd/go/ とか割とそんな感じに見える。

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

### WebAssembly対応

2020-05-31記載。

LLVMベースのコンパイラなのでWASMに対応しているという[TinyGo](https://tinygo.org/)の存在をいま知ったところだけど、Go本体も1.11でWASMを実験的にサポートしたそうだ。

GitHub WikiにWebAssemblyのページがある:

- https://github.com/golang/go/wiki/WebAssembly

> Go 1.11 added an experimental port to WebAssembly. Go 1.12 has improved some parts of it, with further improvements expected in Go 1.13.

気になったので、1.13, 1.14のリリースノートを確認した。

https://golang.org/doc/go1.14#wasm

`js.Value` オブジェクト（Goから参照されるJavaScriptの値）がガベージコレクションの対象になったとか。

https://golang.org/doc/go1.13#ports

`GOARCH=wasm` でWASMコンパイルするとき、 `GOWASM` 環境変数にカンマ区切りで実験的なフィーチャーリストを指定できるようになった。  
有効な値は https://golang.org/cmd/go/#hdr-Environment_variables に記されている。  
2020-05-31現在は `setconv`, `signext` が指定可能。

## 歴史
### ライブラリ管理
#### dep

https://golang.github.io/dep/

「Dep」という依存パッケージ管理ツール。
Go 1.11〜1.13で公式の実験的な扱いだった。

- ドキュメント: https://golang.github.io/dep/docs/

#### vendoring

アプリケーションなどで、依存パッケージを管理する仕組み。  
Go 1.6から正式にサポートされた。  
Go 1.5ではexperimental扱いで、有効化するには環境変数 `GO15VENDOREXPERIMENT` を設定してコンパイルする必要がある。

vendoringのためのツールとして、glideやgomなどがある。

参考:

- [今更だけどGoのVendoringについて思いをはせる - Qiita](http://qiita.com/okamos/items/587a5693a3ae9cae9b88 "今更だけどGoのVendoringについて思いをはせる - Qiita")
- [go vendoring - 隙あらば寝る](http://yoru9zine.hatenablog.com/entry/2016/02/02/054922 "go vendoring - 隙あらば寝る")
- [Glide で Go 言語のパッケージ管理と vendoring - Librabuch](https://librabuch.jp/blog/2016/04/go-lang-vendoring-glide/ "Glide で Go 言語のパッケージ管理と vendoring - Librabuch")

## Child Pages

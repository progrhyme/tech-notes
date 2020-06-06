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

## go CLI

`go` コマンド。

https://golang.org/pkg/cmd/go/

Examples:

```sh
# ビルド
go build

# パッケージ取得
go get

# モジュール管理
go mod

# 実行
go run

# テスト
go test

# 静的解析によって疑わしい問題を報告
go vet

# バージョン表示
go version

# ヘルプ
go help [command]
```

参考:

- [go vetの使い方(go vetとは) - Qiita](https://qiita.com/marnie_ms4/items/b343165efb4235906db7)

## Road to Gopher

Gopherを名乗る上で必須と思われる基礎的なトピックを扱う（予定）。

### 例外処理

入門ガイド:

- [Go by Example: Panic](https://gobyexample.com/panic)
- https://golang.org/ref/spec#Handling_panics

関連項目:

- [言語仕様#panic]({{<ref "spec.md">}}#panic)
- [言語仕様#defer]({{<ref "spec.md">}}#defer)

参考:

- [Go言語のエラーハンドリングについて - Qiita](https://qiita.com/nayuneko/items/3c0b3c0de9e8b27c9548)
- [Defer, Panic, and Recover - The Go Blog](https://blog.golang.org/defer-panic-and-recover)
- [panicはともかくrecoverに使いどころはほとんどない - Qiita](https://qiita.com/ruiu/items/ff98ded599d97cf6646e)
- [golangでrecoverしたときの戻り値 - PartyIX](https://h3poteto.hatenablog.com/entry/2015/12/13/010000)

### 値渡しとポインタ渡し

関連項目:

- [言語仕様#ポインタ]({{<ref "spec.md">}}#ポインタ)

参考:

- [Goでxxxのポインタを取っているプログラムはだいたい全部間違っている - Qiita](http://qiita.com/ruiu/items/e60aa707e16f8f6dccd8 "Goでxxxのポインタを取っているプログラムはだいたい全部間違っている - Qiita")
- [Go言語（golang）における値渡しとポインタ渡しのパフォーマンス影響について - Finatext - Medium](https://medium.com/finatext/go%E8%A8%80%E8%AA%9E-golang-%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E5%80%A4%E6%B8%A1%E3%81%97%E3%81%A8%E3%83%9D%E3%82%A4%E3%83%B3%E3%82%BF%E6%B8%A1%E3%81%97%E3%81%AE%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9%E5%BD%B1%E9%9F%BF%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6-70aa3605adc5)

### コマンドライン引数

入門サンプル:

- [Go by Example: Command-Line Arguments](https://gobyexample.com/command-line-arguments)

関連項目:

- [pkg (stdlib) > flag]({{<ref "std-pkg/flag.md">}})

参考:

- [2020-05-31#GolangのCLIパッケージを改めて探した]({{<ref "20200531.md">}}#golangのcliパッケージを改めて探した)

### ライブラリ管理

[Go 1.14](https://golang.org/doc/go1.14)からGo Modulesが標準機能になったので、これを使いましょう。

ドキュメント:

- https://github.com/golang/go/wiki/Modules
- [Go Modules Reference - The Go Programming Language](https://golang.org/ref/mod)

参考:

- [Using Go Modules - The Go Blog](https://blog.golang.org/using-go-modules)
- [Go言語の依存モジュール管理ツール Modules の使い方 - Qiita](https://qiita.com/uchiko/items/64fb3020dd64cf211d4e)

### 構造体の使い方

参考:

- [Go言語での構造体実装パターン · THINKING MEGANE](https://blog.monochromegane.com/blog/2014/03/23/struct-implementaion-patterns-in-golang/)

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

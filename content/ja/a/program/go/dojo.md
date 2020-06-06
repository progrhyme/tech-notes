---
title: "Road to Gopher"
linkTitle: "道場"
date: 2020-06-06T18:08:05+09:00
weight: 40
---

Gopherを名乗る上で必須と思われる基礎的なトピックを扱う（予定）。

## 入出力

関連項目:

- [pkg (stdlib) > io]({{<ref "std-pkg/_index.md">}}#io)

## 例外処理

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

## 値渡しとポインタ渡し

基本、よほどデータが大きくならない限りは値渡しでよさそう。

関連項目:

- [言語仕様#ポインタ]({{<ref "spec.md">}}#ポインタ)

参考:

- [Goでxxxのポインタを取っているプログラムはだいたい全部間違っている - Qiita](http://qiita.com/ruiu/items/e60aa707e16f8f6dccd8 "Goでxxxのポインタを取っているプログラムはだいたい全部間違っている - Qiita")
- [Go言語（golang）における値渡しとポインタ渡しのパフォーマンス影響について - Finatext - Medium](https://medium.com/finatext/go%E8%A8%80%E8%AA%9E-golang-%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E5%80%A4%E6%B8%A1%E3%81%97%E3%81%A8%E3%83%9D%E3%82%A4%E3%83%B3%E3%82%BF%E6%B8%A1%E3%81%97%E3%81%AE%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9%E5%BD%B1%E9%9F%BF%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6-70aa3605adc5)

## コマンドライン引数

入門サンプル:

- [Go by Example: Command-Line Arguments](https://gobyexample.com/command-line-arguments)

関連項目:

- [pkg (stdlib) > flag]({{<ref "std-pkg/flag.md">}})

参考:

- [2020-05-31#GolangのCLIパッケージを改めて探した]({{<ref "20200531.md">}}#golangのcliパッケージを改めて探した)

## ライブラリ管理

[Go 1.14](https://golang.org/doc/go1.14)からGo Modulesが標準機能になったので、これを使いましょう。

ドキュメント:

- https://github.com/golang/go/wiki/Modules
- [Go Modules Reference - The Go Programming Language](https://golang.org/ref/mod)

参考:

- [Using Go Modules - The Go Blog](https://blog.golang.org/using-go-modules)
- [Go言語の依存モジュール管理ツール Modules の使い方 - Qiita](https://qiita.com/uchiko/items/64fb3020dd64cf211d4e)

## 構造体の使い方

関連項目:

- [言語仕様#構造体]({{<ref "spec.md">}}#構造体)

参考:

- [Go言語での構造体実装パターン · THINKING MEGANE](https://blog.monochromegane.com/blog/2014/03/23/struct-implementaion-patterns-in-golang/)

## インタフェースの使い方

関連項目:

- [言語仕様#インタフェース]({{<ref "spec.md">}}#インタフェース)
- [言語仕様#Type-assertions]({{<ref "spec.md">}}#type-assertions)

参考:

- [【Golang】Golangのinterfaceで知っておくとお得なTips - Qiita](https://qiita.com/romukey/items/e49e28b7dcf645ac91c7)

### Type switches

型アサーションをswitch文と組合せて、値の型によって処理を分岐できる。  
例外処理などでも便利そう。

入門ガイド:

- [Type switches - A Tour of Go](https://tour.golang.org/methods/16)

Examples:

```go
switch v := i.(type) {
case int:
  fmt.Printf("Twice %v is %v\n", v, v*2)
case string:
  fmt.Printf("%q is %v bytes long\n", v, len(v))
default:
  fmt.Printf("I don't know about type %T!\n", v)
}
```

## プロファイリング

※2017年以前の情報

- [runtime/pprof](https://golang.org/pkg/runtime/pprof/ "pprof - The Go Programming Language")という標準pkgを使うのが基本な感じ。
  - その内 [標準パッケージ - progrhyme's Tech Wiki](https://sites.google.com/site/progrhymetechwiki/programming/go/std-pkg "標準パッケージ - progrhyme's Tech Wiki") に書くと思う。
- runtimeのデバッグに役立つ環境変数の話:
  - [GODEBUG | Dave Cheney](https://dave.cheney.net/tag/godebug "GODEBUG | Dave Cheney")

参考:

- [Profiling Go Programs - The Go Blog](https://blog.golang.org/profiling-go-programs "Profiling Go Programs - The Go Blog") ... pprof
- [golangで書かれたプログラムのメモリ使用状況を見る - hakobe-blog ♨](http://hakobe932.hatenablog.com/entry/2014/04/10/010619 "golangで書かれたプログラムのメモリ使用状況を見る - hakobe-blog ♨") ... pprof, net/http/pprof
- [golang profiling の基礎](https://www.slideshare.net/yuichironakazawa2/golang-profiling-77163552 "golang profiling の基礎") ... pprof他
- [golangパフォーマンス3: mapとGC - Qiita](http://qiita.com/oywc410/items/ad8baee00f039705a5c0 "golangパフォーマンス3: mapとGC - Qiita")
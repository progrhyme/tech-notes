---
title: "Road to Gopher"
linkTitle: "道場"
date: 2020-06-06T18:08:05+09:00
weight: 40
---

Gopherを名乗る上で必須と思われる基礎的なトピックを扱う（予定）。

前提:

- [言語仕様]({{<ref "spec.md">}})の内容を把握していること

## 入出力

関連項目:

- [pkg (stdlib) > io]({{<ref "std-pkg/_index.md">}}#io)
- [pkg (stdlib) > io/ioutil]({{<ref "std-pkg/_index.md">}}#ioioutil)

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

メモ:

- 基本、よほどデータが大きくならない限りは値渡しでよさそう
- オブジェクトの中身を書き換えるような処理だと、ポインタ渡しじゃないと駄目。そりゃそうか

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

## 外部コマンド実行

関連項目:

- [pkg (stdlib) > os/exec]({{<ref "std-pkg/_index.md">}}#osexec)

## ファイル操作

関連項目:

- [pkg (stdlib) > os]({{<ref "std-pkg/os.md">}})
- [pkg (stdlib) > io/ioutil]({{<ref "std-pkg/_index.md">}}#ioioutil)

### 実行可能ファイルを判定

Examples:

```go
func isExecutableFile(f os.FileInfo) {
  return !f.IsDir() && f.Mode()&0111 != 0
}
```

参考:

- [unix - How to check if a file is executable in go? - Stack Overflow](https://stackoverflow.com/questions/60128401/how-to-check-if-a-file-is-executable-in-go)

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

### 埋め込み

struct Aをstruct Bに埋め込むと、Bから直接Aのメンバー変数やメソッドにアクセスできる。  
OOPの継承のようなことができる。

※処理をAに委譲しているだけなので、厳密には継承とは異なる。

Examples:

```go
type A struct {
    Name string
    Age  int
}

type B struct {
    A
    // ポインタの場合は *A にして &A{} を渡す
}

func (b B) Print() {
    // 埋め込みで A の Name と Age が使える
    println("name:", b.Name, ", age:", b.Age)
    // 以下でも同じ
    println("name:", b.A.Name, ", age:", b.A.Age)
}

func main() {
    b := B{A{"Tanaka", 31}}
    b.Print() // name: Tanaka, age: 31
}
```

参考:

- [Go言語(golang) 構造体の定義と使い方 - golangの日記](https://golang.hateblo.jp/entry/golang-how-to-use-struct)

### 無名struct

Examples:

```go
anonymous := struct {
  name string
  age int
}{"Taro YAMADA", 24}
```

## インタフェースの使い方

関連項目:

- [言語仕様#インタフェース]({{<ref "spec.md">}}#インタフェース)
- [言語仕様#Type-assertions]({{<ref "spec.md">}}#type-assertions)

参考:

- [インタフェースの実装パターン #golang - Qiita](https://qiita.com/tenntenn/items/eac962a49c56b2b15ee8)
- [【Golang】Golangのinterfaceで知っておくとお得なTips - Qiita](https://qiita.com/romukey/items/e49e28b7dcf645ac91c7)

### ダックタイピング

https://play.golang.org/p/aja9eLk-4-n に動作例を書いた。

Examples:

```go
type walker interface {
	walk()
}

type human struct {
	name string
}

type dog struct {
	name string
}

func (h *human) walk() {
	fmt.Printf("I am %s, walking now.\n", h.name)
}

func (d *dog) walk() {
	fmt.Printf("Bow wow! (%s is walking)", d.name)
}

func watch(w walker) {
	w.walk()
}

func main() {
	h := &human{"Ken"}
	d := &dog{"Hachi"}
	watch(h)
	watch(d)
}
```

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

## オブジェクト指向プログラミング

Golangは型の継承をサポートしていないが、構造体とインタフェースを使いこなすと、オブジェクト指向プログラミングを実現ことができる。

NOTE:

- 構造体の埋め込みは継承とは異なるので、注意が必要
- インタフェースを使うとダックタイピングができるが、インタフェースはレシーバにはできない

参考:

- [Frequently Asked Questions (FAQ) - The Go Programming Language#Is_Go_an_object-oriented_language](https://golang.org/doc/faq#Is_Go_an_object-oriented_language)
- [Go言語で「embedded で継承ができる」と思わないほうがいいのはなぜか？ - Qiita](https://qiita.com/Maki-Daisuke/items/511b8989e528f7c70f80)
- [オブジェクト指向言語としてGolangをやろうとするとハマること - Qiita](https://qiita.com/shibukawa/items/16acb36e94cfe3b02aa1)
  - 上の牧さんの記事とほぼ同じことを言っている
- [Goはオブジェクト指向言語だろうか？ | POSTD](https://postd.cc/is-go-object-oriented/)

## 正規表現

Webサーバなどで使うときは、パフォーマンスに気をつける必要がありそう。

関連項目:

- [pkg (stdlib) > regexp]({{<ref "std-pkg/_index.md">}}#regexp)

参考:

- [逆引きGolang (正規表現)](https://ashitani.jp/golangtips/tips_regexp.html)
- [regexpとの付き合い方 〜 Go言語標準の正規表現ライブラリのパフォーマンスとアルゴリズム〜 - Eureka Engineering - Medium](https://medium.com/eureka-engineering/regexp%E3%81%A8%E3%81%AE%E4%BB%98%E3%81%8D%E5%90%88%E3%81%84%E6%96%B9-go%E8%A8%80%E8%AA%9E%E6%A8%99%E6%BA%96%E3%81%AE%E6%AD%A3%E8%A6%8F%E8%A1%A8%E7%8F%BE%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AA%E3%81%AE%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9%E3%81%A8%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0-984b6cbeeb2b)

## バリデータ

次の2つが有名そう:

- https://pkg.go.dev/github.com/go-playground/validator
- https://github.com/go-ozzo/ozzo-validation

参考:

- [Go言語のバリデーションチェックライブラリ(ozzo-validation)を分かりやすくまとめてみた - Qiita](https://qiita.com/gold-kou/items/201a19d9d0c760cc2104)
- [go-playground/validator でバリデーションを実装する｜maco｜note](https://note.com/mkudo/n/n139de888a151)

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

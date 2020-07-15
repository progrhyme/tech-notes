---
title: "Data Types"
linkTitle: "データ型"
date: 2020-07-05T12:06:10+09:00
weight: 100
---

データ型の取り回しやよくあるユースケース、発展的な使い方について。

## 文字列

関連項目:

- [pkg (stdlib) > fmt]({{<ref "../std-pkg/fmt.md">}})
- [pkg (stdlib) > strconv]({{<ref "../std-pkg/_index.md">}}#strconv)
- [pkg (stdlib) > strings]({{<ref "../std-pkg/strings.md">}})

How-to:

- 改行コードを取り除きたい -> [strings.TrimRight]({{<ref "../std-pkg/strings.md">}}#func-trimright)を使う

参考:

- [逆引きGolang (文字列)](https://ashitani.jp/golangtips/tips_string.html)
- [Goの文字列結合のパフォーマンス - Qiita](https://qiita.com/ono_matope/items/d5e70d8a9ff2b54d5c37)

### string -> 数値変換

```go
var i int
var s string="123"

// やり方①
i, e := strconv.Atoi(s)
fmt.Println(i) // -> 123

// やり方②
_, e = fmt.Fscan(strings.NewReader(s), &i)
```

どっちが速いかは比べてない。

strconv.Atoiだと、sの末尾に改行文字が入ってるとエラーになった。  
fmt.Fscanlnだったら大丈夫だった。

### string <-> []byte変換

```go
// string -> []byte
s := "foobar"
b := []byte(s)

// []byte -> string
string(b)
```

ただし、 `string -> []byte` では、メモリコピーが走るそうだ

参考:

- [golang で string を \[\]byte にキャストするとメモリコピーが走ります - Qiita](https://qiita.com/ikawaha/items/3c3994559dfeffb9f8c9)
- [golang で string を \[\]byte にキャストしてもメモリコピーが走らない方法を考えてみる - Qiita](https://qiita.com/mattn/items/176459728ff4f854b165)
- [go - How to assign string to bytes array - Stack Overflow](https://stackoverflow.com/questions/8032170/how-to-assign-string-to-bytes-array)

### ASCII文字 <-> byte変換

```go
s := "ABC"
s[0]       //=> 65
string(82) //=> "R"
```

### 繰り返し

bytes, stringsパッケージにRepeat関数がある:

```go
buf := []byte("あいうえお")
str := "あいうえお"

fmt.Println(string(bytes.Repeat(buf, 3)))
fmt.Println(strings.Repeat(str, 3))
```

参考:

- [Golang: 文字列を繰り返す - Sarabande.jp](https://blog.sarabande.jp/post/89685305348)

## 配列・スライス

参考:

- [go言語のslice操作をまとめてみた（shiftしたりpushしたり） - Qiita](https://qiita.com/egnr-in-6matroom/items/282aa2fd117aab9469bd)
- [図解 Go Slice Tricks - Folioscope](https://i-beam.org/2019/12/09/go-slice-tricks/)

### スライスのpush/pop/(un)shift

基本操作的な:

```go
// push
slice = append(slice, x)

// pop
x := slice[len(slice)-1]
slice = slice[:len(slice)-1]

// unshift
slice = append([]T{x}, slice...)

// shift
x := slice[0]
slice = slice[1:]
```

#### unshiftについて

```go
slice, slice[0] = append(slice[:1], slice[0:]...), 追加要素
```

↑こういう書き方もあるが、何をやっているか。

これはGoの多値代入を使って、2回の代入を1行で書いている。  
具体例とともに分解して示すと、下のようになっている:

```go
slice := []int{1, 2, 3}
x := -1

slice = append(slice[:1], slice[0:]...)
//=> [1, 1, 2, 3]
//slice = append(slice[:1], slice...) でも良い

slice[0] = x
//=> [-1, 1, 2, 3]
```

### もっとスライスを操作

```go
// 単一要素の削除
a = append(a[:i], a[i+1:]...)
// 単一要素の挿入
a = append(a[:i], append([]T{x}, a[i:]...)...)
```

## ポインタ

関連項目:

- [言語仕様#ポインタ]({{<ref "../spec/type.md">}}#ポインタ)

参考:

- [Big Sky :: Go のポインタの躓きやすい点](https://mattn.kaoriya.net/software/lang/go/20190516095124.htm)

### 引数

メモ:

- 基本、よほどデータが大きくならない限りは値渡しでよさそう
- オブジェクトの中身を書き換えるような処理だと、ポインタ渡しじゃないと駄目。そりゃそうか

参考:

- [Goでxxxのポインタを取っているプログラムはだいたい全部間違っている - Qiita](http://qiita.com/ruiu/items/e60aa707e16f8f6dccd8 "Goでxxxのポインタを取っているプログラムはだいたい全部間違っている - Qiita")
- [Go言語（golang）における値渡しとポインタ渡しのパフォーマンス影響について - Finatext - Medium](https://medium.com/finatext/go%E8%A8%80%E8%AA%9E-golang-%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E5%80%A4%E6%B8%A1%E3%81%97%E3%81%A8%E3%83%9D%E3%82%A4%E3%83%B3%E3%82%BF%E6%B8%A1%E3%81%97%E3%81%AE%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9%E5%BD%B1%E9%9F%BF%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6-70aa3605adc5)

### 戻り値

参考:

- [名前付き戻り値との正しい付き合い方 - Eureka Engineering - Medium](https://medium.com/eureka-engineering/named-return-values-7f485d867df0)

## 構造体の使い方

関連項目:

- [言語仕様#構造体]({{<ref "../spec/type.md">}}#構造体)

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

- [言語仕様#インタフェース]({{<ref "../spec/type.md">}}#インタフェース)
- [言語仕様#Type-assertions]({{<ref "../spec/type.md">}}#type-assertions)

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

## 独自型定義
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

関連項目:

- [言語仕様#iota]({{<ref "../spec/_index.md">}}#iota)

参考:

- [GoのEnumイディオム - Qiita](http://qiita.com/awakia/items/c81c7816b9aea5422250 "GoのEnumイディオム - Qiita")
- [Big Sky :: Re: GoLangでJavaのenumっぽいライブラリ作った話](https://mattn.kaoriya.net/software/lang/go/20141208093852.htm "Big Sky :: Re: GoLangでJavaのenumっぽいライブラリ作った話")
- [Ten Useful Techniques in Go – Fatih Arslan](https://arslan.io/2015/10/08/ten-useful-techniques-in-go/ "Ten Useful Techniques in Go – Fatih Arslan")
- https://godoc.org/golang.org/x/tools/cmd/stringer

### mapや配列

Example:

```go
type pos [2]int
type myMap map[string]pos

func (m *myMap) set(k string, p pos) {
	(*m)[k] = p
}

func main() {
	p := [2]int{5, 10}
	m := myMap{}
	m.set("foo", p)
	fmt.Println("m = ", m)
}
```

注意点はメソッドを使うとき:

- レシーバはポインタ型にする。でないと値渡しになって、結果が反映されない
- ので、メソッド内ではデリファレンスして使う
- 呼び出し側で値を初期化してメソッドを呼び出す

---
title: "Data Types"
linkTitle: "データ型"
description: https://golang.org/ref/spec#Types
date: 2020-07-05T12:05:42+09:00
---

## 基本型

```go
bool

string

int  int8  int16  int32  int64
uint uint8 uint16 uint32 uint64 uintptr

byte // uint8 の別名

rune // int32 の別名
     // Unicode のコードポイントを表す

float32 float64

complex64 complex128
```

## 配列・スライス

配列は固定長。スライスは可変長。

```go
a := [...]int{1, 2, 3} // 配列

s1 := []int{1, 2, 3} // スライス
s2 := []int{5, 6, 7}

// 構造体のスライス
ss := []struct {
    i int
    b bool
}{
    {2, true},
    {3, false},
    {5, true},
    {7, true},
    {11, false},
    {13, true},
}

// スライスの結合
s1 = append(s1, 4)
s1 = append(s1, s2...) // スライス同士の結合では "..." が必要
```

"Slicing"というテクニックで配列をスライスに変換できる。

```go
a := [5]byte{'a', 'b', 'c', 'd', 'e'}
s := a[:] // aを参照するスライス
```

参考:

- [Go Slices: usage and internals - The Go Blog](https://blog.golang.org/go-slices-usage-and-internals "Go Slices: usage and internals - The Go Blog")
- [Go言語のArrayとSliceについて - done is better than perfect](http://dibtp.hateblo.jp/entry/2014/07/06/190804 "Go言語のArrayとSliceについて - done is better than perfect")
- [Goでsliceに要素追加, slice同士の結合 - Qiita](https://qiita.com/hash/items/eb7d780c57fe245a9ae7 "Goでsliceに要素追加, slice同士の結合 - Qiita")

### 多次元配列・スライス

Examples:

```go
// 二次元スライスを作成
matrix := [][]float64{{0, 0}, {0, 1}, {1, 0}, {1, 1}}

// 上と等価
matrix := make([][]float64, 4)
matrix[0] = []float64{0, 0}
matrix[1] = []float64{0, 1}
matrix[2] = []float64{1, 0}
matrix[3] = []float64{1, 1}

fmt.Println(matrix) //=> [[0 0] [0 1] [1 0] [1 1]]
```

参考:

- [Goで二次元配列の初期化を一行で行う - Qiita](https://qiita.com/r9y9/items/362b4029b05cbca2cc70)

## map

https://golang.org/ref/spec#Map_types

初期値はnilで、データを入れようとするとパニックが起こるので、事前に割当てが必要。

```go
// NG
var ages map[string]int
ages["carol"] = 21

// OK
ages := map[string]int{"carol": 21}

// OK
var ages map[string]int
ages = make(map[string]int)
ages["carol"] = 21

// OK
ages := make(map[string]int)
ages["carol"] = 21

for name, age := range ages {
    fmt.Printf("%s is %d years old.\n", name, age)
}
```

Tips:

- mapの要素数は `len(mapVal)` でわかる

参考:

- [逆引きGolang (マップ)](https://ashitani.jp/golangtips/tips_map.html)

### 要素取得時のヒット検査

```go
age, ok := ages["bob"]
if ok {
    // hit
} else {
    // miss
}
```

### mapのマージ

[逆引きGolang (マップ)](https://ashitani.jp/golangtips/tips_map.html#map_Merge)より。  
愚直に書く感じか。

```go
func merge(m1, m2 map[string]string) map[string]string {
    merged := map[string]string{}

    for k, v := range m1 {
        merged[k] = v
    }
    for k, v := range m2 {
        merged[k] = v
    }
    return merged
}
```

https://play.golang.org/p/OmBHp53UIxn

## 構造体

https://golang.org/ref/spec#Struct_types

Examples:

```go
type Vertex struct {
	X int
	Y int
}

v := Vertex{}
v.X = 5

p := &v // ポインタ
p.Y = 1e9 // ポインタでも . でメンバ変数にアクセスできる
fmt.Println(v) //=> {5 1000000000}
```

### 初期化

構造体の初期化方法を示すサンプルコード:

```go
// 例
type Foo struct {
    Name string
    Age  int
}

// (1)
f := Foo{}
f.Name = "foo"
f.Age  = 5

// (2)
f := Foo{"foo", 5} // 全てのフィールドの指定が必要

// (3)
f := Foo{Age: 5, Name: "foo"} // 任意フィールドの省略が可能。順番も入れ替え可能
```

もし構造体に初期値を設定したい場合、コンストラクタ的な専用の関数を作る必要があるっぽい。

参考:

- [[Go] 構造体の初期化方法まとめ - Qiita](http://qiita.com/cotrpepe/items/b8e7f70f27813a846431 "[Go] 構造体の初期化方法まとめ - Qiita")
- [【Go】structにデフォルトの値を設定したい - /dev/null](http://gitpub.hatenablog.com/entry/2015/01/24/213223 "【Go】structにデフォルトの値を設定したい - /dev/null")

### タグ

構造体の定義内でメンバ変数に任意の文字列でタグを付けることができる。

Examples:

```go
struct {
    microsec  uint64 `protobuf:"1"`
    serverIP6 uint64 `protobuf:"2"`
}

type Server struct {
    Host      string `json:"host" toml:"host"`
    IPAddress string `json:"ip_address" toml:"ip_address"`
    Port      int    `json:"port" toml:"port"`
    Note      string `json:"note" toml:"note"`
}
```

Tips:

- ホワイトスペースで区切って複数設定できる
- reflectで参照できるが、ライブラリから使われることが多い
  - バリデータ、（デ）シリアライザなど

参考:

- [Goの構造体にメタ情報を付与するタグの基本 - Qiita](https://qiita.com/itkr/items/9b4e8d8c6d574137443c)
- [Struct タグについて — プログラミング言語 Go | text.Baldanders.info](https://text.baldanders.info/golang/struct-tag/)

## インタフェース

https://golang.org/ref/spec#Interface_types

インタフェース型はinterfaceと呼ばれるメソッドの組を持つ。  
インタフェース型の値は、メソッドの組と併せて任意の型の値を保持できる。
いわばインタフェースのスーパーセットであり、インタフェースの「実装」と呼ばれる。

初期化されてないインタフェース型の値は `nil` 。

Examples:

```go
type Reader interface {
	Read(p []byte) (n int, err error)
	Close() error
}

type Writer interface {
	Write(p []byte) (n int, err error)
	Close() error
}
```

入門ガイド:

- [Go by Example: Interfaces](https://gobyexample.com/interfaces)

### 埋め込み

interfaceを別のinterfaceに埋め込むことができる。  
埋め込まれたinterfaceはメソッド集合のユニオンを持つinterfaceとなる。

```go
// ReadWriter's methods are Read, Write, and Close.
type ReadWriter interface {
	Reader  // includes methods of Reader in ReadWriter's method set
	Writer  // includes methods of Writer in ReadWriter's method set
}
```

このとき、同名のメソッドは型が同じでないとエラーになる。

### Type assertions

[インタフェース型](#インタフェース)の値 `x` と型 `T` があるとき、

```go
x.(T)
```

は、 `x` が `nil` でなく、型 `T` であることをアサートする。  
この形式を「type assertion」という。

上のtype assertionが成り立つとき:

- `T` がインタフェース型でないなら、 `x` の型は `T` に等しい
- `T` がインタフェース型なら、 `x` は `T` を実装している
- 式の値は `T` 型になる

Examples:

```go
var x interface{} = 7          // x has dynamic type int and value 7
i := x.(int)                   // i has type int and value 7

type I interface { m() }

func f(y I) {
	s := y.(string)        // illegal: string does not implement I (missing method m)
	r := y.(io.Reader)     // r has type io.Reader and the dynamic type of y must implement both I and io.Reader
	…
}
```

type assertionが失敗するとrun-time panicが起こる。  
が、panicを発生させない代入のやり方がある。

Examples:

```go
v, ok = x.(T)
v, ok := x.(T)
var v, ok = x.(T)
var v, ok T1 = x.(T)
```

この構文で、 `ok` はtype assertionの成功時に `true` となる。  
失敗時には `false` となり、 `v` は `T` 型のゼロ値となる。

入門ガイド:

- [Type assertions - A Tour of Go](https://tour.golang.org/methods/15)

## 型変換

Examples:

```go
var i int = 42
var f float64 = float64(i)
var u uint = uint(f)

// より縮めて下のように書ける
i := 42
f := float64(i)
u := uint(f)
```

## 型宣言

https://golang.org/ref/spec#Type_declarations

基底型に別名をつけることができる。

Examples:

```go
// 組み込み型を基にする
type MyInt int
// 他 パッケージ 型を基にする
type MyWriter io.Writer
// 型リテラルを基にする
type Person struct {
    Name string
}
```

### 型エイリアス

型の別名を定義できる。

Examples:

```go
type Applicant = http.Client
```

参考:

- [Go 1.9 と Type Alias — プログラミング言語 Go | text.Baldanders.info](https://text.baldanders.info/golang/go-1_9-and-type-alias/)

## ポインタ

https://golang.org/ref/spec#Pointer_types

- `*p` はポインタ `p` の指す変数の値を表す
- `&v` は `v` のポインタを表す

Examples:

```go
i, j := 42, 2701
var p1 *int  // declare a pointer

p1 = &i          // point to i
fmt.Println(*p1) // read i through the pointer
*p1 = 21         // set i through the pointer
fmt.Println(i)   // see the new value of i

p2 := &j         // point to j
*p2 = *p2 / 37   // divide j through the pointer
fmt.Println(j)   // see the new value of j
```

入門ガイド:

- [Go by Example: Pointers](https://gobyexample.com/pointers)

関連項目

- [道場#ポインタ]({{<ref "../dojo/type.md">}}#ポインタ)

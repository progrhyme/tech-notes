---
title: "言語仕様"
linkTitle: "言語仕様"
description: https://golang.org/ref/spec
date: 2020-04-26T08:10:52+09:00
weight: 30
---

## 字句、リテラル
### 予約語

https://golang.org/ref/spec#Keywords

```
break        default      func         interface    select
case         defer        go           map          struct
chan         else         goto         package      switch
const        fallthrough  if           range        type
continue     for          import       return       var
```

### 文字列

https://golang.org/ref/spec#String_literals

`` `foo` `` ... raw string literal. ヒアドキュメントのように使える。

Examples:

```go
help := `Usage:
  hogehoge
  fugafuga
`
fmt.Println(help)
```

### rune

https://golang.org/ref/spec#Rune_literals

int32のaliasで、Unicode文字を扱うためのもの。

`'x'`, `'\n'` のように、シングルクォートで囲んで表現する。

参考:

- [Goのruneを理解するためのUnicode知識 - Qiita](https://qiita.com/seihmd/items/4a878e7fa340d7963fee)

## 変数

https://golang.org/ref/spec#Variables

Examples:

```go
// 型が同じものをまとめて宣言
var c, python, java bool

// 宣言と同時に初期化
var i, j int = 1, 2
```

### 定数

Examples:

```go
const (
    Pi = 3.14
    Big = 1 << 100
)
```

- 文字(character)、文字列(string)、boolean、数値(numeric)のみで使える
- `:=` を使って宣言できない
- 数値の定数は高精度な値。intの上限を越える値も保持できる

### 変数のエクスポート

https://golang.org/ref/spec#Exported_identifiers

```go
package foo

var privateVar string = "this is private" // パッケージ外から見えない
var PublicVar string = "this is public"   // パッケージ外から見える

// パッケージ外から見える
type Person struct {
    Name string // パッケージ外から見える
    age  int    // パッケージ外から見えない
}

// パッケージ外から見えない
type ninja struct {
    skill *Skill
    hp    int
}
```

参考:

- [Go言語のスコープについて - ryochack.clipboard](http://d.hatena.ne.jp/ryochack/20120115/1326567659 "Go言語のスコープについて - ryochack.clipboard")
- [json - Capitals in struct fields - Stack Overflow](https://stackoverflow.com/questions/24837432/capitals-in-struct-fields)

### ゼロ値

変数に初期値を与えずに宣言すると、ゼロ値が与えられる。  
型によって以下のようになる:

- 数値型（int, floatなど）: `0`
- bool型: `false`
- string型: "" （空文字列）
- ポインタ型: `nil`

## データ型

https://golang.org/ref/spec#Types

### 基本型

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

### 配列・スライス

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

#### 多次元配列・スライス

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

### map

初期値はnilで、データを入れようとするとパニックが起こるので、事前に割当てが必要。

```go
// NG
var ages map[string]int
ages["carol"] = 21

// OK
var ages map[string]int
ages = make(map[string]int)
ages["carol"] = 21

// OK
ages := make(map[string]int)
ages["carol"] = 21
```

#### 要素取得時のヒット検査

```go
age, ok := ages["bob"]
if ok {
    // hit
} else {
    // miss
}
```

### 構造体

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

#### 初期化

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

#### タグ

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

### インタフェース

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

#### 埋め込み

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

### 型変換

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

### 型宣言

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

#### 型エイリアス

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

- [道場#値渡しとポインタ渡し]({{<ref "dojo.md">}}#値渡しとポインタ渡し)

## 真偽判定

真偽判定（ifの条件式）に使えるのはbool型の値のみのようだ。  
LLみたいに数値や文字列を真偽判定に用いることはできない。

```go
true  //=> true
false //=> false
s := ""
if s { //=> エラー。文字列は判定できない
    :
}
len(s) > 0 //=> false
s == "" //=> true
i := 1
if i { //=> エラー。数値は判定できない
    :
}
```

参考:

- [What is the best way to test for an empty string in Go? - Stack Overflow](https://stackoverflow.com/questions/18594330/what-is-the-best-way-to-test-for-an-empty-string-in-go)

## 制御構文
### switch

https://golang.org/ref/spec#Switch_statements

Examples:

```go
switch tag {
default: s3()
case 0, 1, 2, 3: s1()
case 4, 5, 6, 7: s2()
}

switch x := f(); {  // missing switch expression means "true"
case x < 0: return -x
default: return x
}

switch {
case x < y: f1()
case x < z: f2()
case x == 4: f3()
}

// 型で分岐
var i interface{}
i = 100
switch v := i.(type) {
case int:
    fmt.Println(v*2)
case string:
    fmt.Println(v+"hoge")
default:
    fmt.Println("default")
}
```

### ループ

`for` しかない

Examples:

```go
for {
  // 無限ループ
}

for i := 1; i < 100; i++ {
  // iが[1, 100)の間
}

// collection要素のイテレーション
dayOfWeeks := [...]string{"月", "火", "水", "木", "金", "土", "日"}
for arrayIndex, dayOfWeek := range dayOfWeeks {
    fmt.Printf("%d番目の曜日は%s曜日です。\n", arrayIndex + 1, dayOfWeek)
}
```

※mapをイテレーションする場合、取り出し順はランダムになる。

参考:

- [繰り返し - はじめてのGo言語](http://cuto.unirita.co.jp/gostudy/post/loop-statement/)

## 関数

https://golang.org/ref/spec#Function_types

シグネチャの例:

```go
func()
func(x int) int
// 連続する複数の引数の型が同じときは、最後の型以外を省略できる
func(a, _ int, z float32) bool
func(a, b int, z float32) (bool)
func(prefix string, values ...int)
func(a, b int, z float64, opt ...interface{}) (success bool)
func(int, int, float64) (float64, *[]int)
func(n int) func(p *T)
```

入門ガイド:

- [Go by Example: Functions](https://gobyexample.com/functions)

Limitation:

- Rubyとかにあるような引数にデフォルト値を与えるような仕様はない
  - 構造体を使って似たようなことはできる。下の参考に挙げたリンク先を参照

参考:

- [overloading - Optional Parameters in Go? - Stack Overflow](https://stackoverflow.com/questions/2032149/optional-parameters-in-go/13603885#13603885)

### 無名関数（クロージャ）

https://golang.org/ref/spec#Function_literals

```go
f := func(x, y int) int { return x + y }
```

### 可変長引数

https://golang.org/ref/spec#Passing_arguments_to_..._parameters

ある関数の最後の引数 `p` が `...T` と記述されたなら、 `p` の型は `[]T` である。  
呼び出し側が `p` に何も与えなかった場合、 `p` は `nil` となる。

Examples:

```go
func Greeting(prefix string, who ...string)
Greeting("nobody")
Greeting("hello:", "Joe", "Anna", "Eileen")
```

呼び出し側はスライス変数sを使って `s...` のように記述できる。

Examples:

```go
s := []string{"James", "Jasmine"}
Greeting("goodbye:", s...)
```

参考:

- [Goで可変引数の関数にスライスを展開して渡す - Qiita](https://qiita.com/hnakamur/items/c3560a4b780487ef6065)

## メソッド

https://golang.org/ref/spec#Method_declarations

レシーバのある関数。

Examples:

```go
func (p *Point) Length() float64 {
	return math.Sqrt(p.x * p.x + p.y * p.y)
}

func (p *Point) Scale(factor float64) {
	p.x *= factor
	p.y *= factor
}
```

- レシーバの型は `type` で定義された型か、そのポインタ（基底型と呼ばれる）
- レシーバ型はポインタやインタフェースであってはならない
- レシーバ型はメソッドと同じパッケージで定義されなければならない

メソッドの型は、レシーバを第1引数とする関数。
例えば、上述の `Scale` は次の型を持つ:

```go
func(p *Point, factor float64)
```

ただし、この形式で宣言された関数はメソッドではない。

## 式
### セレクタ

https://golang.org/ref/spec#Selectors

レシーバがパッケージ名以外のもので `.` でアクセスされるもの。
[構造体](#構造体)のメンバ変数か[メソッド](#メソッド)を指すことが多い。

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

## 文
### defer

https://golang.org/ref/spec#Defer_statements

入門ガイド:

- https://gobyexample.com/defer

ある関数の中で `defer 関数` の形式で書かれる。  
当該関数から `return` する前に、deferで指定された関数が確実に実行される。  
エラー発生時のclean up処理などに用いられる。

Examples:

```go
lock(l)
defer unlock(l)  // unlocking happens before surrounding function returns

// prints 3 2 1 0 before surrounding function returns
for i := 0; i <= 3; i++ {
	defer fmt.Print(i)
}

// f returns 42
func f() (result int) {
	defer func() {
		// result is accessed after it was set to 6 by the return statement
		result *= 7
	}()
	return 6
}
```

## レキシカルスコープ

https://golang.org/ref/spec#Declarations_and_scope

- Goのコードは、ブロックによるレキシカルスコープを持つ
- ブロックで宣言された識別子は、内部ブロックで再宣言できる
  - 内部で宣言された識別子のスコープは内部ブロックに閉じる

Examples:

https://play.golang.org/p/HOmvzO1l1qc

```go
s := "main scope"
{
    s := "inner scope"
    fmt.Printf("Hello, %s\n", s)
}
fmt.Printf("Hello, %s\n", s)
```

実行結果:

```
Hello, inner scope
Hello, main scope
```

参考:

- [Try Golang! ローカル変数のスコープに注意すべし - VELTRA Engineering - Medium](https://medium.com/veltra-engineering/local-var-scope-in-golang-24833dd4018b)

### ブロック

https://golang.org/ref/spec#Blocks

上のように `{ ... }` でブロックを作れる。  
Perlっぽい。

Spec:

- packageはpackage blockを持つ
- if, for, switchなんかも自身のブロックを持つ。
- ブロックはネストできる

## 日付・時刻

### 日時フォーマット

Go言語の日時のフォーマット関数（timeパッケージの[func (Time) Format)](https://golang.org/pkg/time/#Time.Format)）に与えられる引数は、2006-01-02T15:04:05（月曜）の日時となっている。

これはアメリカで時刻を表記する際の順番で、1月2日午後3時4分5秒2006年となり、わかりやすかったからだそうだ。

参考:

- [Goのtimeパッケージのリファレンスタイム（2006年1月2日）は何の日？ - Qiita](https://qiita.com/ruiu/items/5936b4c3bd6eb487c182)

## goroutine

OSのネイティブスレッドより扱いやすくしたもの。
スレッドとファイバーの良いとこ取り。
`go` というキーワードを付けるとgoroutineが作られる。

Examples:

```go
// 別のgoroutineを作って既存関数を実行
go Function()

// 別のgoroutineを作って、無名関数を実行
go func() {
  // goroutine内で実行したい処理
}
```

参考:

- [Go言語で非同期処理の結果を受け取る - Qiita](https://qiita.com/najeira/items/47539ab346fa0c00dc62)

## チャネル

SYNOPSIS:

```go
// バッファなし
tasks := make(chan string)
// バッファ付き
tasks := make(chan string, 10)

// データ送信
tasks <- "cmake .."
tasks <- "cmake . --build Debug"

// データ受信
task := <-tasks
// データ受信 + クローズ判定
task, ok := <-tasks
// データを読み捨てる
<-wait
```

Examples:

- https://gobyexample.com/channels

### select文

複数のチャネルを待機する場合に使う。

Examples:

```go
// ブロックせずに受信し、かつ、チャネルがクローズ済みかどうかチェックする
select {
case v, ok := <- ch:
    if ok {
        fmt.Println(v)
    } else {
        fmt.Println("closed")
    }
default:
    fmt.Println("no value")
}

// ブロックせずに送信
select {
case ch <- v:
    fmt.Println("sent")
default:
    fmt.Println("no capacity")
}
```

参考:

- [Go言語でチャネルとselect - Qiita](https://qiita.com/najeira/items/71a0bcd079c9066347b4)
- [select - はじめてのGo言語](http://cuto.unirita.co.jp/gostudy/post/go_select/)

## ビルトイン関数
### append

https://golang.org/pkg/builtin/#append

`func append(slice []Type, elems ...Type) []Type`

sliceに要素、またはsliceを結合し、新たなsliceを返す。

```go
slice = append(slice, elem1, elem2)
slice = append(slice, anotherSlice...)
```

### panic

https://golang.org/pkg/builtin/#panic

`func panic(v interface{})`

Examples:

```go
panic("a problem")

_, err := os.Create("/tmp/file")
if err != nil {
    panic(err)
}
```

関連項目:

- [道場#例外処理]({{<ref "dojo.md">}}#例外処理)

## パッケージ
### import

https://golang.org/ref/spec#Import_declarations

Examples:

```go
import (
    "fmt"
    . "math"     // Exportされた関数等を自パッケージのもののように使える
    s "strings"  // sとしてimport
    _ "testing"  // importするけど使わない
)
```

構文:

```
ImportDecl       = "import" ( ImportSpec | "(" { ImportSpec ";" } ")" ) .
ImportSpec       = [ "." | PackageName ] ImportPath .
ImportPath       = string_lit .
```

参考:

- [【Go】import 書き方まとめ - Qiita](https://qiita.com/taji-taji/items/5a4f17bcf5b819954cc1)

### init()関数による初期化

* ソースファイルに1つ `func init()` を記述できる
* ソースファイル読み込み時に1回実行される
* importされるpackageのinit()が先に実行される
  * pがqをimportしているとき、pのinit()より先にqのinit()が完了している
  * mainパッケージのinit()が最後に実行される

参考:

- [Effective Go - golang.jp](http://golang.jp/tag/effective-go/page/2 "Effective Go - golang.jp")

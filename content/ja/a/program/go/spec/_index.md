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

#### iota

https://golang.org/ref/spec#Iota

0から始まる連番の整数値を生成できる。

Examples:

```go
const (
    // 定数宣言で右辺を省略すると直前と同じ式が使われる
    c0 = iota  // c0 == 0
    c1         // c1 == 1
    c2         // c2 == 2
)

const (
    a = 1 << iota  // a == 1  (iota == 0)
    b              // b == 2  (iota == 1)
    c = 3          // c == 3  (iota == 2, unused)
    d = 1 << iota  // d == 8  (iota == 3)
)

const (
	u         = iota * 42  // u == 0     (untyped integer constant)
	v float64 = iota * 42  // v == 42.0  (float64 constant)
	w                      // w == 84    (untyped integer constant)
)

const x = iota  // x == 0
const y = iota  // y == 0
```

関連項目:

- [道場#enum]({{<ref "../dojo/type.md">}}#enum)

参考:

- [Golangのconst識別子iotaの紹介 - Qiita](https://qiita.com/curepine/items/2ae2f6504f0d28016411)
- [Golangで iotaの開始番号を指定する - Qiita](https://qiita.com/DQNEO/items/d3349d683967fd8be151)

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
- スライス: `[]` （空スライス）
- map: `nil`
- 構造体: `{}` （空の構造体）
- ポインタ型: `nil`
- 関数型: `nil`

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

参考:

- [switch による条件分岐 | まくまくHugo/Goノート](https://maku77.github.io/hugo/go/switch.html)

### ループ

https://golang.org/ref/spec#For_statements

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

### ラベル

大域脱出や、gotoで使える。

Examples:

```go
OuterLoop:
  for {
      for {
          break OuterLoop
      }
      if someCondition {
          goto End
      }
  }

Switch:
  switch x {
  case y:
    for {
        break Switch
    }
  }

End:
  os.Exit(0)
```

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

- [道場#例外処理]({{<ref "../dojo/_index.md">}}#例外処理)

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

#### import cycle not allowed

相互import, 循環importはNG.  
コンパイルエラーになる。

参考:

- [Golang で import cycle not allowed に引っかかった人へ - Qiita](https://qiita.com/ko-watanabe/items/0141fa20da9f6f30b754)

### init()関数による初期化

* ソースファイルに1つ `func init()` を記述できる
* ソースファイル読み込み時に1回実行される
* importされるpackageのinit()が先に実行される
  * pがqをimportしているとき、pのinit()より先にqのinit()が完了している
  * mainパッケージのinit()が最後に実行される

参考:

- [Effective Go - golang.jp](http://golang.jp/tag/effective-go/page/2 "Effective Go - golang.jp")

---
title: "言語仕様"
linkTitle: "言語仕様"
date: 2020-04-26T08:10:52+09:00
---

リファレンス https://golang.org/ref/spec

## 変数

https://golang.org/ref/spec#Variables

### パッケージ変数

```go
package foo

var privateVar string = "this is private" // 外部から見えない
var PublicVar string = "this is public"   // 外部から見える
```

参考:

- [Go言語のスコープについて - ryochack.clipboard](http://d.hatena.ne.jp/ryochack/20120115/1326567659 "Go言語のスコープについて - ryochack.clipboard")

## データ型

https://golang.org/ref/spec#Types

### 配列・スライス

配列は固定長。スライスは可変長。

```go
a := [...]int{1, 2, 3} // 配列

s1 := []int{1, 2, 3} // スライス
s2 := []int{5, 6, 7}

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

#### 初期化

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

## 日付・時刻

### 日時フォーマット

Go言語の日時のフォーマット関数（timeパッケージの[func (Time) Format)](https://golang.org/pkg/time/#Time.Format)）に与えられる引数は、2006-01-02T15:04:05（月曜）の日時となっている。

これはアメリカで時刻を表記する際の順番で、1月2日午後3時4分5秒2006年となり、わかりやすかったからだそうだ。

参考:

- [Goのtimeパッケージのリファレンスタイム（2006年1月2日）は何の日？ - Qiita](https://qiita.com/ruiu/items/5936b4c3bd6eb487c182)

## ポインタ

参考:

- [Goでxxxのポインタを取っているプログラムはだいたい全部間違っている - Qiita](http://qiita.com/ruiu/items/e60aa707e16f8f6dccd8 "Goでxxxのポインタを取っているプログラムはだいたい全部間違っている - Qiita")

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


## 文法
### ループ

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


## パッケージ

### init()関数による初期化

* ソースファイルに1つ `func init()` を記述できる
* ソースファイル読み込み時に1回実行される
* importされるpackageのinit()が先に実行される
  * pがqをimportしているとき、pのinit()より先にqのinit()が完了している
  * mainパッケージのinit()が最後に実行される

参考:

- [Effective Go - golang.jp](http://golang.jp/tag/effective-go/page/2 "Effective Go - golang.jp")
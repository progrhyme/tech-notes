---
title: "fmt"
linkTitle: "fmt"
description: https://pkg.go.dev/fmt
date: 2020-06-10T01:55:32+09:00
weight: 110
---

## About

書式付きの入出力機能を提供するパッケージ。

Examples:

```go
const name, age = "Kim", 22
fmt.Println(name, "is", age, "years old.")
_, err := fmt.Printf("%s is %d years old.\n", name, age)

if err != nil {
    fmt.Fprintln(os.Stderr, "Error occured!!")
    fmt.Fprintf(os.Stderr, "Fprintf: %v\n", err)
}
```

## 書式指定子

だいたいprintfと一緒だけど、違うやつとか難しいやつを出くわしたときに追記していくつもり。

`%v`, `%+v` が便利。

 書式 | 値の型 | 説明
------|--------|------
 %v | any | 値のデフォルトの書式で出力
 %+v | struct | フィールド名も表示してくれる
 %p | ポインタ | `0x` プレフィックス付きの16進数でアドレスを表示

参考:

- https://linux.die.net/man/3/fprintf

## func Errorf

https://pkg.go.dev/fmt?tab=doc#Errorf

```go
func Errorf(format string, a ...interface{}) error
```

書式付きメッセージを使ってerrorを作るときに便利な関数。  
更に、 `%w` にerror型の値を入れることで、そのエラーをラップしたerrorを作れる。

Example:

```go
err := fmt.Errorf("Error occured! %w", errors.New("I am guilty!"))
fmt.Printf("Error: %v", err)
```

実行結果:

```sh
$ go run main.go
Error: Error occured! I am guilty!
```

関連項目:

- [errors]({{<ref "errors.md">}})

## func Scan

https://pkg.go.dev/fmt?tab=doc#Scan

```go
func Scan(a ...interface{}) (n int, err error)
```

標準入力からスペース区切りで入力を受付け、変数に格納する。  
改行もスペースとみなされる。  
読み取った数が引数より少なかったらエラーを返す。

任意の入力ソースから読み取るには、Fscan, Fscanf, Fscanlnを使う。

Examples:

```go
var a, b string
fmt.Scan(&a, &b)
```

実行例:

```sh
# それぞれa, bにセットされる
$ go run main.go
x y

# 改行しても次の文字列を入れるまで終わらない
$ go run main.go
x
y

# zは捨てられる
$ go run main.go
x y z
```

## func Scanln

```go
func Scanln(a ...interface{}) (n int, err error)
```

Scanと似ているが、改行で処理を止める。

Examples:

```go
var a, b string
fmt.Print("Input 2 strings: ")
n, e := fmt.Scanln(&a, &b)
if e != nil {
        panic(e)
}
fmt.Printf("Read %d words. a = %s, b = %s\n", n, a, b)
```

実行例:

```sh
$ go run main.go
Input 2 strings: x y
Read 2 words. a = x, b = y

# 入力を与えずに改行するとエラー
$ go run main.go
Input 2 strings: 
panic: unexpected newline

goroutine 1 [running]:
main.main()
        main.go:12 +0x27f
exit status 2
```

## func Sprintf

https://pkg.go.dev/fmt?tab=doc#Sprintf

シグネチャ:

```go
func Sprintf(format string, a ...interface{}) string
```

Examples:

```go
const name, age = "Kim", 22
s := fmt.Sprintf("%s is %d years old.\n", name, age)
```

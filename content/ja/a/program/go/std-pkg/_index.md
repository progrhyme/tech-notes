---
title: "標準パッケージ"
linkTitle: "pkg (stdlib)"
description: https://golang.org/pkg/
date: 2020-05-31T16:18:58+09:00
weight: 50
---

## bufio

バッファリング付きI/Oを提供する。

Examples:

```go
// 1行ずつテキストを読み込んで、EOFが入力されるまで読んだ行をそのまま表示し続ける
scanner := bufio.NewScanner(os.Stdin)
for scanner.Scan() {
	fmt.Println(scanner.Text()) // Println will add back the final '\n'
}
if err := scanner.Err(); err != nil {
	fmt.Fprintln(os.Stderr, "reading standard input:", err)
}
```

実行例:

```sh
$ go run main.go
xx yy zz
xx yy zz
a   b c   d
a   b c   d
     # 注: 空入力で改行しても処理は終わらない

     # EOF入力で終了
```

参考:

- [CLI#ターミナルでEOFを入力する方法]({{<ref "/a/cli/_index.md">}}#ターミナルでeofを入力する方法)

## context

https://golang.org/pkg/context/

Webサーバとかで引きずり回すコンテキスト。  

SYNOPSIS:

```go
ctx := context.Background() # context.Contextな構造体を生成

## タイムアウト付きコンテキストを生成。cancelはタイムアウト時に実行される
ctx2, cancel := context.WithDeadline(ctx, time.Now().Add(timeout))
defer cancel()
```

参考:

- [Go1.7のcontextパッケージ | SOTA](http://deeeet.com/writing/2016/07/22/context/ "Go1.7のcontextパッケージ | SOTA")

## errors

https://golang.org/pkg/errors/

Go 1.13で `.Is`, `.As`, `.Unwrap` が加わり、かなり強化されたようだ。

参考:

- [pkg/errors から徐々に Go 1.13 errors へ移行する - blog.syfm](https://syfm.hatenablog.com/entry/2019/12/27/193348)

## fmt

https://pkg.go.dev/fmt

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

### 書式指定子

だいたいprintfと一緒だけど、違うやつとか難しいやつを出くわしたときに追記していくつもり。

`%v`, `%+v` が便利。

 書式 | 値の型 | 説明
------|--------|------
 %v | any | 値のデフォルトの書式で出力
 %+v | struct | フィールド名も表示してくれる
 %p | ポインタ | `0x` プレフィックス付きの16進数でアドレスを表示

参考:

- https://linux.die.net/man/3/fprintf

### func Scan

https://pkg.go.dev/fmt?tab=doc#Scan

```go
func Scan(a ...interface{}) (n int, err error)
```

標準入力からスペース区切りで入力を受付け、変数に格納する。  
改行もスペースとみなされる。  
読み取った数が引数より少なかったらエラーを返す。

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

### func Scanln

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

### func Sprintf

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

## io

https://golang.org/pkg/io/

基礎的なI/Oのインタフェースを提供する。  
osパッケージなどにある様々なI/Oプリミティブを抽象化する。

参考:

- [【Go入門】ioパッケージ ～ 入出力処理の抽象化と共通化](https://leben.mobi/go/io-reader-writer/go-programming/)
- [ASCII.jp：Goならわかるシステムプログラミング](https://ascii.jp/serialarticles/1235262/)

### type Reader (interface)

https://golang.org/pkg/io/#Reader

定義:

```go
type Reader interface {
    Read(p []byte) (n int, err error)
}
```

実装例:

- os.File, strings.Reder, bytes.Buffer, net.Conn

### type Writer (interface)

https://golang.org/pkg/io/#Writer

定義:

```go
type Writer interface {
    Write(p []byte) (n int, err error)
}
```

## io/ioutil

https://golang.org/pkg/io/ioutil/

### func ReadDir

```go
func ReadDir(dirname string) ([]os.FileInfo, error)
```

ディレクトリ内のファイルをリストする。

Examples:

```go
files, err := ioutil.ReadDir(".")
if err != nil {
    log.Fatal(err)
}

for _, file := range files {
    fmt.Println(file.Name())
}
```

参考:

- [Golangでディレクトリ内のファイル一覧を入手する - Qiita](https://qiita.com/tanksuzuki/items/7866768c36e13f09eedb)

## log

https://golang.org/pkg/log/

ロガー。ログレベルの概念はない。

`log.Print` など、標準のロガーを使うやり方と、 `log.New(...)` で `Logger` を作って使うやり方がある。

SYNOPSIS:

```go
// 標準のロガーを使う
log.SetPrefix("[info] ")
log.Printf("a = %v", a)

// ロガーを生成して使う
logger := log.New(os.Stderr, "[error] ", flag.LstdFlags|flag.Llongfile)
if err != nil {
  logger.Fatalf("Error! %v", err) // ログ出力後、 os.Exit(1)
}
```

参考:

- [go言語におけるロギングについて](http://blog.satotaichi.info/logging-frameworks-for-go/ "go言語におけるロギングについて")

## os

See [os]({{<ref "os.md">}})

## os/exec

https://golang.org/pkg/os/exec/

コマンド実行で使う。

SYNOPSIS:

```go
cmd := exec.Command("sh", "-c", "echo stdout; echo 1>&2 stderr")

// コマンドの出力を標準（エラー）出力に設定
cmd.Stdout = os.Stdout
cmd.Stderr = os.Stderr

// コマンド実行
err := cmd.Run()

// コマンド実行し、stdoutを取得
out, err := cmd.Output()

// stdout, stderrをまとめて受け取る
stdoutStderr, err := cmd.CombinedOutput()
```

## path/filepath

https://golang.org/pkg/path/filepath/

- `func Base` ... basenameコマンド相当
- `func Dir` ... dirnameコマンド相当

Examples:

```go
fmt.Println("On Unix:")

fmt.Println(filepath.Base("/foo/bar/baz.js")) //=> baz.js
fmt.Println(filepath.Base("/foo/bar/baz/"))   //=> baz
fmt.Println(filepath.Base("dev.txt"))         //=> dev.txt

fmt.Println(filepath.Dir("/foo/bar/baz.js")) //=> /foo/bar
fmt.Println(filepath.Dir("/foo/bar/baz/"))   //=> /foo/bar/baz
fmt.Println(filepath.Dir("dev.txt"))         //=> .
fmt.Println(filepath.Dir("../todo.txt"))     //=> ..
```

### func Join

https://golang.org/pkg/path/filepath/#Join

Signature:

```go
func Join(elem ...string) string
```

ファイルパスの要素を結合してファイルパス文字列を作って返す。

Examples:

```go
// Unix
filepath.Join("a", "b", "c") //=> a/b/c
```

### func Walk

https://golang.org/pkg/path/filepath/#Walk

Signature:

```go
func Walk(root string, walkFn WalkFunc) error
```

- Perl5の `File::Find::find` に似てる。
- ディレクトリを再帰的に探索して、関数 `WalkFunc` を実行

参考:

- https://stackoverflow.com/questions/6608873/file-system-scanning-in-golang

## regexp

https://golang.org/pkg/regexp/

正規表現の文法は `\C` を除いて https://github.com/google/re2/wiki/Syntax に従っている。  
文法の概要については次を実行して見るとよい:

```sh
go doc regexp/syntax
```

Examples:

```go
// Compile the expression once, usually at init time.
// Use raw strings to avoid having to quote the backslashes.
var validID = regexp.MustCompile(`^[a-z]+\[[0-9]+\]$`)

fmt.Println(validID.MatchString("adam[23]"))
fmt.Println(validID.MatchString("eve[7]"))
fmt.Println(validID.MatchString("Job[48]"))
fmt.Println(validID.MatchString("snakey"))
```

関連項目:

- [道場#正規表現]({{<ref "/a/program/go/dojo.md">}}#正規表現)

参考:

- [逆引きGolang (正規表現)](https://ashitani.jp/golangtips/tips_regexp.html)

## syscall [Deprecated]

https://golang.org/pkg/syscall/

=> https://pkg.go.dev/golang.org/x/sys

Go 1.4でフリーズされて、上に移ったみたい。

参考:

- https://golang.org/s/go1.4-syscall

## time

https://golang.org/pkg/time/

SYNOPSYS:

```go
td = 30 * time.Seconds() # time.Duration型で30秒
t1 = time.Now() # 現在日時を time.Time型で返す
t2 = t1.Add(td) # 30秒後の日時を time.Time型で
```

Examples:

- https://gobyexample.com/timeouts


### func After

https://golang.org/pkg/time/#After

```go
func After(d Duration) <-chan Time
```

タイムアウトを実現するときによく使われる。

Example:

```go
select {
case m := <-c:
        handle(m)
case <-time.After(5 * time.Minute):
        fmt.Println("timed out")
}
```

More examples:

- https://gobyexample.com/timeouts

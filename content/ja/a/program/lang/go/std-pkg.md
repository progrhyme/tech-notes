---
title: "標準パッケージ"
linkTitle: "pkg (stdlib)"
description: https://golang.org/pkg/
date: 2020-05-31T16:18:58+09:00
weight: 50
---

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

## flag

https://golang.org/pkg/flag/

コマンドラインオプションをパースしてくれる君。

- ヘルプ付き
- ショートオプションとロングオプション両対応したいときはちょっとめんどい（後述）

SYNOPSIS:

```go
var (
  verbose bool
  num int
  text string
)

// flag登録
// 第2引数 ... コマンドラインオプション
// 第3引数 ... デフォルト値
// 第4引数 ... ヘルプで表示される文言
flag.BoolVar(&verbose, "v", false, "Verbose output")
flag.IntVar(&verbose, "n", 0, "Number")
flag.StringVar(&verbose, "t", "", "Text")

// コマンド引数のパース
flag.Parse()
```

ロングオプション対応するときは、上の例だと

```go
flag.BoolVar(&verbose, "verbose", false, "Verbose output")
```

を足すと `-v` と合わせて `-verbose` でも行けるようになる。  
ただちょっとコードの見た目がアレな感じになるので、そこまで行くと `flags` なりを使うかーという気持ちにならないでもない。

参考:

- [Go言語のflagパッケージを使う - uragami note](http://ryochack.hatenablog.com/entry/2013/04/17/232753 "Go言語のflagパッケージを使う - uragami note")
- [Go by Example: Command-Line Flags](https://gobyexample.com/command-line-flags)

### サブコマンド対応

Examples:

```go
package main

import (
    "flag"
    "fmt"
    "os"
)

func main() {
    fooCmd := flag.NewFlagSet("foo", flag.ExitOnError)
    fooEnable := fooCmd.Bool("enable", false, "enable")
    fooName := fooCmd.String("name", "", "name")

    barCmd := flag.NewFlagSet("bar", flag.ExitOnError)
    barLevel := barCmd.Int("level", 0, "level")

    if len(os.Args) < 2 {
        fmt.Println("expected 'foo' or 'bar' subcommands")
        os.Exit(1)
    }

    switch os.Args[1] {

    case "foo":
        fooCmd.Parse(os.Args[2:])
        fmt.Println("subcommand 'foo'")
        fmt.Println("  enable:", *fooEnable)
        fmt.Println("  name:", *fooName)
        fmt.Println("  tail:", fooCmd.Args())
    case "bar":
        barCmd.Parse(os.Args[2:])
        fmt.Println("subcommand 'bar'")
        fmt.Println("  level:", *barLevel)
        fmt.Println("  tail:", barCmd.Args())
    default:
        fmt.Println("expected 'foo' or 'bar' subcommands")
        os.Exit(1)
    }
}
```

参考:

- [Go by Example: Command-Line Subcommands](https://gobyexample.com/command-line-subcommands)

### ヘルプメッセージのカスタマイズ

パッケージ変数 `Usage` に独自関数を設定することでカスタマイズできる。

Examples:

```go
func usage() {
	fmt.Fprintln(os.Stderr, "blah blah blah")
	fmt.Fprintf(os.Stderr, "Usage of %s:\n", os.Args[0])
	flag.PrintDefaults()
}

func main() {
  flag.Usage = usage
}
```

### func Arg

`func Arg(i int) string`

フラグでないi番目のコマンドライン引数を返す。
`Arg(0)` が最初の引数。

### func Args

`func Args() []string`

フラグでないコマンドライン引数のリストを返す。

### func (*FlagSet) NArg

`func (f *FlagSet) NArg() int`

フラグ処理後に残った引数の数を返す。

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

https://golang.org/pkg/os/

### 環境変数の操作

参考:

- [Go by Example: Environment Variables](https://gobyexample.com/environment-variables "Go by Example: Environment Variables")

### ファイル操作

SYNOPSIS:

```go
// ファイル内容読み取り
file, err := os.Open(path)
if err != nil {
    panic(err)
}
defer file.close
buf, err := ioutil.ReadAll(file)

// ファイル作成
file, err := os.Create(path)
// エラー処理省略
defer file.close
err = file.Write(text)

// ファイル or ディレクトリ削除
err := os.Remove(path)
```

### func Getenv

https://golang.org/pkg/os/#Getenv

```go
func Getenv(key string) string
```

keyの環境変数を返す。

### func Getwd

https://golang.org/pkg/os/#Getwd

```go
func Getwd() (dir string, err error)
```

カレントディレクトリの絶対パスを返す。

### type File

https://golang.org/pkg/os/#File

オープンしたファイルディスクリプタを表現する構造体。

#### func Create

https://golang.org/pkg/os/#Create

ファイル作成。

## os/exec

https://golang.org/pkg/os/exec/

コマンド実行で使う。

SYNOPSIS:

```go
cmd := exec.Command("sh", "-c", "echo stdout; echo 1>&2 stderr")

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

### func Walk

`func Walk(root string, walkFn WalkFunc) error`

- Perl5の `File::Find::find` に似てる。
- ディレクトリを再帰的に探索して、関数 `WalkFunc` を実行

参考:

- https://stackoverflow.com/questions/6608873/file-system-scanning-in-golang

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



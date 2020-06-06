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

### Variables

https://golang.org/pkg/os/#pkg-variables

```go
var (
    Stdin  = NewFile(uintptr(syscall.Stdin), "/dev/stdin")
    Stdout = NewFile(uintptr(syscall.Stdout), "/dev/stdout")
    Stderr = NewFile(uintptr(syscall.Stderr), "/dev/stderr")
)
```

### func Getenv

https://golang.org/pkg/os/#Getenv

```go
func Getenv(key string) string
```

keyの環境変数を返す。  
取得できなかった場合は空文字が返る。

### func Getwd

https://golang.org/pkg/os/#Getwd

```go
func Getwd() (dir string, err error)
```

カレントディレクトリの絶対パスを返す。

### func NewFile

https://golang.org/pkg/os/#NewFile

```go
func NewFile(fd uintptr, name string) *File
```

> NewFile returns a new File with the given file descriptor and name.

### func UserHomeDir

https://golang.org/pkg/os/#UserHomeDir

```go
func UserHomeDir() (string, error)
```

Unix系システムなら `$HOME`, Windowsなら `%USERPROFILE%` の値を返す。

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



---
title: "os"
linkTitle: "os"
description: https://golang.org/pkg/os/
date: 2020-06-06T21:15:56+09:00
weight: 600
---

## os

https://golang.org/pkg/os/

### 環境変数の操作

Examples:

```go
os.Setenv("FOO", "1")
fmt.Println("FOO:", os.Getenv("FOO")) //=> FOO: 1
fmt.Println("BAR:", os.Getenv("BAR")) //=> BAR: 
val, ok := os.LookupEnv("BAR")
// val => ""
// ok => false
```

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

### Constants

https://golang.org/pkg/os/#pkg-constants

```go
// Flags for OpenFile. ファイルオープン時のモード
const (
    // O_RDONLY, O_WRONLY, O_RDWR のどれか1つだけ指定されないといけない
    O_RDONLY int = syscall.O_RDONLY // open the file read-only.
    O_WRONLY int = syscall.O_WRONLY // open the file write-only.
    O_RDWR   int = syscall.O_RDWR   // open the file read-write.
    // 後のフラグは任意
    O_APPEND int = syscall.O_APPEND // append data to the file when writing.
    O_CREATE int = syscall.O_CREAT  // create a new file if none exists.
    O_EXCL   int = syscall.O_EXCL   // used with O_CREATE, file must not exist.
    O_SYNC   int = syscall.O_SYNC   // open for synchronous I/O.
    O_TRUNC  int = syscall.O_TRUNC  // truncate regular writable file when opened.
)

// Path separator
const (
  PathSeparator     = '/' // OS-specific path separator
  PathListSeparator = ':' // OS-specific path list separator
)
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

### func Chdir

https://golang.org/pkg/os/#Chdir

```go
func Chdir(dir string) error
```

カレントディレクトリを変更する。  
エラーは `*PathError` 型。

### func Chmod

https://golang.org/pkg/os/#Chmod

```go
func Chmod(name string, mode FileMode) error
```

Example:

```go
// UNIX系システムでファイルに実行ビットを立てる。一部エラー処理省略
fi, _ := os.Stat(path)
if err := os.Chmod(path, fi.Mode()|0111); err != nil {
  log.Fatal(err)
}
```

### func Create

https://golang.org/pkg/os/#Create

```go
func Create(name string) (*File, error)
```

- ファイルを作成し、モード `O_RDWR` （読み書き両用）でオープンする
- ファイルが存在する場合、truncateされる
- 作成されるファイルのパーミッションには `0666` が指定される（umask前）

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

### func Mkdir

https://golang.org/pkg/os/#Mkdir

```go
func Mkdir(name string, perm FileMode) error
```

与えられたパーミッションでディレクトリを作成する。

Unix系OSだと、umask値によって挙動がちょっと変わるっぽい。

参考:

- [Go言語でファイル操作: ディレクトリの作り方 - Qiita](https://qiita.com/suin/items/af8f306dc6b38a293ef5)

### func MkdirAll

```go
func MkdirAll(path string, perm FileMode) error
```

- 途中のディレクトリも必要なら作ってくれる
  - 途中のディレクトリもパーミッションは同じになる
- 既にディレクトリがあったら何もせず、 `nil` を返す

### func NewFile

https://golang.org/pkg/os/#NewFile

```go
func NewFile(fd uintptr, name string) *File
```

> NewFile returns a new File with the given file descriptor and name.

### func Open

https://golang.org/pkg/os/#Open

```go
func Open(name string) (*File, error)
```

モード `O_RDONLY` （読み取り専用）でファイルを開く。

### func OpenFile

https://golang.org/pkg/os/#OpenFile

```go
func OpenFile(name string, flag int, perm FileMode) (*File, error)
```

[flag](#constants)（モード）やパーミッションを指定してファイルを開く。

### func Readlink

https://golang.org/pkg/os/#Readlink

```go
func Readlink(name string) (string, error)
```

シンボリックリンクのリンク先を返す。  
シンボリックリンクでなければ空文字を返すが、エラーになるわけではない。  
エラーは `*PathError` なので、これはnameが読めないときとかに起こるのだと思う。

### func Stat

```go
func Stat(name string) (FileInfo, error)
```

ファイルパスを受け取って、ファイルの情報を返す。  
エラーがあったら、きっと `*PathError`

参考:

- [Go言語 (golang) ファイル・ディレクトリの存在チェック](https://www.sukerou.com/2017/08/go-golang.html)

### func Symlink

https://golang.org/pkg/os/#Symlink

```go
func Symlink(src, link string) error
```

srcへのlinkを作る。  
エラーは `*LinkError` 型。

### func TempDir

https://golang.org/pkg/os/#TempDir

```go
func TempDir() string
```

デフォルトのテンポラリファイル用のディレクトリパスを返す。

- UNIX系OSなら `$TMPDIR` または `/tmp`

### func UserHomeDir

https://golang.org/pkg/os/#UserHomeDir

```go
func UserHomeDir() (string, error)
```

Unix系システムなら `$HOME`, Windowsなら `%USERPROFILE%` の値を返す。

### type File

https://golang.org/pkg/os/#File

オープンしたファイルディスクリプタを表現する構造体。

## os/exec

https://golang.org/pkg/os/exec/

コマンド実行で使う。

SYNOPSIS:

```go
cmd := exec.Command("sh", "-c", "echo stdout; echo 1>&2 stderr")

// コマンドの出力を標準（エラー）出力に設定
cmd.Stdout = os.Stdout
cmd.Stderr = os.Stderr
// cmd.Stdin = os.Stdin // 標準入力も設定可能

// コマンド実行
err := cmd.Run()

// コマンド実行し、stdoutを取得
out, err := cmd.Output()

// stdout, stderrをまとめて受け取る
stdoutStderr, err := cmd.CombinedOutput()
```

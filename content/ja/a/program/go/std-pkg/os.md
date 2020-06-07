---
title: "os"
linkTitle: "os"
description: https://golang.org/pkg/os/
date: 2020-06-06T21:15:56+09:00
weight: 600
---

## How-to
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

## Reference
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

### func Readlink

https://golang.org/pkg/os/#Readlink

```go
func Readlink(name string) (string, error)
```

シンボリックリンクのリンク先を返す。

### func Stat

```go
func Stat(name string) (FileInfo, error)
```

ファイルパスを受け取って、ファイルの情報を返す。  
エラーがあったら、きっと `*PathError`

参考:

- [Go言語 (golang) ファイル・ディレクトリの存在チェック](https://www.sukerou.com/2017/08/go-golang.html)

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

---
title: "path"
linkTitle: "path"
date: 2020-06-28T19:13:12+09:00
weight: 650
---

## path

https://golang.org/pkg/path/

URLなど `/` 区切りのパスを扱うパッケージ。

## path/filepath

https://golang.org/pkg/path/filepath/

ファイル名やパス名の操作に使える。

参考:

- [Big Sky :: Golang で物理ファイルの操作に path/filepath でなく path を使うと爆発します。](https://mattn.kaoriya.net/software/lang/go/20171024130616.htm)

### Examples

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

### func Abs

https://golang.org/pkg/path/filepath/#Abs

```go
func Abs(path string) (string, error)
```

pathの絶対パスを返す。

参考:

- [逆引きGolang (ファイル)#相対パスから絶対パスを求める](https://ashitani.jp/golangtips/tips_file.html#file_AbsPath)

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
- WalkFuncに与える関数シグネチャは下のWalkFunc型を参照

参考:

- https://stackoverflow.com/questions/6608873/file-system-scanning-in-golang

### type WalkFunc

```go
type WalkFunc func(path string, info os.FileInfo, err error) error
```

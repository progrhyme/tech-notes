---
title: "io"
linkTitle: "io"
description: https://golang.org/pkg/io/
date: 2020-06-28T19:11:59+09:00
weight: 200
---

## io

https://golang.org/pkg/io/

基礎的なI/Oのインタフェースを提供する。  
osパッケージなどにある様々なI/Oプリミティブを抽象化する。

参考:

- [【Go入門】ioパッケージ ～ 入出力処理の抽象化と共通化](https://leben.mobi/go/io-reader-writer/go-programming/)
- [ASCII.jp：Goならわかるシステムプログラミング](https://ascii.jp/serialarticles/1235262/)

### func Copy

https://golang.org/pkg/io/#Copy

```go
func Copy(dst Writer, src Reader) (written int64, err error)
```

srcからdstに書き込む。  
終了条件は、EOFに到達するか、エラーが発生すること。

Example:

```go
// 例: ファイルのコピー
// エラー処理は省略
src, _ := os.Open(srcName)
defer src.Close()
dst, _ := os.Create(dstName)
defer dst.Close()

io.Copy(dst, src)
```

参考:

- [\[Go言語\] ファイルをコピーする方法 - Qiita](https://qiita.com/cotrpepe/items/93e4a072c249a933e795)

### func TeeReader

https://golang.org/pkg/io/#TeeReader

```go
func TeeReader(r Reader, w Writer) Reader
```

rをwに書き込みつつ、同時に読み取れるReaderを提供する。  
入力を複製したいときに使える。

Example:

```go
r := strings.NewReader("some io.Reader stream to be read\n")
var buf bytes.Buffer
tee := io.TeeReader(r, &buf)

printall := func(r io.Reader) {
    b, _ := ioutil.ReadAll(r) // エラー処理省略
    fmt.Printf("%s", b)
}

printall(tee)
printall(&buf)
```

https://play.golang.org/p/p4bxk_oxr52

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

### Variables

```go
// /dev/null 的な存在。出力を破棄したいときに使うといい
var Discard io.Writer = devNull(0)
```

参考:

- [Go言語(golang)で出力を破棄する - golangの日記](https://golang.hateblo.jp/entry/2018/10/24/181434)

### func ReadDir

https://golang.org/pkg/io/ioutil/#ReadDir

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

### func ReadFile

https://golang.org/pkg/io/ioutil/#ReadFile

```go
func ReadFile(filename string) ([]byte, error)
```

ファイルを一気に読み込む。

Example

```go
content, err := ioutil.ReadFile("testdata/hello")
if err != nil {
    log.Fatal(err)
}
fmt.Printf("File contents: %s", content)
```

### func TempDir

https://golang.org/pkg/io/ioutil/#TempDir

```go
func TempDir(dir, pattern string) (name string, err error)
```

- dirの下位にテンポラリっぽい名前のディレクトリを作る。
- dirが空文字だったら、デフォルトのテンポラリファイルのディレクトリが使われる（See [os.TempDir]({{<ref "os.md">}}#tempdir)）
- 作ったディレクトリは自分で消さないと消えない
- patternは `*` を含む文字列を与えることができ、最後に現れた `*` がランダムに置換される。

Examples:

```go
logsDir, err := ioutil.TempDir(os.TempDir(), "*-logs")
if err != nil {
    log.Fatal(err)
}
defer os.RemoveAll(logsDir) // clean up
:
```

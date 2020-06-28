---
title: "標準パッケージ"
linkTitle: "pkg (stdlib)"
description: https://golang.org/pkg/
date: 2020-05-31T16:18:58+09:00
weight: 50
---

## archive/tar

https://golang.org/pkg/archive/tar/

tarアーカイブへのアクセスを実装。

## archive/zip

https://golang.org/pkg/archive/zip/

ZIPアーカイブの読み書き機能を提供。

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

Tips:

- 1行だけ読み取るなら、Scan()を1回だけ実行すればよい

参考:

- [CLI#ターミナルでEOFを入力する方法]({{<ref "/a/cli/_index.md">}}#ターミナルでeofを入力する方法)
- [Go言語で標準入力 - Qiita](https://qiita.com/kosukeKK/items/865e06de03d20664a83f)

## compress/gzip

https://pkg.go.dev/compress/gzip

RFC 1952に準拠したgzip圧縮ファイルの読み書き。

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

## go/build

https://golang.org/pkg/go/build/

Goパッケージの情報を集める。

### Build Constraints

https://golang.org/pkg/go/build/#hdr-Build_Constraints

build tagのこと。  
ここに詳しい仕様が書いてある。

関連項目:

- [go CLI#build-flags]({{<ref "/a/program/go/cli.md">}}#build-flags)

Example:

```go
// +build linux,386 darwin,!cgo
```

build tagは、上のように `// +build` で始まる行に記される。

`,` 区切りでAND条件を、スペース区切りでOR条件を、 `!` をprefixにつけることでNOT条件を表す。  
即ち、上のbuild tagをブール演算で表記すると、

```
(linux AND 386) OR (darwin AND (NOT cgo))
```

となる。

コマンド実行例:

```sh
go build -tags linux       # マッチしない
go build -tags linux,386   # マッチする
go build -tags darwin      # マッチする
go build -tags darwin,cgo  # マッチしない
```

`-tags` オプションで指定されたbuild tagにマッチしない場合、そのファイルは無視され、コンパイル対象とならない。

メモ:

- `GOOS`, `GOARCH` といったクロスコンパイル時に指定される環境変数もbuild tagとして渡されるのだと思う

特別なbuild tagとして、以下を記すと常にコンパイル対象から除外される:

```go
// +build ignore
```

Spec:

- build tagはファイルの先頭に書かなければならない
- build tagを複数行書くこともできる。評価される条件は、各行のAND条件になる
- build tagを記した後には空行が必要

参考:

- [go build -tagsを使ってRelease/Debugを切り替える - flyhigh](https://shinpei.github.io/blog/2014/10/07/use-build-constrains-or-build-tag-in-golang)

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

関連項目:

- [道場#ロギング]({{<ref "/a/program/go/dojo.md">}}#ロギング)

### Constants

https://pkg.go.dev/log?tab=doc#pkg-constants

```go
const (
	Ldate         = 1 << iota     // the date in the local time zone: 2009/01/23
	Ltime                         // the time in the local time zone: 01:23:23
	Lmicroseconds                 // microsecond resolution: 01:23:23.123123.  assumes Ltime.
	Llongfile                     // full file name and line number: /a/b/c/d.go:23
	Lshortfile                    // final file name element and line number: d.go:23. overrides Llongfile
	LUTC                          // if Ldate or Ltime is set, use UTC rather than the local time zone
	Lmsgprefix                    // move the "prefix" from the beginning of the line to before the message
	LstdFlags     = Ldate | Ltime // initial values for the standard logger
)
```

↑log.Newするときflag引数に与えるビット列の定義。

## runtime

https://golang.org/pkg/runtime/

Goのランタイムとやりとりする操作を提供するパッケージ。

Examples:

```go
// スタックトレースの表示
// iをインクリメントしていき、スタックトレースを表示する
i := 0
for {
    pt, file, line, ok := runtime.Caller(i)
    if !ok {
        // 取得できなくなったら終了
        break
    }
    funcName := runtime.FuncForPC(pt).Name()
    fmt.Printf("file=%s, line=%d, func=%v\n", file, line, funcName)
    i += 1
}
```

参考:

- [\[Go\] ファイル名、行数、関数名、スタックトレースをランタイム時に取得する - YoheiM .NET](https://www.yoheim.net/blog.php?q=20171006)

## strconv

https://pkg.go.dev/strconv

文字列と基本データ型間の変換機能を実装している。

Example:

```go
v := "10"
if s, err := strconv.Atoi(v); err == nil {
	fmt.Printf("%T, %v", s, s) //=> int, 10
}
```

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

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

https://pkg.go.dev/bufio

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

### func NewScanner

https://pkg.go.dev/bufio?tab=doc#NewScanner

```go
func NewScanner(r io.Reader) *Scanner
```

rに対するScannerを生成。  
デフォルトで改行区切りとなる。

### type Scanner (struct)

https://pkg.go.dev/bufio?tab=doc#Scanner

スキャナーオブジェクト。読み取ったテキストやエラーを保持する。

#### func Split

https://pkg.go.dev/bufio?tab=doc#Scanner.Split

```go
func (s *Scanner) Split(split SplitFunc)
```

読取り時にテキストを分割する方法（1回のs.Scan()でどこまで読み取るか）を変更する。

Example:

```go
scanner := bufio.NewScanner(strings.NewReader(input))
// 空白文字区切りで読み取る
scanner.Split(bufio.ScanWords)
// Count the words.
count := 0
for scanner.Scan() {
	count++
}
// エラー処理は省略
fmt.Printf("%d\n", count)
```

See also https://pkg.go.dev/bufio?tab=doc#example-Scanner-Words

## compress/gzip

https://pkg.go.dev/compress/gzip

RFC 1952に準拠したgzip圧縮ファイルの読み書き。

## context

https://golang.org/pkg/context/

Webサーバとかで引きずり回すコンテキスト。  

Examples:

```go
ctx := context.Background() # context.Contextな構造体を生成

// タイムアウト付きコンテキストを生成。cancelはタイムアウト時に実行される
ctx2, cancel := context.WithDeadline(ctx, time.Now().Add(timeout))
defer cancel()

// 時間指定。↑とほぼ同じだと思う
ctx, cancel := context.WithTimeout(context.Background(), 50*time.Millisecond)
defer cancel()
```

参考:

- https://blog.golang.org/context
- 2016 [Go1.7のcontextパッケージ | SOTA](http://deeeet.com/writing/2016/07/22/context/ "Go1.7のcontextパッケージ | SOTA")
- 2019年3月 [context.WithCancel, WithTimeout で知っておいた方が良いこと - Carpe Diem](https://christina04.hatenablog.com/entry/tips-for-context-with-cancel_1)
- 2019年7月 [golang contextの使い方とか概念(contextとは)的な話 - Qiita](https://qiita.com/marnie_ms4/items/985d67c4c1b29e11fffc)
- 2019年12月 [Go の Context を学ぶ - Qiita](https://qiita.com/TsuyoshiUshio@github/items/34b63b663ffd56125c07) ... 簡単な概念の説明とサンプルコード

### contextとは

contextパッケージのgodoc序文より。

contextパッケージはContext型を定義する。
これはタイムアウトやキャンセルのためのシグナルなどリクエストに紐づく値を保持する。
これらの値はAPIの境界を越えるものだったり、プロセス間で使われるものだ。

- サーバに入ってくるリクエストはContextを作るべきだし、サーバへのリクエストはContextを受け入れるべき
- これらの間（サーバがリクエストを処理する間 or Contextを生成してサーバにリクエストを送信するまでの間）で関数が連鎖するときは、Contextは伝播しないといけない
- ただし、伝播してきたContextをWithCancelやWithDeadline, WithTimeout, WithValueで作り直したContextに置き換えることができる
- Contextがキャンセルされたとき、そのContextに由来するすべてのContextも同様にキャンセルされるべきである。

Context利用時の作法:

- Contextを構造体の中に保持してはいけない。必要とする全ての関数に明示的に渡すこと。第1引数として、典型的には `ctx` を仮引数名とする
- 関数が許していても、Contextにnilを渡さないこと。代わりに context.TODO を渡すこと
- context ValuesはプロセスやAPIをまたぐリクエストスコープのデータに使うようにして、関数へのオプショナルなパラメータのために使わないこと

ユースケース:

- goroutineのキャンセル

参考:

- 2019年3月 [初心者がGo言語のcontextを爆速で理解する ~ cancel編 ~ - Qiita](https://qiita.com/yoshinori_hisakawa/items/a6608b29059a945fbbbd)

## crypto/sha256

https://golang.org/pkg/crypto/sha256/

SHA224, SHA256ハッシュアルゴリズムの実装。

### func New

https://golang.org/pkg/crypto/sha256/#New

```go
func New() hash.Hash
```

Example:

```go
h := sha256.New()
h.Write([]byte("hello world\n"))
fmt.Printf("%x", h.Sum(nil))
```

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

## hash

https://golang.org/pkg/hash/

データのハッシュ値を求めるためのインタフェースを提供する。

利用例については、[crypto/sha256#New](#func-new)を参照。

## hash/crc32

https://golang.org/pkg/hash/crc32/

CRC-32の実装。

関連項目:

- [セキュリティ > 符号化#CRC]({{<ref "/a/security/encode.md">}}#crc)

### func NewIEEE

https://golang.org/pkg/hash/crc32/#NewIEEE

```go
func NewIEEE() hash.Hash32
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

関連項目:

- [道場#ロギング]({{<ref "/a/program/go/dojo/_index.md">}}#ロギング)

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

### Constants

```go
const (
  // 386, amd64, arm, s390x, and so on
  GOARCH string = sys.GOARCH
  // darwin, freebsd, linux, and so on
  GOOS string = sys.GOOS
)
```

Tips:

- GOOSとGOARCHの組合せを見るには `go tool dist list` を実行するといい

## sort

https://golang.org/pkg/sort/

スライスやユーザ定義のコレクションをソートするプリミティブを提供。

### func Sort

https://golang.org/pkg/sort/#Sort

```go
func Sort(data Interface)
```

dataの中身を昇順に並び替える。  

- data.Lenを1回実行
- `O(n*log(n))` 回数、data.Lessとdata.Swapを実行

### func Strings

https://golang.org/pkg/sort/#Strings

```go
func Strings(a []string)
```

stringのスライスを昇順に並び替え。

Example:

```go
s := []string{"Go", "Bravo", "Gopher", "Alpha", "Grin", "Delta"}
sort.Strings(s)
fmt.Println(s)
//=> [Alpha Bravo Delta Go Gopher Grin]
```

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

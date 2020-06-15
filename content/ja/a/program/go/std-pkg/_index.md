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

Tips:

- 1行だけ読み取るなら、Scan()を1回だけ実行すればよい

参考:

- [CLI#ターミナルでEOFを入力する方法]({{<ref "/a/cli/_index.md">}}#ターミナルでeofを入力する方法)
- [Go言語で標準入力 - Qiita](https://qiita.com/kosukeKK/items/865e06de03d20664a83f)

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

Examples:

```go
func do() error {
    :
    if !check() {
        return errors.New("Something is wrong!")
    }
    :
    return nil
}
```

関連項目:

- [道場#例外処理]({{<ref "/a/program/go/dojo.md">}}#例外処理)

参考:

- [pkg/errors から徐々に Go 1.13 errors へ移行する - blog.syfm](https://syfm.hatenablog.com/entry/2019/12/27/193348)

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

### Variables

```go
// /dev/null 的な存在。出力を破棄したいときに使うといい
var Discard io.Writer = devNull(0)
```

参考:

- [Go言語(golang)で出力を破棄する - golangの日記](https://golang.hateblo.jp/entry/2018/10/24/181434)

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

## testing

https://golang.org/pkg/testing/

テストやベンチマークで利用するパッケージ。

Examples:

```go
import testing

func TestAbs(t *testing.T) {
    got := Abs(-1)
    if got != 1 {
        t.Errorf("Abs(-1) = %d; want 1", got)
    }
}
```

### type T

テストの状態を保持する。

#### func Errorf

https://golang.org/pkg/testing/#T.Errorf

```go
func (c *T) Errorf(format string, args ...interface{})
```

- Errorメソッドの書式指定対応版
- よく使われる
- Logf + Fail

#### func Run

https://golang.org/pkg/testing/#T.Run

```go
func (t *T) Run(name string, f func(t *T)) bool
```

サブテストを実行する。

## text/template

https://golang.org/pkg/text/template/

関連項目:

- [道場#テンプレート]({{<ref "dojo.md">}}#テンプレート)

Examples:

```go
const letter = `
Dear {{.Name}},
{{if .Attended}}
It was a pleasure to see you at the wedding.
{{- else}}
It is a shame you couldn't make it to the wedding.
{{- end}}
{{with .Gift -}}
Thank you for the lovely {{.}}.
{{end}}
Best wishes,
Josie
`

// Prepare some data to insert into the template.
type recipient struct {
    Name, Gift string
    Attended   bool
}
var recipients = []recipient{
    {"Aunt Mildred", "bone china tea set", true},
    {"Uncle John", "moleskin pants", false},
    {"Cousin Rodney", "", false},
}

// Create a new template and parse the letter into it.
t := template.Must(template.New("letter").Parse(letter))

// Execute the template for each recipient.
for _, r := range recipients {
    err := t.Execute(os.Stdout, r)
    if err != nil {
        log.Println("executing template:", err)
    }
}
```

実行すると次のようになる:

```
Dear Aunt Mildred,

It was a pleasure to see you at the wedding.
Thank you for the lovely bone china tea set.

Best wishes,
Josie

Dear Uncle John,

It is a shame you couldn't make it to the wedding.
Thank you for the lovely moleskin pants.

Best wishes,
Josie

Dear Cousin Rodney,

It is a shame you couldn't make it to the wedding.

Best wishes,
Josie
```

### type Template

https://golang.org/pkg/text/template/#Template

```go
type Template struct {
    *parse.Tree
    // contains filtered or unexported fields
}
```

パースされたテンプレート。

#### func Delims

https://golang.org/pkg/text/template/#Template.Delims

```go
func (t *Template) Delims(left, right string) *Template
```

デリミタ（区切り文字）を設定する。  
デフォルトは `{{`, `}}` 。  
テンプレートを返すので、メソッドチェインできる。
（なんかここだけRubyっぽい）

```go
const script = `export <<.EnvKey>>=${<<.EnvKey>>:-"<<.Default>>"}
`
t := template.Must(template.New("script").Delims("<<", ">>").Parse(script))
t.Execute(os.Stdout, struct{ EnvKey, Default string}{"FOO", "foo"})
```

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

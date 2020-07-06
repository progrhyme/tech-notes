---
title: "flag"
linkTitle: "flag"
description: https://golang.org/pkg/flag/
date: 2020-06-06T14:44:40+09:00
weight: 100
---

## About

コマンドラインオプションをパースしてくれる君。

- ヘルプ付き
- ショートオプションとロングオプション両対応したいときはちょっとめんどい（後述）

### 関連パッケージ

非公式で、flagの高機能版:

- [jessevdk/go-flags](https://github.com/jessevdk/go-flags)
- [spf13/pflag]({{<ref "/a/program/go/3rd-pkg/_index.md">}}#spf13pflag)

## SYNOPSIS

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

## How-to
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

パッケージ変数 `Usage` や、 `type FlagSet` のメンバ変数 `Usage` に独自関数を設定することで、出力をカスタマイズできる。

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

## Reference
### func Arg

`func Arg(i int) string`

フラグでないi番目のコマンドライン引数を返す。
`Arg(0)` が最初の引数。

### func Args

シグネチャ:

```go
func Args() []string
```

フラグでないコマンドライン引数のリストを返す。

### type FlagSet

https://golang.org/pkg/flag/#FlagSet

```go
type FlagSet struct {
    Usage func() // usage表示時に呼ばれる関数
}
```

#### func (*FlagSet) NArg

シグネチャ:

```go
func (f *FlagSet) NArg() int
```

フラグ処理後に残った引数の数を返す。

#### func (*FlagSet) SetOutput

https://golang.org/pkg/flag/#FlagSet.SetOutput

シグネチャ:

```go
func (f *FlagSet) SetOutput(output io.Writer)
```

usageやエラーメッセージの出力先を設定する。  
outputがnilのときは `os.Stderr` が使われる。

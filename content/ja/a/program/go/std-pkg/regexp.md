---
title: "regexp"
linkTitle: "regexp"
description: https://golang.org/pkg/regexp/
date: 2020-06-14T15:53:04+09:00
weight: 750
---

## About

正規表現の文法は `\C` を除いて https://github.com/google/re2/wiki/Syntax に従っている。  
文法の概要については次を実行して見るとよい:

```sh
go doc regexp/syntax
```

関連項目:

- [道場#正規表現]({{<ref "/a/program/go/dojo.md">}}#正規表現)

参考:

- [逆引きGolang (正規表現)](https://ashitani.jp/golangtips/tips_regexp.html)

## Examples

```go
// Compile the expression once, usually at init time.
// Use raw strings to avoid having to quote the backslashes.
var validID = regexp.MustCompile(`^[a-z]+\[[0-9]+\]$`)

fmt.Println(validID.MatchString("adam[23]"))
fmt.Println(validID.MatchString("eve[7]"))
fmt.Println(validID.MatchString("Job[48]"))
fmt.Println(validID.MatchString("snakey"))
```

## Reference
### type Regexp

https://golang.org/pkg/regexp/#Regexp

コンパイルされた正規表現を表す。

#### func FindStringSubmatch

https://golang.org/pkg/regexp/#Regexp.FindStringSubmatch

```go
func (re *Regexp) FindStringSubmatch(s string) []string
```

FindSubmatchのstring版。

Examples:

```go
re := regexp.MustCompile(`a(x*)b(y|z)c`)
fmt.Printf("%q\n", re.FindStringSubmatch("-axxxbyc-"))
fmt.Printf("%q\n", re.FindStringSubmatch("-abzc-"))
```

実行結果:

```
["axxxbyc" "xxx" "y"]
["abzc" "" "z"]
```

#### func FindSubmatch

https://golang.org/pkg/regexp/#Regexp.FindSubmatch

```go
func (re *Regexp) FindSubmatch(b []byte) [][]byte
```

グループ化された正規表現を使って、後方参照のようなことができる。

Examples:

```go
re := regexp.MustCompile(`foo(.?)`)
fmt.Printf("%q\n", re.FindSubmatch([]byte(`seafood fool`)))
```

実行結果:

```
["food" "d"]
```

参考:

- [Go 言語で正規表現のグループ化した文字列を取得する - nise_nabeの日記](https://nisenabe.hatenablog.com/entry/2013/01/29/045559)

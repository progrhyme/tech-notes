---
title: "strings"
linkTitle: "strings"
description: https://pkg.go.dev/strings
date: 2020-06-14T15:52:27+09:00
weight: 800
---

UTF-8文字列を扱うためのシンプルな関数を提供する。

## Reference
### func Contains

https://golang.org/pkg/strings/#Contains

```go
func Contains(s, substr string) bool
```

sが部分文字列substrを含むかどうか。

### func HasPrefix

https://pkg.go.dev/strings?tab=doc#HasPrefix

```go
func HasPrefix(s, prefix string) bool
```

sがprefixから始まってるかチェックする。

Examples:

```go
strings.HasPrefix("Gopher", "Go") //=> true
strings.HasPrefix("Gopher", "C")  //=> false
strings.HasPrefix("Gopher", "")   //=> true
```

### func TrimRight

https://pkg.go.dev/strings?tab=doc#TrimRight

```go
func TrimRight(s string, cutset string) string
```

末尾の改行コードを取り除きたいときなどに便利。

```go
strings.TrimRight(s, "\r\n")
```

参考:

- [\[Go\]stringsパッケージのTrimLeftとTrimRightの挙動について - 白帽子研究室](https://sites.google.com/site/sbwhitecap/blog/2014/06/14a)

### func TrimSuffix

https://pkg.go.dev/strings?tab=doc#TrimSuffix

```go
func TrimSuffix(s, suffix string) string
```

拡張子とか除くときに便利。  
マッチしなければそのまま返してくれるので使いやすい。

TrimRightという似たような関数もある。

### type Builder

io.Writerを実装した文字列を効率よく作る型。  
初期化不要で使える。

Examples:

```go
var b strings.Builder
for i := 3; i >= 1; i-- {
    fmt.Fprintf(&b, "%d...", i)
}
b.WriteString("ignition")
fmt.Println(b.String())
```

参考:

- [Go1.10で入るstrings.Builderを検証した #golang - Qiita](https://qiita.com/tenntenn/items/94923a0c527d499db5b9)

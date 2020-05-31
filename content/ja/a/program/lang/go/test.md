---
title: "Testing"
linkTitle: "テスト"
date: 2020-05-31T16:18:23+09:00
weight: 70
---

Goのテストに関する情報をまとめる。

## Getting Started

- 基本的に、標準の [testing](https://golang.org/pkg/testing/) pkgを使う
- フレームワークは使わない。愚直に書く

## Go Blog関連エントリ

- 2016-10-03 [Using Subtests and Sub-benchmarks - The Go Blog](https://blog.golang.org/subtests) ... Go 1.7で導入されたsubtests, sub-benchmarksについて
- 2015-05-07 [Testable Examples in Go - The Go Blog](https://blog.golang.org/examples)

## Topics
### Goで結合・統合・外部テストを書く

pkgに対する単体テスト以外のテストにもGoのtesting pkgを使うことができる。  
やり方は簡単で、 `package foo_test` な `foo_test.go` を書くだけ。

```go
package foo_test

import "testing"

func TestFoo(t *testing.T) {
    : // テストコード
}
```

参考:

- [プログラミング言語Go](http://amzn.to/2tXDqfc)

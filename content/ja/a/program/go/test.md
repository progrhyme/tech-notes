---
title: "Testing"
linkTitle: "テスト"
date: 2020-05-31T16:18:23+09:00
weight: 70
---

Goのテストに関する情報をまとめる。

## Getting Started

- `go test` コマンドでテストを実行する（後述）
- 基本的に、標準のtesting pkgを使う

関連項目:

- [pkg (stdlib) > testing]({{<ref "std-pkg/_index.md">}}#testing)

Tips:

- フレームワークは使わない。愚直に書く

入門ガイド:

- [Go by Example: Testing](https://gobyexample.com/testing)

参考:

- [春の入門祭り 🌸 #01 Goのテストに入門してみよう！ | フューチャー技術ブログ](https://future-architect.github.io/articles/20200601/)

### 例

package xのテストを書くとする。

- package xのコードが置かれたディレクトリに `*_test.go` というファイルを作る
  - 先頭行は `package x`
- `func TestXxx(t *testing.T)` という関数を作り、その中にテストコードを書く
  - `t.Errorf` 関数でエラーをレポート
  - エラーが報告されなければ、その関数は成功したことになる

### テストの実行

See Also: [goコマンド#test]({{<ref "cli.md">}}#test)

モジュールのルートディレクトリで下のように実行するとよい:

```sh
go test [-v] ./...
```

`-v` を付けると個々のテストケースが見える。  
サブテストの中も見える。

Spec:

- `*_test.go` というファイルがテスト対象
- `.`, `_` で始まるファイルは無視される（ `_test.go` も）
- `testdata` というディレクトリは無視される

## How-to
### テーブルドリブンテスト

サブテスト（t.Run）と組み合わせる。

Examples:

```go
var flagtests = []struct {
	in  string
	out string
}{
	{"%a", "[%a]"},
	{"%-a", "[%-a]"},
	{"%+a", "[%+a]"},
	{"%#a", "[%#a]"},
	{"% a", "[% a]"},
	{"%0a", "[%0a]"},
	{"%1.2a", "[%1.2a]"},
	{"%-1.2a", "[%-1.2a]"},
	{"%+1.2a", "[%+1.2a]"},
	{"%-+1.2a", "[%+-1.2a]"},
	{"%-+1.2abc", "[%+-1.2a]bc"},
	{"%-1.2abc", "[%-1.2a]bc"},
}
func TestFlagParser(t *testing.T) {
	var flagprinter flagPrinter
	for _, tt := range flagtests {
		t.Run(tt.in, func(t *testing.T) {
			s := Sprintf(tt.in, &flagprinter)
			if s != tt.out {
				t.Errorf("got %q, want %q", s, tt.out)
			}
		})
	}
}
```

NOTE:

- `t.Parallel()` を使うと並列化もできる

参考:

- https://github.com/golang/go/wiki/TableDrivenTests

### I/Oを伴うテスト

bytes.Bufferや[strings.Builder]({{<ref "std-pkg/strings.md">}}#type-builder)を使うといい。

参考:

- [I/O を伴うテストには bytes.Buffer が便利 - Qiita](https://qiita.com/yuya_takeyama/items/c4211fa77488cb6915ec)

### テストデータを用意する

testdata/ というディレクトリに入れる。  
これはパッケージとみなされない。

参考:

- https://golang.org/cmd/go/#hdr-Test_packages

## pkg

テストで使えるパッケージ。

### google/go-cmp

https://pkg.go.dev/github.com/google/go-cmp/cmp

値の比較のためのユーティリティ。

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

## Go Blog関連エントリ

- 2016-10-03 [Using Subtests and Sub-benchmarks - The Go Blog](https://blog.golang.org/subtests) ... Go 1.7で導入されたsubtests, sub-benchmarksについて
- 2015-05-07 [Testable Examples in Go - The Go Blog](https://blog.golang.org/examples)

---
title: "コーディング"
linkTitle: "コーディング"
date: 2020-07-14T23:11:44+09:00
weight: 50
---

## コーディング規約

公式ガイド:

- [Effective Go - The Go Programming Language](https://golang.org/doc/effective_go.html)
- [CodeReviewComments · golang/go Wiki](https://github.com/golang/go/wiki/CodeReviewComments) ... Goらしい書き方を学べる
  - 邦訳: [Go Codereview Comments](https://knsh14.github.io/translations/go-codereview-comments/)

### Mixed Caps

- https://golang.org/doc/effective_go.html#mixed-caps
- https://github.com/golang/go/wiki/CodeReviewComments#mixed-caps

複数の単語から成る名前には以下のような命名を行う:

- `mixedCaps` ... unexported
- `MixedCaps` ... exported

定数でも同じ。  
`os.O_CREATE` とかは他言語由来の一部の例外。

参考:

- [constants - Go naming conventions for const - Stack Overflow](https://stackoverflow.com/questions/22688906/go-naming-conventions-for-const)

## ドキュメントコメント

ドキュメンテーションコメント、いわゆるGoDocの書き方。

公式リソース:

- [Effective Go - The Go Programming Language#Commentary](https://golang.org/doc/effective_go.html#commentary)
- [Godoc: documenting Go code - The Go Blog](https://blog.golang.org/godoc)
- [Testable Examples in Go - The Go Blog](https://blog.golang.org/examples)

参考:

- [チョットできるGoプログラマーになるための詳解GoDoc - Qiita](https://qiita.com/shibukawa/items/8c70fdd1972fad76a5ce)
- [GoDocドキュメントの書き方 - Plan 9とGo言語のブログ](https://blog.lufia.org/entry/2018/05/14/150400)

### Exampleをつける

上の参考記事を読むといい。

ポイント:

- テストコードとして記述する。 `xxx_test.go` というファイルに書く。
- **package名はテスト対象のパッケージと異なる。 `package xxx_test` のように `_test` を付ける**
  - 同じでも動くんだけど、Exampleとしては相応しくないコードになる

## リファクタリング

関連項目:

- [tools > gorename]({{<ref "../tools.md">}}#cmdgorename)

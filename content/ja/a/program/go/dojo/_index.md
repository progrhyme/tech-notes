---
title: "Road to Gopher"
linkTitle: "道場"
date: 2020-06-06T18:08:05+09:00
weight: 40
---

Gopherを名乗る上で必須と思われる基礎的なトピックを扱う（予定）。

前提:

- [言語仕様]({{<ref "../spec/_index.md">}})の内容を把握していること

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

## 例外処理

入門ガイド:

- [Go by Example: Errors](https://gobyexample.com/errors)
- [Go by Example: Panic](https://gobyexample.com/panic)
- https://golang.org/ref/spec#Handling_panics

関連項目:

- [pkg (stdlib) > errors]({{<ref "../std-pkg/errors.md">}})
- [言語仕様#panic]({{<ref "../spec/_index.md">}}#panic)
- [言語仕様#defer]({{<ref "../spec/_index.md">}}#defer)

参考:

- [Go言語のエラーハンドリングについて - Qiita](https://qiita.com/nayuneko/items/3c0b3c0de9e8b27c9548)
- [Golangのエラーハンドリングの基本 - Qiita](https://qiita.com/shoichiimamura/items/13199f420ebaf0f0c37c)
- [Defer, Panic, and Recover - The Go Blog](https://blog.golang.org/defer-panic-and-recover)
- [panicはともかくrecoverに使いどころはほとんどない - Qiita](https://qiita.com/ruiu/items/ff98ded599d97cf6646e)
- [golangでrecoverしたときの戻り値 - PartyIX](https://h3poteto.hatenablog.com/entry/2015/12/13/010000)
- [Golangでエラー時にスタックトレースを表示する - Qiita](https://qiita.com/deeeet/items/dacc71932393ab35d9f8)

## ドキュメントコメント

ドキュメンテーションコメント、いわゆるGoDocの書き方。

公式リソース:

- [Effective Go - The Go Programming Language#Commentary](https://golang.org/doc/effective_go.html#commentary)
- [Godoc: documenting Go code - The Go Blog](https://blog.golang.org/godoc)
- [Testable Examples in Go - The Go Blog](https://blog.golang.org/examples)

参考:

- [チョットできるGoプログラマーになるための詳解GoDoc - Qiita](https://qiita.com/shibukawa/items/8c70fdd1972fad76a5ce)
- [GoDocドキュメントの書き方 - Plan 9とGo言語のブログ](https://blog.lufia.org/entry/2018/05/14/150400)

## テスト

See [テスト]({{<ref "../test.md">}})

## コマンドライン

関連項目:

- [入出力 > 標準入出力]({{<ref "io.md">}}#標準入出力)

参考:

- [ボイラプレート編 - #golang で CLI 作るときにいつもつかうやつ - Qiita](https://qiita.com/izumin5210/items/25a27d4f3c5078588f79)

### コマンド引数

入門サンプル:

- [Go by Example: Command-Line Arguments](https://gobyexample.com/command-line-arguments)

関連項目:

- [pkg (stdlib) > flag]({{<ref "../std-pkg/flag.md">}})

参考:

- [2020-05-31#GolangのCLIパッケージを改めて探した]({{<ref "20200531.md">}}#golangのcliパッケージを改めて探した)

## 外部コマンド実行

関連項目:

- [pkg (stdlib) > os/exec]({{<ref "../std-pkg/os.md">}}#osexec)

## ファイル操作

関連項目:

- [pkg (stdlib) > os]({{<ref "../std-pkg/os.md">}})
- [pkg (stdlib) > path/filepath]({{<ref "../std-pkg/path.md">}}#pathfilepath)

参考:

- [逆引きGolang (ファイル)](https://ashitani.jp/golangtips/tips_file.html)

### ディレクトリ操作

参考:

- [逆引きGolang (ディレクトリ)](https://ashitani.jp/golangtips/tips_dir.html)

### 実行可能ファイルを判定

Examples:

```go
func isExecutableFile(f os.FileInfo) {
  return !f.IsDir() && f.Mode()&0111 != 0
}
```

参考:

- [unix - How to check if a file is executable in go? - Stack Overflow](https://stackoverflow.com/questions/60128401/how-to-check-if-a-file-is-executable-in-go)

### シンボリックリンクを判別

いくつか使える関数があるが、どれも一発で行かなくて少しだけ面倒くさい。

Example:

```go
if link, err := os.Readlink(path); link != "" {
  fmt.Printf("[Symlink] %s -> %s")
} else {
  fmt.Printf("[Not Symlink] %s")
}
```

他に使えそうな関数:

- os.Lstat
- filepath.EvalSymlinks

参考:

- [golangでsymlink判別を実施する - Qiita](https://qiita.com/letusfly85/items/e9ecd6eafc0b03d8f57f)

## ライブラリ管理

[Go 1.14](https://golang.org/doc/go1.14)からGo Modulesが標準機能になったので、これを使いましょう。

ドキュメント:

- https://github.com/golang/go/wiki/Modules
- [Go Modules Reference - The Go Programming Language](https://golang.org/ref/mod)

関連項目:

- [2020-06-08#はじめてのGo-Module]({{<ref "20200608.md">}}#はじめてのgo-module)

参考:

- [Using Go Modules - The Go Blog](https://blog.golang.org/using-go-modules)
- [Go言語の依存モジュール管理ツール Modules の使い方 - Qiita](https://qiita.com/uchiko/items/64fb3020dd64cf211d4e)

## ビルド

関連項目:

- [エコシステム#ビルド・公開]({{<ref "../ecosystem/_index.md">}}#ビルド公開)

## モジュール作成

上の[ライブラリ管理](#ライブラリ管理)で述べたGo Moduleの仕組みを使う。

### モジュール更新

新しいバージョンを公開する場合、pkg.go.devにすぐに反映されないことがある。  
その場合、以下いずれかの操作を行う:

- proxy.golang.org に当該バージョンのモジュールをリクエストする
  - 例) https://proxy.golang.org/example.com/my/module/@v/v1.0.0.info にGETリクエストを送る
- GOPROXY="https://proxy.golang.org" をつけてmodule-aware modeでgo getする
  - 例) `GOPROXY="https://proxy.golang.org" GO111MODULE=on go get example.com/my/module@v1.0.0`

関連項目:

- [2020-06-20#Go-moduleの更新をpkg.go.devに反映する]({{<ref "20200620.md">}}#go-moduleの更新をpkggodevに反映する)

Reference:

- https://go.dev/about
- https://proxy.golang.org/

## オブジェクト指向プログラミング

Golangは型の継承をサポートしていないが、構造体とインタフェースを使いこなすと、オブジェクト指向プログラミングを実現ことができる。

NOTE:

- 構造体の埋め込みは継承とは異なるので、注意が必要
- インタフェースを使うとダックタイピングができるが、インタフェースはレシーバにはできない

参考:

- [Frequently Asked Questions (FAQ) - The Go Programming Language#Is_Go_an_object-oriented_language](https://golang.org/doc/faq#Is_Go_an_object-oriented_language)
- [Go言語で「embedded で継承ができる」と思わないほうがいいのはなぜか？ - Qiita](https://qiita.com/Maki-Daisuke/items/511b8989e528f7c70f80)
- [オブジェクト指向言語としてGolangをやろうとするとハマること - Qiita](https://qiita.com/shibukawa/items/16acb36e94cfe3b02aa1)
  - 上の牧さんの記事とほぼ同じことを言っている
- [Goはオブジェクト指向言語だろうか？ | POSTD](https://postd.cc/is-go-object-oriented/)

## ロギング

標準のlogパッケージはミニマルなので、他言語から来たプログラマーなど、各位で拡張したくなることがよくある。

関連項目:

- [pkg (stdlib) > log]({{<ref "../std-pkg/_index.md">}}#log)

参考:

- [loggingについて話そう - Qiita](https://qiita.com/methane/items/cedbf546ae2db8a63c3d) ... Goにおける思想的な
- [Log パッケージで遊ぶ — プログラミング言語 Go | text.Baldanders.info](https://text.baldanders.info/golang/logger/) ... ログレベル対応など
- [go言語におけるロギングについて - blog.satotaichi.info](http://blog.satotaichi.info/logging-frameworks-for-go/) ... 筆者のオススメパッケージ紹介

## 正規表現

Webサーバなどで使うときは、パフォーマンスに気をつける必要がありそう。

関連項目:

- [pkg (stdlib) > regexp]({{<ref "../std-pkg/regexp.md">}})

参考:

- [逆引きGolang (正規表現)](https://ashitani.jp/golangtips/tips_regexp.html)
- [regexpとの付き合い方 〜 Go言語標準の正規表現ライブラリのパフォーマンスとアルゴリズム〜 - Eureka Engineering - Medium](https://medium.com/eureka-engineering/regexp%E3%81%A8%E3%81%AE%E4%BB%98%E3%81%8D%E5%90%88%E3%81%84%E6%96%B9-go%E8%A8%80%E8%AA%9E%E6%A8%99%E6%BA%96%E3%81%AE%E6%AD%A3%E8%A6%8F%E8%A1%A8%E7%8F%BE%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AA%E3%81%AE%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9%E3%81%A8%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0-984b6cbeeb2b)

## テンプレート

標準パッケージのhtml/templateやtext/templateがよく使われる。

関連項目:

- [pkg (stdlib) > text/template]({{<ref "../std-pkg/text.md">}}#texttemplate)

参考:

- [Golang Templates Cheatsheet | curtisvermeeren.github.io](https://curtisvermeeren.github.io/2017/09/14/Golang-Templates-Cheatsheet)

### template構文

html/templateやtext/templateの構文。

Examples:

```html
<ul>
  <!-- ループ処理 -->
  {{ range $i, $val := . }}
    <ul>{{ $i }} : {{ $val }}
  {{ end }}
</ul>
```

Tips:

- テンプレートにstructやmapを渡すと、 `.key` のような形で要素/メンバ変数にアクセスできる

参考:

- [Go言語のテンプレート機能について - Qiita](https://qiita.com/ryokwkm/items/774927f43a3fc5d89cb0)
- [テンプレート機能を使用する (text/template, html/template) | まくまくHugo/Goノート](https://maku77.github.io/hugo/go/template.html)

## リファクタリング

関連項目:

- [tools > gorename]({{<ref "../tools.md">}}#cmdgorename)

## デバッグ

キーワード:

- スタックトレース

関連項目:

- [pkg (stdlib) > runtime]({{<ref "../std-pkg/_index.md">}}#runtime)
- [エコシステム#デバッガ]({{<ref "../ecosystem/_index.md">}}#デバッガ)

## バリデータ

次の2つが有名そう:

- https://pkg.go.dev/github.com/go-playground/validator
- https://github.com/go-ozzo/ozzo-validation

参考:

- [Go言語のバリデーションチェックライブラリ(ozzo-validation)を分かりやすくまとめてみた - Qiita](https://qiita.com/gold-kou/items/201a19d9d0c760cc2104)
- [go-playground/validator でバリデーションを実装する｜maco｜note](https://note.com/mkudo/n/n139de888a151)

## プロファイリング

※2017年以前の情報

- [runtime/pprof](https://golang.org/pkg/runtime/pprof/ "pprof - The Go Programming Language")という標準pkgを使うのが基本な感じ。
  - その内 [標準パッケージ - progrhyme's Tech Wiki](https://sites.google.com/site/progrhymetechwiki/programming/go/std-pkg "標準パッケージ - progrhyme's Tech Wiki") に書くと思う。
- runtimeのデバッグに役立つ環境変数の話:
  - [GODEBUG | Dave Cheney](https://dave.cheney.net/tag/godebug "GODEBUG | Dave Cheney")

参考:

- [Profiling Go Programs - The Go Blog](https://blog.golang.org/profiling-go-programs "Profiling Go Programs - The Go Blog") ... pprof
- [golangで書かれたプログラムのメモリ使用状況を見る - hakobe-blog ♨](http://hakobe932.hatenablog.com/entry/2014/04/10/010619 "golangで書かれたプログラムのメモリ使用状況を見る - hakobe-blog ♨") ... pprof, net/http/pprof
- [golang profiling の基礎](https://www.slideshare.net/yuichironakazawa2/golang-profiling-77163552 "golang profiling の基礎") ... pprof他
- [golangパフォーマンス3: mapとGC - Qiita](http://qiita.com/oywc410/items/ad8baee00f039705a5c0 "golangパフォーマンス3: mapとGC - Qiita")

## 構造化データファイルの取り扱い

YAML, JSON, TOMLなど。

関連項目:

- [pkg (stdlib) > encoding/json]({{<ref "../std-pkg/encoding.md">}}#encodingjson)
- [pkg (3rd) > go-yaml/yaml]({{<ref "../3rd-pkg/_index.md">}}#go-yamlyaml)
- [言語仕様#構造体-タグ]({{<ref "../spec/type.md">}}#タグ)

参考:

- [golang は ゆるふわに JSON を扱えまぁす! — KaoriYa](https://www.kaoriya.net/blog/2016/06/25/)

## プラグイン機構

Go 1.8で[plugin](https://golang.org/pkg/plugin/)パッケージが標準ライブラリに入った。

他に、RPCスタイルの[hashicorp/go-plugin](https://github.com/hashicorp/go-plugin)などもある。

参考:

- [Go 1.8のpluginパッケージを試してみる - Qiita](https://qiita.com/qt-luigi/items/47a7913145fc747da0c7)
- [Go言語でプラグイン機構をつくる | SOTA](https://deeeet.com/writing/2015/04/28/pingo/)

## リフレクション

reflectパッケージを使う。

参考:

- [Go 言語 reflect チートシート - Qiita](https://qiita.com/nirasan/items/b6b89f8c61c35b563e8c)

---
title: "goコマンド"
linkTitle: "go CLI"
description: https://golang.org/cmd/go/
date: 2020-06-08T23:36:27+09:00
weight: 20
---

## Overview

Examples:

```sh
# ビルド
go build

# パッケージ取得
go get

# モジュール管理
go mod

# 実行
go run

# テスト
go test

# 静的解析によって疑わしい問題を報告
go vet

# バージョン表示
go version

# ヘルプ
go help [command]
```

参考:

- [go vetの使い方(go vetとは) - Qiita](https://qiita.com/marnie_ms4/items/b343165efb4235906db7)

## 環境変数

 Variable | Values | Description
----------|--------|-------------
 GO111MODULE | **auto**, on, off | 「module-aware mode」が有効かどうか。デフォルトではgo.modの有無で判定される
 GOMOD | （右記） | go.modの絶対パス。go.modがなければos.DevNullの値。「module-aware mode」が無効なら、空文字列

## Module

https://golang.org/cmd/go/#hdr-Module_support

「module-aware mode」については、上記の環境変数およびgo.modファイルの有無で判定される。  
これにより、 `go get` などの挙動が変わる。

参考:

- [Go 1.13 に向けて知っておきたい Go Modules とそれを取り巻くエコシステム - blog.syfm](https://syfm.hatenablog.com/entry/2019/08/10/170730#f-b5157852)

## build

https://golang.org/cmd/go/#hdr-Compile_packages_and_dependencies

Examples:

```sh
go build
go build -o path/to/out
```

## get

Examples:

```sh
go get <package>

# ログメッセージを表示
go get -v <package>
```

2020-06-08現在、（Moduleが登場したGo 1.11以降で） `go get` には2つのモードがある:

- [Legacy GOPATH go get](https://golang.org/cmd/go/#hdr-Legacy_GOPATH_go_get)
- module-aware go get

後者についてはweb上ではヘルプを見つけられていないが、 `go help module-get` を実行するか、「module-aware mode」で `go help get` を実行すると、ヘルプが見られる。  
逆に、「module-aware mode」を無効にして `go help get` を実行するか、 `go help gopath-get` を実行すると、legacy GOPATH modeの `go get` のヘルプが見られる。

実行例:

```sh
$ go help gopath-get
The 'go get' command changes behavior depending on whether the
go command is running in module-aware mode or legacy GOPATH mode.
This help text, accessible as 'go help gopath-get' even in module-aware mode,
describes 'go get' as it operates in legacy GOPATH mode.

Usage: go get [-d] [-f] [-t] [-u] [-v] [-fix] [-insecure] [build flags] [packages]

Get downloads the packages named by the import paths, along with their
dependencies. It then installs the named packages, like 'go install'.
:
（以下略）

$ go help module-get
The 'go get' command changes behavior depending on whether the
go command is running in module-aware mode or legacy GOPATH mode.
This help text, accessible as 'go help module-get' even in legacy GOPATH mode,
describes 'go get' as it operates in module-aware mode.

Usage: go get [-d] [-t] [-u] [-v] [-insecure] [build flags] [packages]

Get resolves and adds dependencies to the current development module
and then builds and installs them.
:
（以下略）
```

### gopath-get

GOPATHの下にパッケージをダウンロードし、インストールする。  
パッケージのソースは `GOPATH/src/<import-path>` に展開される。

常に最新版が取得され、複数バージョンを混在させられないという問題があった。

### module-get

（go.modに記された）現在開発中のモジュールに対し依存モジュールを解決して、ビルドとインストールを行う。  

Spec:

- バージョン指定でインストールできる。例: `go get golang.org/x/text@v0.3.0`
- go.modがあるディレクトリで実行すると、 `go.mod`, `go.sum` が更新され、取得したモジュールが依存に追加される
- moduleは `GOPATH/pkg/mod` に取得され、バイナリは `GOPATH/bin` にインストールされる
- モジュールの外で `GO111MODULE=on` を指定して実行することもできる

取得パスについては `go help modules` に記載があった:

> In module-aware mode, GOPATH no longer defines the meaning of imports
during a build, but it still stores downloaded dependencies (in GOPATH/pkg/mod)
and installed commands (in GOPATH/bin, unless GOBIN is set).

とのこと。

## test

https://golang.org/cmd/go/#hdr-Test_packages

```sh
go test [build/test flags] [packages] [build/test flags & test binary flags]
```

関連項目:

- [Golang > テスト]({{<ref "test.md">}})

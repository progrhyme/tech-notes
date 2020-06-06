---
title: "Public Packages"
linkTitle: "pkg (3rd)"
date: 2020-05-31T21:16:45+09:00
weight: 1000
---

公式ではないが、公開されていて利用できるパッケージの情報を記す。

## まとめサイト

- https://awesome-go.com/

## go-git/go-git

- https://github.com/go-git/go-git
- https://pkg.go.dev/github.com/go-git/go-git/v5

pure GoによるGitライブラリ。  
[Gitの公式ページ](https://git-scm.com/book/en/v2/Appendix-B%3A-Embedding-Git-in-your-Applications-go-git)でも紹介されている。

インメモリで処理され、コマンドをフォークしないので、gitコマンドをラップして使うよりはいいかもしれない。
ただし、2020-06-02現在、gitコマンドの全てを網羅しているわけではない。

互換性については、 https://github.com/go-git/go-git/blob/master/COMPATIBILITY.md を見るべし。

参考:

- [golangのgit ライブラリ「go-git」を使ってインメモリでgit操作をする | Developers.IO](https://dev.classmethod.jp/articles/in-memory-git-commit-and-push/)

## jinzhu/configor

https://github.com/jinzhu/configor

YAML, JSON, TOML, 環境変数に対応した設定ツール。

Usage:

```go
package main

import (
	"fmt"
	"github.com/jinzhu/configor"
)

var Config = struct {
	APPName string `default:"app name"`

	DB struct {
		Name     string
		User     string `default:"root"`
		Password string `required:"true" env:"DBPassword"`
		Port     uint   `default:"3306"`
	}

	Contacts []struct {
		Name  string
		Email string `required:"true"`
	}
}{}

func main() {
	configor.Load(&Config, "config.yml")
	fmt.Printf("config: %#v", Config)
}
```

上のコード用のconfig.ymlの例:

```YAML
appname: test

db:
  name:     test
  user:     test
  password: test
  port:     1234

contacts:
- name: i test
  email: test@test.com
```

## spf13/pflag

- https://github.com/spf13/pflag
- https://pkg.go.dev/github.com/spf13/pflag

標準パッケージ [flag]({{<ref "std-pkg/flag.md">}}) の高機能版。  
GNUスタイルのロングオプションが作れる。

flagを拡張しているので、flagでできることは基本的にpflagでもできる。  
ので、flagについても併せて見ること。

Examples:

```go
import flag "github.com/spf13/pflag"

// Set as pointer
var ip *int
ip = flag.Int("flagname", 1234, "help message for flagname")

// Set as variable
var flagvar int
flag.IntVar(&flagvar, "flagname", 1234, "help message for flagname")

// Custom flags which satifsfy Value interface
flag.Var(&flagVal, "name", "help message for flagname")

// Parse arguments into flags
flag.Parse()

switch flag.NArg() {
case 0:
	// 引数なし
case 1:
	// 引数1個
default:
	// それ以上
}
```

参考:

- [How to set subcommand specific flags · Issue #195 · spf13/pflag](https://github.com/spf13/pflag/issues/195)
- [spf13/pflagの使い方](https://naoty.dev/posts/110.html)

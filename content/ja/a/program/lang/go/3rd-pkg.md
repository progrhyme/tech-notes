---
title: "Public Packages"
linkTitle: "pkg (3rd)"
date: 2020-05-31T21:16:45+09:00
weight: 1000
---

公式ではないが、公開されていて利用できるパッケージの情報を記す。

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

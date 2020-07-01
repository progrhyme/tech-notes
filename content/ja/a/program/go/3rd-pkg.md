---
title: "Public Packages"
linkTitle: "pkg (3rd)"
date: 2020-05-31T21:16:45+09:00
weight: 1000
---

公式ではないが、公開されていて利用できるパッケージの情報を記す。

## まとめサイト

- https://awesome-go.com/

## blang/semver

- https://github.com/blang/semver
- https://pkg.go.dev/github.com/blang/semver/v4

semVerを取り扱う人気のパッケージ。  
`X.Y.Z` 形式でないものを `semver.Make` に食わせるとエラーになって `0.0.0` になってしまう。

Example:

```go
raw := []string{"1.2.3", "1.0", "1.3", "2", "0.4.2"}
vs := make([]semver.Version, len(raw))
for i, r := range raw {
	v, err := semver.Make(r)
	if err != nil {
		fmt.Printf("Error parsing version: %s. %v\n", r, err)
	}

	vs[i] = v
}

semver.Sort(vs)
fmt.Printf("sorted: %v\n", vs)
/*
Error parsing version: 1.0. No Major.Minor.Patch elements found
Error parsing version: 1.3. No Major.Minor.Patch elements found
Error parsing version: 2. No Major.Minor.Patch elements found
sorted: [0.0.0 0.0.0 0.0.0 0.4.2 1.2.3]
*/
```

https://play.golang.org/p/OZVwXRRnl4s

## go-git/go-git

- https://github.com/go-git/go-git
- https://pkg.go.dev/github.com/go-git/go-git/v5

pure GoによるGitライブラリ。  
[Gitの公式ページ](https://git-scm.com/book/en/v2/Appendix-B%3A-Embedding-Git-in-your-Applications-go-git)でも紹介されている。

インメモリで処理され、コマンドをフォークしないので、gitコマンドをラップして使うよりはいいかもしれない。
ただし、2020-06-02現在、gitコマンドの全てを網羅しているわけではない。

互換性については、 https://github.com/go-git/go-git/blob/master/COMPATIBILITY.md を見るべし。

Tips:

- `Plain*` 関数を使うと、ふつうの `git` コマンドに近い使い方ができる（Not インメモリ処理）

参考:

- [golangのgit ライブラリ「go-git」を使ってインメモリでgit操作をする | Developers.IO](https://dev.classmethod.jp/articles/in-memory-git-commit-and-push/)

### func PlainClone

https://pkg.go.dev/github.com/go-git/go-git/v5@v5.1.0?tab=doc#PlainClone

```go
func PlainClone(path string, isBare bool, o *CloneOptions) (*Repository, error)
```

ふつうの `git clone` コマンドのように使える関数。

Examples:

```go
_, err := git.PlainClone(path, false, &git.CloneOptions{
	URL: "https://github.com/git-fixtures/basic.git",
})
if err != nil {
	log.Fatal(err)
}
```

### func PlainOpen

https://pkg.go.dev/github.com/go-git/go-git/v5@v5.1.0?tab=doc#PlainOpen

```go
func PlainOpen(path string) (*Repository, error)
```

Examples:

```go
// path上のリポジトリを開いてgit pull相当の操作を実行
repo, err := git.PlainOpen(path)
wtree, err := repo.Worktree()
err = wtree.Pull(&git.PullOptions{})
```

### type Repository

https://pkg.go.dev/github.com/go-git/go-git/v5@v5.1.0?tab=doc#Repository

リポジトリを表現する型。

#### func Worktree

https://pkg.go.dev/github.com/go-git/go-git/v5@v5.1.0?tab=doc#Repository.Worktree

```go
func (r *Repository) Worktree() (*Worktree, error)
```

ワーキングツリーを取得する関数。

### type Worktree

https://pkg.go.dev/github.com/go-git/go-git/v5@v5.1.0?tab=doc#Worktree

gitのワーキングツリーを表す型。

#### func Pull

https://pkg.go.dev/github.com/go-git/go-git/v5@v5.1.0?tab=doc#Worktree.Pull

```go
func (w *Worktree) Pull(o *PullOptions) error
```

ワーキングツリー上で `git pull` 相当の操作を実行。  
変更がなければ `NoErrAlreadyUpToDate` を返す。

## goccy/go-yaml

https://github.com/goccy/go-yaml

Yet AnotherなYAMLライブラリ。

参考:

- 作者のエントリ: [GoでYAMLを扱うすべての人を幸せにするべく、ライブラリをスクラッチから書いた話 - Qiita](https://qiita.com/goccy/items/86abe72b472993b5516a)

## go-yaml/yaml

https://pkg.go.dev/gopkg.in/yaml.v2

GoにおけるYAMLライブラリのデファクト。

参考:

- [Go言語(golang) YAMLの使い方 - golangの日記](https://golang.hateblo.jp/entry/2018/11/08/183555)

### ファイルから読み込む

Example:

```go
f, err := os.Open("hello.yml")
if err != nil {
	log.Fatal(err)
}
defer f.Close()

d := yaml.NewDecoder(f)

var m map[string]interface{}

if err := d.Decode(&m); err != nil {
	log.Fatal(err)
}

fmt.Printf("%v\n", m) // map[name:Tanaka age:30]
```

### func NewDecoder

https://pkg.go.dev/gopkg.in/yaml.v2?tab=doc#NewDecoder

```go
func NewDecoder(r io.Reader) *Decoder
```

### func Unmarshal

https://pkg.go.dev/gopkg.in/yaml.v2?tab=doc#Unmarshal

```go
func Unmarshal(in []byte, out interface{}) (err error)
```

YAMLをデコードしてstructかmapに読み込む。

Examples:

```go
// structに読み込む
type T struct {
    F int `yaml:"a,omitempty"`
    B int
}
var t T
yaml.Unmarshal([]byte("a: 1\nb: 2"), &t)

// mapに読み込む
var m map[string]interface{}
data := `
name: Tanaka
age: 30
`

yaml.Unmarshal([]byte(data), &m)
fmt.Printf("%v\n", m) //=> map[name:Tanaka age:30]
```

参考:

- [go で yaml 等を「map\[interface{}\]interface{}」型で読み込んだ際の動的型の参照方法 - Qiita](https://qiita.com/yamasaki-masahide/items/d6e406c4c11d5870a1c6)
- https://github.com/progrhyme/tutorials/blob/master/golang/yaml/decode.go

### type Decoder

https://pkg.go.dev/gopkg.in/yaml.v2?tab=doc#Decoder

#### func Decode

```go
func (dec *Decoder) Decode(v interface{}) (err error)
```

## h2non/filetype

- https://github.com/h2non/filetype
- https://pkg.go.dev/github.com/h2non/filetype

Goでバイナリファイルの種類を識別するためのライブラリ。  
アドホックに独自フォーマットを追加することも可能。

対応フォーマット例:

- 画像: jpg, png, gif, bmp, webp
- 動画
- 音声
- 圧縮ファイル: zip, gz, tar, elf
- 文書: doc, docx, xls, xlsx, ppt, pptx
- フォント
- アプリケーション: wasm

## hashicorp/go-version

- https://github.com/hashicorp/go-version
- https://pkg.go.dev/github.com/hashicorp/go-version

SemVer以外も想定するならこちらを使うのがよさそう。

Example:

```go
raw := []string{"1.1", "0.7.1", "1.4-beta", "1.4", "2"}
vs := make([]*version.Version, len(raw))
for i, r := range raw {
	v, err := version.NewVersion(r)
	if err != nil {
		fmt.Printf("Error parsing version: %s. %v\n", r, err)
	}

	vs[i] = v
}

sort.Sort(version.Collection(vs))
fmt.Printf("sorted: %v\n", vs)
//=> sorted: [0.7.1 1.1.0 1.4.0-beta 1.4.0 2.0.0]
```

https://play.golang.org/p/B_OBt8NeImn

Tips:

- `Version#.Original` で元のバージョンを取り出せるようだ

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

## Masterminds/semver

- https://pkg.go.dev/github.com/Masterminds/semver/v3

blang/semverと違い、1桁や2桁のバージョンも解釈できる。  
hashicorp/go-versionとほぼ一緒で、インタフェースもよく似ている。

Example:

```go
raw := []string{"1.2.3", "1.0", "1.3", "2", "0.4.2",}
vs := make([]*semver.Version, len(raw))
for i, r := range raw {
	v, err := semver.NewVersion(r)
	if err != nil {
		t.Errorf("Error parsing version: %s", err)
	}

	vs[i] = v
}

sort.Sort(semver.Collection(vs))
//=> sorted: [0.4.2 1.0.0 1.2.3 1.3.0 2.0.0]
```

https://play.golang.org/p/y6ABmgtJ9Yf

Tips:

- `Version#.Original` で元のバージョンを取り出せるようだ

## mholt/archiver

- https://github.com/mholt/archiver
- https://pkg.go.dev/github.com/mholt/archiver/v3

各種圧縮形式に対応した人気のパッケージで、CLIとしても、ライブラリとしても利用できる。  
各種形式に対応するためかそれなりに依存が多いが、自前で各種形式に対応したくないときは便利に使えそう。

Examples:

```go
// 圧縮形式は拡張子から判別される
err := Unarchive("blog_site.zip", "extracted/mysite")
if err != nil {
	log.Fatal(err)
}
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

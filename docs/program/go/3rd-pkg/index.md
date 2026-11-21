---
date: '2020-05-31T21:16:45+09:00'
---

# Public Packages

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

## google/go-cmp/cmp

https://pkg.go.dev/github.com/google/go-cmp/cmp

主にテストで使える値の比較のためのライブラリ。

Example:

```go
got, want := MakeGatewayInfo()

if diff := cmp.Diff(want, got); diff != "" {
	t.Errorf("MakeGatewayInfo() mismatch (-want +got):\n%s", diff)
}
```

メモ:

- cmp.Diff は文字列でも構造体でもhuman readableな感じで差分が見れて便利

参考:

- [構造体などをテストするのに便利なgoogle/go-cmpの使い方 - Qiita](https://qiita.com/hgsgtk/items/bd78bada902c91745fa5)

## google/go-github

- https://github.com/google/go-github
- https://pkg.go.dev/github.com/google/go-github/v32/github

GitHub APIクライアントライブラリ。

Examples:

```go
client := github.NewClient(nil)

// list all organizations for user "willnorris"
orgs, _, err := client.Organizations.List(ctx, "willnorris", nil)
```

### アクセストークンによる認証

golang.org/x/oauth2を使うのが簡単。

```go
import "golang.org/x/oauth2"

ctx := context.Background()
ts := oauth2.StaticTokenSource(
	&oauth2.Token{AccessToken: "... your access token ..."},
)
tc := oauth2.NewClient(ctx, ts)

client := github.NewClient(tc)

// list all repositories for the authenticated user
repos, _, err := client.Repositories.List(ctx, "", nil)
```

### type RepositoriesService

https://pkg.go.dev/github.com/google/go-github/v32/github?tab=doc#RepositoriesService

#### func GetLatestRelease

https://pkg.go.dev/github.com/google/go-github/v32/github?tab=doc#RepositoriesService.GetLatestRelease

```go
func (s *RepositoriesService) GetLatestRelease(ctx context.Context, owner, repo string) (*RepositoryRelease, *Response, error)
```

GitHub上の最新リリースを取得。

Example:

```go
release, res, err := client.Repositories.GetLatestRelease(ctx, owner, repo)
```

APIリファレンス: https://developer.github.com/v3/repos/releases/#get-the-latest-release

## gookit/color

- https://github.com/gookit/color
- https://pkg.go.dev/github.com/gookit/color

Examples:

```go
color.Red.Println("Simple to use color")
color.Green.Print("Simple to use color")
color.Cyan.Printf("Simple to use %s\n", "color")

color.Danger.Println("DANGER")   // 赤太字
color.Success.Println("SUCCESS") // 緑太字
```

Hint:

- 色が表示されないなと思ったら、IsSupport256ColorやIsSupportColor関数で端末が対応しているか確認する。どちらかは必要そう
- ~~IsTerminal関数で、依存なしでTTY判定ができそう~~ <- 2020-07-03現在、Windowsしか実装されてなかった

参考:

- [コンソールの色付けにはgookit/colorが便利 - Qiita](https://qiita.com/shibukawa/items/3f8974bd074b20ed2b95)

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

## pmezard/go-difflib

- https://github.com/pmezard/go-difflib
- https://pkg.go.dev/github.com/pmezard/go-difflib/difflib

unified diffが取れる使いやすいライブラリ。  
Pythonのdifflibのポートだそうだ。

※2018年で更新が止まっており、メンテされていない。

Example:

```go
diff := difflib.UnifiedDiff{
    A:        difflib.SplitLines("foo\nbar\n"),
    B:        difflib.SplitLines("foo\nbaz\n"),
    FromFile: "Original",
    ToFile:   "Current",
    Context:  3,
}
text, _ := difflib.GetUnifiedDiffString(diff)
fmt.Printf(text)
```

出力:

```diff
--- Original
+++ Current
@@ -1,3 +1,3 @@
 foo
-bar
+baz
```

## sergi/go-diff/diffmatchpatch

- https://github.com/sergi/go-diff
- https://pkg.go.dev/github.com/sergi/go-diff/diffmatchpatch

使い方が難しいライブラリ。  
DiffPrettyText関数で色付きdiffは出せるのだけど、unified形式のdiffの出し方がわからん。

参考:

- [GolangのdiffMatchPatchライブラリで行単位diffをする - Qiita](https://qiita.com/shibukawa/items/dd75ad01e623c4c1166b)
- [春の入門祭り🌸 #8 人生を豊かにする文字列diff入門 | フューチャー技術ブログ](https://future-architect.github.io/articles/20200610/)
    - https://github.com/shibukawa/cdiff ... 上の記事で紹介されている

## spf13/pflag

- https://github.com/spf13/pflag
- https://pkg.go.dev/github.com/spf13/pflag

標準パッケージ [flag](../std-pkg/flag.md) の高機能版。  
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

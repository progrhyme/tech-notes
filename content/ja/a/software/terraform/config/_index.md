---
title: "Configuration"
linkTitle: "Configuration"
date: 2020-04-26T23:06:12+09:00
weight: 100
---

設定ファイルの記法等。

v0.12以降に対応。  
v0.11以前は子ページを見よ。

## 基本文法

- https://www.terraform.io/docs/configuration/syntax.html

### 文字列

- `$` をそのまま文字列内で扱いたいときは `"$$"` とエスケープする。

## 変数管理
### Variables

https://www.terraform.io/docs/configuration/variables.html

terraformで使用する変数は `.tf` ファイル内に `variable` ブロックで定義する。  
定義ブロック内で `default` 値を設定することもできるが、以下のいくつかの方法で値を注入できる。

- `.tfvars` ファイルに HCL or JSON で記述し、terraform実行時に `-var-file <FILE>` という引数で渡す
  - カレントディレクトリ直下の `terraform.tfvars` ファイルまたはsuffixが `.auto.tfvars` のファイルは自動的に読み込まれる。
- terraform実行時に `-var 'key=value'` という引数で渡す
- 環境変数 `TF_VAR_keyname` を設定すると `keyname` 変数がセットされる

参考:

- [Terraform で変数を使う - Qiita](https://qiita.com/ringo/items/3af1735cd833fb80da75 "Terraform で変数を使う - Qiita")

### Local Values

https://www.terraform.io/docs/configuration/locals.html

module内などのスコープで使える変数を定義する。  
variableで定義した変数を参照したり、演算結果を使ったり出来るので便利。

参考:

- [【モダンTerraform】VariableとLocal Valuesの使い分けについて \- febc技術メモ](http://febc-yamamoto.hatenablog.jp/entry/2018/01/30/185416)

## Types (v0.12〜)

https://www.terraform.io/docs/configuration/types.html

### Primitive Types

- `string`
- `number`
- `bool`

NOTE:

- `string` <=> [`number`, `bool`] の型変換が必要に応じて自動的に行われる
  - 例:
    - `true` <=> `"true"`
    - `false` <=> `"false"`

### Complex Types

Collection Types:

- `list(...)`
  - 例: `list(string)`
- `map(...)`
  - 各要素のラベル（キー）はstring型
  - 例: `map(string)` だったら、各要素の値がstring型ということ
- `set(...)`

Structural Types:

- `ojbect(...)`
  - 例: `object({ name=string, age=number })`
- `tuple(...)`
  - 例: `tuple([string, number, bool])`

## Expressions (v0.12〜)

https://www.terraform.io/docs/configuration/expressions.html

### Splat

https://www.terraform.io/docs/configuration/expressions.html#splat-expressions

`[*]` によるリストの展開

Examples

```HCL
# 1
var.list[*].id

## for式による↑と等価な構文
[for o in var.list : o.id]

# 2
var.list[*].interfaces[0].name

## for式による↑と等価な構文
[for o in var.list : o.interfaces[0].name]
```

### Dynamic blocks

https://www.terraform.io/docs/configuration/expressions.html#dynamic-blocks

resource内のブロックの繰り返し記述をDRYに書けるようになった。

Example:

```HCL
resource "aws_elastic_beanstalk_environment" "tfenvtest" {
  name                = "tf-test-name"
  application         = "${aws_elastic_beanstalk_application.tftest.name}"
  solution_stack_name = "64bit Amazon Linux 2018.03 v2.11.4 running Go 1.12.6"

  dynamic "setting" {
    for_each = var.settings
    content {
      namespace = setting.value["namespace"]
      name = setting.value["name"]
      value = setting.value["value"]
    }
  }
}
```

※あまり使いすぎない方がいいと書いてある。

## Functions (v0.12〜)
https://www.terraform.io/docs/configuration/functions.html

v0.11以前は `Interpolation Syntax` だったもの。

### Collection
#### concat
https://www.terraform.io/docs/configuration/functions/concat.html

listの結合

Examples:

```HCL
> concat(["a", ""], ["b", "c"])
[
  "a",
  "",
  "b",
  "c",
]
```

### Encoding
#### jsondecode
https://www.terraform.io/docs/configuration/functions/jsondecode.html

JSONをデコードしてobject(map), tuple(list), stringなどを作る。  
逆の操作をする関数は `jsonencode`

Examples:

```HCL
> jsondecode("{\"hello\": \"world\"}")
{
  "hello" = "world"
}
> jsondecode("true")
true
```

### String
#### format

https://www.terraform.io/docs/configuration/functions/format.html

printfのような書式指定出力機能を提供する。

構文:

```HCL
format(spec, values...)
```

Examples:

```HCL
> format("Hello, %s!", "Ander")
Hello, Ander!
> format("There are %d lights", 4)
There are 4 lights
```

## メタパラメータ

https://www.terraform.io/docs/configuration/resources.html#meta-parameters

全てのresourceで使えるパラメータ。

- count (int) ... リソースを作成する件数。
- depends_on (list of strings) ... リソースやmoduleの依存関係を指定する。
- lifecycle (block)

### for_each (v0.12.6〜)

`count` のように複数のリソースを定義できる。

参考:

- [Terraformのfor_eachで配列を渡したときのインデックス取得 - Qiita](https://qiita.com/KAndy/items/611d6d6ab9ca0f3047b8)

### lifecycle

このブロックは以下のキーを取る:

- `create_before_destroy` (bool) ... リソースを作り直すときに、元のを削除する前に
新しいリソースを作っておく。
- `prevent_destroy` (bool) ... リソースの削除を防ぐ
- `ignore_changes` (list of strings) ... リソースの特定のパラメータの変化を無視する
  - 例えば、AWS AutoScalinGroupで下のように設定しておくと、スケールアウトしたときにterraformを適用してもインスタンス数をリセットして事故になることを防ぐことができる。

```hcl
resource "aws_autoscaling_group" "my_cluster" {
  min_size = 1
  max_size = 10
  desired_capacity = 1

  lifecycle {
    ignore_changes = ["desired_capacity"]
  }
}
```

参考:

- [Terraform職人入門: 日々の運用で学んだ知見を淡々とまとめる - Qiita#リソースの差分を無視する](https://qiita.com/minamijoyo/items/1f57c62bed781ab8f4d7#%E3%83%AA%E3%82%BD%E3%83%BC%E3%82%B9%E3%81%AE%E5%B7%AE%E5%88%86%E3%82%92%E7%84%A1%E8%A6%96%E3%81%99%E3%82%8B "Terraform職人入門: 日々の運用で学んだ知見を淡々とまとめる - Qiita")


## Workspaces

https://www.terraform.io/docs/state/workspaces.html

`.tf` ファイル内で `${terraform.workspace}` でworkspace名を参照できる。

Example:

```HCL
resource "aws_instance" "example" {
  count = "${terraform.workspace == "default" ? 5 : 1}"

  # ... other arguments
}
```

参考:
- [はじめてのTerraform 0.12 ～実践編～ | Future Tech Blog - フューチャーアーキテクト](https://future-architect.github.io/articles/20190819/)


## Terraform

https://www.terraform.io/docs/configuration/terraform.html

Terraformの設定。

Example:

```HCL
terraform {
  backend "s3" {
    :
  }

  required_version >= "0.12.0"
}
```

## Backends

https://www.terraform.io/docs/backends/

- [S3](https://www.terraform.io/docs/backends/types/s3.html)
- [GCS](https://www.terraform.io/docs/backends/types/gcs.html)


### Partial Configuration

https://www.terraform.io/docs/backends/config.html#partial-configuration

一部の設定を `.tf` ファイルではなくコマンドラインや外部ファイルで渡す方式。

## Module

レシピを module という単位にまとめて再利用性を高めることができる。

- https://www.terraform.io/docs/modules/usage.html
- https://www.terraform.io/docs/configuration/modules.html

Tips:

- module内では `${module.path}` によってmoduleのルートパスを取得できる
  - 相対パス `.` などでは上手く行かないケースがありそう

参考:

- [terraform module内でtemplatefile関数を実行した際に、ファイルが見つけられなくて困った - Qiita](https://qiita.com/mh4gf/items/0590038ed41a698b7623)


## Data Source

データを既存インフラや他のTerraform被管理物から取ってくる。

- https://www.terraform.io/docs/configuration/data-sources.html

## Output

moduleの属性値を他のmoduleで利用できるようにしたり、remote stateとして他の環境から参照可能にしたりする。

https://www.terraform.io/docs/configuration/outputs.html

## How-to
### resourceを二重ループで作成する

for構文はネストできるので、for構文で所望のパラメータを持ったリストを生成し、それを `for_each` や `count` で使う。

Example:

```HCL
locals {
  params = flatten([
    for project in var.project_ids :
    [ for key in var.keys : join(",", [project, key]) ]
  ])
}

resource "foo_resource" "my_foo" {
  for_each = toset(local.params)
  project  = split(",", each.value)[0]
  key      = split(",", each.value)[1]
}
```

NGなやり方（v0.13以前）:

- `for_each` や `count` 単体ではできない
- moduleの中で `for_each` や `count` を使い、moduleを `for_each` や `count` で定義する <- サポートされていない

参考:

- [Terraformのmoduleでcount/for_eachが使えない問題 • masu-mi's blog(Dirty Cache)](https://blog.masu-mi.me/post/2020/04/22/terraform-module-count-for_each/)

## Topics
### count VS for_each

Terraform v0.12から `for_each` によって複数のresourceの定義が可能になった。  
従来の `count` と違い、個々のresourceのtfstate内の識別子は連番の番号ではなく、文字列のキーがつくので、要素の追加や削除があっても複数のresourceがまとめて作り直される、ということがない。

よって、 `for_each` が使えるならば、 `for_each` を使ったほうがいい。

参考:

- [Terraformで配列をloopする時はfor_eachを使った方がいい - cloudfishのブログ](https://cloudfish.hatenablog.com/entry/2020/02/19/183548)

## Child Pages

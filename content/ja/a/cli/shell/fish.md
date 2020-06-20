---
title: "fish shell"
linkTitle: "fish"
description: https://fishshell.com/
date: 2020-06-20T16:39:53+09:00
weight: 200
---

## About

> **Finally, a command line shell for the 90s**  
> fish is a smart and user-friendly command line shell for Linux, macOS, and the rest of the family.

使いやすいシェルとして人気のもの。

- C++ 実装
- POSIX **非互換**
- プラグイン機能がある

参考:

- [fish-shell でシェルの海をスイスイ泳いでみた | 株式会社ヌーラボ(Nulab inc.)](https://nulab.com/ja/blog/backlog/fish-shell-tutorial/)
- [fish shellが結構良かった話 - Qiita](https://qiita.com/hennin/items/33758226a0de8c963ddf)
- [シェル芸人のためのfish入門 - Qiita](https://qiita.com/kuwa72/items/f3a90fcd215938f5817e) ... Bashとの違いがわかりやすかった

## Getting Started

Install:

- https://fishshell.com/ の「Go fish」から

Documentation:

- https://fishshell.com/docs/current/
  - [Tutorial — fish-shell 3.1.2 documentation](https://fishshell.com/docs/current/tutorial.html)

有志和訳:

- https://natsukium.github.io/fish-docs-jp/

## Spec

- 配列のインデックスは1から始まる

### 変数のスコープ

https://fishshell.com/docs/current/#variable-scope

3種類のスコープ:

- **Universal** ... 該当ユーザの全fishセッションで共有される
- **Global** ... 現在のfishセッションに閉じるが、他のブロックスコープに結びつかず、 `set -e` で明示的に消されない限り消えない
- **Local** ... 特定のブロックに関連付けられ、ブロックを抜けると消える。ブロックは `for`, `while`, `if`, `function`, `begin` や `switch` で作られ、 `end` で閉じる

Examples:

```sh
# Universal. -U, --universal で定義
set -U fish_user_paths . $fish_user_paths

# Global. -g, --global で定義
set -g PATH $HOME/bin $PATH

begin
  # Local. -l, --local で定義
  set -l pirate 'There be treasure in them thar hills'
end

echo $pirate # pirateはlocalなので何も出力されない
```

## Commands

https://fishshell.com/docs/current/commands.html

### contains

https://fishshell.com/docs/current/cmds/contains.html

```sh
contains [OPTIONS] KEY [VALUES...]
```

ワードがリストに含まれるか調べる。  
オプション `-i, --index` を付けると、ワードのインデックス値を返す。

Example:

```sh
# PATHにまだ含まれていなければ追加
if not contains $HOME/bin $PATH
  set PATH $HOME/bin $PATH
end
```

### eval

https://fishshell.com/docs/current/cmds/eval.html

```sh
eval [COMMANDS...]
```

テキストをコマンドとして評価する。  
コマンドが標準入力を使わないのなら `source` を使ったほうがいいかも。

Example:

```sh
set cmd ls \| cut -c 1-12
eval $cmd
```

### function

https://fishshell.com/docs/current/cmds/function.html

```sh
function NAME [OPTIONS]; BODY; end
```

関数を作る。

Example:

```sh
function ll
    ls -l $argv
end
```

Spec:

- 引数は `$argv` でリストとして渡される

### functions

https://fishshell.com/docs/current/cmds/functions.html

```sh
functions [ -a | --all ] [ -n | --names ]
functions [ -D | --details ] [ -v ] FUNCTION
functions -c OLDNAME NEWNAME
functions -d DESCRIPTION FUNCTION
functions [ -e | -q ] FUNCTIONS...
```

関数を表示したり消したりする。

 Option | 機能
--------|------
`-a, -all` | `_` で始まるものも全て表示
 `-e, --erase FUNCTIONS...` | 関数を消す

Examples:

```sh
functions -n
# Displays a list of currently-defined functions

functions -c foo bar
# Copies the 'foo' function to a new function called 'bar'

functions -e bar
# Erases the function ``bar``
```

### if

https://fishshell.com/docs/current/cmds/if.html

```sh
if CONDITION; COMMANDS_TRUE...;
[else if CONDITION2; COMMANDS_TRUE2...;]
[else; COMMANDS_FALSE...;]
end
```

条件分岐構文として使える。

Example:

```sh
if test -f foo.txt
    echo foo.txt exists
else if test -f bar.txt
    echo bar.txt exists
else
    echo foo.txt and bar.txt do not exist
end
```

### set

https://fishshell.com/docs/current/cmds/set.html

```sh
set [SCOPE_OPTIONS]
set [OPTIONS] VARIABLE_NAME VALUES...
set [OPTIONS] VARIABLE_NAME[INDICES]... VALUES...
set ( -q | --query ) [SCOPE_OPTIONS] VARIABLE_NAMES...
set ( -e | --erase ) [SCOPE_OPTIONS] VARIABLE_NAME
set ( -e | --erase ) [SCOPE_OPTIONS] VARIABLE_NAME[INDICES]...
set ( -S | --show ) [VARIABLE_NAME]...
```

シェル変数の表示や操作を行う。

関連項目:

- [変数のスコープ](#変数のスコープ)

 Option | 機能
--------|------
 `-e, --erase NAME` | 変数を削除する
 `-x, --export NAME VALUES...` | 変数をエクスポートし、環境変数にする
 `-u, --unexport NAME VALUES...` | 変数をアンエクスポートし、環境変数ではなくする

Examples:

```sh
# Prints all global, exported variables.
set -xg

# Sets the value of the variable $foo to be 'hi'.
set foo hi

# $fooを配列と見なして"there"をappendする
set -a foo there

# Does the same thing as the previous two commands the way it would be done pre-fish 3.0.
set foo hi
set foo $foo there

# 先頭に要素を追加
set foo "Hello, " $foo

# Removes the variable $smurf
set -e smurf

# Changes the fourth element of the $PATH list to ~/bin
set PATH[4] ~/bin

# PATH変数の3つ目を削除
set -e PATH[3]
```

### source

https://fishshell.com/docs/current/cmds/source.html

```sh
# 1
source FILENAME [ARGUMENTS...]

# 2
somecommand | source
```

ファイルや標準入力から受け取ったコマンド群を現在のシェルのコンテキストで評価・実行する。

### test

https://fishshell.com/docs/current/cmds/test.html

```sh
# 1
test [EXPRESSION]

# 2
[ [EXPRESSION] ]
```

[POSIX shellのtest]({{<ref "posix/_index.md">}}#test)ユーティリティのように機能する。  
互換性のために2番めの構文も利用可能だが、fishでは `test ...` 形式が好まれるとのこと。

Examples:

```sh
if test -d /tmp
    cp /etc/motd /tmp/motd
end

if test -n "$MANPATH"
    echo $MANPATH
end

if ! test -r secret.txt
    echo "Can't read secret.txt" >&2
end

if test \( -f /foo -o -f /bar \) -a \( -f /baz -o -f /bat \)
    echo Success
end

if test $status -ne 0
    echo "Previous command failed"
end
```

## パッケージ管理

関連項目:

- [シェル > パッケージ管理]({{<ref "/a/cli/shell/pkg-man.md">}})

### fisher

https://github.com/jorgebucaran/fisher

人気のパッケージ管理ツール。

Examples:

```sh
# oh-my-fishのテーマをfisherでインストール
fisher add oh-my-fish/theme-<テーマ名>
```

参考:

- [初心者がShellを知りFish〜Fisherを導入するまで - Qiita](https://qiita.com/nutsinshell/items/5f111184b50f7081c92f)
- [fisher v3 で変わったこと | Hi120kiのメモ](https://hi120ki.github.io/blog/posts/20190123/)

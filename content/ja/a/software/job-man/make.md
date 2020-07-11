---
title: "GNU make"
linkTitle: "GNU make"
description: >
  [GNU make](https://www.gnu.org/software/make/manual/make.html)
date: 2020-05-04T19:50:02+09:00
weight: 260
---

## Getting Started

公式リファレンスは↑

サードパーティーのリファレンス的資料:

- [GNU make 日本語訳(Coop編) - 目次](http://www.ecoop.net/coop/translated/GNUMake3.77/make_toc.jp.html) ... 1998年ぐらい。古い
- [Makefileの関数 - Qiita](http://qiita.com/chibi929/items/b8c5f36434d5d3fbfa4a)

## Quickstart

使えるMakefileの例

```Makefile
.PHONY: default build clean

default: build

clean:
  rm -rf dist/

timestamp:
  date +%s > timestamp

build: timestamp another-file
  some_build_command
```

Tips:

- ターゲットの依存ターゲットは複数記すことができる。

参考:

- [- 自動化のためのGNU Make入門講座 - Makefileの基本：ルール](http://objectclub.jp/community/memorial/homepage3.nifty.com/masarl/article/gnu-make/rule.html)


## Makefile 構文
### 変数

変数定義のやり方について。

"=" と ":=" は違う。

```Makefile
src = foo.c
ymd := $(shell date +%Y%m%d)
```

参考:

- [GNU make: 6. 変数の使用法](http://quruli.ivory.ne.jp/document/make_3.79.1/make-jp_5.html "GNU make: 6. 変数の使用法")

#### $(CURDIR)

makeを実行しているプロセスのカレントディレクトリを返す。

参考:

- https://www.gnu.org/software/make/manual/html_node/Recursion.html
- [今日のMake Tips：CURDIR変数 - 檜山正幸のキマイラ飼育記](http://d.hatena.ne.jp/m-hiyama/20080805/1217915354 "今日のMake Tips：CURDIR変数 - 檜山正幸のキマイラ飼育記")

### 関数
#### $(foreach name, LIST, command)

ループ実行

### .PHONYターゲット

https://www.gnu.org/software/make/manual/html_node/Phony-Targets.html

ファイルを生成しないやつ

```Makefile
.PHONY: clean

clean:
    rm *.o tmp
```

複数の.PHONYターゲットをまとめて記述することもできる

```Makefile
.PHONY: all clean deps
```

### 条件分岐

[7 Conditional Parts of Makefiles](https://www.gnu.org/software/make/manual/make.html#Conditionals)

Example:

```Makefile
libs_for_gcc = -lgnu
normal_libs =

foo: $(objects)
ifeq ($(CC),gcc)
        $(CC) -o foo $(objects) $(libs_for_gcc)
else
        $(CC) -o foo $(objects) $(normal_libs)
endif
```

### `$` のエスケープ

シェルの文脈で `$` を使いたいときは `$$` と記すことで実現できる。

Examples:

```Makefile
time:
	now=$$(date); echo $$now
```

参考:

- [GNU make - SanRin舎](https://tmsanrinsha.net/post/2018/01/gnu-make/)

## makeコマンド

公式マニュアル:

- [9 How to Run make](https://www.gnu.org/software/make/manual/make.html#Running)
  - [9.5 Overriding Variables](https://www.gnu.org/software/make/manual/make.html#Overriding)
  - [9.7 Summary of Options](https://www.gnu.org/software/make/manual/make.html#Options-Summary)

SYNOPSIS:

```sh
# デフォルトのタスク（＝最上部で定義されたタスク）を実行
make

# タスク名を指定して実行。複数指定可
make task1 [task2 ...]

# Makefileを指定する
make -f|--file <Makefile>

# dry-run
make -n|--dry-run

# 変数の設定
#  Makefile内で定義されていれば、オーバーライドする
make CFLAGS=-g
```

その他のオプション:

 オプション | 意味
------------|------
 `-j|--jobs[=N]` | 同時実行数を指定。See [5.4 Parallel Execution](https://www.gnu.org/software/make/manual/make.html#Parallel)
 `-e|--environment-overrides` | 環境変数をオーバーライドする
 `-d` | デバッグ情報を表示。 `--debug=a` と同じ
 `--trace` | 実行時のトレース情報を表示する
 `-s|--silent|--quiet` | 実行されるタスクをプリントしない
 `-h|--help` | ヘルプ表示
 `-v|--version` | バージョン表示

## Tips
### 必要なディレクトリを作ってタスク実行

```Makefile
BUILD_DIR := path/to/build

$(BUILD_DIR):
    mkdir -p $(BUILD_DIR)

all: $(BUILD_DIR)
    cd $(BUILD_DIR) && some_commands

.PHONY: all
```

### 環境変数の取扱い

環境変数はMakeの変数として参照できる。例: `$(CFLAGS)`

参考:

- [GNU Make のふたつの変数の使い分け - Qiita](https://qiita.com/kojiohta/items/54b1a9f7d482c35dc4fa)
- [GNU make 日本語訳(Coop編) - 変数の利用法](https://www.ecoop.net/coop/translated/GNUMake3.77/make_6.jp.html)

## How-to
### コマンドに引数を渡したい

`make CFAGS=-g` みたいに変数経由で渡すことになりそう。

参考:

- [Makefileにパラメータを渡す方法と条件文 - Qiita](https://qiita.com/liubin/items/69d9faf804e82ddec376)

## Cookbooks
### カレントディレクトリを表示する幾つかの方法

```Makefile
pwd:
    pwd
    echo $(shell pwd)
    echo $(PWD)
    echo $$PWD
    echo $(CURDIR)
```

実行例:

```sh
$ make
pwd
/home/progrhyme/tmp/make
echo /home/progrhyme/tmp/make
/home/progrhyme/tmp/make
echo /home/progrhyme/tmp/make
/home/progrhyme/tmp/make
echo $PWD
/home/progrhyme/tmp/make
echo /home/progrhyme/tmp/make
/home/progrhyme/tmp/make
```

## 参考

- [Makefileで遊ぼう 〜 階乗, フィボナッチ数, Brainfuck処理系まで - プログラムモグモグ](http://itchyny.hatenablog.com/entry/20120213/1329135107)
  - 入門レベルで割とよく使う感じの機能がまとまってる。

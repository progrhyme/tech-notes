---
title: "ファイル操作"
linkTitle: "ファイル操作"
date: 2020-07-03T16:21:09+09:00
weight: 2500
---

## find

Man Page:

- Linux: https://linux.die.net/man/1/find
- macOS: https://www.unix.com/man-page/osx/1/find/

ファイルやディレクトリを検索する。  
`-exec` オプションで見つけたファイルに対してコマンド実行することもできる。

※LinuxとmacOSでオプションが異なる

Examples:

```sh
# path以下のファイル、ディレクトリを全てリストアップ
find <path>
# ファイルのみリストアップ
find <path> -type f
# 拡張子指定で検索
find <path> -name "*.txt"

# 3日以内に更新されたファイルを探す
find <path> -mtime -mtime -3

# 3日以上前のファイルを探して全て削除
find <path> -type f -mtime +3 -exec rm -f {} \;
```

時間指定オプション:

 オプション | 意味
------------|------
 -mmin | ファイルのデータが最後に修正された日時（分指定）
 -mtime | ファイルのデータが最後に修正された日時（日指定）
 -amin | ファイルのデータに最後にアクセスされた日時（分指定）
 -atime | ファイルのデータに最後にアクセスされた日時（日指定）
 -cmin | ファイルのデータとステータスが最後に修正された日時（分指定）
 -ctime | ファイルのデータとステータスが最後に修正された日時（日指定）

参考:

- [find で日数が過ぎたファイルを検索・削除する | キュア子の開発ブログ](https://curecode.jp/tech/find-mtime-delete/)
- [findコマンドのmtimeオプションまとめ - Qiita](https://qiita.com/narumi_/items/9ea27362a1eb502e2dbc)

## mktemp

[Man page of MKTEMP](https://linuxjm.osdn.jp/html/GNU_coreutils/man1/mktemp.1.html)

一時ファイル、またはディレクトリを作成する。

```sh
mktemp
# ディレクトリを作成
mktemp -d
```

参考:

- [mktemp Man Page - macOS - SS64.com](https://ss64.com/osx/mktemp.html)

## readlink(1)

[Man page of READLINK](https://linuxjm.osdn.jp/html/GNU_coreutils/man1/readlink.1.html)

Examples:

```sh
# シンボリックリンクのリンク先を返す。再帰的に探索はしない
readlink <link>

# realpathと同じ働きをする
readlink -f <file>
```

## realpath(1)

[Man page of REALPATH](https://linuxjm.osdn.jp/html/GNU_coreutils/man1/realpath.1.html)

引数として与えられたファイル or ディレクトリの絶対パスを返す。
シンボリックリンクであれば、リンク先を再帰的に解決する。

## tee

標準出力に書きつつファイルにも書く、ということをやりたいときに使う。

```bash
./a.sh | tee a.log
./a.sh | tee -a a.log # 追記
./a.sh 2>&1 | tee a.log # 標準エラーもファイルに書く
```

参考:

- [teeコマンドの使い方 - Qiita](https://qiita.com/wnoguchi/items/2fc3ec11043d139dc6bb "teeコマンドの使い方 - Qiita")

## touch

[Man page of TOUCH](https://linuxjm.osdn.jp/html/gnumaniak/man1/touch.1.html)

```bash
touch -t 201807040100 path/to/file # mtimeを2018/7/4 01:00に変更
```

GNUオプション: ※macOSでは使えない

 Option | 効果
--------|-----
 `--[d]ate=日時` | 日時を指定する際に、 `-t` オプションの代わりに使える。dateコマンドの書式で日時を渡せるようだ

参考:

- [【 touch 】コマンド――タイムスタンプを変更する／新規ファイルを作成する：Linux基本コマンドTips（23） \- ＠IT](http://www.atmarkit.co.jp/ait/articles/1606/14/news013.html)

## umask

Examples:

```sh
# 現在のumask値を表示
umask

# umaskを022に設定
umask 022
```

関連項目:

- [OS > Linux#umask]({{<ref "/a/os/linux/_index.md">}}#umask)

参考:

- [Linux umask command help and examples](https://www.computerhope.com/unix/uumask.htm)

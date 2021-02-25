---
title: "UNIX系コマンド"
linkTitle: "UNIX系コマンド"
description: >
  UNIX系OSで使えるコマンド
date: 2020-04-27T19:37:41+09:00
simple_list: true
weight: 800
---

筆者はLinuxかmacOSを使うことが多い。  

## About

Linux（GNU系）とmacOS（BSD系）では同じコマンドでもオプションや挙動が違うことがあるので、注意が必要。

参考:

- [List of Unix commands - Wikipedia](https://en.wikipedia.org/wiki/List_of_Unix_commands) ... IEEE規格らしい

### 関連ページ

- [macOS#GNUコマンドを使う]({{<ref "/a/os/mac/_index.md">}}#gnuコマンドを使う)

## リファレンス

- [SS64 Command line reference](https://ss64.com/) ... Linux, macOS etc.

## 日付・時刻・時間
### date

https://linuxjm.osdn.jp/html/GNU_coreutils/man1/date.1.html

※macOS（BSD系）だとオプションが異なる

Examples:

```sh
# 書式指定
date +%Y%m%d # YYYYMMDD
date +%FT%T  # ISO8601風
date +%s     # unixtime
date +%s.%N  # ナノ秒まで取得
date +%s.%3N # ミリ秒まで取得

# 日時指定/相対
## GNU系
date -d tomorrow # 明日
date -d '1 hour' # 1時間後
date -d '1 days ago' # 昨日
## macOS
date -v -1d # 昨日

# 日時指定/絶対
## GNU系
date -d @1530675922 # unixtime
## macOS
date -r 1530675922 # unixtime

# ファイルのタイムスタンプを取得
date -r FILE
## unixtime形式で取得
date +%s -r FILE
```

NOTE:

- Mac だと `-d '〜'` オプションが使えない
- `%N` はGNU拡張らしい

参考:

- [日付を取得する | UNIX & Linux コマンド・シェルスクリプト リファレンス](http://shellscript.sunone.me/date.html "日付を取得する | UNIX & Linux コマンド・シェルスクリプト リファレンス")
- [date コマンド \| コマンドの使い方\(Linux\) \| hydroculのメモ](https://hydrocul.github.io/wiki/commands/date.html)
- [date コマンドで日時のミリ秒単位まで表示する - Qiita](https://qiita.com/niwasawa/items/9502e97b6c4d28d24042)
- [dateコマンドで、ファイルのタイムスタンプを取得 | ex1-lab](https://ex1.m-yabe.com/archives/4311)
- macOS:
  - [date(1) \[osx man page\]](https://www.unix.com/man-page/osx/1/date/)
- [unixtimeとdatetimeを変換する（Mac/BSD編） - Qiita](https://qiita.com/zaburo/items/6929bea1f094c8c6a4fc)
- [Macのdateコマンドで前日の日付を取得する - Qiita](https://qiita.com/___uhu/items/3c2312359da542cda163)

## アーカイブ
### zip/unzip

```bash
## dir/ を再帰的に圧縮
## 展開すると dir/ も出来る
zip -r foo.zip dir/

## 中身を bar/ に展開
unzip foo.zip -d bar/
```

参考:

- [Linuxコマンド集 - 【 zip 】 ファイルを圧縮する（拡張子.zip）：ITpro](http://itpro.nikkeibp.co.jp/article/COLUMN/20060228/231001/?rt=nocnt "Linuxコマンド集 - 【 zip 】 ファイルを圧縮する（拡張子.zip）：ITpro")
- [Linux基本コマンドTips（35）：unzipコマンド――ZIPファイルからファイルを取り出す - ＠IT](http://www.atmarkit.co.jp/ait/articles/1607/26/news014.html "Linux基本コマンドTips（35）：unzipコマンド――ZIPファイルからファイルを取り出す - ＠IT")

## チェックサム
### cksum

ファイルのCRCチェックサムを算出し、ファイルサイズとともに表示する。

※CRC-32 (IEEE規格)とは異なる

例:

```sh
$ cksum foo.txt
4032292776 319 foo.txt
```

関連項目:

- [セキュリティ > 符号化#CRC]({{<ref "/a/security/encode.md">}}#crc)

参考:

- [GNU Coreutils: 6.3 cksum: CRC チェックサムとバイト数を表示する](https://linuxjm.osdn.jp/info/GNU_coreutils/coreutils-ja_36.html)
- [Linuxコマンド【 cksum 】ファイルのCRCチェックサムとサイズを表示 - Linux入門 - Webkaru](https://webkaru.net/linux/cksum-command/)

### md5sum

MD5ハッシュ値を算出

例:

```sh
$ md5sum foo.txt
1d1e64beb5220bf54122293141185c1a  foo.txt
```

参考:

- [【MD5 SHA1 SHA256 CRC】ハッシュ値（チェックサム）の確認方法 | server-memo.net](https://www.server-memo.net/tips/chcksum.html)

### shasum

SHAチェックサムを算出する。  
`-a` オプションでアルゴリズムを指定できる。  
デフォルトはSHA-1

Examples:

```sh
$ shasum foo.txt
f1d2d2f924e986ac86fdf7b36c94bcdf32beec15  foo.txt

$ shasum foo.txt -a 256
b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b878ae4944c  foo.txt
```

類似コマンド:

- sha1sum
- sha256sum
- sha512sum

例:

```sh
$ sha256sum foo.txt
b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b878ae4944c  foo.txt
```

## ファイルシステム
### exportfs

```bash
exportfs -a  # /etc/exports の全てのディレクトリをエクスポート
exportfs -v  # 現在エクスポート中のディレクトリ一覧
```

参考:

- [exportfs コマンド](https://www.ibm.com/support/knowledgecenter/ja/ssw_aix_71/com.ibm.aix.cmds2/exportfs.htm)


### mount

```sh
## uid, gid指定
mount -o uid=1000,gid=1000 /dev/sdb1 /mnt
```

※NFSの場合、uid/gid指定は不可


See also:

- https://sites.google.com/site/progrhymetechwiki/linux/fs

参考:

- [【 mount 】コマンド――ファイルシステムをマウントする：Linux基本コマンドTips（183） - ＠IT](http://www.atmarkit.co.jp/ait/articles/1802/15/news035.html)
- [製品レビュー：企業ユーザーのためのSFU 3.5活用ガイダンス　第1回　SFU 3.5の概要とNFS機能　2．NFSとユーザー名マッピング - ＠IT](http://www.atmarkit.co.jp/fwin2k/productreview/sfu35-01/sfu35_01_03.html)


### umount

```sh
umount <mount先>
umount <mount元>
```

## リソース管理
### top(1)

[top(1): tasks - Linux man page](https://linux.die.net/man/1/top)

Examples:

```sh
# インタラクティブモード
top
## 描画間隔を5秒に変更
top -d 5

# バッチモードで1回だけ実行
top -b -n 1
## CPUコアごとの負荷も表示
top -b -n 1 -1
```

インタラクティブモードの主な操作:

- `M` ... メモリ使用率順にソート
- `P` ... CPU使用率順にソート
- `1` ... CPUコアごとの負荷を表示
- `c` ... プロセス名詳細を表示（トグル）
- `q` ... 終了
- `F` or `O` ... ソートするフィールドを選ぶ
- `R` ... ソートの昇順/降順を切り替え

Mac版の違い:

- `-b` オプションやバッチモードがなさそう
- CPUコアごとに負荷を見る方法がわからん

参考:

- [\[Linux\] top コマンドをインタラクティブに操作する | バシャログ。](http://bashalog.c-brains.jp/11/05/24-220315.php)

## ユーティリティー
### history

Bash, Zshで引数の扱いが異なるところがある。

```sh
# Zsh
history -N

# Bash
history N
```

参考:

- [【Mac】historyコマンドの表示件数でハマってしまった件 - Qiita](https://qiita.com/JUNO-LEARN/items/5322cccb1aff5661604d)

### timeout

```sh
timeout <N> command args...
```

指定した秒数の経過後、コマンドを終了する。

オプション:

 オプション | 意味
----------|------
 `-s <シグナル>` <br /> `--signal=<シグナル>` | タイムアウト時に送信するシグナル。デフォルトは `TERM`
 `-k <N>` <br /> `--kill-after=<N>` | 最初のタイムアウトでシグナル送信後、指定時間を過ぎてもコマンドが動いている場合、 `KILL` シグナルを送る

参考:

- [【 timeout 】コマンド――制限時間を付けて指定のコマンドを実行する：Linux基本コマンドTips（316） - ＠IT](https://www.atmarkit.co.jp/ait/articles/1906/27/news008.html)

### watch

```bash
watch -n <N> command args...
```

N秒ごとにコマンドを実行して出力を表示。

参考:

- [watch コマンド | コマンドの使い方(Linux) | hydroculのメモ](https://hydrocul.github.io/wiki/commands/watch.html "watch コマンド | コマンドの使い方(Linux) | hydroculのメモ")

### xargs

NOTE:

- ※Qiitaに記事を書いており、そちらを更新するケースもある:
  - [xargsコマンドの備忘録 - Qiita](https://qiita.com/progrhyme/items/2e2d58aba3b1be804e19)

 オプション | GNU | macOS | 機能
------------|-----|-------|------
 -r | Yes | ? | 入力が空白しかないときはコマンド実行しない

参考:

- [Man page of XARGS](https://linuxjm.osdn.jp/html/GNU_findutils/man1/xargs.1.html)
- [xargs - FreeBSD Manual Pages](https://www.freebsd.org/cgi/man.cgi?query=xargs&amp;apropos=0&amp;sektion=0&amp;manpath=FreeBSD+8.0-RELEASE&amp;format=html)
- [xargs Man Page - macOS - SS64.com](https://ss64.com/osx/xargs.html)

## Child Pages

---
title: "UNIX系コマンド"
linkTitle: "UNIX系コマンド"
description: >
  UNIX系OSで使えるコマンド
date: 2020-04-27T19:37:41+09:00
weight: 800
---

筆者はLinuxかmacOSを使うことが多い。

## About

参考:

- [List of Unix commands - Wikipedia](https://en.wikipedia.org/wiki/List_of_Unix_commands) ... IEEE規格らしい

### 関連ページ

- [macOS#GNUコマンドを使う]({{<ref "/a/os/mac/_index.md">}}#gnuコマンドを使う)

## リファレンス

- [SS64 Command line reference](https://ss64.com/) ... Linux, macOS etc.

## 日付・時刻・時間
### date

https://linuxjm.osdn.jp/html/GNU_coreutils/man1/date.1.html

Examples:

```sh
# 書式指定
date +%Y%m%d # YYYYMMDD
date +%FT%T  # ISO8601風
date +%s     # unixtime
date +%s.%N  # ナノ秒まで取得
date +%s.%3N # ミリ秒まで取得

# 日時指定/相対
date -d tomorrow # 明日
date -d '1 hour' # 1時間後
date -d '1 days ago' # 昨日

# 日時指定/絶対
date -d @1530675922 # unixtime

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

## ファイル操作
### find

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

### mktemp

[Man page of MKTEMP](https://linuxjm.osdn.jp/html/GNU_coreutils/man1/mktemp.1.html)

一時ファイル、またはディレクトリを作成する。

```sh
mktemp
# ディレクトリを作成
mktemp -d
```

参考:

- [mktemp Man Page - macOS - SS64.com](https://ss64.com/osx/mktemp.html)

### readlink(1)

[Man page of READLINK](https://linuxjm.osdn.jp/html/GNU_coreutils/man1/readlink.1.html)

Examples:

```sh
# シンボリックリンクのリンク先を返す。再帰的に探索はしない
readlink <link>

# realpathと同じ働きをする
readlink -f <file>
```

### realpath(1)

[Man page of REALPATH](https://linuxjm.osdn.jp/html/GNU_coreutils/man1/realpath.1.html)

引数として与えられたファイル or ディレクトリの絶対パスを返す。
シンボリックリンクであれば、リンク先を再帰的に解決する。

### tee

標準出力に書きつつファイルにも書く、ということをやりたいときに使う。

```bash
./a.sh | tee a.log
./a.sh | tee -a a.log # 追記
./a.sh 2>&1 | tee a.log # 標準エラーもファイルに書く
```

参考:

- [teeコマンドの使い方 - Qiita](https://qiita.com/wnoguchi/items/2fc3ec11043d139dc6bb "teeコマンドの使い方 - Qiita")


### touch

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

### umask

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

## テキスト処理
### grep

```bash
## ファイル名だけ表示
grep -l PATTERN [PATH]
```

### head

https://linuxjm.osdn.jp/html/GNU_textutils/man1/head.1.html

```sh
## 先頭1行を表示
head -1 [file...]
## 先頭20行を表示
head -n 20 [file...]

## 先頭256Bを表示
head -c 256 [file...]
## 先頭256KBを表示
head --bytes 256k [file...]
```

### printf(1)

書式を指定して文字列を標準出力に出力。

シェルのビルトイン関数と /usr/bin/printf がある。
違いはよくわからない。

```sh
printf "%s %02d" foo 1
#=> foo 01
env LANG=ja_JP.UTF-8 printf "%'d" 1234567890
#=> 1,234,567,890
```

参考:

- [【 printf 】コマンド――データを整形して表示する：Linux基本コマンドTips（319） - ＠IT](https://www.atmarkit.co.jp/ait/articles/1907/05/news012.html)
- [シェルスクリプトで数字を３桁ごとのカンマ区切りにする](https://blog.cles.jp/item/5819)

### sed

https://linuxjm.osdn.jp/html/GNU_sed/man1/sed.1.html

与えられたテキストに対して、sedスクリプトで指定された文字列置換を行って結果のテキストを表示するストリームエディタ。

macOSとLinuxで挙動が違うので、注意が必要。

Examples:

```sh
# 各行のxを1つyに置換した結果を表示
sed s/x/y/ foo.txt
# 各行のxをすべてyに置換した結果を表示
sed -e s/x/y/g foo.txt
# 全文字をすべてyに置換した結果を表示
cat foo.txt | sed 's/./y/g'
# xをyに、aをbに置換
sed -e s/x/y/ -e s/a/b/ foo.txt
```

 オプション | 効果
----------|------
 --[e]xpression=SCRIPT | 実行するコマンドとしてスクリプトを追加
 --[f]ile=FILE | 実行するコマンドとしてスクリプトファイルを追加
 --[r]egexp-extended | （※Linux）拡張正規表現を使う
 -E | （※macOS）拡張正規表現を使う

※ `-e`, `-f` のどちらの指定もなければ、最初のオプションでない引数がsedスクリプトとして解釈される。

### sort

```bash
## 第2フィールドで数値の降順ソート
cat file | sort -nr -k2
```

参考:

- https://linuxjm.osdn.jp/html/gnumaniak/man1/sort.1.html
- [sort コマンド | コマンドの使い方(Linux) | hydroculのメモ](https://hydrocul.github.io/wiki/commands/sort.html "sort  コマンド | コマンドの使い方(Linux) | hydroculのメモ")


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

## ユーザ管理
### getent

```sh
getent group <group> # グループに属しているユーザをリスト
```

参考:

- [Linuxコマンドでユーザーのグループ確認・変更。 - Qiita](https://qiita.com/niiyz/items/53aa4195dcc69db2052b)

### gpasswd

```bash
gpasswd -a <login> <group> # ユーザをグループに所属させる
gpasswd -d <login> <group> # ユーザをグループから削除
```

参考:

- [【 gpasswd 】コマンド――ユーザーが所属するグループを管理する：Linux基本コマンドTips（72） - ＠IT](http://www.atmarkit.co.jp/ait/articles/1612/12/news016.html "【 gpasswd 】コマンド――ユーザーが所属するグループを管理する：Linux基本コマンドTips（72） - ＠IT")

### groupadd

グループ作成。

```bash
groupadd newgroup
```

参考:

- [Linuxコマンド【 groupadd 】新規グループの作成 - Linux入門 - Webkaru](https://webkaru.net/linux/groupadd-command/ "Linuxコマンド【 groupadd 】新規グループの作成 - Linux入門 - Webkaru")

### passwd

```bash
passwd -l <login> # アカウントをロック
passwd -u <login> # アンロック
```

ロックされたアカウントはログインできず、利用不可になる。

参考:

- [Linux ユーザーアカウントをロック・アンロックする](http://kazmax.zpp.jp/linux/account_lock.html "Linux ユーザーアカウントをロック・アンロックする")

### useradd

ユーザ追加。オプション多数

オプション | 意味
----------------|-------
`-m` | ホームディレクトリ作成
`-s <SHELL>` | ログインシェルを指定

Examples:

```Bash
## ホームディレクトリ作成
useradd -m <login>
## ログインシェルを/bin/bashに
useradd -s /bin/bash <login> 
```

参考:
- [useraddコマンドについて詳しくまとめました 【Linuxコマンド集】](https://eng-entrance.com/linux-command-useradd)


### usermod

```bash
usermod -g admin <login> # 主グループを変更
usermod -aG ops,app,... <login> # 副グループ追加
```

参考:

- [usermodコマンドについて詳しくまとめました 【Linuxコマンド集】](https://eng-entrance.com/linux-command-usermod "usermodコマンドについて詳しくまとめました 【Linuxコマンド集】")

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

## プロセス管理
### kill(1)

[Man page of KILL](https://linuxjm.osdn.jp/html/util-linux/man1/kill.1.html)

Examples:

```sh
# シグナル名のリストを表示
kill -l

# プロセスにSIGTERMを送信
kill <PID>...

# SIGHUPを送信
kill -HUP <PID>...

# プロセスの生存確認
kill -0 <PID>
```

NOTE:

- macOSだと少しオプションが違うかも
- シェルのビルトインと /bin/kill でも少しオプションが違う

See Also:

- [OS > Linux#Signal]({{<ref "/a/os/linux/_index.md">}}#signal)

参考:

- [kill Man Page - macOS - SS64.com](https://ss64.com/osx/kill.html)
- [killでプロセスに「0」を送ると、プロセスの生存確認ができる - Perl日記](http://r9.hateblo.jp/entry/2018/01/15/193444)

### pgrep

プロセス名で検索して該当するプロセス番号を表示。

Examples:

```sh
pgrep perl
```

### pkill

プロセス名で指定してシグナルを送信する。

Examples:

```sh
pkill perl
```

### ps

[Man page of PS](https://linuxjm.osdn.jp/html/procps/man1/ps.1.html)

Examples:

```sh
ps aux
ps aufxwww
ps auxwww -L
ps -ef
ps -efL
```

Options:

option | 意味
---------|---------
`f` | forest, プロセスをツリー状に表示
`-L` | スレッド表示。 `f` と同時に指定はできない

### trap

シグナルによってプロセスが中断・停止させられたときに、実行するコマンドを指定する。

Syntax:

```sh
trap 'コマンド' シグナルリスト
```

Examples:

```sh
trap 'echo trapped.' 1 2 3 15

# trapをリセットする
trap 1 2 3 15
```

NOTE:

- SIGKILL (9) はtrapできない

See Also:

- [OS > Linux#Signal]({{<ref "/a/os/linux/_index.md">}}#signal)

参考:

- [シグナルと trap コマンド | UNIX &amp; Linux コマンド・シェルスクリプト リファレンス](https://shellscript.sunone.me/signal_and_trap.html)
- [shellのtrapについて覚え書き - Qiita](https://qiita.com/ine1127/items/5523b1b674492f14532a)
- [trap コマンド | コマンドの使い方(Linux) | hydroculのメモ](https://hydrocul.github.io/wiki/commands/trap.html)

## ユーティリティー
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

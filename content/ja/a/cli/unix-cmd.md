---
title: "UNIX系コマンド"
linkTitle: "UNIX系コマンド"
description: >
  UNIX系OSで使えるコマンド
date: 2020-04-27T19:37:41+09:00
---

筆者はLinuxかmacOSを使うことが多い。

## About

参考:

- [List of Unix commands - Wikipedia](https://en.wikipedia.org/wiki/List_of_Unix_commands) ... IEEE規格らしい。

## 日付・時刻・時間
### date

```bash
## 書式指定
date +%Y%m%d # YYYYMMDD
date +%FT%T # ISO8601風
date +%s # unixtime

## 日時指定/相対
date -d tomorrow # 明日
date -d '1 hour' # 1時間後
date -d '1 days ago' # 昨日

## 日時指定/絶対
date -d @1530675922 # unixtime
```

NOTE:

- Mac だと `-d '〜'` オプションが使えない

参考:

- [日付を取得する | UNIX & Linux コマンド・シェルスクリプト リファレンス](http://shellscript.sunone.me/date.html "日付を取得する | UNIX & Linux コマンド・シェルスクリプト リファレンス")
- [date コマンド \| コマンドの使い方\(Linux\) \| hydroculのメモ](https://hydrocul.github.io/wiki/commands/date.html)

## ファイル操作
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

```bash
touch -t 201807040100 path/to/file # mtimeを2018/7/4 01:00に変更
```

参考:

- [【 touch 】コマンド――タイムスタンプを変更する／新規ファイルを作成する：Linux基本コマンドTips（23） \- ＠IT](http://www.atmarkit.co.jp/ait/articles/1606/14/news013.html)

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
### watch

```bash
watch -n <N> command args...
```

N秒ごとにコマンドを実行して出力を表示。

参考:

- [watch コマンド | コマンドの使い方(Linux) | hydroculのメモ](https://hydrocul.github.io/wiki/commands/watch.html "watch コマンド | コマンドの使い方(Linux) | hydroculのメモ")

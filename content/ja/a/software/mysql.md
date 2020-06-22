---
title: "MySQL"
linkTitle: "MySQL"
description: https://www.mysql.com/
date: 2020-06-22T16:02:33+09:00
weight: 400
---

## About

アイコンはイルカ。

## InnoDB

MySQL 5.1ぐらいからデフォルトのストレージエンジンになった。  
MySQL 5.7からシステムテーブルでも使われるようになった。

### ロック

- [MySQL :: MySQL 5\.6 リファレンスマニュアル :: 14\.2\.6 InnoDB のレコード、ギャップ、およびネクストキーロック](https://dev.mysql.com/doc/refman/5.6/ja/innodb-record-level-locks.html)

### データ構造

- [MySQL :: MySQL 5.6 リファレンスマニュアル :: 14.2.13.7 物理的な行構造](https://dev.mysql.com/doc/refman/5.6/ja/innodb-physical-record.html)

## Features
### オンラインDDL

- [MySQL :: MySQL 5.6 リファレンスマニュアル :: 14.11.1 オンライン DDL の概要](https://dev.mysql.com/doc/refman/5.6/ja/innodb-create-index-overview.html "MySQL :: MySQL 5.6 リファレンスマニュアル :: 14.11.1 オンライン DDL の概要")

MySQL 5.5 or MySQL 5.1 with InnoDB Pluginで、CREATE/DROP INDEX時にテーブルコピーを行わないように最適化された。  
これは高速インデックス作成と呼ばれた。
5.6では更に多くのALTER TABLE操作をテーブルコピーなしでできるようになってる。

## CLI
### mysqldump

https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html

## How-to
### クエリ結果をTSVで出力

- `mysqldump`
- `mysql -e "select ..."` の形式だと、CSVでは出力できないらしい。

参考:

- [MySQLのデータをcsv,tsv形式でダンプする - Qiita](https://qiita.com/d-dai/items/e56c2e5abf558328373f)
- 2009年8月 [MySQL の結果を csv 形式で標準出力させたい - いけむランド](https://fd0.hatenablog.jp/entry/20090801/p1)
- 2013年4月 [MySQLリモートDBの結果をローカルCSVファイルに出力する方法 | 開発メモるアル](http://shusatoo.net/db/mysql/mysql-remote-db-result-output-local-csvfile/)

### データベースの Rename をどうやるか

- DB 名指定で RENAME TABLE
  - `RENAME TABLE prev_database.t TO new_databaes.t;`
- mysqldump して restore

参考: [How to Rename a Database in MySQL | Chartio](https://chartio.com/resources/tutorials/how-to-rename-a-database-in-mysql/ "How to Rename a Database in MySQL | Chartio")

### 遅延レプリケーション

MySQL5.6以降の場合、Slave側で以下を実行:

```sql
CHANGE MASTER TO MASTER_DELAY = N; -- Nは正の整数
```

参考:

- [MySQL :: MySQL 5.6 リファレンスマニュアル :: 17.3.9 遅延レプリケーション](https://dev.mysql.com/doc/refman/5.6/ja/replication-delayed.html "MySQL :: MySQL 5.6 リファレンスマニュアル :: 17.3.9 遅延レプリケーション")

## Topics
### 接続のタイムアウトに関する設定

色々パラメータがあって混乱しがちなのでまとめたい。

#### サーバ側

See https://dev.mysql.com/doc/refman/5.6/ja/server-system-variables.html

- net_read_timeout ... 接続からデータ読み込みに失敗したら切断
- net_write_timeout ... 接続に対してデータ書き込みに失敗したら切断
- wait_timeout ... クライアントがアイドルになったら切断
- interactive_timeout ... インタラクティブセッションにおけるwait_timeout
- net_retry_count ... 通信失敗時のリトライ回数

参考:

- wait_timeout について:
  - [MyNA(日本MySQLユーザ会) 2015年4月 に行ってきた #mysql_jp - weblog of key_amb](http://keyamb.hatenablog.com/entry/2015/04/23/004126 "MyNA(日本MySQLユーザ会) 2015年4月 に行ってきた #mysql_jp - weblog of key_amb")

#### クライアント側

See https://dev.mysql.com/doc/refman/5.6/ja/mysql-options.html

- MYSQL_OPT_CONNECT_TIMEOUT ... サーバにつながらないときにタイムアウト
- MYSQL_OPT_READ_TIMEOUT ... 接続からデータ読み込めないときにタイムアウト
- MYSQL_OPT_WRITE_TIMEOUT ... 接続にデータ書き込めないときにタイムアウト
- MYSQL_OPT_RECONNECT ... 接続が切れたと判断したら再接続

PerlやRubyのクライアントではよく `connect_timeout`, `read_timeout` といった接続時のオプションになっている。

## Reference
### CREATE TABLE

- https://dev.mysql.com/doc/refman/5.6/ja/create-table.html

Tips:

- `CREATE TABLE B LIKE A;` でテーブルAと同じカラム構成のテーブルBを作れる。

参考:

- [MySQLの CREATE TABLE ... LIKE ... - 不思議なサービスをつくる新人プログラマーの日記](http://d.hatena.ne.jp/tnnsst35/20110604/1307181215 "MySQLの CREATE TABLE ... LIKE ... - 不思議なサービスをつくる新人プログラマーの日記")

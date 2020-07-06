---
title: "MySQL"
linkTitle: "MySQL"
description: https://www.mysql.com/
date: 2020-06-22T16:02:33+09:00
weight: 400
---

## About

アイコンはイルカ。

## Docker

公式イメージ: https://hub.docker.com/_/mysql

## InnoDB

MySQL 5.1ぐらいからデフォルトのストレージエンジンになった。  
MySQL 5.7からシステムテーブルでも使われるようになった。

### ロック

- [MySQL :: MySQL 5\.6 リファレンスマニュアル :: 14\.2\.6 InnoDB のレコード、ギャップ、およびネクストキーロック](https://dev.mysql.com/doc/refman/5.6/ja/innodb-record-level-locks.html)

### データ構造

- [MySQL :: MySQL 5.6 リファレンスマニュアル :: 14.2.13.7 物理的な行構造](https://dev.mysql.com/doc/refman/5.6/ja/innodb-physical-record.html)

## CLI Options

https://dev.mysql.com/doc/refman/8.0/en/option-file-options.html

サーバ、クライアント両対応のオプションっぽい。

 Option | 機能
--------|-----
 `--defaults-file` | my.cnfなどの設定ファイル。これを指定すると一部の例外を除き他の設定ファイルを読まなくなる
 `--defaults-extra-file` | my.cnfなどの設定ファイル。グローバルオプションファイルを読んだ後、ログインパスのファイルを読む前に読み込まれる

NOTE:

- `--defaults-file` 等のオプションは他のオプションハンドリングにも関わるから、他のオプションよりも前に指定しないといけない、とドキュメントに書かれている

> Because these options affect option-file handling, they must be given on the command line and not in an option file. To work properly, each of these options must be given before other options, with these exceptions:

## Specs
### CHARSETとCOLLATE

ドキュメント:

- [MySQL :: MySQL 5.6 リファレンスマニュアル :: 10.1.4 接続文字セットおよび照合順序](https://dev.mysql.com/doc/refman/5.6/ja/charset-connection.html)

キーワード:

- 🍣🍺問題, ハハパパ問題

SQLでの確認方法:

```sql
-- charset
show variables like 'chara%';
-- collation
show variables like 'collation%';
```

#### クライアントでの指定

いくつか設定方法がある:

- `my.cnf` での指定
- 接続後にSQLで指定:
  - `SET NAMES '<charset>' [COLLATE '<collation>']` <- 基本、これでよさそう

### SQL Mode

https://dev.mysql.com/doc/refman/8.0/en/sql-mode.html

サーバのSQLモード。

- `NO_ZERO_DATE` ... `0000-00-00` を日付として許可しない。

## Features
### オンラインDDL

- [MySQL :: MySQL 5.6 リファレンスマニュアル :: 14.11.1 オンライン DDL の概要](https://dev.mysql.com/doc/refman/5.6/ja/innodb-create-index-overview.html "MySQL :: MySQL 5.6 リファレンスマニュアル :: 14.11.1 オンライン DDL の概要")

MySQL 5.5 or MySQL 5.1 with InnoDB Pluginで、CREATE/DROP INDEX時にテーブルコピーを行わないように最適化された。  
これは高速インデックス作成と呼ばれた。
5.6では更に多くのALTER TABLE操作をテーブルコピーなしでできるようになってる。

## How-to
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

### タイムゾーンの設定

SQLで変更する場合:

```sql
-- SUPER権限があれば、サーバグローバルの設定を変えることができる
-- 稼働中のシステムで実行する場合は最大の注意が必要
SET GLOBAL time_zone = <timezone>;

-- クライアントはセッションごとにタイムゾーン設定を変更できる
SET time_zone = <timezone>;
```

参考:

- [MySQL :: MySQL 5.6 リファレンスマニュアル :: 10.6 MySQL Server でのタイムゾーンのサポート](https://dev.mysql.com/doc/refman/5.6/ja/time-zone-support.html)
- 下のトピックの方

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

### タイムゾーン

- TIMESTAMPはUNIX TIMESTAMP値を保持しており、タイムゾーンによって日時が変わる
- DATETIMEはタイムゾーンも含めて値を保持している

参考:

- [MySQLのタイムゾーン - @tmtms のメモ](https://tmtms.hatenablog.com/entry/2015/08/22/mysql-timezone)

## Cookbooks

TODO: 標準SQLについて別ページにまとめ、ここには差分だけ記す。

### CREATE TABLE

Examples:

```sql
CREATE TABLE animals (
     id MEDIUMINT NOT NULL AUTO_INCREMENT,
     name CHAR(30) NOT NULL,
     PRIMARY KEY (id)
);
```

### CREATE DATABASE

Examples:

```sql
CREATE DATABASE foo CHARACTER SET utf8mb4;
```

参考:

- [データベースを作成する(CREATE DATABASE文) | MySQLの使い方](https://www.dbonline.jp/mysql/database/index1.html)

### INSERT

Examples:

```sql
INSERT INTO animals (name) VALUES
    ('dog'),('cat'),('penguin'),
    ('lax'),('whale'),('ostrich');
```

## Reference
### CREATE TABLE

- https://dev.mysql.com/doc/refman/5.6/ja/create-table.html

Tips:

- `CREATE TABLE B LIKE A;` でテーブルAと同じカラム構成のテーブルBを作れる。

参考:

- [MySQLの CREATE TABLE ... LIKE ... - 不思議なサービスをつくる新人プログラマーの日記](http://d.hatena.ne.jp/tnnsst35/20110604/1307181215 "MySQLの CREATE TABLE ... LIKE ... - 不思議なサービスをつくる新人プログラマーの日記")

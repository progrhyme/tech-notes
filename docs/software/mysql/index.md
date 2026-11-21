---
date: '2020-06-22T16:02:33+09:00'
description: https://www.mysql.com/
---

# MySQL

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

### 権限

https://dev.mysql.com/doc/refman/8.0/en/grant.html

GRANT文やREVOKE文で指定できる権限。

 権限 | 付与可能レベル | 意味
-----|--------------|-----
 PROCESS | グローバル | ユーザーが SHOW PROCESSLIST を使用してすべてのプロセスを表示できるようにする

### INFORMATION_SCHEMA

https://dev.mysql.com/doc/refman/5.6/ja/information-schema.html

メタデータDB

#### COLUMNS

https://dev.mysql.com/doc/refman/5.6/ja/information-schema-columns-table.html

## Features
### レプリケーション
#### レプリケーションとトリガー

Ref. [MySQL :: MySQL 5.6 リファレンスマニュアル :: 17.4.1.32 レプリケーションとトリガー](https://dev.mysql.com/doc/refman/5.6/ja/replication-features-triggers.html)

- ステートメントベースレプリケーションの場合
    - トリガーがスレーブでも実行される
- 行ベースレプリケーションの場合
    - トリガーはスレーブでは実行されない
    - マスターの行変更が複製され、スレーブに適用される

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

## Versions

### EOL

[MySQL :: MySQL Product Support EOL Announcements](https://www.mysql.com/jp/support/eol-notice.html)

参考:

- [MySQL | End of Life(EOL)まとめサイト](https://support-version.com/index.php?MySQL)
- [MySQL Community Edition の EOL について - Qiita](https://qiita.com/witchcraze/items/820dd848d48dfb8a5f96)

### 8
#### 8.0.21

https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-21.html

- mysqldumpに `PROCESS` 権限が必要に（または `--no-tablespaces` オプション指定）

#### 8.0.16

https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-16.html

- global / schema / tablespaceレベルでDEFAULT ENCRYPTIONを設定可能に

参考:

- [MySQL 8.0.16 でテーブルスペース・REDO ログ／UNDO ログ・システムテーブル暗号化 - Qiita](https://qiita.com/hmatsu47/items/bae53fd0f6d09511732c)

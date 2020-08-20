---
title: "SQL"
linkTitle: "SQL"
date: 2020-08-20T11:54:48+09:00
---

SQLリファレンス。

標準SQLについてはSee [SQL]({{<ref "/a/sql.md">}})

## DML
### INSERT

Examples:

```sql
INSERT INTO animals (name) VALUES
    ('dog'),('cat'),('penguin'),
    ('lax'),('whale'),('ostrich');
```

## DDL
### CREATE DATABASE

Examples:

```sql
CREATE DATABASE foo CHARACTER SET utf8mb4;
```

参考:

- [データベースを作成する(CREATE DATABASE文) | MySQLの使い方](https://www.dbonline.jp/mysql/database/index1.html)

### CREATE TABLE

- https://dev.mysql.com/doc/refman/5.6/ja/create-table.html

Examples:

```sql
CREATE TABLE animals (
     id MEDIUMINT NOT NULL AUTO_INCREMENT,
     name CHAR(30) NOT NULL,
     PRIMARY KEY (id)
);
```

Tips:

- `CREATE TABLE B LIKE A;` でテーブルAと同じカラム構成のテーブルBを作れる。

参考:

- [MySQLの CREATE TABLE ... LIKE ... - 不思議なサービスをつくる新人プログラマーの日記](http://d.hatena.ne.jp/tnnsst35/20110604/1307181215 "MySQLの CREATE TABLE ... LIKE ... - 不思議なサービスをつくる新人プログラマーの日記")

## その他
### SHOW BINARY LOGS

- https://dev.mysql.com/doc/refman/5.6/ja/show-binary-logs.html

binlogファイルを一覧表示する

```sql
SHOW BINARY LOGS
SHOW MASTER LOGS
```

### SHOW BINLOG EVENTS

- https://dev.mysql.com/doc/refman/5.6/ja/show-binlog-events.html

Syntax:

```sql
SHOW BINLOG EVENTS
   [IN 'log_name'] [FROM pos] [LIMIT [offset,] row_count]
```

NOTE:

- LIMIT句なしで指定すると全バイナリログの内容を出力するので、リソースを大量に消費する可能性がある

### SHOW GRANTS

https://dev.mysql.com/doc/refman/8.0/en/show-grants.html

Examples:

```sql
-- 現在のユーザの権限を表示
SHOW GRANTS;
```

---
title: "クライアント"
linkTitle: "クライアント"
date: 2020-06-26T13:24:36+09:00
---

mysql, mysqldumpといったCLIやクライアントライブラリを介した利用、設定方法等について。

## Configuration

関連項目:

- [MySQL#CLI-Options]({{<ref "/a/software/mysql/_index.md">}}#cli-options)

### my.cnf

代表的な設定ファイル。

## CLI
### mysql

### mysqldump

https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html

 Option | 説明
--------|-----
 `--no-tablespaces, -y` | CREATE LOGFILE GROUP ステートメントおよび CREATE TABLESPACE ステートメントを出力に書き出さない

### パスワードの渡し方

`mysql -u$USER -p$PASS` みたいなやり方をしてると警告が出るようになったのは 5.5 ぐらいからだったかな？

このページにガイドがある:

- [MySQL :: MySQL 5.6 リファレンスマニュアル :: 6.1.2.1 パスワードセキュリティーのためのエンドユーザーガイドライン](https://dev.mysql.com/doc/refman/5.6/ja/password-security-user.html)

要点:

- `~/.my.cnf` 等に書いておけばよい

メモ:

- PostgreSQLよりはゆるふわな感じ

## How-to
### クエリ結果をCSV/TSVで出力

- `mysqldump` ... CSV/TSV両対応しているが、サーバローカルにしか吐けないっぽい
- `mysql -e "select ..."` の形式だと、TSVでは出力できるが、CSVでは出力できないらしい

参考:

- [MySQLのデータをcsv,tsv形式でダンプする - Qiita](https://qiita.com/d-dai/items/e56c2e5abf558328373f)
- 2009年8月 [MySQL の結果を csv 形式で標準出力させたい - いけむランド](https://fd0.hatenablog.jp/entry/20090801/p1)
- 2013年4月 [MySQLリモートDBの結果をローカルCSVファイルに出力する方法 | 開発メモるアル](http://shusatoo.net/db/mysql/mysql-remote-db-result-output-local-csvfile/)


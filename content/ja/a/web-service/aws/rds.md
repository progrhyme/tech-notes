---
title: "RDS"
linkTitle: "RDS"
date: 2020-09-16T13:09:11+09:00
weight: 700
---

## 仕様
### パラメータ

- Aurora PostgreSQL
  - https://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/UserGuide/AuroraPostgreSQL.Reference.html

### 管理ユーザ

`rdsadmin` という管理ユーザが作られるが、ユーザは操作不能。  
より弱い権限のユーザで作業することになる。

参考:

- https://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/UserGuide/CHAP_MySQL.html
- https://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Security.html
- [PostgreSQL Deep Dive: RDS for PostgreSQLの中を覗いてみた（追記あり）](http://pgsqldeepdive.blogspot.com/2013/11/rds-for-postgresql.html)

## Features

### 拡張モニタリング

https://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html

- IAM設定が必要

### Maintenance API

- https://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/APIReference/API_DescribePendingMaintenanceActions.html
  - 未適用のメンテナンス情報取得

### イベント通知

[Amazon RDS イベント通知の使用 - Amazon Relational Database Service](https://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/UserGuide/USER_Events.html "Amazon RDS イベント通知の使用 - Amazon Relational Database Service")

RDSに関する様々なイベントの通知をSNSで受け取ることができる。

## Topics
### メンテナンス情報の通知

RDSではセキュリティアップデートなどで再起動される場合にアカウントのメールアドレスに通知してくれない。

ので、DescribePendingMaintenanceActions APIを叩いて、未適用のメンテナンス情報を取得するのが良さそう。  
イベント通知機能ではメンテナンスが起こったことは取得できるが、事前通知はしてくれない。

参考:

- [Amazon RDSのメンテナンスについて調べてみた | 本日も乙](http://blog.jicoman.info/2017/01/rds_maintenance/ "Amazon RDSのメンテナンスについて調べてみた | 本日も乙")
- [Amazon RDS メンテナンス - Amazon Relational Database Service](https://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html "Amazon RDS メンテナンス - Amazon Relational Database Service")

## MySQL
### ストアドプロシージャ

[MySQL RDSインスタンスで利用できるシステムストアドプロシージャのリファレンス](https://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/UserGuide/Appendix.MySQL.SQLRef.html)

#### mysql.rds_show_configuration

https://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/UserGuide/mysql_rds_show_configuration.html

バイナリログを保持する時間数を表示する。

```sql
CALL mysql.rds_show_configuration;
```

## PostgreSQL

ログの保持期間:

- DBパラメータグループの `rds.log_retention_period` で設定する。分単位。デフォルトは `4320` (3日分).

参考:

- [PostgreSQL データベースのログファイル \- Amazon Relational Database Service](https://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.PostgreSQL.html)

### How-to

- [PostgreSQL の一般的な DBA タスク - Amazon Relational Database Service](https://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.html)
  - pg_repackの利用

## Aurora
### Getting Started

- [Amazon Aurora の概要 - Amazon Relational Database Service](http://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/UserGuide/Aurora.Overview.html "Amazon Aurora の概要 - Amazon Relational Database Service")

### 監視
#### CloudWatchメトリクス

https://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/UserGuide/Aurora.Monitoring.html

AWS/RDS

| メトリクス | 説明 | Applies to |
|-----------------|-------|---------------|
| FreeLocalStorage | 一時テーブルやログで使用可能なストレージ容量。インスタンスタイプごとに上限値が決まっているようだ。 | MySQL, PostgreSQL |
| VolumeBytesUsed | 使用されたストレージ容量(Byte) | MySQL, PostgreSQL |

### フェールオーバー

`tier0 > tier1 > ... > tier15` と優先順位が設定できる。  

異なるインスタンスタイプのレプリカを立ち上げてフェールオーバーさせることが簡単にできるみたい。

参考:

- [\[新機能\]RDS for Auroraでフェイルオーバー先の優先順序を指定できます ｜ Developers.IO](https://dev.classmethod.jp/cloud/aws/amazon-aurora-failover-order/ "[新機能]RDS for Auroraでフェイルオーバー先の優先順序を指定できます ｜ Developers.IO")
- [Auroraのインスタンスタイプ変更をフェイルオーバで行ってみた ｜ Developers.IO](https://dev.classmethod.jp/cloud/aws/aurora-changed-failover/ "Auroraのインスタンスタイプ変更をフェイルオーバで行ってみた ｜ Developers.IO")

### Tips
#### temporary diskのサイズがインスタンスサイズに比例

2019-08-01時点で非公開仕様らしい。  
実用上ネックになり得るのでスケールダウン時には要注意。

### Topics
#### Auroraは1インスタンスでも可用性高い

- ダウンタイムは10分ぐらいとか
  - [Amazon Aurora DB クラスターの管理 - Amazon Relational Database Service](http://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/UserGuide/Aurora.Managing.html "Amazon Aurora DB クラスターの管理 - Amazon Relational Database Service")

参考:

- https://aws.amazon.com/jp/rds/details/multi-az/
- [ちょっと待って！Auroraを使う時にMulti-AZが本当に必要ですか？ ｜ Developers.IO](https://dev.classmethod.jp/cloud/aws/decision-method-for-aurora-multiaz/ "ちょっと待って！Auroraを使う時にMulti-AZが本当に必要ですか？ ｜ Developers.IO")

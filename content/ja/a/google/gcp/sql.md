---
title: "Cloud SQL"
linkTitle: "SQL"
description: https://cloud.google.com/sql
date: 2020-05-18T16:04:01+09:00
weight: 800
---

## Tools
### Cloud SQL Proxy

Cloud SQL第2世代インスタンスにアクセスできる公式のプロキシサーバ。

Getting Started:

- [Cloud SQL Proxy について | Cloud SQL for MySQL | Google Cloud](https://cloud.google.com/sql/docs/mysql/sql-proxy?hl=ja)
- [Cloud SQL Proxy を使用して MySQL クライアントを接続する | Cloud SQL for MySQL](https://cloud.google.com/sql/docs/mysql/connect-admin-proxy?hl=ja)

#### 仕様

接続文字列 `INSTANCE_CONNECTION_NAME`

例:

```
myproject:myregion:myinstance
```

#### プライベートIPでの接続

https://cloud.google.com/sql/docs/mysql/connect-admin-proxy?hl=ja#private-ip

- プロキシがそのインスタンスと同じVPCネットワークにアクセスできるリソース上にある必要がある
- インスタンスにパブリックIPとプライベートIPの両方が設定されているときは、 `-ip_address_types=PRIVATE` オプションを指定する

#### systemd対応

下の記事にあるように、SystemdのTemplate Unit Filesを使うと、1台で複数のDBに接続したいときに便利。

参考:

- [Cloud SQL Proxy (TCP Socket)を systemd で起動させる - Qiita](https://qiita.com/kumanoryo/items/ef3fbec70b4138ffe1c2)
- [systemd#Template Unit Files]({{<ref "/a/software/systemd/_index.md">}}#template-unit-files)

## Topics
### 外部IPアドレス
第2世代のインスタンスのIPアドレスはデフォルトで固定。

https://cloud.google.com/sql/docs/mysql/connect-external-app

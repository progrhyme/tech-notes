---
title: "ユーザ管理"
linkTitle: "ユーザ管理"
date: 2020-07-03T16:24:55+09:00
weight: 2700
---

## getent

```sh
getent group <group> # グループに属しているユーザをリスト
```

参考:

- [Linuxコマンドでユーザーのグループ確認・変更。 - Qiita](https://qiita.com/niiyz/items/53aa4195dcc69db2052b)

## gpasswd

```bash
gpasswd -a <login> <group> # ユーザをグループに所属させる
gpasswd -d <login> <group> # ユーザをグループから削除
```

参考:

- [【 gpasswd 】コマンド――ユーザーが所属するグループを管理する：Linux基本コマンドTips（72） - ＠IT](http://www.atmarkit.co.jp/ait/articles/1612/12/news016.html "【 gpasswd 】コマンド――ユーザーが所属するグループを管理する：Linux基本コマンドTips（72） - ＠IT")

## groupadd

グループ作成。

```bash
groupadd newgroup
```

参考:

- [Linuxコマンド【 groupadd 】新規グループの作成 - Linux入門 - Webkaru](https://webkaru.net/linux/groupadd-command/ "Linuxコマンド【 groupadd 】新規グループの作成 - Linux入門 - Webkaru")

## passwd

```bash
passwd -l <login> # アカウントをロック
passwd -u <login> # アンロック
```

ロックされたアカウントはログインできず、利用不可になる。

参考:

- [Linux ユーザーアカウントをロック・アンロックする](http://kazmax.zpp.jp/linux/account_lock.html "Linux ユーザーアカウントをロック・アンロックする")

## useradd

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

## usermod

```bash
usermod -g admin <login> # 主グループを変更
usermod -aG ops,app,... <login> # 副グループ追加
```

参考:

- [usermodコマンドについて詳しくまとめました 【Linuxコマンド集】](https://eng-entrance.com/linux-command-usermod "usermodコマンドについて詳しくまとめました 【Linuxコマンド集】")

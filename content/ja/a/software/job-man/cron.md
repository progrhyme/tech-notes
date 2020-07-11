---
title: "cron"
linkTitle: "cron"
date: 2020-07-11T17:03:05+09:00
weight: 50
---

## About

UNIX系OSで古くから使われる常駐デーモンで、設定したスケジュールに従って、プログラムを定期実行するもの。

参考:

- [cronとは - IT用語辞典 e-Words](http://e-words.jp/w/cron.html)

## Spec

POSIXで規定されている。

See https://pubs.opengroup.org/onlinepubs/9699919799/utilities/crontab.html#tag_20_25_07

## Tools

- https://crontab.guru/
  - CRON構文チェッカー兼ジェネレーター

## Pitfalls

cronあるあるなトラブル事例などについて。

- `crontab -r` で消してしまう事案
- cronの書式を間違えて起動しない
- STDOUT, STDERR垂れ流しでログが出まくる
- ジョブの多重起動
- crontabを設定したマシンが死んでしまい、crontabの内容を復旧できない

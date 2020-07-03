---
title: "プロセス管理"
linkTitle: "プロセス管理"
date: 2020-07-03T16:25:04+09:00
weight: 2550
---

## kill(1)

[Man page of KILL](https://linuxjm.osdn.jp/html/util-linux/man1/kill.1.html)

Examples:

```sh
# シグナル名のリストを表示
kill -l

# プロセスにSIGTERMを送信
kill <PID>...

# SIGHUPを送信
kill -HUP <PID>...

# プロセスの生存確認
kill -0 <PID>
```

NOTE:

- macOSだと少しオプションが違うかも
- シェルのビルトインと /bin/kill でも少しオプションが違う

See Also:

- [OS > Linux#Signal]({{<ref "/a/os/linux/_index.md">}}#signal)

参考:

- [kill Man Page - macOS - SS64.com](https://ss64.com/osx/kill.html)
- [killでプロセスに「0」を送ると、プロセスの生存確認ができる - Perl日記](http://r9.hateblo.jp/entry/2018/01/15/193444)

## pgrep

プロセス名で検索して該当するプロセス番号を表示。

Examples:

```sh
pgrep perl
```

## pkill

プロセス名で指定してシグナルを送信する。

Examples:

```sh
pkill perl
```

## ps

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

## trap

シグナルによってプロセスが中断・停止させられたときに、実行するコマンドを指定する。

Syntax:

```sh
trap 'コマンド' シグナルリスト
```

Examples:

```sh
trap 'echo trapped.' 1 2 3 15

# trapをリセットする
trap 1 2 3 15
```

NOTE:

- SIGKILL (9) はtrapできない

See Also:

- [OS > Linux#Signal]({{<ref "/a/os/linux/_index.md">}}#signal)

参考:

- [シグナルと trap コマンド | UNIX &amp; Linux コマンド・シェルスクリプト リファレンス](https://shellscript.sunone.me/signal_and_trap.html)
- [shellのtrapについて覚え書き - Qiita](https://qiita.com/ine1127/items/5523b1b674492f14532a)
- [trap コマンド | コマンドの使い方(Linux) | hydroculのメモ](https://hydrocul.github.io/wiki/commands/trap.html)

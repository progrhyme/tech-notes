---
title: "journalctl"
linkTitle: "journalctl"
description: Query the systemd journal
date: 2020-05-18T16:16:57+09:00
---

https://www.freedesktop.org/software/systemd/man/journalctl.html

systemdのログをクエリするためのCLI.

Examples:

```sh
# tail -f する
journalctl -f
# 最新のログを表示
journalctl -e
# ユニット(sshd, httpd, etc.)を指定
journalctl -u ユニット名
```

参考:

- [journalctl 最低限覚えておくコマンド - Qiita](http://qiita.com/aosho235/items/9fbff75e9cccf351345c)

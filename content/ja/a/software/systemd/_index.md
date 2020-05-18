---
title: "systemd"
linkTitle: "systemd"
description: System and Service Manager
date: 2020-05-18T16:14:32+09:00
---

https://www.freedesktop.org/wiki/Software/systemd/

昨今のLinuxのinit（最初に起動するプログラム）としてほぼデファクトになっているソフトウェア。

## Configuration
### systemd.unit

https://www.freedesktop.org/software/systemd/man/systemd.unit.html

#### Template Unit Files

コマンドとかほぼ同じなんだけど、パラメータの異なるServiceを複数動かしたいようなときに使う。

参考:

- [systemdのユニットファイルをテンプレート化する - redj’s blog](https://redj.hatenablog.com/entry/2020/02/08/180950)

## systemctl

CLI

https://www.freedesktop.org/software/systemd/man/systemctl.html

### daemon-reload

https://www.freedesktop.org/software/systemd/man/systemctl.html#daemon-reload

configと全unit fileを再読込みする。

```sh
systemctl daemon-reload
```

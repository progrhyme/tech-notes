---
title: "Linux"
linkTitle: "Linux"
date: 2020-05-21T21:32:53+09:00
weight: 400
---

## About

[Linux（リナックス）とは - IT用語辞典 e-Words](http://e-words.jp/w/Linux.html)によれば、「世界で最も普及している、オープンソースのOS」。

- [The Linux Kernel Archives](https://www.kernel.org/)
- [The Linux Foundation – Supporting Open Source Ecosystems](https://www.linuxfoundation.org/)
- [Linux.org](https://www.linux.org/)

## Kernel
### Signal

[Man page of SIGNAL](http://linuxjm.osdn.jp/html/LDP_man-pages/man7/signal.7.html)

プロセス間通信の仕組みの1つ。

シグナルの一部:

 番号 | シグナル名
------|------------
 1 | HUP
 2 | INT
 3 | QUIT
 9 | KILL
 10 | USR1
 11 | SEGV
 13 | PIPE
 14 | ALRM
 15 | TERM
 17 | CHLD
 18 | CONT

シグナルの一覧は `kill -l` などのコマンドで確認できる。

See Also:

- [UNIX系コマンド#kill(1)]({{<ref "/a/cli/unix-cmd/_index.md">}}#kill1)

参考:

- [シグナル (Unix) - Wikipedia](https://ja.wikipedia.org/wiki/%E3%82%B7%E3%82%B0%E3%83%8A%E3%83%AB_(Unix))
- [UNIXシグナル一覧 CapmNetwork](http://capm-network.com/?tag=UNIX%E3%82%B7%E3%82%B0%E3%83%8A%E3%83%AB%E4%B8%80%E8%A6%A7)

### Process
#### Exit Code

予約済みExit Codes:

| Code | Meaning | 備考 |
|---------|-------------|--------|
| 1 | エラー全般 | |
| 2 | シェルビルトイン関数の誤用 | |
| 126 | コマンド実行不可 | |
| 127 | command not found | |
| 128 | exitに不正な引数 | |
| 128+n | シグナル n で致命的エラー | KILL => 137, TERM => 143 |
| 130 | Ctrl-C | |
| 255* | 範囲外のステータス | |

参考:

- [Exit Codes With Special Meanings](http://tldp.org/LDP/abs/html/exitcodes.html "Exit Codes With Special Meanings")
- [コマンドラインツールを書くなら知っておきたい Bash の 予約済み Exit Code - Qiita](https://qiita.com/Linda_pp/items/1104d2d9a263b60e104b "コマンドラインツールを書くなら知っておきたい Bash の 予約済み Exit Code - Qiita")

## 仕様
### ブートシーケンス

参考:

- [Linuxのブートシーケンス - Qiita](https://qiita.com/taichitk/items/b3b69705be0e270e9f6e)

### ファイルパーミッション

参考:

- [Linux: SUID、SGID、スティッキービットまとめ - Qiita](https://qiita.com/aosho235/items/16434a490f9a05ddb0dc)
- [【コマンド含め一通りわかる】Linuxパーミッションについてのまとめ](https://eng-entrance.com/category/linux/linux-permission)
  - [【Linux初心者向け】スティッキービットとは？と設定方法](https://eng-entrance.com/linux-permission-stickybit)
  - [【初心者でもすぐわかる】SUIDとは？と設定方法](https://eng-entrance.com/linux-permission-suid)
  - [【Linuxパーミッション】SGIDとは？と設定方法](https://eng-entrance.com/linux-permission-sgid)

#### umask

ファイル、ディレクトリ作成時のパーミッションは、umask値によって異なる。

基本値:

- ファイル: `666`
- ディレクトリ: `777`

「（基本値） - （umask値）」がデフォルトのパーミッションとなる。

例:

- umask = `022` のとき
  - ディレクトリ作成 => パーミッションは `755`
  - ファイル作成 => パーミッションは `644`

関連項目:

- [UNIX系コマンド#umask]({{<ref "/a/cli/unix-cmd/_index.md">}}#umask)

参考:

- [Linuxのファイル・ディレクトリ作成した時のパーミッション (umask) - Qiita](https://qiita.com/yuki2006/items/3774bf765eb5ef7deabc)

## セキュリティ
### SELinux

RHEL系の機能かな（？）

- [SELinuxの無効化 - Qiita](https://qiita.com/hanaita0102/items/5d3675e4dc1530b255ba "SELinuxの無効化 - Qiita")
- [5.4. SELinux の有効化および無効化 - Red Hat Customer Portal](https://access.redhat.com/documentation/ja-jp/red_hat_enterprise_linux/6/html/security-enhanced_linux/sect-security-enhanced_linux-working_with_selinux-enabling_and_disabling_selinux "5.4. SELinux の有効化および無効化 - Red Hat Customer Portal")

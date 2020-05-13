---
title: "Zsh"
linkTitle: "Zsh"
date: 2020-04-28T00:14:04+09:00
weight: 900
---

http://www.zsh.org/

## Documentation

- [zsh: The Z Shell Manual](http://zsh.sourceforge.net/Doc/Release/)

## Source Code

- https://sourceforge.net/p/zsh/code/ci/master/tree/
- https://github.com/zsh-users/zsh ... Mirror

## Configuration

```zsh
# history -i でコマンドの実行時間表示
setopt extended_history
```

参考:

- [Unix 系 OS でコマンド実行間にタイムスタンプを付ける](https://orumin.blogspot.com/2017/10/unix-os.html)

### プロンプト
#### vcs_info

メモ:

- `check-for-changes` をtrueにしても、まだgitの管理下にない新規ファイルがあるだけだと `stagedstr` にも `unstagedstr` にも表れない。

参考:

- [zsh/vcs_info-examples at master · zsh-users/zsh](https://github.com/zsh-users/zsh/blob/master/Misc/vcs_info-examples)
- [zshのターミナルにリポジトリの情報を表示してみる · けんごのお屋敷](http://tkengo.github.io/blog/2013/05/12/zsh-vcs-info/)
- [Show Git State in ZSH Prompt via vcs_info | Timothy Basanov](https://timothybasanov.com/2016/04/23/zsh-prompt-and-vcs_info.html)

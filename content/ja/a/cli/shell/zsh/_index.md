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
- [zsh 設定 - プロンプト -](http://tegetegekibaru.blogspot.com/2012/08/zsh_2.html)

### プロンプト

参考:

- [zshプロンプトのカスタマイズ - Qiita](https://qiita.com/yamagen0915/items/77fb78d9c73369c784da)

#### プロンプトの種類

 プロンプト | 説明
----------|------
 PROMPT  | 左プロンプト
 RPROMPT | 右プロンプト
 SPROMPT | correctで訂正の候補を出すときに表示されるプロンプトです
 PROMPT2, RPOMPT2 | コマンドが複数行になった時に表示されるプロンプトです
 PROMPT3 | ?
 PROMPT4 | ?

#### 特殊文字

 文字 | 出力内容 | 例
-----|---------|----
 %n | ユーザー名 | root
 %# | ユーザー種別 | #（rootのとき）<br />%（root以外）
 %m | ホスト名 | localhost
 %d, %/ | カレントディレクトリ | /home/me/dir
 %~ | カレントディレクトリ | ~/dir
 %C | カレントディレクトリ | dir
 %T | 時間 (HH:MM) |
 %* | 時間 (HH:MM:SS) |
 %D | 日付 (YY-MM-DD) |

#### 色

こんな感じで色を付けられれる。

```sh
# ①依存なし
PROMPT='%F{cyan} $n %f'

# ②colorsを使う
autoload -Uz colors
colors

PROMPT='%{${fg[cyan]}%} $n %{${reset_color}%}'
```

色の文字か番号で色を指定できる。

 番号 | 色
-----|----
 0 | black
 1 | red
 2 | green
 3 | yellow
 4 | blue
 5 | magenta
 6 | cyan
 7 | white

参考:

- [zshでプロンプトをカラー表示する - Qiita](https://qiita.com/mollifier/items/40d57e1da1b325903659)

#### 色: 256色対応

参考:

- [zshのプロンプトを256色表示にする＋好きなフォーマットで時刻表示 - Qiita](https://qiita.com/butaosuinu/items/770a040bc9cfe22c71f4)

NOTE:

- （2020-05-19）上のZshパラメータを使う方法がUbuntu 18.04デスクトップ環境 + 端末アプリだと上手く行ってない

#### 複数行対応

左側のPROMPTなら改行文字を入れればいいが、 `precmd()` でプリントするという手もある。  
`print -P` オプションを付けると、PROMPTのフォーマットで出力できるみたい。

参考:

- [zsh の右プロンプトを2行にする - Qiita](https://qiita.com/eexiech8aNahShee/items/355cd4d884ce03656285)
- [prompt - Multiline RPROMPT in zsh - Super User](https://superuser.com/questions/974908/multiline-rprompt-in-zsh)

#### vcs_info

メモ:

- `check-for-changes` をtrueにしても、まだgitの管理下にない新規ファイルがあるだけだと `stagedstr` にも `unstagedstr` にも表れない。

参考:

- [zsh/vcs_info-examples at master · zsh-users/zsh](https://github.com/zsh-users/zsh/blob/master/Misc/vcs_info-examples)
- [zshのターミナルにリポジトリの情報を表示してみる · けんごのお屋敷](http://tkengo.github.io/blog/2013/05/12/zsh-vcs-info/)
- [Show Git State in ZSH Prompt via vcs_info | Timothy Basanov](https://timothybasanov.com/2016/04/23/zsh-prompt-and-vcs_info.html)

## Child Pages

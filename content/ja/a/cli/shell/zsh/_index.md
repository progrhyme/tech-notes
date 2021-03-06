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

## Syntax
### 配列

Bashと違って、配列の添字が `1` から始まることに注意が必要。

```sh
a=(x y z)
echo $a[1] #=> x
echo $a[2] #=> y
```

参考:

- [zsh の配列操作の基本から応用まで - Qiita](https://qiita.com/mollifier/items/f897b3fddd2d10369333)

## Configuration

```zsh
# history -i でコマンドの実行時間表示
setopt extended_history
```

参考:

- [Unix 系 OS でコマンド実行間にタイムスタンプを付ける](https://orumin.blogspot.com/2017/10/unix-os.html)
- [zsh 設定 - プロンプト -](http://tegetegekibaru.blogspot.com/2012/08/zsh_2.html)

### Options

http://zsh.sourceforge.net/Doc/Release/Options.html

`setopt`, `unsetopt` はPOSIXの `set +/-o` の代わりにzshoptionsの設定に用いることができる。 `set +/-o` も使えるみたい。

Examples:

```sh
setopt shwordsplit # 他のシェルと文字列変数の分割方法を揃える
setopt ksharrays   # 配列の添字を0から始める
```

参考:

- [zshoptions(1): zsh options - Linux man page](https://linux.die.net/man/1/zshoptions)
- [スクリプト言語としてみた各POSIXシェルの特徴と互換性上の注意点まとめ - Qiita](https://qiita.com/ko1nksm/items/8d28d4f7cb2c325c00fa#-zsh---z-shell)

#### emulate

他のシェルと互換性のあるモード。色んなオプションがセットされる。

```sh
emulate -R sh  # POSIX shに近いモード
emulate -R ksh # ksh (bash) に近いモード
```

参考:

- [zsh でシェルスクリプトを書くときの留意点 - 拡張 POSIX シェルスクリプト Advent Calendar 2013 - ダメ出し Blog](https://fumiyas.github.io/2013/12/03/zsh-scripting.sh-advent-calendar.html)

### helpコマンド

[Zsh - ArchWiki#ヘルプコマンド](https://wiki.archlinux.jp/index.php/Zsh#.E3.83.98.E3.83.AB.E3.83.97.E3.82.B3.E3.83.9E.E3.83.B3.E3.83.89)より。

> Bashとは違って、Zshは組み込まれている `help` コマンドを有効にしていません。Zshでhelpを使うには、以下をzshrcに追加してください:

```sh
autoload -U run-help
autoload run-help-git
autoload run-help-svn
autoload run-help-svk
unalias run-help
alias help=run-help
```


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

Examples:

```sh
# Zshパラメータ利用
# - %F{文字色番号}
# - %K{背景色番号}
# - %f ... 文字色リセット
# - %k ... 背景色リセット
PROMPT="%K{082}%F{001}[%n@%m]%f%k"

# エスケープシーケンス利用
PROMPT=$'%{\e[30;48;5;082m%}%{\e[38;5;001m%}[%n@%m]%{\e[0m%}'
```

- 上2つはどちらも同じ効果を表す
- エスケープシーケンスについては See [シェル#ANSIエスケープシーケンス]({{<ref "/a/cli/shell/_index.md">}}#ansiエスケープシーケンス)

参考:

- [zshのプロンプトを256色表示にする＋好きなフォーマットで時刻表示 - Qiita](https://qiita.com/butaosuinu/items/770a040bc9cfe22c71f4)

MEMO:

- （2020-05-19）上のZshパラメータを使う方法がUbuntu 18.04デスクトップ環境 + 端末アプリだと上手く行ってない
- （2020-05-24）macOS + iTerm2なら上手く行った^

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

## Feature
### ZLE

[Zsh Line Editor](http://zsh.sourceforge.net/Doc/Release/Zsh-Line-Editor.html).

Zshのコマンドライン編集機能。

たぶん、peco等でキーボードショートカットを作るときに使う人が多いのではないかな。

Examples:

```sh
# 編集を終了し、入力されたコマンドを実行する
zle accept-line
# 画面をクリアする
zle clear-screen
```

参考:

- [コマンドライン編集機能 Zsh Line Editor を使いこなす - Qiita](https://qiita.com/b4b4r07/items/8db0257d2e6f6b19ecb9)

## Tools

パッケージ管理ツールについては、[シェル > パッケージ管理]({{<ref "/a/cli/shell/pkg-man.md">}})参照。

### Packages / Plugins

- https://github.com/zsh-users/zsh-syntax-highlighting
  - fish shellのようなシンタックスハイライトを提供してくれる
  - See [2020-05-22#Ubuntu 18.04でzsh-syntax-highlightingを入れた]({{<ref "20200522.md">}}#ubuntu-1804でzsh-syntax-highlightingを入れた)

## Child Pages

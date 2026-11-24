# Starship

公式サイト: https://starship.rs/

## About

Rust 製の、シェル共通のプロンプト。公式サイトの紹介文（訳）は、「最小限で高速、かつ無限にカスタマイズできる、任意のシェル向けのプロンプト」。ライセンスは ISC。

- 対応シェル: Bash、Zsh、fish、PowerShell、Nushell、Xonsh など。
- 設定は、TOML ファイル 1 つに書く。シェルごとの設定は要らない。
- カレントディレクトリの内容に応じて、必要な情報だけを出す（Git のブランチ、言語のバージョン、環境変数など）。
- 公式ガイドは、Nerd Font を入れて、ターミナルで有効にするよう案内している。

参考:

- [公式ガイド](https://starship.rs/guide/)
- [設定のリファレンス](https://starship.rs/config/)
- ソースコード: https://github.com/starship/starship

## Getting Started

macOS では、Homebrew で入れる。

```sh
brew install starship
```

シェルの設定ファイルの末尾で、有効にする。

```zsh
# ~/.zshrc
eval "$(starship init zsh)"
```

Bash は `eval "$(starship init bash)"`、fish は `starship init fish | source` を、それぞれの設定ファイルに書く。

設定ファイルは、`~/.config/starship.toml` を読む。場所は、環境変数 `STARSHIP_CONFIG` で変えられる。

```sh
# 別のファイルで、プロンプトの見た目を試す
STARSHIP_CONFIG=/path/to/starship.toml zsh
```

## Usage

### 設定の基本

プロンプト全体の書式は、トップレベルの `format` に書く。既定は `$all` で、有効なモジュールをすべて並べる。`format` に書いたモジュールだけが表示されるので、表示を絞りたいときは、必要なものだけを並べる。

```toml
add_newline = false

format = """
$directory\
$git_branch\
$git_status\
$character"""
```

| キー | 内容 |
| :--- | :--- |
| `format` | プロンプトの書式。`$モジュール名` で、モジュールを並べる |
| `right_format` | 右側に出す内容。既定は空 |
| `add_newline` | プロンプトの前に空行を入れるか。既定は `true` |
| `command_timeout` | Starship が実行するコマンドの制限時間。既定は 500 ミリ秒 |

モジュールごとの設定は、`[モジュール名]` のテーブルに書く。見た目は `style` で指定する。`fg:black bg:blue` のように、前景色と背景色を書ける。

### 確認用のコマンド

```sh
starship prompt             # 左側のプロンプトを出力する
starship prompt --right     # 右側のプロンプトを出力する
starship explain            # 今のプロンプトの内訳を表示する
```

`env_var` モジュールなど、環境変数を読むモジュールを試すときは、コマンドの前に環境変数を付けて実行する。

```bash
MY_VALUE="sample" starship prompt
```

### directory

カレントディレクトリを出すモジュール。

| キー | 内容 |
| :--- | :--- |
| `truncation_length` | 親ディレクトリを何階層まで出すか。既定は 3 |
| `truncate_to_repo` | Git リポジトリのルートまでで切り詰めるか。既定は `true` |
| `fish_style_pwd_dir_length` | 0 でないとき、切り詰める部分を、指定の文字数で表示する |

`fish_style_pwd_dir_length = 1` にすると、fish のように、親ディレクトリを 1 文字に縮められる。公式の例では、`rock/and/roll` を残して、前の部分を `/b/t/c/o/` のように縮めている。

### git_branch、git_status

`git_status` は、変更の状態を、記号で出す。記号は、キーごとに変えられる。

| キー | 既定の記号 | 状態 |
| :--- | :--- | :--- |
| `conflicted` | `=` | 競合 |
| `ahead` | `⇡` | リモートより進んでいる |
| `behind` | `⇣` | リモートより遅れている |
| `diverged` | `⇕` | 分岐している |
| `untracked` | `?` | 追跡されていないファイル |
| `modified` | `!` | 変更あり |
| `staged` | `+` | ステージ済み |
| `deleted` | `✘` | 削除 |

### env_var

環境変数の値を出すモジュール。`[env_var.名前]` のテーブルを、複数書ける。

```toml
[env_var.MY_VALUE]
variable = "MY_VALUE"
format = "[ $env_value ](bg:cyan fg:black)"
```

シェル関数の結果を出したいときは、プロンプトを描く前に、関数で環境変数を export しておくと、このモジュールで出せる。

### custom

コマンドの出力を出すモジュール。`[custom.名前]` のテーブルに書く。

| キー | 内容 |
| :--- | :--- |
| `command` | 出力を表示するコマンド |
| `when` | 終了ステータスが 0 のときだけ表示する、条件のコマンド |
| `format` | 書式。`$output`、`$symbol`、`$style` が使える |
| `symbol`、`style` | 記号と見た目 |

## 注意点

2026-11-25 時点で、バージョン 1.27.0 を使って確かめたことを書く。

### zsh の RPROMPT が上書きされる

`starship init zsh` は、`right_format` を設定していなくても、`RPROMPT` を上書きする。`.zshrc` に書いた `RPROMPT` の時刻などは、消える。

右側に出したいものは、Starship の `right_format` で出す。時刻なら `time` モジュールを使う。

```toml
right_format = "$time"

[time]
disabled = false
time_format = "%T"
style = "fg:247"
format = "[$time]($style)"
```

### env_var は、変数が空でも書式を出す

環境変数が空文字で定義されていると、`env_var` モジュールは、値が空のまま書式を出す。記号だけが残る。モジュールごと消したいときは、空にせず、`unset` する。

### custom のコマンドは別プロセスで動く

`custom` の `command` と `when` は、別のプロセスで実行される。シェルの関数と、export していないシェル変数は、見えない。

### powerline の矢印は、エスケープで書く

powerline の矢印（U+E0B0。私用領域の文字）は、貼り付けやツールを通すと、欠けることがある。TOML の文字列では、`"\ue0b0"` のエスケープで書ける。Git のブランチの記号（U+E0A0）も、`"\ue0a0"` と書く。

## agnoster 風の設定

Oh My Zsh の agnoster テーマのように、背景色付きの矢印でセグメントを区切る設定。セグメントは、背景色付きの1区画のこと。矢印などの区切りの記号は、powerline 用の記号を含むフォントが要る。

```toml
add_newline = false

format = """
$hostname\
$directory\
$git_branch\
$git_status\
${custom.dir_end}\
$character"""

# 後ろにセグメントが続くときだけ矢印が出るよう、前のセグメントが矢印を持つ
[hostname]
ssh_only = true
format = "[ $hostname ](bg:white fg:black)[\ue0b0](fg:white bg:blue)"

[directory]
truncation_length = 1
fish_style_pwd_dir_length = 1
truncate_to_repo = false
style = "bg:blue fg:black"
format = "[ $path ]($style)"

[git_branch]
symbol = "\ue0a0"
style = "bg:green fg:black"
format = "[\ue0b0](fg:blue bg:green)[ $symbol $branch ]($style)"

# 閉じ矢印は括弧の外に置く。このモジュールは Git リポジトリ内でしか動かないため、
# 状態が空でも、矢印は出る
[git_status]
style = "bg:green fg:black"
format = "([$all_status$ahead_behind ]($style))[\ue0b0](fg:green)"
staged = "●"
modified = "✚"
untracked = "…"

# Git リポジトリの外での、パスの閉じ矢印
[custom.dir_end]
when = "! git rev-parse --is-inside-work-tree >/dev/null 2>&1"
# format で $output を使わないため、command は何でもよい。
# バージョン 1.27.0 では、出力が空でも、symbol は表示された
command = "true"
symbol = "\ue0b0"
style = "fg:blue"
format = "[$symbol]($style)"

[character]
format = " "
```

- セグメントの間の矢印は、直後のセグメントが表示されるときだけ出したい。そこで、前のセグメントが、矢印を持つ。
- Git リポジトリの内か外かで、最後のセグメントが変わる。内は `git_status` が、外は `custom.dir_end` が、閉じ矢印を出す。
- agnoster は、変更の有無で Git のセグメントの背景色（緑と黄）を変える。Starship の `style` は、状態では切り替わらないので、緑に固定して、状態は記号で示している。

参考:

- [2026-11-25 のメモ](../../memo/2026/20261125.md)
- [Oh My Zsh](zsh/ohmyzsh.md)

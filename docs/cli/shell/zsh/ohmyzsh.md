---
date: '2020-05-16T09:12:08+09:00'
description: https://ohmyz.sh/
---

# Oh My Zsh

## About
OSSのZshコンフィグレーションフレームワーク。

- ソースコード: https://github.com/ohmyzsh/ohmyzsh

## Getting Started

- Install ... ソースコードのREADME.mdの通り。
- Documents: [GitHub Wiki](https://github.com/ohmyzsh/ohmyzsh/wiki)
    - [Themes](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes)
    - [Plugins](https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins)

## Usage
### Update

https://github.com/ohmyzsh/ohmyzsh#getting-updates

2, 3週間に1回ぐらいシェル上でアップグレードのチェックが掛かるらしい。  
または、 `upgrade_oh_my_zsh` を実行すると手動アップデートが可能。

## Custom Plugins

サードパーティー製のプラグイン。

`$ZSH_CUSTOM` or `${oh-my-zshのインストールディレクトリ}/custom` 以下に配置すればよさそう。

### zsh-autosuggestions

https://github.com/zsh-users/zsh-autosuggestions

fishみたいにhistoryから自動補完を効かせてくれるやつ。

参考:

- [2020-05-16#zsh-autosuggestionsをインストールして設定](../../../memo/2020/20200516.md#zsh-autosuggestionsをインストールして設定)

## 暗黙で有効になる設定

`oh-my-zsh.sh` は、`lib/` 配下のファイルを読み込み、`.zshrc` に書いていない設定も有効にする。外すと、これらが無効になる。

!!! note
    次の内容は、素の `.zshrc` で確かめた。確かめた条件を、次に示す。バージョン、テーマ、プラグインによって、結果は変わりうる。

    - 日付とバージョン: 2026-11-25 時点の Oh My Zsh（`master`）と、zsh 5.9。macOS。
    - Oh My Zsh あり: `.zshrc` に、`ZSH`、`ZSH_CACHE_DIR`、自動更新の無効化（`zstyle ':omz:update' mode disabled`）と、`source $ZSH/oh-my-zsh.sh` だけを書く。`ZSH_THEME` と `plugins` は、書かない。
    - Oh My Zsh なし: `.zshrc` を、空にする。
    - 比べ方: どちらも、設定ファイルのない `HOME` で、対話シェルとして起動し、起動後の `setopt`、`bindkey`、`alias`、環境変数を出力して、差分を取る。

### setopt

`setopt` が出力するのは、既定値と違うオプションだけ。次のオプションは、Oh My Zsh ありのときだけ出力された。

| オプション | 内容 |
| :--- | :--- |
| `auto_cd` | ディレクトリ名だけを入力すると、`cd` する |
| `auto_pushd` | `cd` で自動的に `pushd` する |
| `pushd_ignore_dups` | `pushd` で、重複するディレクトリを積まない |
| `pushd_minus` | `cd -N` の向きを逆にする |
| `share_history` | 複数のシェルでヒストリを共有する |
| `extended_history` | 履歴に、実行した時刻を記録する |
| `hist_ignore_dups` | 直前と同じコマンドを、履歴に残さない |
| `hist_ignore_space` | 空白で始まるコマンドを、履歴に残さない |
| `hist_expire_dups_first` | 履歴が上限を超えたら、重複を先に削除する |
| `hist_verify` | 履歴展開（`!!` など）を、実行前に確認する |
| `always_to_end` | 補完後に、カーソルを語の末尾へ移す |
| `complete_in_word` | 語の途中でも補完する |
| `interactive_comments` | 対話シェルでも、`#` のコメントを許可する |
| `long_list_jobs` | ジョブの通知を、長い形式で出す |
| `no_flow_control` | `Ctrl-S`、`Ctrl-Q` のフロー制御を無効にする |
| `prompt_subst` | プロンプトの中で、変数展開とコマンド置換をする |

`.zshrc` に `setopt no_share_history` と書いても、その後で `oh-my-zsh.sh` を読み込むと、`share_history` に戻る。設定の効き方は、読み込みの順番で決まる。

### 履歴の変数

| 変数 | Oh My Zsh なし | あり |
| :--- | ---: | ---: |
| `HISTSIZE` | 2000 | 50000 |
| `SAVEHIST` | 1000 | 10000 |

### キーバインド

補完の初期化（`compinit`）が追加するキーバインドは、Oh My Zsh の分から除いた。`compinit` だけを書いた `.zshrc` とも比べて、切り分けた。

| キー | Oh My Zsh なし（zsh の既定） | あり |
| :--- | :--- | :--- |
| `↑`、`↓` | `up-line-or-history`、`down-line-or-history` | 入力済みの先頭文字で、履歴を絞り込む（`up-line-or-beginning-search`、`down-line-or-beginning-search`） |
| `Ctrl-←`、`Ctrl-→` | 未割り当て | `backward-word`、`forward-word` |
| `Ctrl-Delete` | 未割り当て | `kill-word` |
| `PageUp`、`PageDown` | 未割り当て | `up-line-or-history`、`down-line-or-history` |
| `Shift-Tab` | 未割り当て | `reverse-menu-complete` |
| `Space` | 通常の入力 | `magic-space`（履歴展開を、入力時に展開する） |
| `Ctrl-X Ctrl-E` | 未割り当て | `edit-command-line` |
| `Alt-m` | 未割り当て | `copy-prev-shell-word` |
| `Alt-l` | `down-case-word` | `ls` を実行する |
| `Alt-w` | `copy-region-as-kill` | `kill-region` |

`Delete`（`^[[3~`）は、Oh My Zsh がなくても、`delete-char` に割り当てられていた。

### エイリアス

Oh My Zsh なしでは、`alias` の出力は 2 件だった。Oh My Zsh ありでは、次の 26 件が増える。

| 種類 | エイリアス |
| :--- | :--- |
| ディレクトリの移動 | `..` を含む `...`、`....`、`.....`、`......`（上位ディレクトリへ移動）、`-`（`cd -`）、`1` から `9`（`cd -1` から `cd -9`） |
| `ls` | `ls`（`ls -G`）、`l`、`lsa`（`ls -lah`）、`la`（`ls -lAh`）、`ll`（`ls -lh`） |
| `grep` | `grep`（`--color=auto` と、`.git` などの `--exclude-dir`）、`egrep`（`grep -E`）、`fgrep`（`grep -F`） |
| その他 | `_`（`sudo `）、`md`（`mkdir -p`）、`rd`（`rmdir`）、`history`（関数 `omz_history`） |

### 環境変数

`PAGER` と `LESS` が export されていないときだけ、`PAGER=less`、`LESS=-R` を設定する（`less` がなければ `PAGER=more`）。

## Theme: agnoster

テーマは、`ZSH_THEME` で選ぶ。agnoster は、背景色付きの矢印（powerline の記号）で、セグメントを区切るテーマ。powerline 対応のフォントが要る。

- `build_prompt` 関数が、`prompt_status`、`prompt_segment`、`prompt_git`、`prompt_end` を呼んで、プロンプトを組み立てる。
- `PROMPT='%{%f%b%k%}$(build_prompt) '` のように、`PROMPT` から `build_prompt` を呼ぶ。
- `build_prompt` を、自分の定義で上書きすると、セグメントを入れ替えられる。
- `prompt_segment` と `prompt_end` を、自分の関数から呼ぶと、同じ見た目のセグメントを、別の行に出せる。

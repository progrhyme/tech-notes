---
date: '2026-11-21'
description: https://github.com/anyenv/anyenv
---

# anyenv

`**env` 系のバージョン管理ツール(rbenv、pyenv、nodenv など)をまとめて導入・管理するツール。

- Source: https://github.com/anyenv/anyenv
- 導入できる `**env` の定義: https://github.com/anyenv/anyenv-install

## 管理できるもの

`anyenv install --list` で、導入できる `**env` の一覧が出る。主なもの:

| ツール | 管理する対象 |
| :--- | :--- |
| nodenv | Node.js |
| pyenv | Python |
| rbenv | Ruby |
| goenv | Go |
| jenv | Java |
| tfenv | Terraform |
| plenv | Perl |
| phpenv | PHP |

- 一覧には、他に denv、erlenv、exenv、hsenv、jlenv、kubectlenv、luaenv、sbtenv、scalaenv、swiftenv、Renv、crenv などがある(2026-11 時点)。
- 導入した `**env` は、`~/.anyenv/envs/` の下に置かれる。

## Getting Started

macOS の場合は、[Homebrew](brew.md) で入れられる。

```sh
brew install anyenv
```

初期化して、シェルの設定に `anyenv init -` を足す。

```sh
anyenv install --init   # 定義(anyenv-install)の取得。初回のみ
```

```sh
# .zshrc などに追記
eval "$(anyenv init -)"
```

- `anyenv init -` は、導入済みの `**env` の初期化も、まとめて行う。個別の `**env` の初期化を、シェルの設定に書かなくてよい。
- `anyenv install --init` は、`~/.config/anyenv/anyenv-install` に定義を clone する。実行前に確認を求められる(対話式)。

## Usage

```sh
anyenv install --list      # 導入できる **env の一覧
anyenv install nodenv      # nodenv を導入する
anyenv install --init      # 定義(anyenv-install)を取得する
anyenv versions            # 導入済みの **env とそのバージョン
```

導入した `**env` の使い方は、それぞれのコマンドに従う。例えば nodenv なら、`nodenv install <version>` で Node.js を入れる。

- 追加した `**env` を有効にするには、シェルの再起動(`exec $SHELL -l`)が要る。

## 関連ページ

- [Node.js のバージョン管理](../../program/js/node/index.md#nodejsのバージョン管理) ... nodenv
- [Homebrew](brew.md)
- [2020-04-28 のメモ](../../memo/2020/20200428.md) ... macOS で anyenv 経由の nodenv を試した
- [2020-05-10 のメモ](../../memo/2020/20200510.md#ubuntuでもanyenvを使うことにした) ... Ubuntu でも anyenv を使うことにした

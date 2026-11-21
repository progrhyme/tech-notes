# just

[just](https://just.systems/) ... プロジェクト固有のコマンドを保存して実行するための、Rust 製のコマンドランナー。

- リポジトリ: <https://github.com/casey/just>
- マニュアル: <https://just.systems/man/en/>
- ライセンス: CC0-1.0
- 2026-11-21 時点の最新リリースは 1.59.0

## About

コマンド(recipe と呼ぶ)を `justfile` というファイルに書き、`just <recipe>` で実行する。
構文は [GNU make](make.md) に似ているが、ビルドシステムではなく、コマンドランナーとして作られている。

make との主な違い:

- ファイルの更新日時による再ビルド判定をしない。そのため、`.PHONY` が要らない。
- recipe に引数(フラグやオプションを含む)を渡せる。
- 未定義の recipe や循環依存は、実行前に静的に検出される。
- `.env` ファイルを読み込める(`set dotenv-load`)。
- `justfile` があるディレクトリの配下のどこからでも実行できる(カレントディレクトリから親へ向かって探す)。
- Python や Node.js など、シェル以外の言語で recipe を書ける(shebang recipe)。
- 追加の依存なしで、Linux、macOS、Windows で動く。

## Install

macOS の Homebrew:

```bash
brew install just
```

そのほかの方法:

- `cargo install just`
- 各 OS のパッケージマネージャー(公式 README に一覧がある)
- [GitHub Releases](https://github.com/casey/just/releases) のビルド済みバイナリ

動作確認:

```bash
just --version
```

## Quickstart

プロジェクトのルートに `justfile` を作る。ファイル名の大文字・小文字は区別されない。隠しファイルにしたいときは `.justfile` でもよい。

```just
build:
  cc main.c foo.c bar.c -o main

# テストを実行する
test: build
  ./test

sloc:
  @echo "`wc -l *.c` lines of code"
```

実行例:

```bash
# 引数なし: 先頭の recipe(または [default] 属性の recipe)を実行する
just

# recipe を指定して実行する。複数指定できる
just test
just build sloc
```

挙動:

- 実行する各行は、実行前に標準エラー出力へ表示される。行頭に `@` を付けると、表示しない。
- 行が失敗すると、その recipe は止まる。
- `test: build` のように書くと、`build` が先に実行される(依存関係)。
- インデントは、スペースでもタブでもよい。ただし、1つの recipe の中では統一する。

## justfile の構文

### 変数と式

```just
version := "1.0.0"
today := `date +%Y%m%d`

release:
  echo "release {{version}} ({{today}})"
```

- `:=` で変数を定義する。
- `{{...}}` で、変数や式を recipe の中に展開する。
- バッククォートで、コマンドの出力を値にできる。

### recipe の引数

```just
build target="debug":
  cargo build --{{target}}
```

```bash
just build           # target は debug
just build release
```

- `name="default"` でデフォルト値を指定する。
- `*args`(0個以上)、`+args`(1個以上)で、可変長の引数を受け取る。

### 設定(set)

```just
set dotenv-load
set shell := ["bash", "-uc"]
```

- `set dotenv-load`: `.env` から環境変数を読み込む。
- `set shell := [...]`: recipe の各行を実行するシェルを変える。デフォルトは `sh -cu`。

### 属性

recipe の直前に `[...]` で書く。

```just
[private]
helper:
  echo helper

[confirm]
clean:
  rm -rf dist/
```

- `[default]`: 引数なしの `just` で実行する recipe にする。
- `[private]`: `just --list` に出さない(`_` で始まる名前でも同じ)。
- `[confirm]`: 実行前に確認を求める。
- `[group('name')]`: `--list` での表示をグループ分けする。
- `[windows]`、`[unix]` など: OS ごとに recipe を切り替える。

### shebang recipe

recipe の本体の先頭に shebang を書くと、その言語で実行される。

```just
hello:
  #!/usr/bin/env python3
  print("Hello from Python")
```

### 分割

- `import 'path'`: 別ファイルの内容を取り込む。
- `mod name`: サブモジュールとして読み込む。`just name::recipe` で呼ぶ。

## just コマンド

```bash
# recipe の一覧(直前のコメントが説明として出る)
just --list

# justfile のひな形を作る
just --init

# justfile を整形する
just --fmt

# 変数の評価結果を表示する
just --evaluate

# 対話的に recipe を選んで実行する(fzf が必要)
just --choose

# 別の justfile を指定する
just --justfile <path> <recipe>
```

- シェル補完スクリプトは `just --completions <shell>` で出力できる。
- 実行される recipe は、デフォルトでは、`justfile` のあるディレクトリで動く。

!!! note
    `just` は make のように、ファイルの更新状況を見て実行を省略することはない。
    「出力ファイルが新しければ再ビルドしない」という挙動が必要な場合は、make などのビルドシステムを使う。

## Tips

### 各行は別のシェルで実行される

recipe の各行は、行ごとに新しいシェルで実行される。このため、ある行の `cd` や変数の設定は、次の行に引き継がれない。

```just
foo:
  cd bar && pwd   # 同じ行にまとめる
```

複数行にまたがる処理は、shebang recipe にするか、`set working-directory` や `[working-directory]` 属性を使う。

## 参考

- [GitHub - casey/just](https://github.com/casey/just)
- [Just Programmer's Manual](https://just.systems/man/en/)

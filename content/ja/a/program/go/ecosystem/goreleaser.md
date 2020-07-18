---
title: "GoReleaser"
linkTitle: "GoReleaser"
description: https://goreleaser.com/
date: 2020-06-11T00:21:42+09:00
---

2020-07-18 このページの内容を元にQiitaに記事を書いた:

- [GoReleaser覚え書き - Qiita](https://qiita.com/progrhyme/items/d6db1bbb2a9d3c43ab33)

## About

https://goreleaser.com/intro/

Goプロジェクトのリリース自動化ツール。

主な機能:

- バイナリのクロスコンパイル
- GitHub / GitLabへの公開
  - 公開済みのtagを参照してreleaseを作り、バイナリをアップロードする
  - Release Note生成 ... commit logからChange Logを生成

CIツールから使われることを念頭に作られているようだが、ローカルにインストールして実行することもできる。

参考:

- [goreleaser を使って Github Releases へ簡単デプロイ #golang - Qiita](https://qiita.com/ynozue/items/f939cff562ec782b33f0)
- [GitHub Actions での goreleaser と Docker Image の Push | | 1Q77](https://blog.1q77.com/2020/04/github-actions-goreleaser-docker-image-push/)

## Installation

https://goreleaser.com/install/

macOS:

```sh
brew install goreleaser/tap/goreleaser
```

Snap (Ubuntu, etc.):

```sh
sudo snap install --classic goreleaser
```

Docker:

```sh
docker pull goreleaser/goreleaser
```

## Usage

ここではローカルで実行できる手順を示すが、CIツールを使うにしても、大まかなプロセスの内容は変わらない。

### ①.goreleaser.ymlの生成

.goreleaser.ymlは、goreleaserを使うために必須の設定ファイルで、ふつうはプロジェクトのルートディレクトリに置く。  
goreleaserコマンドのオプションでパスを指定可能なので、好みで変えることはできそう。

次のコマンドで雛形を生成できる:

```sh
goreleaser init
```

### ②設定の編集

生成したYAMLを編集して、挙動をカスタマイズすることができる。
自分がよく使う設定については後述する。

### ③APIトークンの設定

GitHubやGitLabにリリースする際、goreleaserが利用するAPIトークンを設定する必要がある。
GitHubの場合、次のようにする:

```sh
export GITHUB_TOKEN="<YOUR API TOKEN>"
```

GitHub Actionsで設定する場合については後述する。

### ④goreleaserコマンド実行

ローカルから実行する場合、GitHubにタグをpushした後、次のコマンドでリリースを行う:

```sh
goreleaser --rm-dist
```

### Dockerでgoreleaserを実行

④で示したように、ローカルにインストールしたgoreleaserのバイナリを使ってビルドを行うと、生成物にカレントパス（など）の情報が含まれてしまう。
即ち、生成されたバイナリを実行して、panicした際などにビルド環境のパスが露出したりする。

これを避けるには、CIから実行するか、goreleaserのDockerイメージを使って実行するとよい。

dockerコマンドで実行する場合は次のようにする:

```sh
src_path="/go/src/github.com/<account>/<repo>"  # Module/パッケージに合わせて適切に設定する
docker run --rm --privileged \
  -v $PWD:$src_path \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -w $src_path \
  -e GITHUB_TOKEN \
  goreleaser/goreleaser release --rm-dist
```

### （ローカル実行時の）ハマりポイント

主にローカルで実行する際に、初心者が一度はハマるだろうと思われるポイント:

- ワーキングツリーの最新のコミットが最新のタグと一致してないとNG
  - これはCIでも同じと思われる
- ワーキングツリーがdirtyだと失敗する。管理外のファイル、ディレクトリがあってもNG
- 前回のビルド生成物が残っているなどで `dist/` が空じゃないとき、 `--rm-dist` オプションを付けてないと失敗する

## Configuration

`.goreleaser.yml` でカスタマイズしたくなりそうなところや、設定のTipsを記す。

（公式サイトに詳しいYAMLのサンプルがあるのは良いのだけど、大き過ぎて見切れてるとつらいのなんとかならないかな。。）

### テンプレート変数

GoReleaserでは、YAML内の様々なフィールドでGoのテンプレート機能を使えるようだ。

使える変数は https://goreleaser.com/customization/templates に記されている。

### Builds

https://goreleaser.com/customization/build/

```YAML
builds:
# 複数のビルド対象を記述可能
- 
  # mainパッケージまたはmain.goへのパス
  # デフォルトは "."
  main: ./cmd/main.go

  # デフォルトは [linux, darwin]
  # Windowsもサポートしたいなら足す
  goos:
  - linux
  - darwin
  goarch:
  # デフォルトでは386（32-bit）も含まれる
  - amd64
```

### Archive

https://goreleaser.com/customization/archive/

アーカイブファイル形式や、含めるファイルとか、ファイル名の設定。

```YAML
archives:
- 
  # デフォルトはtar.gzだけど、単バイナリでいいときとか変えたくなりそう
  #format: binary

  # アップロードされるファイルで、GOOSやGOARCHの文字列を置換したいときに設定する。
  # 特にこだわりがなければ設定不要
  replacements:
    amd64: x86_64

  files:
  # アーカイブに何も追加したくない場合は、マッチしないglob文字列を書かないといけない
  - nothing*
```

### Release

https://goreleaser.com/customization/release/

GitHubやGitLabに作成するリリースに関する設定。

```YAML
changelog:
  # changelog要らない場合はtrueに設定。デフォルトは未設定
  skip: true
  # changelogにcommit logを昇順・降順どちらで載せるか（だと思う）
  sort: asc
  filters:
    # 無視するcommit log
    exclude:
    - '^docs:'
    - '^test:'
```

リリースノートをもっと自由にカスタマイズしたい場合、goreleaserコマンドの引数に指定する。

```sh
# 静的ファイル
goreleaser --release-notes=FILE
# コマンドで動的に生成
goreleaser --release-notes <(some_change_log_generator)
```

## Features
### Homebrew Formula生成

https://goreleaser.com/customization/homebrew/

GoReleaserでHomebrewのFormulaを生成することができる。

参考:

- [メモ > 2020-07-18#GoReleaserでHomebrewのFormulaを作るようにした]({{<ref "20200718.md">}}#goreleaserでhomebrewのformulaを作るようにした)
- [GoReleaser+GithubActionsを使って、releaseファイルのアップロードとhomebrew対応を自動で行う - 年中アイス](https://reiki4040.hatenablog.com/entry/2020/02/10/080000)
- [goreleaserで簡単にオレオレコマンドをbrew installできちゃう - Qiita](https://qiita.com/momotaro98/items/a421c8b3412dec3fb2fc)
- [goreleaserでHomebrewのFormulaを自動生成する - Qiita](https://qiita.com/knqyf263/items/53dd0d0916afc5472281)

## CI設定

各種CIツールへの設定方法についても公式ガイドがあって捗る。

### GitHub Actions

https://goreleaser.com/ci/actions/

公式のアクションを利用できるので、簡単。

2020-06-14現在、[progrhyme/shelp](https://github.com/progrhyme/shelp)での設定は下の通り。

```YAML
name: goreleaser

on:
  push:
    tags:
      - '*'

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
        with:
          # コミットログからリリースノートを作るならこのオプションが必要
          fetch-depth: 0
      - uses: actions/setup-go@v2
        with:
          go-version: 1.14
      - name: Run GoReleaser
        uses: goreleaser/goreleaser-action@v2
        with:
          version: latest
          args: release --rm-dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

参考:

- [2020-06-17#goreleaserのドキュメントに修正PRを送った]({{<ref "20200617.md">}}#goreleaserのドキュメントに修正prを送った)

#### 任意のコマンドでリリースノートを生成

これについては、Qiitaに記事を書いた:

- [ChangeLogからGitHub用のリリースノートを作ってGoReleaserでリリースする - Qiita](https://qiita.com/progrhyme/items/e2fb3ceb772430bea4d9)

最終的に、binqでは次のように設定した（一部抜粋）:

```YAML
steps:
  - run: ./gen-release-note.sh > /tmp/release-note.md
  - uses: goreleaser/goreleaser-action@v2
    with:
      version: latest
      args: release --rm-dist --release-notes=/tmp/release-note.md
```

初め、 `--release-notes <(./gen-release-note.sh)` とやろうとしたが、GitHub Action上でエラーになってしまった:

- https://github.com/binqry/binq/runs/874286495?check_suite_focus=true

```
generating changelog
   ⨯ release failed after 2.35s error=open <(./gen-release-note.sh): no such file or directory
##[error]The process '/opt/hostedtoolcache/goreleaser-action/0.140.0/x64/goreleaser' failed with exit code 1
```

その後、何度か試したが、どうもプロセス置換 `<(...)` で上手くコマンドが動かないようだった。  
※ひょっとしたら、shで起動していてプロセス置換が効いてないとか？

参考:

- [bashのプロセス置換(Process Substitution)で中間ファイルを不要に - grep Tips *](https://www.greptips.com/posts/189/)

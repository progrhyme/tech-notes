---
title: "goreleaser"
linkTitle: "goreleaser"
description: https://goreleaser.com/
date: 2020-06-11T00:21:42+09:00
---

## About

Goプロジェクトのリリース自動化ツール。

主な機能:

- バイナリのクロスコンパイル
- GitHub / GitLabへの公開
  - 公開済みのtagを参照してreleaseを作り、バイナリをアップロードする
  - Release Note生成 ... commit logからChange Logを生成

CIと組合せて使うことも、ローカルから実行することもできる。

参考:

- [goreleaser を使って Github Releases へ簡単デプロイ #golang - Qiita](https://qiita.com/ynozue/items/f939cff562ec782b33f0)
- [GitHub Actions での goreleaser と Docker Image の Push | | 1Q77](https://blog.1q77.com/2020/04/github-actions-goreleaser-docker-image-push/)

## Install

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

雛形となる `.goreleaser.yml` を生成:

```sh
goreleaser init
```

YAMLを編集して設定をカスタマイズすることができる。

リリースを実行する前に、GitHubのAPI Tokenを環境変数に設定しておく必要がある:

```sh
export GITHUB_TOKEN="<YOUR API TOKEN>"
```

GitHubにタグをpushした後、次のコマンドでリリースを行う:

```sh
goreleaser --rm-dist
```

ただし、ふつうにこうやって実行するとカレントパスの情報がバイナリに含まれてしまう。  
ので、CIから実行するか、Dockerを使う方がベター。

dockerコマンドで実行する場合は次のようにする:

```sh
docker run --rm --privileged \
  -v $PWD:/go/src/github.com/<account>/<repo> \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -w /go/src/github.com/<account>/<repo> \
  -e GITHUB_TOKEN \
  goreleaser/goreleaser release --rm-dist
```

NOTE:

- ワーキングツリーの最新のコミットが最新のタグと一致してないとNG
- ワーキングツリーがdirtyだと失敗する。管理外のファイル、ディレクトリがあってもNG
- `dist/` が空じゃないとき、 `--rm-dist` オプションを付けてないと失敗する

## カスタマイズ

`.goreleaser.yml` でカスタマイズしたくなりそうなところを記す。

リファレンス:

- https://goreleaser.com/customization/build/
- https://goreleaser.com/customization/archive/
- https://goreleaser.com/customization/release/

```YAML
builds:
- goos:
  # デフォルトは [linux, darwin]
  # Windowsもサポートしたいなら足す
  - linux
  - darwin
  goarch:
  # デフォルトは386も含まれるが、もう要らないんじゃないかな
  - amd64
```

```YAML
archives:
- 
  # デフォルトはtar.gzだけど、単バイナリでいいときとか変えたくなりそう
  format: binary

  # アップロードされるファイルで、GOOSやGOARCHの文字列を置換したい
  # ときに設定する。設定しなくてもよさそう
  replacements:
    amd64: x86_64
```

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

## CI設定

各種CIツールへの設定方法についても公式ガイドがあって捗る。

### GitHub Actions

https://goreleaser.com/ci/actions/

公式のアクションを利用できるので、簡単。

2020-06-14現在、[shelp](https://github.com/progrhyme/shelp)での設定は下の通り。

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
      # fetch git commits
      - name: Unshallow
        # Changelogを直前のtagから生成するため
        run: git fetch --prune --unshallow --tags --force
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

NOTE:

- `Unshallow`ステップの `git fetch` のオプションに `--tags --force` を足す必要があった。これについてはドキュメントに修正PRを送った
  - https://github.com/goreleaser/goreleaser/pull/1608
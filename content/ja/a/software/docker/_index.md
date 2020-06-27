---
title: "Docker"
linkTitle: "Docker"
description: https://www.docker.com/
date: 2020-04-29T11:59:18+09:00
weight: 100
---

## Documentation

公式:

- https://docs.docker.com/
- リファレンス: https://docs.docker.com/reference/
  - [Dockerfile](https://docs.docker.com/engine/reference/builder/)
  - [dockerコマンド](https://docs.docker.com/engine/reference/commandline/docker/)

3rd Party:

- [Docker ドキュメント日本語化プロジェクト — Docker-docs-ja](http://docs.docker.jp/)

## Getting Started

入門コンテンツ:

- [Engine tutorials | Docker Documentation](https://docs.docker.com/engine/tutorials/)

## Registry
### API

https://docs.docker.com/registry/spec/api/

認証:

- [Token Authentication Specification | Docker Documentation](https://docs.docker.com/registry/spec/auth/token/)

参考:

- [Docker Registry API v2を利用してtag、manifest、imageの情報を取得する](https://himenon.github.io/docker/registry-api/)

### CLI

https://github.com/genuinetools/reg

v2 APIに対応したCLI. Webサーバや脆弱性スキャン機能まである。

Install:

- `go get`
- バイナリをGitHub ReleasesからDL

Examples:

```sh
# タグ一覧
reg tags <repo>
```

## Docker Hub

https://hub.docker.com/

Dockerイメージのレジストリサービス。  
有料プランなら非公開リポジトリも作れる。

### 公式イメージ
#### openjdk

- https://hub.docker.com/_/openjdk
- https://github.com/docker-library/openjdk/

Javaのリリースサイクルが短くなったこともあり、メンテされているバージョンが多くて所望のイメージを探すのにちょっと苦労する。

## Child Pages

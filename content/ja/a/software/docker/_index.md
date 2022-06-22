---
title: "Docker"
linkTitle: "Docker"
description: https://www.docker.com/
date: 2020-04-29T11:59:18+09:00
weight: 90
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

## How-to
### dockerコンテナからホストOSのlocalhostにアクセスする

Docker for MacやDocker for Windowsなら、 `host.docker.internal` でアクセスできる。

Examples:

```sh
docker run -it --rm mysql mysql -hhost.docker.internal -uroot -p
```

参考:

- [Dockerのコンテナの中からホストOS上のプロセスと通信する方法 - Qiita](https://qiita.com/ijufumi/items/badde64d530e6bade382)

## Knowledge
### コンテナの終了コード

 Exit Code | 意味
-----------|-----
 0 | 正常終了
 1 | アプリケーションエラー
 137 | SIGKILL (OOMなど)
 139 | SIGSEGV
 143 | SIGTERM

参考:

- [Understanding Docker Container Exit Codes | by Sandeep Madamanchi | Better Programming | Medium](https://medium.com/better-programming/understanding-docker-container-exit-codes-5ee79a1d58f6)

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

## Child Pages

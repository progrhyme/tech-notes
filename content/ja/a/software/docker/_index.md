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

#### タグ一覧

V2: https://docs.docker.com/registry/spec/api/#tags

参考:

- [2020-06-26#docker registry APIを叩いてtag検索するCLIを作った]({{<ref "20200626.md">}}#docker-registry-apiを叩いてtag検索するcliを作った)
- V1: [dockerイメージの検索とタグ一覧の取得、使い方の確認方法 | ぱーくん plus idea](https://web.plus-idea.net/2019/07/docker-image-search-tag/)

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

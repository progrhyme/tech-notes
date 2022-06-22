---
title: "Docker Image"
linkTitle: "Image"
date: 2022-06-22T11:57:49+09:00
weight: 200
---

## About
Dockerイメージ、あるいは、Linuxコンテナのイメージについて。

## 汎用
### scratch

最小限のイメージ。

- https://hub.docker.com/_/scratch

参考:

- [Dockerのscratchイメージを探検する | DevelopersIO](https://dev.classmethod.jp/articles/exploration-to-docker-scratch/)

### distroless

scratchと似た最小のイメージ。  
シェルやOSパッケージを含まない。

https://github.com/GoogleContainerTools/distroless

参考:

- [コンテナイメージとしてdistrolessを使うべき理由って？ | mediba Creator × Engineer Blog](https://ceblog.mediba.jp/post/662840014480326656/%E3%82%B3%E3%83%B3%E3%83%86%E3%83%8A%E3%82%A4%E3%83%A1%E3%83%BC%E3%82%B8%E3%81%A8%E3%81%97%E3%81%A6distroless%E3%82%92%E4%BD%BF%E3%81%86%E3%81%B9%E3%81%8D%E7%90%86%E7%94%B1%E3%81%A3%E3%81%A6)

## プログラム言語系
### openjdk

- https://hub.docker.com/_/openjdk
- https://github.com/docker-library/openjdk/

Javaのリリースサイクルが短くなったこともあり、メンテされているバージョンが多くて所望のイメージを探すのにちょっと苦労する。

## 関連項目

[Docker Hub]({{<ref "./_index.md">}}#docker-hub)

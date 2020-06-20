---
title: "Netlify"
linkTitle: "Netlify"
description: https://www.netlify.com/
date: 2020-06-20T19:48:36+09:00
weight: 350
---

Webサイトのホスティングサービス。

主に静的サイト向けだが、FaaSとしても使える？  
各種静的サイトジェネレータによるビルドに対応しており、GitHubなどのソースコードを連携することでサイトへの継続的デプロイを設定することができる。

## Getting Started

1. Sign up
   - GitHub IDで登録できる
1. リポジトリ連携
   - GitHub, GitLabなどから選べる
   - Netlifyで公開したいリポジトリに対して権限を与えるとよい
1. ビルド設定 -> デプロイ

参考:

- [NetlifyとGithubを連携させ、サイトのアップロード作業を自動化する方法 – 株式会社ライトコード](https://rightcode.co.jp/blog/information-technology/netlify-github-up)

## Pricing

https://www.netlify.com/pricing/

 項目 | STARTER | PRO
---|---------|-----
 基本料金 | 無料 | $45/月
 メンバー数 | 1 | 3
 同時ビルド数 | 1 | 3
 転送量 | 100GB/月 | 400GB/月
 ビルド時間 | 300分/月 | 1,000分/月
 サイト数 | 500 | 無制限

## Configuration

https://docs.netlify.com/configure-builds/common-configurations/

各種ビルドツールを使う場合の設定が並んでいるので、だいたいこの通りにするといい。

### Python

https://docs.netlify.com/configure-builds/manage-dependencies/#python

#### Pythonのバージョン

2020-06-21現在、デフォルトのビルドイメージ（Ubuntu 16）のデフォルトのPythonが2.7になっている。  
Python 3を使うには、下のようにruntime.txtを用意する。

```sh
echo 3.7 > runtime.txt
```

リファレンス:

- https://docs.netlify.com/configure-builds/get-started/#build-image-selection ... ビルドイメージの選択
- https://github.com/netlify/build-image/blob/xenial/included_software.md#languages ... Ubuntu 16でサポートされているプログラム言語ランタイム

### netlify.toml

[File-based configuration | Netlify Docs](https://docs.netlify.com/configure-builds/file-based-configuration/)

もっと細やかな設定がしたいときに使えそう。

#### 依存ライブラリの設定

リポジトリにrequirements.txtを用意する。

## How-to
### GitHub ActionsでNetlifyにデプロイ

NetlifyでビルドできるのにわざわざGitHub Actionsを使うのはなぜだろうと思ったら、ビルド時間の無料枠を節約するためらしい。  
それなら別のサービスを使うのと変わらないのではないか、という気もするのだが。

NOTE:

- Netlifyにリポジトリを連携する前に設定しないと面倒なことになるかもしれない

参考記事より引用:

> Netlifyの仕様上Githubのリポジトリと紐付きがある場合プッシュしたタイミングでデプロイを自動で行います。  
そのためGithub Actionsでジョブ実行前にデプロイが完了してしまうため紐付きを解除する必要がありますが、Netlifyコミュニティに依頼しない限り紐付きを解除することができない

参考:

- [Netlifyへのデプロイをビルド時間0で行うためのGitHub Actions - Qiita](https://qiita.com/nwtgck/items/e9a355c2ccb03d8e8eb0)
- [Github ActionsでNetlifyに自動デプロイする - kosa3 - Medium](https://medium.com/@kosa3/github-actions%E3%81%A7netlify%E3%81%AB%E8%87%AA%E5%8B%95%E3%83%87%E3%83%97%E3%83%AD%E3%82%A4%E3%81%99%E3%82%8B-22ac30e02528)

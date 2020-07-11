---
title: "GitHub"
linkTitle: "GitHub"
description: >
  https://github.com/
date: 2020-04-26T13:50:09+09:00
weight: 200
---

## 稼働/障害 情報

https://www.githubstatus.com/

## Documentation

https://help.github.com/

- 邦訳: https://help.github.com/ja

## Pages

リポジトリと連携可能な静的サイトホスティングサービス。

関連項目:

- [2020-06-24#GitHub PagesをJSONサーバとして使う]({{<ref "20200624.md">}}#github-pagesをjsonサーバとして使う)

## Deployments

Deploymentを作成するとリポジトリに「environment」というメニューができて、デプロイ履歴などが見えるようになる。

ドキュメント:

- [Viewing deployment activity for your repository - GitHub Help](https://help.github.com/en/github/administering-a-repository/viewing-deployment-activity-for-your-repository)
- [Deployments | GitHub Developer Guide](https://developer.github.com/v3/repos/deployments/)

## 認証
### トークン

トークンの種類:

- Personal Access Token
  - GitHub API利用時に作成するもの
- GitHub Token in GitHub Actions
  - GitHub Actionsのアクション内で利用できるトークンで、 `secrets.GITHUB_TOKEN` で参照できる

このトークンはパスワード認証時にパスワードの代わりに利用できる。  
ので、下のように使うこともできる。

```sh
git clone "https://${owner}:${GITHUB_TOKEN}@github.com/${owner}/${repo}.git"
```

URLにトークンが入っているので、上のコマンドでcloneしたリポジトリは、トークンにリポジトリへの書込み権限があれば、そのままpushすることができる。

これを利用して、例えばGitHub Actionsによってリポジトリを自動更新することもできる。

参考:

- [Creating a personal access token - GitHub Docs](https://docs.github.com/ja/github/authenticating-to-github/creating-a-personal-access-token)
- [【GitHub Actions】CIを使って毎日自動でGitHubに草を生やそうｗｗｗ - Qiita](https://qiita.com/ykhirao/items/65fee829ee0478187027#comments)

## Child Pages

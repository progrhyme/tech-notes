---
title: "Cloud Identity and Access Management (IAM)"
linkTitle: "Cloud IAM"
description: https://cloud.google.com/iam
date: 2020-05-04T09:26:28+09:00
weight: 120
---

https://cloud.google.com/iam/docs

Cloud IAM. Google IDベースのアクセス管理ができる。

Googleグループを設定することもできる。

## Reference

- [IAM permissions reference](https://cloud.google.com/iam/docs/permissions-reference)


## How-to
### Compute Engineへのアクセス権限

関係するRoles:

 Role | Description
--------|-----------------
 roles/compute.instanceAdmin.v1 | インスタンスの作成・削除・編集など
 roles/iam.serviceAccountUser | サービスアカウントの利用。インスタンス作成にも必要
 roles/iap.tunnelResourceAccessor | IAP経由でインスタンスにSSHするために必要

参考:

- [IAP で保護されたリソースへのアクセスの管理 | Identity-Aware Proxy のドキュメント | Google Cloud](https://cloud.google.com/iap/docs/managing-access?hl=ja)


## 参考

- [よくある質問 | Cloud Identity and Access Management のドキュメント | Google Cloud](https://cloud.google.com/iam/docs/faq?hl=ja "よくある質問  |  Cloud Identity and Access Management のドキュメント  |  Google Cloud")
- [GCPのCloud IAMを試してみた | サイバーエージェント 公式エンジニアブログ](https://ameblo.jp/principia-ca/entry-12144854519.html "GCPのCloud IAMを試してみた | サイバーエージェント 公式エンジニアブログ")

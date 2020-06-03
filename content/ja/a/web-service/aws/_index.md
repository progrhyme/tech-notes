---
title: "Amazon Web Service"
linkTitle: "AWS"
description: http://aws.amazon.com/
date: 2020-06-03T13:41:40+09:00
weight: 20
---

## 各種制限

- [AWS サービス制限 - アマゾン ウェブ サービス](http://docs.aws.amazon.com/ja_jp/general/latest/gr/aws_service_limits.html "AWS サービス制限 - アマゾン ウェブ サービス")
- [Amazon EC2 インスタンスの構成 - Amazon Elastic Compute Cloud](http://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/ebs-ec2-config.html "Amazon EC2 インスタンスの構成 - Amazon Elastic Compute Cloud") ... 最大帯域幅/スループット/IOPS

Tips:

- リージョン内のVPC数の上限(デフォルト5個)を増やすと、合わせてリージョン内のインターネットゲートウェイ数の上限も増やしてもらえる。

## サポート

プラン: https://aws.amazon.com/jp/premiumsupport/signup/

## マネジメントコンソール
### 複数アカウントの切替

1. Cross-Account Accessを使う
  - [Amazon Web Services ブログ: 【AWS発表】AWSマネジメントコンソールへのCross\-Account Access](http://aws.typepad.com/aws_japan/2015/01/new-cross-account-access-in-the-aws-management-console.html)
1. Chromeで複数ユーザ作って頑張る
  - 参考: [Google Chromeで複数AWSアカウントでの作業を快適に行う方法 ｜ Developers\.IO](https://dev.classmethod.jp/cloud/google-chrome-multi-aws-account/)

## 請求とコスト管理

- [コスト配分タグの使用 \- AWS 請求情報とコスト管理](https://docs.aws.amazon.com/ja_jp/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html)
  - 特定のタグを付けることでコスト管理しやすくなる

### Budgets
#### ベストプラクティス

[AWS Budgets のベストプラクティス - AWS 請求情報とコスト管理](https://docs.aws.amazon.com/ja_jp/awsaccountbilling/latest/aboutv2/budgets-best-practices.html)

- 予算の予測には約5週間の使用状況データが必要

#### SNS通知

予算の通知にSNSトピックを使う場合、ポリシー設定が必要。

- [予算の通知に関連付ける Amazon SNS トピックの作成 \- AWS 請求情報とコスト管理](https://docs.aws.amazon.com/ja_jp/awsaccountbilling/latest/aboutv2/budgets-sns-policy.html)

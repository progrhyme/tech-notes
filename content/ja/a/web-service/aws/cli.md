---
title: "AWS CLI"
linkTitle: "CLI"
description: https://aws.amazon.com/jp/cli/
date: 2020-06-03T13:41:48+09:00
---

## About

https://github.com/aws/aws-cli

NOTE:

- 2020-02-12 AWS CLI v2が一般利用可能になった。
  - [AWS CLI v2 が一般利用可能となりました | Amazon Web Services ブログ](https://aws.amazon.com/jp/blogs/news/aws-cli-v2-is-now-generally-available/)

## Install

- [AWS Command Line Interface のインストール - AWS Command Line Interface](http://docs.aws.amazon.com/ja_jp/cli/latest/userguide/installing.html "AWS Command Line Interface のインストール - AWS Command Line Interface")

### macOS

- 公式ガイド: [macOS での AWS CLI バージョン 2 のインストール - AWS Command Line Interface](https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/install-cliv2-mac.html)

※2020-06-03 Homebrewでv2が入るが、なぜかpythonに依存している。  
https://formulae.brew.sh/formula/awscli

## Dockerイメージ

※過去の記述である

https://hub.docker.com/r/mesosphere/aws-cli/ がちゃんとしてそう。

## Reference

- [aws — AWS CLI 2 Command Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html)
- [aws — AWS CLI 1 Command Reference](https://docs.aws.amazon.com/cli/latest/reference/)

※以下、古いWikiの内容をマイグレートしたので、v1の情報が元になっているものが多い。

### configure

```bash
# credential等がちゃんと設定されてるか確認
aws configure list
```

参考:

- [S3 バケットの「認証情報が見つかりません」エラーを修正する](https://aws.amazon.com/jp/premiumsupport/knowledge-center/s3-locate-credentials-error/)

### logs

http://docs.aws.amazon.com/cli/latest/reference/logs/index.html

CloudWatch Logs.

- http://docs.aws.amazon.com/cli/latest/reference/logs/get-log-events.html
  - `--start-time`, `--end-time` の引数はミリ秒単位のunixtime
  - `--limit` は10000が上限で、より大きな値を指定するとバリデーションエラーになる。

Examples:

```sh
# 2017/12/20 8:50 - 9:10のログを取得
$ date +%s -d "2017-12-20 08:50:00"
1513727400
$ date +%s -d "2017-12-20 09:10:00"
1513728600
$ aws logs get-log-events \
  --log-group-name <your-log-group> --log-stream-name <your-log-stream> \
  --start-time 1513727400000 --end-time 1513728600000
```

### sns

- https://docs.aws.amazon.com/cli/latest/reference/sns/
  - https://docs.aws.amazon.com/cli/latest/reference/sns/publish.html

Examples:

```sh
# テキストファイルの内容を送信
aws sns publish --topic-arn "arn:aws:sns:ap-northeast-1:${AWS_ACCOUNT_ID}:${topic}" --subject "my sns notification" --message file://path/to/message-file

# コマンドの実行結果を送信
aws sns publish --topic-arn "arn:aws:sns:ap-northeast-1:${AWS_ACCOUNT_ID}:${topic}" --message "$(cat path/to/file)"
```

### ssm

http://docs.aws.amazon.com/cli/latest/reference/ssm/index.html

Parameter Store:

- http://docs.aws.amazon.com/cli/latest/reference/ssm/get-parameter.html
- http://docs.aws.amazon.com/cli/latest/reference/ssm/get-parameters.html
- http://docs.aws.amazon.com/cli/latest/reference/ssm/put-parameter.html

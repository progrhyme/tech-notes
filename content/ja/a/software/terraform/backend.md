---
title: "Backends"
linkTitle: "Backends"
description: >
  https://www.terraform.io/docs/backends/
date: 2020-04-26T23:05:57+09:00
weight: 300
---

> A "backend" in Terraform determines how state is loaded and how an operation such as `apply` is executed. This abstraction enables non-local file state storage, remote execution, etc.

## gcs

https://www.terraform.io/docs/backends/types/gcs.html

- 認証用の `credentials` または `access_token` が必要。
  - https://cloud.google.com/sdk/gcloud/reference/auth/application-default/login で作成できるユーザのApplication Default Credentialsでも良い


## s3

https://www.terraform.io/docs/backends/types/s3.html

- ロックしたいときはDynamoDBを使う。
  - オプション `dynamodb_table` を指定する

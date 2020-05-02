---
title: "Backends"
linkTitle: "Backends"
description: >
  https://www.terraform.io/docs/backends/
date: 2020-04-26T23:05:57+09:00
weight: 300
---

> A "backend" in Terraform determines how state is loaded and how an operation such as `apply` is executed. This abstraction enables non-local file state storage, remote execution, etc.

## Documentation

- [Configuration](https://www.terraform.io/docs/backends/config.html)
- [Init](https://www.terraform.io/docs/backends/init.html)
- [State Storage & Locking](https://www.terraform.io/docs/backends/state.html)

## gcs

https://www.terraform.io/docs/backends/types/gcs.html

Example:

```HCL
terraform {
  backend "gcs" {
    bucket  = "tf-state-prod"
    prefix  = "terraform/state"
  }
}
```

- 認証用の `credentials` または `access_token` が必要。

### config variables

- `credentials` ... GCPのサービスアカウントキー（JSON）のパスを指定する
  - 環境変数 `GOOGLE_BACKEND_CREDENTIALS` or `GOOGLE_CREDENTIALS` によってパスを指定することもできる
  - https://cloud.google.com/sdk/gcloud/reference/auth/application-default/login で作成できるユーザの[Application Default Credentials](https://cloud.google.com/docs/authentication/production)でも良い

```sh
gcloud auth application-default login
```

See also:

- [Providers > Google]({{< ref "/a/software/terraform/provider/google.md" >}}#configuration)

## s3

https://www.terraform.io/docs/backends/types/s3.html

- ロックしたいときはDynamoDBを使う。
  - オプション `dynamodb_table` を指定する

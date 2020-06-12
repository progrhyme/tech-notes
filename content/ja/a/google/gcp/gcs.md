---
title: "Cloud Storage"
linkTitle: "GCS"
description: https://cloud.google.com/products/storage/
date: 2020-06-13T02:01:27+09:00
weight: 220
---

## Documentation

- Best Practices: https://cloud.google.com/storage/docs/best-practices
- [Bucket locations | Cloud Storage | Google Cloud](https://cloud.google.com/storage/docs/locations?hl=en#location-r)

## Spec

- [オブジェクトのバージョニング | Cloud Storage | Google Cloud](https://cloud.google.com/storage/docs/object-versioning?hl=ja)

## アクセス制御
### IAM

[Cloud Identity and Access Management | Cloud Storage | Google Cloud](https://cloud.google.com/storage/docs/access-control/iam)

関連項目:

- [CLI#gsutil-iam]({{<ref "cli.md">}}#iam)

#### メンバータイプ

Cloud Storageバケットのみに適用できる特別なメンバータイプがある:

- `projectOwner:[PROJECT_ID]`
- `projectEditor:[PROJECT_ID]`
- `projectViewer:[PROJECT_ID]`

いずれかにロールを付与すると、指定したプロジェクトに対して指定された権限を持つすべてのメンバーが、選択されたロールを取得する。

ただし、これらの権限はコンソールや `gsutil iam ch` コマンドでは設定できないようだ。  
`gsutil iam set` コマンドであれば設定することができる。

Example:

```sh
gsutil iam set policy.json gs://my-bucket
```

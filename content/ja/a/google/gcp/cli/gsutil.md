---
title: "gsutil"
linkTitle: "gsutil"
date: 2020-11-10T09:49:42+09:00
weight: 50
---

Cloud Storage用のPython製CLI

- ドキュメント: https://cloud.google.com/storage/docs/gsutil
- コマンドリファレンス: https://cloud.google.com/storage/docs/gsutil/commands/help

## バケット操作

- [mb](https://cloud.google.com/storage/docs/gsutil/commands/mb)
- [rb](https://cloud.google.com/storage/docs/gsutil/commands/rb)

Examples:

```sh
# バケット作成
gsutil mb -l asia gs://mybucket
# バケット削除
gsutil rb [-f] gs://<bucket_name>
```

## iam

https://cloud.google.com/storage/docs/gsutil/commands/iam

```sh
# bucket/objectのIAM権限を取得
gsutil iam get gs://bucket[/path]
# bucket/objectにIAM権限を設定
gsutil iam set [-afRr] [-e <etag>] file gs://bucket[/path] ...
# bucket/objectにIAM権限を設定。メンバー単位で個々に設定
gsutil iam ch [-fRr] binding ... gs://bucket
```

関連項目:

- [GCS#IAM]({{<ref "gcs.md">}}#iam)

## ls

https://cloud.google.com/storage/docs/gsutil/commands/ls

バケットやオブジェクトのリスト表示。

Examples:

```sh
gsutil ls gs://my-bucket/

# 古いバージョンも含める
gsutil ls -a gs://my-bucket/
```

## rm

https://cloud.google.com/storage/docs/gsutil/commands/rm

オブジェクトの削除。

Examples:

```sh
# subdir/ 直下のオブジェクトを削除
gsutil rm gs://bucket/subdir/*
# subdir/ 下の全てのオブジェクトを削除
gsutil rm gs://bucket/subdir/**
# 上と同じ
gsutil rm -r gs://bucket/subdir/

# 古いバージョンも含めて削除
gsutil rm -a gs://bucket/path/to/object
```

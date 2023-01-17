---
title: "API"
linkTitle: "API"
date: 2023-01-17T12:58:35+09:00
weight: 10
---

## Client Library

Golang: https://pkg.go.dev/google.golang.org/api

## Drive API

https://developers.google.com/drive/api

Google Driveに対する操作

### 共有ドライブを使う

https://developers.google.com/drive/api/guides/enable-shareddrives

- APIで共有ドライブに対する操作を有効にするには、APIリクエスト時に `supportsAllDrives=true` というパラメータを付与しなければならない

### Go言語での実装

```go
# 共有ドライブのサポート

r, err := srv.Files.List().SupportsAllDrives(true).PageSize(1000)
resp, err := srv.Files.Get(id).SupportsAllDrives(true).Context(ctx).Download()
```

参考: [Google Drive API v3をサービスアカウトとGoから利用 | フューチャー技術ブログ](https://future-architect.github.io/articles/20211022a/)

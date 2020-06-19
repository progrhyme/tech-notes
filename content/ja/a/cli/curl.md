---
title: "curl"
linkTitle: "curl"
description: https://curl.haxx.se/
date: 2020-06-19T20:30:40+09:00
weight: 100
---

## Documentation

- Man: https://curl.haxx.se/docs/manpage.html

## Options

 Option | 意味
----------|--------
 `-H, --header <header/@file>` | HTTPヘッダを付加
 `-L, --location` | リダイレクトに対応。3XXステータスとLocationヘッダが返ってきたら、新しい宛先にリクエストを再送する
 `-o <file>` | ダウンロードしたデータを `<file>` に保存
 `-o -` | 上の特別な場合で、標準出力に結果を出力
 `-s, --silent` | 進捗を表示しない
 `-sS` | 進捗は要らないけどエラーは表示する。 `-S` は `--show-error`
 `-x <method>` | 指定したHTTPメソッドでリクエスト
 `-v` | HTTPリクエスト、レスポンスの詳細を表示

参考:

- [curl option 覚え書き - Qiita](https://qiita.com/takayukioda/items/edf371b3566bea64d046)

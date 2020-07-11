---
title: "エコシステム"
linkTitle: "エコシステム"
date: 2020-06-08T00:52:03+09:00
weight: 1100
---

他のページで触れていない、Go言語による開発などで使われるサードパーティー製のツール。

See Also:

- [tools]({{<ref "tools.md">}})

メモ:

- TinyGoなどの話題もここに載せるかもしれない。

## 開発環境
### Visual Studio Code
#### デバッガの利用

1. 必要なツールのインストール
   - 下のdelveなど
1. タスク設定ファイルの用意
   - 最初にデバッグ実行するときにlaunch.jsonが作られるので、必要に応じて編集すればいい
1. ブレークポイントの設定
1. デバッグ実行
   - main関数のあるファイルで `Run > Start Debugging`
   - `Test*` な関数だったら、エディタ上で「debug test」をクリックすることも可能

launch.jsonについて:

- `"args": []` にコマンドライン引数を入れることができる

参考:

- [Visual Studio CodeでGo言語のデバッグ環境を整える - Qiita](https://qiita.com/momotaro98/items/7fbcad57a9d8488fe999)
  - NOTE: `GOPATH` の設定は不要

## デバッガ

https://github.com/go-delve/delve が有名。

参考:

- [delveでGolangのデバッグ - Carpe Diem](https://christina04.hatenablog.com/entry/2017/07/16/094140)

## タスクランナー
### GNU make

Go言語による開発で割とよく使われるようだ。

関連項目:

- [Software > GNU make]({{<ref "/a/software/job-man/make.md">}})

参考:

- [Go言語開発を便利にするMakefileの書き方 - Qiita](https://qiita.com/yoskeoka/items/317a3afab370155b3ae8)

## CI
### GitHub Actions

関連項目:

- [Webサービス > GitHub > Actions > Actions#setup-go]({{<ref "/a/web-service/github/action/action.md">}}#setup-go)

参考:

- https://github.com/progrhyme/shelp
- [【GitHub Actions】Go言語の自動テストからリリースまでを作ってみた - Qiita](https://qiita.com/x-color/items/f60025c20a547a7355b5)
- [Github actionsでgo mod download, test, lint - Qiita](https://qiita.com/0daryo/items/045be6ef98ae8164e8e7)

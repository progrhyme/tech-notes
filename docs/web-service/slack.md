---
date: '2020-06-11T00:01:59+09:00'
description: https://slack.com/
---

# Slack

## Documentation

- （日本語）[Slack ヘルプセンター | Slack](https://slack.com/intl/ja-jp/help)
- https://api.slack.com/ ... API Docs

## Features
### @ で始まる任意のユーザグループを作る

- [User Groups – Slack Help Center](https://get.slack.help/hc/en-us/articles/212906697-User-Groups "User Groups – Slack Help Center")

## Apps

- イントロ: https://api.slack.com/start/overview#apps

### チュートリアル

アプリの作成:

- [Create a Slack app and authenticate with Postman | Slack](https://api.slack.com/tutorials/slack-apps-and-postman)

アプリのカスタマイズ:

- Homeタブの作成: [Building a home for your app 🏡 | Slack](https://api.slack.com/tutorials/app-home-with-modal)

### 認証・認可

[Basic app setup | Slack](https://api.slack.com/authentication/basics)

### アプリの配布

- Overview: https://api.slack.com/start/distributing
- アプリの公開: https://api.slack.com/start/distributing/public

Hints:

- デフォルトではアプリを作成したワークスペースのみにインストールされる。この際、アプリでは全機能が有効
- OAuth 2.0対応をすることで、アプリを公開することができる
- 更に、SlackのApp Directoryに登録することで、一定の品質と有用性を保証することができる

参考:

- [SlackのOAuthを使って独自アプリをインストールさせる | Workabroad.jp](https://workabroad.jp/posts/2239)
- [Slack の OAuth API を使ってみる : まだプログラマーですが何か？](http://dotnsf.blog.jp/archives/1074688701.html)

### 参考事例

- [【初心者向けGAS×Slack】はじめてのSlackアプリを作成しよう](https://tonari-it.com/gas-slack-create-app/) ... GASでSlackに天気予報を通知。SlackアプリとしてはSingle-Workspaceモードで、Incoming Webhookしか使ってない。
- [Google Apps Script で Slack Botを作ってみた。(お勉強編) - Qiita](https://qiita.com/Quikky/items/9de56c049304885a4f4f) ... ↑に毛が生えた程度の事例だが、GASのエンドポイントでSlashコマンドにも対応している。

## メッセージAPI
### メッセージ書式

- https://api.slack.com/docs/messages#formatting_messages

↑が入り口。一部の書式は API リクエスト時のみ有効で、手打ちでは駄目っぽい。  
たとえば、 `<URL|Text>` によるリンク記法。

(2020-04-14) 追記。ややAPIが複雑化しているように思う。

- https://api.slack.com/messaging/composing/layouts

参考:

- [slack でのいろんな表記方法 - Qiita](http://qiita.com/amanoiverse/items/186c71af92c9494ab26f "slack でのいろんな表記方法 - Qiita")
- [Slack API attachmentsチートシート - Qiita](https://qiita.com/daikiojm/items/759ea40c00f9b539a4c8#color)

#### 色

https://api.slack.com/reference/messaging/attachments

任意の色が指定可能だけど、プリセットとして `good` （緑）, `warning` （黃）, `danger` （赤）がある。

### Incoming Webhooks (With Apps)

- https://api.slack.com/messaging/webhooks
- [Slack での Incoming Webhook の利用 | Slack](https://slack.com/intl/ja-jp/help/articles/115005265063-Slack-%E3%81%A7%E3%81%AE-Incoming-Webhook-%E3%81%AE%E5%88%A9%E7%94%A8)

シンプルに書くと、アプリを作ってIncoming Webhookを有効にすればいい。  
アプリを配布する場合は話が全然変わってくるが、当該ワークスペースで使うだけならそれで十分である。

参考:

- 2019年7月初出: [slackのIncoming webhookが新しくなっていたのでまとめてみた - Qiita](https://qiita.com/kshibata101/items/0e13c420080a993c5d16)

### Incoming Webhooks (Legacy)

https://api.slack.com/legacy/custom-integrations/incoming-webhooks

※2020-07-19現在、まだ利用できるが、Slack Appsへの移行が推奨されている。

#### メッセージのカスタマイズ

Incoming Webhook特有のパラメータは以下:

- `username` : 投稿者名
- `icon_emoji` : アイコン用絵文字
- `icon_url` : アイコン画像URL
- `channel` : 投稿先チャネルのコード（上書きする場合）

※この辺りのパラメータは新方式（With Apps）の方では使えなくなっている。

あとは普通のメッセージのカスタマイズと同じ（はず）。

## Administration
### Roles & Permissions

- [Slack メンバーの種別と権限 – Slack](https://get.slack.help/hc/ja/articles/201314026-Slack-%E3%83%A1%E3%83%B3%E3%83%90%E3%83%BC%E3%81%AE%E7%A8%AE%E5%88%A5%E3%81%A8%E6%A8%A9%E9%99%90)

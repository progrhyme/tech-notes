---
title: "Slack"
linkTitle: "Slack"
description: https://slack.com/
date: 2020-06-11T00:01:59+09:00
weight: 800
---

## Usage
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


### @ で始まる任意のユーザグループを作る

- [User Groups – Slack Help Center](https://get.slack.help/hc/en-us/articles/212906697-User-Groups "User Groups – Slack Help Center")


## Features
### Incoming Webhooks

https://api.slack.com/legacy/custom-integrations/incoming-webhooks

#### メッセージのカスタマイズ

Incoming Webhook特有のパラメータは以下:

- `username` : 投稿者名
- `icon_emoji` : アイコン用絵文字
- `icon_url` : アイコン画像URL
- `channel` : 投稿先チャネルのコード（上書きする場合）

あとは普通のメッセージのカスタマイズと同じ（はず）。


## Administration
### Roles & Permissions

- [Slack メンバーの種別と権限 – Slack](https://get.slack.help/hc/ja/articles/201314026-Slack-%E3%83%A1%E3%83%B3%E3%83%90%E3%83%BC%E3%81%AE%E7%A8%AE%E5%88%A5%E3%81%A8%E6%A8%A9%E9%99%90)

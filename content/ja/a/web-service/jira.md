---
title: "JIRA"
linkTitle: "JIRA"
description: https://www.atlassian.com/software/jira
date: 2020-06-03T00:22:58+09:00
weight: 230
---

Atlassian社製のITS.

## Features
### リマインダ

- [Jiraにて期限の近い課題の通知を受け取りたい \- Atlassian Community](https://community.atlassian.com/t5/Jira-articles/Jira%E3%81%AB%E3%81%A6%E6%9C%9F%E9%99%90%E3%81%AE%E8%BF%91%E3%81%84%E8%AA%B2%E9%A1%8C%E3%81%AE%E9%80%9A%E7%9F%A5%E3%82%92%E5%8F%97%E3%81%91%E5%8F%96%E3%82%8A%E3%81%9F%E3%81%84/ba-p/770716)

### JQL

JIRA固有の問合せ言語。SQLライク。

ドキュメント:

- [詳細検索 \- 関数リファレンス \- アトラシアン製品ドキュメント](https://ja.confluence.atlassian.com/jirasoftwarecloud/advanced-searching-functions-reference-764478342.html)

参考:

- [JIRAのチケット検索で使うJQLの例\(適宜追加\) \- Qiita](https://qiita.com/takahirono7/items/4052321fe26130957c03)

#### ラベルが空

```
labels is EMPTY
```

参考:

- [Solved: How can I search for issues that do NOT have a cer...](https://community.atlassian.com/t5/Jira-questions/How-can-I-search-for-issues-that-do-NOT-have-a-certain-label/qaq-p/324533)

#### 日付関連

SYNOPSIS:

```
duedate < 1w // 期限1週間以内
duedate < 30d // 期限30日以内
```

※ `duedate < 1m` や `duedate < 1M` は1ヶ月以内としては機能しない

## Plugins

- [Markin – Markdown Editor for JIRA – Fulstech](https://fulstech.wordpress.com/markin-markdown-editor-for-jira/)
  - 良い感じのMarkdownプラグイン
  - https://github.com/fulstech/markin ... Issueでサポートサイト的な使い方をしている

## 管理機能
### "Cc"というフィールドを作る

カスタムフィールドを作れば良いみたい。

参考:

- [How to add CC field in open ticket screen?](https://community.atlassian.com/t5/Jira-Service-Desk-questions/How-to-add-CC-field-in-open-ticket-screen/qaq-p/2152)

### 優先度のフィールドをカスタマイズ

[優先度フィールドの値を定義する \- アトラシアン製品ドキュメント](https://ja.confluence.atlassian.com/adminjiraserver072/defining-priority-field-values-828787742.html)

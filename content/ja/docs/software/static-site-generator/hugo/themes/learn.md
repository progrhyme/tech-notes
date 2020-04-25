---
title: "LEARN"
linkTitle: "LEARN"
date: 2020-04-25T23:43:30+09:00
---

https://learn.netlify.com/en/

ドキュメンテーションに向いた高機能なHugoのテーマ。

## コンテンツ管理

### ページの追加

https://themes.gohugo.io//theme/hugo-theme-learn/en/cont/archetypes/ を参照。

```sh
# Chapterページ
hugo new path/to/chapter/_index.md --kind chapter

# 普通のページ
hugo new path/to/page.md
```

{{% alert title="NOTE" %}}
パスは `content/` からの相対パス。
{{% /alert %}}

## 拡張記法

いくつかHugoの機能を拡張して便利記法を提供してくれているのかな？

[Shortcodes](https://themes.gohugo.io//theme/hugo-theme-learn/en/shortcodes/)に紹介されている。

- [Mermaid](https://mermaid-js.github.io/mermaid/#/)によるフローチャート
- Hugoのサイト設定変数参照
- etc.

などの機能がある。

以下は例:

### 注釈

```
{{%/* notice note */%}}
A notice disclaimer
{{%/* /notice */%}}
```

`note` 以外に、 `info`, `tip`, `warning` が使える。

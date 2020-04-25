---
title: "Hugo"
linkTitle: "Hugo"
date: 2020-04-25T23:38:08+09:00
---

https://gohugo.io

Go言語製の高速な静的サイトジェネレーター。

## Documentation

https://gohugo.io/documentation/

- [Getting Started](https://gohugo.io/getting-started/)
- [Content Management](https://gohugo.io/content-management/)
  - [Front Matter](https://gohugo.io/content-management/front-matter/) ... ページに対して付けることができるメタデータ
- :

## Quickstart

https://gohugo.io/getting-started/quick-start/

```sh
# 新しくサイトを作る
hugo new site your-new-site

# テーマを用意する
cd your-new-site
git init
git submodule add https://github.com/budparr/gohugo-theme-ananke.git themes/ananke
echo 'theme = "ananke"' >> config.toml

# コンテンツを作成する
hugo new posts/my-first-post.md

# hugo serverを起動
hugo server -D
## -D を付けることで draft のページも表示される
```

## Child Pages

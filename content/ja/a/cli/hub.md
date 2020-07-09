---
title: "hub"
linkTitle: "hub"
description: https://hub.github.com/
date: 2020-07-10T06:38:05+09:00
weight: 280
---

## About

OSSのGitHub公式CLI. Go製。

- https://github.com/github/hub

gitコマンドの薄いラッパーとしての性質と、GitHub APIクライアントの性質を持つ。

ドキュメンテーション:

- [hub(1) - make git easier with GitHub](https://hub.github.com/hub.1.html)

## Usage

Examples:

```sh
# clone your own project
hub clone dotfiles
#=> git clone git://github.com/YOUR_USER/dotfiles.git

# clone another project
hub clone github/hub
#=> git clone git://github.com/github/hub.git

# fast-forward all local branches to match the latest state on the remote
cd myproject
hub sync

# list latest open issues in the current repository
hub issue --limit 10

# open the current project's issues page
hub browse -- issues
#=> open https://github.com/github/hub/issues

# open another project's wiki
hub browse rbenv/ruby-build wiki
#=> open https://github.com/rbenv/ruby-build/wiki

# share log output via Gist
hub gist create --copy build.log
#=> (the URL of the new private gist copied to clipboard)
```

### api

https://hub.github.com/hub-api.1.html

ローレベルなAPIコール。

Example:

```sh
# 最新リリースを取得
hub api repos/:owner/:repo/releases/latest
```

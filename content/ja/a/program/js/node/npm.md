---
title: "npm"
linkTitle: "npm"
description: >
  https://www.npmjs.com
date: 2020-04-26T21:03:40+09:00
---

## Documentation

https://docs.npmjs.com/

- [CLI documentation | npm Documentation](https://docs.npmjs.com/cli-documentation/)

## CLI

Examples:

```sh
# help
npm help
npm help <command>

# バージョン表示
npm -v
```

### npm-install

https://docs.npmjs.com/cli-commands/install.html

パッケージをインストールする。

エイリアス: `i, add`

```sh
# 書式
npm install パッケージ [OPTIONS]

npm install [<@scope>/]<name>
npm install [<@scope>/]<name>@<version>

# package.json に従ってインストール
npm install
```

 Option | 説明
--------|-----
 -g|--global | global packageとしてインストール
 --no-save | （package.jsonの）**dependencies** に追加しない

### npm-ls

https://docs.npmjs.com/cli-commands/ls.html

インストールされたパッケージを一覧表示。

エイリアス: `list, la, ll`

```sh
npm ls [[<@scope>/]<pkg> ...]
```

### npm-uninstall

https://docs.npmjs.com/cli-commands/uninstall.html

インストールされたパッケージを削除する。

エイリアス: `remove, rm, un, unlink`

```sh
npm uninstall パッケージ [OPTIONS]
```

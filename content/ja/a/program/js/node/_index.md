---
title: "Node.js"
linkTitle: "Node.js"
description: >
  https://nodejs.org
date: 2020-04-26T20:47:51+09:00
---

## Documentation

- https://nodejs.org/api/

## パッケージマネージャー

- [npm](https://www.npmjs.com)
- [Yarn](https://classic.yarnpkg.com)

## Node.jsのバージョン管理

- [nodebrew](https://github.com/hokaccha/nodebrew)
- nvm

## Modules
### util
https://nodejs.org/api/util.html

#### util.format

https://nodejs.org/api/util.html#util_util_format_format_args

printfみたいなやつ。

console.logなどが内部的に利用しているそうだ。

参考:

- [%o 便利 - Qiita](https://qiita.com/yosuke_furukawa/items/7dc3b9fcf05148a57885)


## package.json

プロジェクトで使うNode.js modulesを管理するためのファイル。

### バージョン記法

参考:

- [package.json のチルダ(~) とキャレット(^) - Qiita](https://qiita.com/sotarok/items/4ebd4cfedab186355867)


#### チルダ表記 `~`

明記したところ以下のバージョンがあがることのみ許容

* `~1.1.2` = `1.1.2 <= version < 1.2.0`
* `~1.1` = `1.1.x` 
* `~1` = `1.x`

オリジナルの定義は、

> Allows patch-level changes if a minor version is specified on the comparator. Allows minor-level changes if not.

#### キャレット表記 `^`

一番左側にある、ゼロでないバージョニングは変えない (それ以下があがることは許容)

* `^1.2.3` := `1.2.3 <= version < 2.0.0`
* `^0.2.3` := `0.2.3 <= version < 0.3.0`
* `^0.0.3` := `0.0.3 <= version < 0.0.4`

オリジナルの定義は

> Allows changes that do not modify the left-most non-zero digit in the [major, minor, patch] tuple.

---
date: '2020-04-26T20:47:51+09:00'
description: 'https://nodejs.org

  '
---

# Node.js

## Documentation

- https://nodejs.org/api/

## パッケージマネージャー

- [npm](https://www.npmjs.com)
- [Yarn](https://classic.yarnpkg.com)

## Node.jsのバージョン管理

- [nodebrew](https://github.com/hokaccha/nodebrew)
- nvm
- [nodenv](https://github.com/nodenv/nodenv)

### nodenv

[rbenv](https://github.com/rbenv/rbenv) 系のバージョン管理ツール。プロジェクトのディレクトリに `.node-version` を置くと、そのバージョンの Node.js が使われる。

- Source: https://github.com/nodenv/nodenv
- [anyenv](../../../software/pkg-man/anyenv.md) で導入・管理できる。

```sh
anyenv install nodenv           # nodenv の導入
nodenv install --list           # 導入できる Node.js のバージョン
nodenv install 24.22.3          # Node.js の導入
echo 24.22.3 > .node-version    # このディレクトリ以下で使うバージョンを固定する
```

- バージョンの導入は、プラグインの [node-build](https://github.com/nodenv/node-build) が担う。anyenv 経由で nodenv を入れると、一緒に入る。
- 導入した直後は、`exec $SHELL -l` などでシェルを再起動する。
- `nodenv global <version>` を設定しないと、`.node-version` のないディレクトリでは Node.js が使えない(`system` の Node.js を使う)。
- 参考: [2020-04-28 のメモ](../../../memo/2020/20200428.md#macでanyenv経由のnodenv経由でnodejsを入れてみた)

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

---
title: "AWK"
linkTitle: "AWK"
date: 2020-06-23T22:49:24+09:00
weight: 10
---

## About

UNIX系OSでテキスト処理用途に用いられる。

プラットフォームによって実装が異なる。
https://en.wikipedia.org/wiki/AWK#Versions_and_implementations を参考に。

## Getting Started

参考:

- [Awk - A Tutorial and Introduction - by Bruce Barnett](https://www.grymoire.com/Unix/Awk.html#uh-0) ... NAWKとGAWKの違いについても述べられている

## Documentation

- [The GNU Awk User’s Guide](https://www.gnu.org/software/gawk/manual/gawk.html) ... gawk
  - 邦訳: [The GNU Awk User's Guide - Table of Contents](http://www.kt.rim.or.jp/~kbk/gawk-30/gawk_toc.html)
- https://linux.die.net/man/1/awk ... gawk

## awkコマンド

```sh
# AWKスクリプトが短いとき
command-output-text | awk '{ AWK SCRIPT }'
awk '{ AWK SCRIPT }' INPUT_FILE1 INPUT_FILE2...

# AWKスクリプトが長いとき
command-output-text | awk -f scirpt.awk
awk -f scirpt.awk INPUT_FILE1 INPUT_FILE2...

# おまけ: AWKスクリプトが実行可能なとき
command-output-text | scirpt.awk
```

 Option | 機能
--------|------
 `-F<c>` | フィールドの区切り文字を `<c>` に変える。例: `-F,` でカンマ区切り

## スクリプティング

```awk
#!/usr/bin/awk -f
BEGIN { print "start" }
      { print } # ループ処理
END   { print "end" }
```

Tips:

- `#` でコメントを書ける

NOTE:

- シバンに `#!/usr/bin/env awk -f` のように記すことはできない
  - See [CLI#シバン]({{<ref "/a/cli/_index.md">}}#シバン)

## Syntax
### 文字列の連結

単純にスペースでつなぐ。

```sh
awk '{print $1 "-" $2 "-" $3}' sample.tsv
```

参考:

- [awkの変数と文字列、正規表現のキホン - Qiita](https://qiita.com/tkykmw/items/89c67530c322baedb002 "awkの変数と文字列、正規表現のキホン - Qiita")

## 参考

- [AWK によるテキストのワンライナー処理クックブック集 - Qiita](https://qiita.com/key-amb/items/754a12eda28e7650a47c "AWK によるテキストのワンライナー処理クックブック集 - Qiita") ... 以前に自分でまとめたもの

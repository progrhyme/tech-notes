---
title: "diff"
linkTitle: "diff"
date: 2020-05-16T11:39:47+09:00
---

テキストファイルの差分を取るコマンド。

Examples:

```sh
# ディレクトリのdiff
diff -r dir1/ dir2/

# コマンドの出力結果を比較
diff <(command1) <(command2)
```

## 関連ツール

- git diff ... See [git#diff]({{<ref "/a/software/git/_index.md">}}#diff)

### colordiff

https://www.colordiff.org/

差分に色を付けて見やすくしてくれる。

公式ドキュメントには見つからないが、macOSならbrewでインストールできる。

```sh
brew install colordiff
```

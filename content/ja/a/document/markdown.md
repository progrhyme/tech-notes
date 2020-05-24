---
title: "Markdown"
linkTitle: "Markdown"
date: 2020-05-24T17:24:36+09:00
weight: 460
---

## CommonMark

https://commonmark.org/

Markdownの原典というべき仕様だが、表現力が乏しかったので亜種がたくさん生まれた。

## Markdownの亜種

- [GitHub Flavored Markdown](https://github.github.com/gfm/)
  - おそらく最も普及している亜種。GitHubでサポートされている。他の亜種もこの仕様を参考にしているものが多そう。デファクトといってもいいかも

## How-to
### バックティック「\`」のエスケープ

字の文で「\`」を表示するには、 `` \` `` のようにエスケープすればいい。

「\`」で囲んだコード内で「\`」を入力するにはどうすればよいか？  
このケースでは、エスケープはしなくていい。

下のように「\`\`」で囲み、ホワイトスペースを挟んで記述すると、 `` ` `` と表示される。

```Markdown
`` ` ``
```

MEMO:

- 2020-05-24 やり方がわからなくてググっていたら下の参考記事を見つけた。

参考:

- [Markdown のインラインコードでバックティックやバックスラッシュをエスケープする方法 - yu8mada](https://yu8mada.com/2018/06/15/how-to-escape-a-backtick-or-a-backslash-inside-inline-code-in-markdown/)

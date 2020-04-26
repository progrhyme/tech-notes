---
title: "Docsy"
linkTitle: "Docsy"
date: 2020-04-26T00:27:11+09:00
---

https://www.docsy.dev/

[Googleが2019年に公開した](https://mag.osdn.jp/19/07/11/162000)Hugoのテーマ。

事例が[ここ](https://www.docsy.dev/docs/examples/)に載っている。  
kubeflow, Knative, Apache Airflowなどで使われている。

20ページ以上のドキュメントサイトを作るときに向いている、と謳っている。  
多言語対応しており、プロダクトのバージョニングも考慮されている。

## Documentation

https://www.docsy.dev/docs/

## Getting Started

https://www.docsy.dev/docs/getting-started/

**Hugoの拡張版**が必要。  
これはSCSSを使っているためのようだ。

参考:

- [Error building site: POSTCSS: failed to transform &quot;scss/main.css&quot; · Issue #235 · google/docsy](https://github.com/google/docsy/issues/235)

### デモサイトのソースをcloneして使う

ふつうのHugo Themeなら、 `hugo new site` してconfig.tomlでthemeを指定すれば大体それっぽく動くのだけど、Docsyはやや作りが複雑なようなので、Exampleサイトのソースを再利用した方が早そう。

```sh
git clone https://github.com/google/docsy-example.git mydocs
cd mydocs
git submodule update --init --recursive
```

---
title: "『Goならわかるシステムプログラミング』"
linkTitle: "Goならわかるシステム…"
description: >
  [Goならわかるシステムプログラミング（紙書籍） – 技術書出版と販売のラムダノート](https://www.lambdanote.com/collections/frontpage/products/go)
date: 2020-05-31T16:18:05+09:00
---

## About

渋川さん（@shibu_jp）の著書。

関連リンク:

- [LambdaNote/errata-gosyspro-1-1: 『Goならわかるシステムプログラミング』正誤情報](https://github.com/LambdaNote/errata-gosyspro-1-1)
- Web連載版: [ASCII.jp：Goならわかるシステムプログラミング](http://ascii.jp/elem/000/001/235/1235262/)

その他:

- [yurakawa/learn-system-programming-with-go: 「Goならわかるシステムプログラミング」の写経](https://github.com/yurakawa/learn-system-programming-with-go)

## 第1章 Go言語で覗くシステムプログラミングの世界

### VS Code環境セットアップ

2018/8/26 記.

そもそも手元のUbuntu 16.04のGoのバージョンが1.7.1と古かったので、リリースされたばかりの11にバージョンアップした。

https://github.com/progrhyme/myenv/commit/15c06dab6adc6f98cae614b8422a6efc4c9b7bde

↑の変更を入れた上で、

```sh
cd /usr/local
mv go go-1.7.1
~/.myenv/script/install-golang.sh
```

VS Codeは最近入れたので省略。  
起動後、 [Goのextension](https://code.visualstudio.com/docs/languages/go)を入れた。

Goの静的解析ツールを色々入れる必要がある。  
最初、気づかなかったが、VS Codeの下のステータスバーみたいなやつの右に「Analysis Tools Missing」と表示されていて、クリックすると一式のインストールを促された。  
これらはgo getされて `$GOPATH/bin/` に配置される。

これで基本的には準備は終わりとのこと。

お約束の「Hello world!」を書いて、 `Debug > Start Without Debugging` を走らせてみる。  
…と、なんかエラー(？)になる。  
設定不備か何かわからないが、 なぜかプロジェクトディレクトリ下の `.vscode/launch.json` が開き、設定追加を促される。  
調べてもよくわからない。

VS Codeを再起動したらふつうに動いた。  
なんじゃこりゃ。。

参考:

- [Go開発環境構築(VSCode, gvm, delve, dep)からHello Worldするまで | Black Everyday Company](https://kuroeveryday.blogspot.com/2017/08/golang-hello-world.html)
- [[Visual Studio Code][Golang][Windows] VSCodeでGoの開発環境を作成する方法まとめ - Qiita](https://qiita.com/koara-local/items/8642d847831b6268d23e#%E5%8F%82%E8%80%83)

---
title: "JavaScript"
linkTitle: "JavaScript"
date: 2020-04-26T20:47:40+09:00
weight: 250
---

[JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript)

## Getting Started

- [JavaScript ガイド - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Guide "JavaScript ガイド - JavaScript | MDN")

Reference:

- [JavaScript リファレンス - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference "JavaScript リファレンス - JavaScript | MDN")
- [JavaScript and HTML DOM Reference](https://www.w3schools.com/jsref/ "JavaScript and HTML DOM Reference")

コーディング規約:

- [Google JavaScript Style Guide](https://google.github.io/styleguide/javascriptguide.xml "Google JavaScript Style Guide")
  - 非公式和訳: [Google JavaScript Style Guide 和訳 — Google JavaScript Style Guide 和訳](http://cou929.nu/data/google_javascript_style_guide/ "Google JavaScript Style Guide 和訳 — Google JavaScript Style Guide 和訳")
- https://github.com/felixge/node-style-guide
- 参考まとめ:
  - [JavaScriptのスタイルガイドまとめ(おすすめ4選) - Qiita](https://qiita.com/takeharu/items/dee0972e5f39bfd4d7c8 "JavaScriptのスタイルガイドまとめ(おすすめ4選) - Qiita")


## Reference
### Date

https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Date

### JSON

https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/JSON

SYNOPSIS:

```JavaScript
const obj = JSON.parse(str)
const str = JSON.stringify(obj)
```

## Tips

### デバッグ

- `debugger;` 文を埋め込む。

参考:

- [JavaScriptのデバッグ方法 – JSを嫌いにならないためのTips | プログラミング | POSTD](http://postd.cc/how-to-not-hate-javascript-tips-from-the-frontline/ "JavaScriptのデバッグ方法 – JSを嫌いにならないためのTips | プログラミング | POSTD")

### 日付と時刻の計算

- [【JavaScript】日付処理 - Qiita](https://qiita.com/kazu56/items/cca24cfdca4553269cab "【JavaScript】日付処理 - Qiita")
- [日付と時刻の計算 (JavaScript)](https://msdn.microsoft.com/ja-jp/library/ee532932%28v=vs.94%29.aspx "日付と時刻の計算 (JavaScript)")

## Topics
### var, let, constの使い分け

2017年12月現在、イマイチよくわかっていない。

参考:

- [JavaScriptにおけるvar/let/constの使い分け](https://sbfl.net/blog/2016/07/14/javascript-var-let-const/ "JavaScriptにおけるvar/let/constの使い分け")

### sprintfなさそう

Node.jsだとutilがある:

- https://nodejs.org/api/util.html

npmもある:

- https://www.npmjs.com/package/sprintf

"0"埋めとか半角スペースで埋める方法としては substr を使った例が出て来る:

- [Javascriptで文字列の０埋め、空白で右寄せでフォーマット - それマグで！](http://takuya-1st.hatenablog.jp/entry/2014/12/03/114154 "Javascriptで文字列の０埋め、空白で右寄せでフォーマット - それマグで！")

自作関数を作る例も出てくる:

- [Javascriptで日付・時刻をフォーマット表示 - Qiita](https://qiita.com/pseudo_foxkeh/items/9297a834bc8e05133e7a "Javascriptで日付・時刻をフォーマット表示 - Qiita")
- [日付フォーマットなど 日付系処理 - Qiita](https://qiita.com/osakanafish/items/c64fe8a34e7221e811d0 "日付フォーマットなど 日付系処理 - Qiita")

日付時刻については、固定フォーマットで出力する関数はある。

参考:

- [日付と時刻文字列 (JavaScript)](https://msdn.microsoft.com/ja-jp/library/ff743760(v=vs.94).aspx "日付と時刻文字列 (JavaScript)")
- [【Javascript入門】日付のフォーマット処理まとめ | 侍エンジニア塾ブログ | プログラミング入門者向け学習情報サイト](https://www.sejuku.net/blog/23064 "【Javascript入門】日付のフォーマット処理まとめ | 侍エンジニア塾ブログ | プログラミング入門者向け学習情報サイト")

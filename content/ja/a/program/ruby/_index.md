---
title: "Ruby"
linkTitle: "Ruby"
description: https://www.ruby-lang.org/
date: 2020-06-25T15:19:13+09:00
weight: 770
---

## About

リポジトリ:

- 公式: https://git.ruby-lang.org/
- ミラー: https://github.com/ruby/ruby
- 2019-04-22まではSVNだった

参考:

- [リポジトリガイド](https://www.ruby-lang.org/ja/documentation/repository-guide/)

## Topics
### 標準入出力

Rubyではインタプリタ起動時に標準入出力に対応するオブジェクトが定数に格納される。  
それらは以下の通り:

| 定数 | 値 |
|--------|----|
| STDIN | rubyプロセス起動時の標準入力。$stdinのデフォルト値 |
| $stdin | 標準入力 |
| STDOUT | rubyプロセス起動時の標準出力。$stdoutのデフォルト値 |
| $stdout | 標準出力 |
| STDERR | rubyプロセス起動時の標準エラー出力。$stderrのデフォルト値 |
| $stderr | 標準エラー出力 |

- STDIN, STDOUT, STDERRは[Objectクラス](https://docs.ruby-lang.org/ja/latest/class/Object.html)で定義されている。
- $stdin, $stdout, $stderrは[Kernelモジュール](https://docs.ruby-lang.org/ja/latest/class/Kernel.html)で定義されているグローバルスコープの変数。
- $stdinにIOオブジェクトを代入することで、入力をリダイレクトできる。
- $stdout, $stderrにIOオブジェクトを代入することで、出力をリダイレクトできる。

参考:

- [Rubyアソシエーション: 入出力](https://www.ruby.or.jp/ja/tech/development/ruby/tutorial/060_in_output.html)
- [Ruby で標準入出力のテスト - Qiita](https://qiita.com/key-amb/items/a134e2c3bea172b3deeb)

#### プロコンにおける標準入力の処理

```ruby
# 1行入力の場合
input = gets.chomp

# 複数行入力の場合
lines = $stdin.readlines  # 各要素は末尾に改行コードを含む
lines = $stdin.read.lines # 上に同じ
```

## Child Pages

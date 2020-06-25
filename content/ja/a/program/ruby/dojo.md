---
title: "Road to Rubyist"
linkTitle: "道場"
date: 2020-06-25T18:38:18+09:00
weight: 100
---

一人前のRubyistを名乗るために必要な基礎的なトピック群を取り扱う予定。

## コマンドライン引数

- `$0` 実行コマンド
- `ARGV` 引数（配列）

```ruby
# sample.rb
puts "$0：#{$0}"
ARGV.each_with_index do |arg, i|
  puts "ARGV[#{i}]：#{arg}"
end
```

実行例:

```sh
$ ruby sample.rb hoge piyo
$0：sample.rb
ARGV[0]：hoge
ARGV[1]：piyo
```

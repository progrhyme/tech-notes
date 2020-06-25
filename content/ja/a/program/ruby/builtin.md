---
title: "組み込みライブラリ"
linkTitle: "組込ライブラリ"
description: https://docs.ruby-lang.org/ja/latest/library/_builtin.html
date: 2020-06-25T15:30:32+09:00
weight: 20
---

## class Array

https://docs.ruby-lang.org/ja/latest/class/Array.html

.ancestors: Enumerable, Object, ...

Examples:

```ruby
[[:a, 3], [:b, 2], [:c, 1]].to_h #=> { a: 3, b: 2, c: 1 }
```

## class Dir

https://docs.ruby-lang.org/ja/latest/class/Dir.html

ディレクトリ操作のためのクラス。

SYNOPSIS:

```ruby
## path以下のファイルで.と..を除いたもの
Dir.children(path)
## カレントディレクトリ以下のファイルを再帰的に取得して配列で返す
Dir.glob('./**')

Dir.chdir(subdir) do
  # subdirにcdしてブロック内の処理を実行
  ...
end
```

## class File

https://docs.ruby-lang.org/ja/latest/class/File.html

ファイルアクセスのためのクラス。

- 親クラス: https://docs.ruby-lang.org/ja/latest/class/IO.html
- 定数: https://docs.ruby-lang.org/ja/latest/class/File=3a=3aConstants.html

SYNOPSIS:

```ruby
if File.exist?(path)
  :
end

File.open('foo.txt') do |file|
  # 1行ずつ読込み
  file.each_line do |line|
    fields = line.chomp.split(/,/)
    :
  end
end

## 1行ずつ処理する他のやり方
File.foreach('foo.txt') { |line| ... }
File.readlines('foo.txt').each { |line| ... }

## まとめて書き込んで閉じる
File.write('out.dat', data)

## 追記モードで開く
File.open('out.dat', File::WRONLY|File::CREAT|File::APPEND) do |file|
  # 排他ロック取得
  file.flock(File::LOCK_EX)
  # 1行ずつ書き込み
  contents.each_line do |line|
    file.puts(line)
  end
end

require 'pathname'
abs_path = Pathname.new(File.expand_path('.')).join(filename)
```

ファイルオープン時のモードについて:

- See https://docs.ruby-lang.org/ja/latest/method/Kernel/m/open.html


参考:

- [【Ruby】よく使うFileクラスを使ったファイル読み込み処理 - Qiita](https://qiita.com/mogulla3/items/fbc2a46478872bebbc47)
- [[Ruby]IO、File、Dirクラスのメソッド - Qiita](https://qiita.com/fkm_y/items/9edbd45652526688de6d)


## class Hash

https://docs.ruby-lang.org/ja/latest/class/Hash.html

.ancestors: Enumerable, Object, ...

Examples:

```ruby
h = { a: 3, b: 2, c: 1 }
h.to_a #=> [[:a, 3], [:b, 2], [:c, 1]]
```


## class Integer

https://docs.ruby-lang.org/ja/latest/class/Integer.html

整数クラス。  
Ruby 2.4から、FixnumとBignumがIntegerに統合された。  
いずれもIntegerのエイリアスとなっている。

参考:

- [Ruby 2.4でIntegerに一本化される整数 - Qiita](https://qiita.com/jkr_2255/items/647c427d2c2f7892fa93)

## class IO

https://docs.ruby-lang.org/ja/latest/class/IO.html

継承ツリー: IO < Enumerable < File::Constants < Object < Kernel < BasicObject

### #read

https://docs.ruby-lang.org/ja/latest/method/IO/i/read.html

```ruby
read(length = nil, outbuf = "") -> String | nil
```

lengthバイト読み込んで、その文字列を返す。

## class Module

https://docs.ruby-lang.org/ja/latest/class/Module.html

### .const_defined? , .const_get

定数定義を調べる。

NOTE:

- 上の階層で定義された定数も参照できる。つまり、 `Foo::Bar` が存在する時、 `Foo::Baz::Bar` が存在しなくても、 `Foo::Baz.const_defined?(:Bar)` は true になる。
  - `Foo::Baz.const_defined?(:Bar, false)` は false
  - 詳しくは下記リンク先、または上のリファレンスマニュアルを参照

参考:

- [Ruby: const_defined? / const_get の罠 – CLARA ONLINE techblog](http://techblog.clara.jp/2014/09/ruby-const_defined-const_get/)


## class Random

https://docs.ruby-lang.org/ja/latest/class/Random.html

擬似乱数生成クラス。

SYNOPSIS:

```ruby
v = Random.rand # Kernel.#rand と同じ

rng = Random.new(Time.now.to_i) # 乱数ジェネレータを作る
rng.rand
rng.rand(10)
rng.rand(0..5)
rng.rand(1.0..3.0)

rng.seed # 乱数の種を返す
```

NOTES:

- Random.rand や Kernel.#rand はデフォルトの乱数ジェネレータである [Random::DEFAULT](https://docs.ruby-lang.org/ja/latest/method/Random/c/DEFAULT.html) を使う。

## class Regexp

https://docs.ruby-lang.org/ja/latest/class/Regexp.html

継承ツリー: Regexp < Object（以下略）

正規表現。

関連項目:

- [言語仕様#正規表現]({{<ref "spec.md">}}#正規表現)

### #match

https://docs.ruby-lang.org/ja/latest/method/Regexp/i/match.html

```ruby
match(str, pos = 0) -> MatchData | nil
match(str, pos = 0) {|m| ... } -> object | nil
```

Examples:

```ruby
p(/(.).(.)/.match("foobar", 3).captures)   # => ["b", "r"]
p(/(.).(.)/.match("foobar", -3).captures)  # => ["b", "r"]
```

## class String

https://docs.ruby-lang.org/ja/latest/class/String.html

継承ツリー:

```
String < Comparable < Object < Kernel < BasicObject
```

文字列クラス。

### #%

https://docs.ruby-lang.org/ja/latest/method/String/i/=25.html

```ruby
self % args -> String
```

printfと同じ規則に従ってargsをフォーマットする

Examples:

```ruby
p "i = %d" % 10       # => "i = 10"
p "i = %x" % 10       # => "i = a"
p "i = %o" % 10       # => "i = 12"

p "i = %#d" % 10      # => "i = 10"
p "i = %#x" % 10      # => "i = 0xa"
p "i = %#o" % 10      # => "i = 012"

p "%d" % 10           # => "10"
p "%d,%o" % [10, 10]  # => "10,12"
```

### #gsub

https://docs.ruby-lang.org/ja/latest/method/String/i/gsub.html

```ruby
gsub(pattern, replace) -> String
```

patternにマッチする部分全てを文字列replaceに置換した文字列を生成して返す。

Examples:

```ruby
p 'abcdefg'.gsub(/def/, '!!')          # => "abc!!g"
p 'abcabc'.gsub(/b/, '<<\&>>')         # => "a<<b>>ca<<b>>c"
p 'xxbbxbb'.gsub(/x+(b+)/, 'X<<\1>>')  # => "X<<bb>>X<<bb>>"
p '2.5'.gsub('.', ',') # => "2,5"
```

NOTE:

- 後方参照は「\1」「\2」...
- 置換文字列に `\` を使いたいときはエスケープが必要

### #match

https://docs.ruby-lang.org/ja/latest/method/String/i/match.html

```ruby
match(regexp, pos = 0) -> MatchData | nil
match(regexp, pos = 0) {|m| ... } -> object
```

regexp.match(self, pos) と同じ。  
See [Regexp#match](#match)

Examples:

```ruby
'hello'.match('(.)\1')      # => #<MatchData "ll" 1:"l">
'hello'.match('(.)\1')[0]   # => "ll"
'hello'.match(/(.)\1/)[0]   # => "ll"
'hello'.match('xx')         # => nil
```

### #split

https://docs.ruby-lang.org/ja/latest/method/String/i/split.html

```ruby
split(sep = $;, limit = 0) -> [String]
split(sep = $;, limit = 0) {|s| ... } -> self
```

Specs:

- 第1引数 sep で指定されたセパレータによって文字列を limit 個まで分割し、結果を文字列の配列で返す
- ブロックを指定すると、配列を返す代わりに分割した文字列でブロックを呼び出す
- sepがnilの場合は、前後の空白文字をstripした上で `$;` or 空白文字列で分割

Examples:

```ruby
p "   a \t  b \n  c".split(/\s+/) # => ["", "a", "b", "c"]

p "   a \t  b \n  c".split(nil)   # => ["a", "b", "c"]
p "   a \t  b \n  c".split(' ')   # => ["a", "b", "c"]   # split(nil) と同じ
p "   a \t  b \n  c".split        # => ["a", "b", "c"]   # split(nil) と同じ
```


## class Time

https://docs.ruby-lang.org/ja/latest/class/Time.html

.ancestors: [Comparable](https://docs.ruby-lang.org/ja/latest/class/Comparable.html), Object, ...

SYNOPSIS:

```ruby
Time.at(0)          #=> 1970-01-01 09:00:00 +0900
Time.at(1531046422) #=> 2018-07-08 19:40:22 +0900
Time.now            #=> 2018-07-08 19:40:22 +0900
Time.now.to_i       #=> 1531046422
```

参考:

- [RubyでUNIXTIME変換 - Qiita](https://qiita.com/mogulla3/items/195ae5d8ad574dfc6baa)

## module Enumerable

https://docs.ruby-lang.org/ja/latest/class/Enumerable.html

SYNOPSIS:

```ruby
(1..3).to_a.include?(3) #=> true

## イテレーション
%w(foo bar baz).each_with_index do |s, i|
  puts "Index: #{i}, Value: #{s}"
end

## 配列操作
(0..9).to_a.reject { |n| n % 2 == 1 } #=> [1, 3, 5, 7, 9]

### sort
h = { a: 3, b: 2, c: 1 }
h.sort_by { |kv| kv[1] } #=> [[:c, 1], [:b, 2], [:a, 3]
```

NOTES:

- `#sort` は安定ではない(=同じ要素が元の順序通りに並ばない)。また、比較処理が重い場合の性能が `#sort_by` より悪い。


## module Kernel

https://docs.ruby-lang.org/ja/latest/class/Kernel.html

全てのクラスから参照できるメソッドを定義している。

### .#open

https://docs.ruby-lang.org/ja/latest/method/Kernel/m/open.html

fileをオープンしてIO(File含む)オブジェクトを返す。  

SYNOPSIS:

```ruby
open(file) do |f|
  f.each_line { |l| ... }
end

open(file, 'w') do |f|
  f.write(content)
end
```

### .#require

https://docs.ruby-lang.org/ja/latest/method/Kernel/m/require.html

```Ruby
require(feature) -> bool
```

Specs:

- 拡張子補完を行う
- 同じファイルの複数回ロードはしない

#### ロードするパスの追加方法

シェルでやる例:

```sh
ruby -I /path/to/lib foo.rb
RUBYLIB=/path/to/lib foo.rb
```

Rubyコード内でやる例:

```ruby
$LOAD_PATH.push('/path/to/lib')
```

参考:

- 2008年10月 [require がロードするファイルを探すパスに追加をする - make world](https://littlebuddha.hatenadiary.org/entry/20081020/1224483302)

### 乱数

- [.#rand](https://docs.ruby-lang.org/ja/latest/method/Kernel/m/rand.html)
- [.#srand](https://docs.ruby-lang.org/ja/latest/method/Kernel/m/srand.html)

SYNOPSIS:

```ruby
srand(Time.now.to_i) # UNIXタイムスタンプで乱数の種を生成
                     # ※やらなくても最初にrand等を実行したときにランダムに設定してくれる

rand            # [0, 1) の実数
rand(10)        # [0, 10) の整数
rand(5.5)       # rand(5)と同じ。[0, 5) の整数

rand(1..6)      # [1, 6] の整数
rand(0...10)    # [1, 10) の整数
rand(1.0..1.5)  # [1.0, 1.5] の実数
rand(1.0...1.5) # [1.0, 1.5) の実数
rand(1..0)      #=> nil
```

See also: https://docs.ruby-lang.org/ja/latest/class/Random.html

### キャストっぽいメソッド

- .Array ... 配列に変換
- .Float ... 浮動小数点数に変換
- .Hash ... [Hash](https://docs.ruby-lang.org/ja/latest/class/Hash.html)に変換
- [.Integer](https://docs.ruby-lang.org/ja/latest/method/Kernel/m/Integer.html) ... 整数を返す。
  - `Integer(arg, base = 0) -> Integer`
- .Rational ... 有理数([Rational](https://docs.ruby-lang.org/ja/latest/class/Rational.html))に変換
- .String ... 文字列に変換

Examples:

```ruby
# .Integer
Integer(4) #=> 4
Integer(9.5) #=> 9

# 2進数
Integer("11", 2) #=> 3
# 10進数
Integer("10") #=> 10
```

## module Math

https://docs.ruby-lang.org/ja/latest/class/Math.html

浮動小数点演算や各種数学関数。

```ruby
Math.log(x)    # eを底とするxの対数
Math.log(x, y) # yを底とするxの対数
```

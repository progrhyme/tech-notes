---
title: "言語仕様"
linkTitle: "言語仕様"
date: 2020-06-25T15:26:36+09:00
weight: 10
---

## リテラル

https://docs.ruby-lang.org/ja/latest/doc/spec=2fliteral.html

### %記法

https://docs.ruby-lang.org/ja/latest/doc/spec=2fliteral.html#percent

一覧:

 構文         | 意味
-------------|------------------
 `%!STRING!` | ダブルクォート文字列
 `%Q!STRING!` | 同上
 `%q!STRING!` | シングルクォート文字列
 `%x!STRING!` | コマンド出力
 `%r!STRING!` | 正規表現
 `%w!STRING!` | 要素が文字列の配列(空白区切り)
 `%W!STRING!` | 要素が文字列の配列(空白区切り)。式展開、バックスラッシュ記法が有効
 `%s!STRING!` | シンボル。式展開、バックスラッシュ記法は無効
 `%i!STRING!` | 要素がシンボルの配列(空白区切り)
 `%I!STRING!` | 要素がシンボルの配列(空白区切り)。式展開、バックスラッシュ記法が有効

Tips:

- `!` だけではなく、色んな記号が区切り文字として使える

Examples:

```ruby
%w(foo bar baz)  #=> ['foo', 'bar, 'baz']
%i(foo\ bar baz) #=> [:"foo bar", :baz]
```

## 変数

### クラス変数、インスタンス変数、クラスインスタンス変数について

- [【まとめ】インスタンス変数、クラス変数、クラスインスタンス変数 - Qiita](http://qiita.com/mogulla3/items/cd4d6e188c34c6819709)
  - 初心者向けのかんたんな説明
- [徒然なるままに｜Rubyの継承についてのはなし（インスタンス変数,クラス変数,クラスインスタンス変数,インスタンスメソッド,クラスメソッド,定数）](http://kamiyasu2.blog.fc2.com/blog-entry-35.html)
  - 上よりも詳しめの解説
- [Rubyでクラスインスタンス変数にインスタンスメソッドからアクセス | EasyRamble](http://easyramble.com/ruby-class-instance-variable.html)

### クラス変数

- `@@` で始まる。
- 継承先と共有されるので、むやみに使うべきではない。

### インスタンス変数

- `@` で始まる。

### クラスインスタンス変数

- `@` で始まる。

## 演算子

演算子式: https://docs.ruby-lang.org/ja/latest/doc/spec=2foperator.html

### 演算子式の定義

再定義できる演算子(メソッド)の定義方法:

https://docs.ruby-lang.org/ja/latest/doc/spec=2fdef.html#operator

特に、単項演算子について:

```ruby
def +@  # +obj
def -@  # -obj
```

## ヒアドキュメント

https://docs.ruby-lang.org/ja/latest/doc/spec=2fliteral.html#here

```ruby
  # 終端行をインデントできない
  puts <<EOS
:
EOS

  # 終端行をインデントできる
  puts <<-EOS
    :
  EOS

  # since v2.3
  # 終端行をインデントできる。途中の行はアンインデントされる
  puts <<~EOS
    :
  EOS
```

参考:

- [Ruby のヒアドキュメントすごい - Qiita](http://qiita.com/Linda_pp/items/32fddbbe117cf03fef0f)
- https://github.com/ruby/ruby/blob/v2_3_0/NEWS

## 正規表現

https://docs.ruby-lang.org/ja/latest/doc/spec=2fregexp.html

## 継承、Mix-in

違うようだが、似ているところもある。

- 継承 `Child < Parent`
- include
- extend
- prepend

include されたとき、継承されたとき、prepend されたときにフックを仕込むことができる。

- inherited
- included
- extended
- prepended

参考:
- http://ref.xaio.jp/ruby/classes/class/inherited
- http://ref.xaio.jp/ruby/classes/module/included
- http://ref.xaio.jp/ruby/classes/module/extended
- https://docs.ruby-lang.org/ja/latest/method/Module/i/prepended.html

### メソッドの探索

具象クラスで定義していないメソッドを実行したとき、継承ツリーを順に辿って、最初に見つかったものが実行される。  
この時の順番は、任意のクラス A に対して、 `A.ancestors` を実行して得られる配列の先頭からとなる。  

```ruby
module M
  def foo
    :m_foo
  end
end

class P
  def foo
    :p_foo
  end
end

class C < P
  include M
end

C.ancestors #=> [C, M, P, Object, PP::ObjectMixin, Kernel, BasicObject]
C.new.foo #=> :m_foo
```

参考:

- [継承, mix-in, include, extend について覚え書き - かせいさんとこ](http://d.hatena.ne.jp/kasei_san/20091021/p1)
- [[Ruby] モジュールの include と クラス継承 - Qiita](https://qiita.com/ksh-fthr/items/6c2b3b231bf26dc5a4e0)

### include されたときにクラスメソッドを追加する

例:

```ruby
module M
  module ClassMethods
    attr_accessor :rw_prop
    attr :ro_prop

    def set_ro_prop(x)
      @ro_prop = x
    end
  end

  def self.included(klass)
    klass.extend ClassMethods
    p "#{klass} extend #{self}::ClassMethods"
  end
end

class A
  include M #=> "A extend M::ClassMethods"
end

p A.rw_prop     = :rw #=> nil
p A.set_ro_prop = :ro #=> :ro
p A.ro_prop     = :ro #=> NoMethodError
```

参考:
- [» ActiveSupport::Concern でハッピーなモジュールライフを送る TECHSCORE BLOG](http://www.techscore.com/blog/2013/03/22/activesupportconcern-%E3%81%A7%E3%83%8F%E3%83%83%E3%83%94%E3%83%BC%E3%81%AA%E3%83%A2%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB%E3%83%A9%E3%82%A4%E3%83%95%E3%82%92%E9%80%81%E3%82%8B/)
- [Ruby でクラスインスタンス変数に対するアクセサの作り方 - Qiita](http://qiita.com/key-amb/items/a9f7d71be66446d85b70)

## 例外処理

https://docs.ruby-lang.org/ja/latest/doc/spec=2fcontrol.html#begin

```ruby
begin
  if a
    raise AisError, "#{a} happened!"
  elsif b
    raise "runtime error!"
  end
rescue AisError => e
  log.warn("#{e.inspect}")
rescue => e
  log.error("Unknown Error! Error: #{e.inspect} at #{e.backtrace}")
else
  # 例外が起きなかったとき
  p "success."
ensure
  # エラーが起きてもここは必ず実行される
  clean_up
end
```

ここで、 `ensure` 節は `rescue` による救済処理よりも先に実行されることに注意。

参考:
- [begin~rescue~ensureとraiseを利用した例外処理の流れと捕捉について - Qiita](http://qiita.com/ktarow/items/9d8f3217bb148f2e51d2 "begin~rescue~ensureとraiseを利用した例外処理の流れと捕捉について - Qiita")

## 無名関数

```ruby
# proc
foo = Proc.new { ... }.call
foo = proc { ... }.call

# lambda
foo = lambda { ... }.call
foo = -> { ... }.call
```

`.call` を使わずにスコープ内のクロージャとして使うこともできる。

```ruby
func = -> { ... }
x = func.call
```

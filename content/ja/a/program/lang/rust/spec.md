---
title: "言語仕様"
linkTitle: "言語仕様"
date: 2020-05-25T02:02:45+09:00
weight: 3200
---

リファレンスについては See [Rust#Documentation]({{<ref "_index.md">}}#documentation)

## 変数

Rustでは変数はデフォルトでイミュータブル（変更不可）。

Examples:

```Rust
let foo = 5; // immutable
let mut bar = 5; // mutable
```

参考:

- [Variables and Mutability - The Rust Programming Language](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html#variables-and-mutability)

## 型

- String provided by [Struct std::string::String]({{<ref "std.md">}}#string-1)

### Associated Function

いわゆる静的メソッド。

例: `String::new`

## 参照

`&` がつくと参照を表す。

Examples:

```Rust
// 例1
use std::io;

fn main() {
  let mut guess = String::new();
    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");
}

// 例2
fn main() {
    let s1 = String::from("hello");
    let len = calculate_length(&s1);
    println!("The length of '{}' is {}.", s1, len);
}

fn calculate_length(s: &String) -> usize {
    s.len()
}
```

参考:

- [References and Borrowing - The Rust Programming Language](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html)

## Attributes（アトリビュート）

https://doc.rust-lang.org/reference/attributes.html

- [アトリビュート - Rust By Example 日本語版](https://doc.rust-jp.rs/rust-by-example-ja/attribute.html)

> モジュール、クレート、要素に対するメタデータ

用途:

- コンパイル時の条件分岐
- クレート名、バージョン、種類の設定
- Lintの無効化
- コンパイラ付属の機能（マクロ、グロブ、インポートなど）の使用
- 外部ライブラリへのリンク
- ユニットテスト用の関数を明示
- ベンチマーク用の関数を明示

Syntax:

```
InnerAttribute:
   #![<Attr>]

OuterAttribute:
   #[<Attr>]

Attr:
    SimplePath <AttrInput>?

AttrInput:
    DelimTokenTree
    | = LiteralExpression (without suffix)
```

NOTE:

- `#![<Attr>]` はcrate attribute（クレート全体に適用）
- `#[<Attr>]` はitem attribute（モジュール or 要素に適用）

Examples:

```Rust
// General metadata applied to the enclosing module or crate.
#![crate_type = "lib"]

// A function marked as a unit test
#[test]
fn test_foo() {
    /* ... */
}

// A conditionally-compiled module
#[cfg(target_os = "linux")]
mod bar {
    /* ... */
}

// A lint attribute used to suppress a warning/error
#[allow(non_camel_case_types)]
type int8_t = i8;

// Inner attribute applies to the entire function.
fn some_unused_variables() {
  #![allow(unused_variables)]

  let x = ();
  let y = ();
  let z = ();
}
```

Attributesの種類:

- Built-in attributes
- Macro attributes
- Derive macro helper attributes
- Tool attributes

### Derive（継承）

https://doc.rust-lang.org/reference/attributes/derive.html

- [Derive - Rust By Example](https://doc.rust-lang.org/stable/rust-by-example/trait/derive.html)
- [継承(Derive) - Rust By Example 日本語版](https://doc.rust-jp.rs/rust-by-example-ja/trait/derive.html)

`[#derive]` アトリビュートによって、型に対して特定のトレイト実装をMixinすることができる。
同名のトレイトを手動実装して挙動をカスタマイズすることも可能。

derive可能なトレイト:

- Eq, PartialEq, Ord, PartialOrd ... 型の比較
- Clone ... コピーによって `&T` から `T` を作成
- Copy ... `=` 演算子を使用したときに所有権の移動ではなくクローンを行う。 `Copy` を実装するには `Clone` も実装されている必要がある
- Hash ... ハッシュ値の計算
- Default ... 空インスタンスを作成
- Debug ... `{:?}` によって値をフォーマット

Examples:

```Rust
// `Centimeters`, a tuple struct that can be compared
// `Centimeters`は比較可能なタプルになる
#[derive(PartialEq, PartialOrd)]
struct Centimeters(f64);

// `Inches`, a tuple struct that can be printed
// `Inches`はプリント可能なタプルになる
#[derive(Debug)]
struct Inches(i32);

impl Inches {
    fn to_centimeters(&self) -> Centimeters {
        let &Inches(inches) = self;

        Centimeters(inches as f64 * 2.54)
    }
}

// `Seconds`, a tuple struct with no additional attributes
// `Seconds`には特にアトリビュートを付け加えない。
struct Seconds(i32);

fn main() {
    let _one_second = Seconds(1);

    // Error: `Seconds` can't be printed; it doesn't implement the `Debug` trait
    //println!("One second looks like: {:?}", _one_second);
    // TODO ^ この行をアンコメントしてみましょう。

    // Error: `Seconds` can't be compared; it doesn't implement the `PartialEq` trait
    //let _this_is_true = (_one_second == _one_second);
    // TODO ^ この行をアンコメントしてみましょう

    let foot = Inches(12);

    println!("One foot equals {:?}", foot);

    let meter = Centimeters(100.0);

    let cmp =
        if foot.to_centimeters() < meter {
            "smaller"
        } else {
            "bigger"
        };

    println!("One foot is {} than one meter.", cmp);
}
```


参考:

- [Rustの構造体などに追加できる振る舞いを確認する - Qiita](https://qiita.com/apollo_program/items/2495dda519ae160971ed)

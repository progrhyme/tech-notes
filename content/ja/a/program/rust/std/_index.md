---
title: "std Library"
linkTitle: "std"
description: https://doc.rust-lang.org/std/
date: 2020-05-25T01:21:21+09:00
weight: 800
---

Rustの標準ライブラリ。

## プリミティブ型
### str

https://doc.rust-lang.org/std/primitive.str.html

See also [Module std::str](#str-1)

"string slice" とも呼ばれる。

Examples:

```Rust
let hello = "Hello, world!";

// with an explicit type annotation
let hello: &'static str = "Hello, world!";
```

## マクロ
### eprint

[Macro std::eprint](https://doc.rust-lang.org/std/macro.eprint.html)

標準エラー出力（[io::stderr]({{<ref "io.md">}}#stderr-struct)）に書き込む以外は[print!](#print)と同じ。

Examples:

```Rust
eprint!("Error: Could not complete task");
```

### eprintln

[Macro std::eprintln](https://doc.rust-lang.org/std/macro.eprintln.html)

[println!](#println)の標準エラー出力版。

### format

[Macro std::format](https://doc.rust-lang.org/std/macro.format.html)

書式指定付きで `String` を作る。  
書式についての詳細は[std::fmt]({{<ref "fmt.md">}})を見よ。

ふつうは文字列の結合や補間に用いられる。

値を文字列に変換するには、[to_string](#tostring-trait)を用いると良い。

Examples:

```Rust
format!("Hello");                 // => "Hello"
format!("Hello, {}!", "world");   // => "Hello, world!"
format!("The number is {}", 1);   // => "The number is 1"
format!("{:?}", (3, 4));          // => "(3, 4)" Debug output
format!("{value}", value=4);      // => "4"
format!("{} {}", 1, 2);           // => "1 2"
format!("{:04}", 42);             // => "0042" with leading zeros
```

### print

[Macro std::print](https://doc.rust-lang.org/std/macro.print.html)

標準出力（[io::stdout]({{<ref "io.md">}}#stdout-struct)）に書き込む。  
改行しないことを除いて `println` と同等。

`format!` と同じ書式指定が可能。See [std::fmt]({{<ref "fmt.md">}})

バッファリングされる可能性があるので、明示的に[io::stdout().flush()](#flush-required-method)を実行する必要があるかもしれない。

エラー出力には[eprint!](#eprint)を使うこと。

### println

[Macro std::println](https://doc.rust-lang.org/std/macro.println.html)

Examples:

```Rust
println!(); // prints just a newline
println!("hello there!");
println!("format {} arguments", "some");
```

## ops (Module)

[Module std::ops](https://doc.rust-lang.org/std/ops/)

オーバーロード可能な演算子。  
このモジュールで定義されたトレイトを実装することで、各種演算子のオーバーロードを可能にする。

Examples:

```Rust
use std::ops::{Add, Sub};

#[derive(Debug, PartialEq)]
struct Point {
    x: i32,
    y: i32,
}

impl Add for Point {
    type Output = Point;

    fn add(self, other: Point) -> Point {
        Point {x: self.x + other.x, y: self.y + other.y}
    }
}

impl Sub for Point {
    type Output = Point;

    fn sub(self, other: Point) -> Point {
        Point {x: self.x - other.x, y: self.y - other.y}
    }
}

assert_eq!(Point {x: 3, y: 3}, Point {x: 1, y: 0} + Point {x: 2, y: 3});
assert_eq!(Point {x: -1, y: -3}, Point {x: 1, y: 0} - Point {x: 2, y: 3});
```

### Deref (Trait)

[Trait std::ops::Deref](https://doc.rust-lang.org/std/ops/trait.Deref.html)

`*v` のように、イミュータブルなデリファレンスの演算に使われる。

ガイド:

- [Derefトレイトにより、参照を通してデータにアクセスできる - The Rust Programming Language](https://doc.rust-jp.rs/book/second-edition/ch15-02-deref.html)

## path (Module)

[Module std::path](https://doc.rust-lang.org/std/path/index.html)

クロスプラットフォームなパス操作機能を提供する。

Examples:

```Rust
use std::path::Path;
use std::ffi::OsStr;

let path = Path::new("/tmp/foo/bar.txt");

let parent = path.parent();
assert_eq!(parent, Some(Path::new("/tmp/foo")));

let file_stem = path.file_stem();
assert_eq!(file_stem, Some(OsStr::new("bar")));

let extension = path.extension();
assert_eq!(extension, Some(OsStr::new("txt")));

// パスの作成や変更
use std::path::PathBuf;

// This way works...
let mut path = PathBuf::from("c:\\");

path.push("windows");
path.push("system32");

path.set_extension("dll");

// ... but push is best used if you don't know everything up
// front. If you do, this way is better:
let path: PathBuf = ["c:\\", "windows", "system32.dll"].iter().collect();
```

### PathBuf (Struct)

[Struct std::path::PathBuf](https://doc.rust-lang.org/std/path/struct.PathBuf.html#method.display)

ミュータブルなパス。[String](#string-struct)と同族。

#### display (Method from Deref)

https://doc.rust-lang.org/std/path/struct.PathBuf.html#method.display

`pub fn display(&self) -> Display`

[Trait fmt::Display]({{<ref "fmt.md">}}#display-trait)を実装したオブジェクトを返す。

Examples:

```Rust
use std::path::Path;

let path = Path::new("/tmp/foo.rs");

println!("{}", path.display());
```

## prelude (Module)

[Module std::prelude](https://doc.rust-lang.org/std/prelude/)

全てのRustプログラムで自動的にimportされる必要最小限のライブラリ。  
`std::io::prelude` のように、独自のpreludeを持つライブラリも多いそうだ。

## result (Module)

[Module std::result](https://doc.rust-lang.org/std/result/)

`Result` 型によるエラーハンドリングを行う。

### Result (Enum)

[Enum std::result::Result](https://doc.rust-lang.org/std/result/enum.Result.html)

```Rust
pub enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

success or failureを表す型。

Variants:

- `Ok(T)` ... success valueを保持する
- `Err(E)` ... error valueを保持する

#### expect (Method)

https://doc.rust-lang.org/std/result/enum.Result.html#method.expect

`pub fn expect(self, msg: &str) -> T`

- 値が `Err` ならメッセージ付きでパニックする

Examples:

```Rust
let x: Result<u32, &str> = Err("emergency failure");
x.expect("Testing expect"); // panics with `Testing expect: emergency failure`
Run
```

#### unwrap (Method)

https://doc.rust-lang.org/std/result/enum.Result.html#method.unwrap

`pub fn unwrap(self) -> T`

- 値が `Err` ならパニックする

Examples:

```Rust
let x: Result<u32, &str> = Err("emergency failure");
x.unwrap(); // panics with `emergency failure`
```

## str (Module)

[Module std::str](https://doc.rust-lang.org/std/str/)

See also [プリミティブ型 str](#str)

## string (Module)

[Module std::string](https://doc.rust-lang.org/std/string/)

UTF-8エンコード。

### String (Struct)

[Struct std::string::String](https://doc.rust-lang.org/std/string/struct.String.html)

See also [プリミティブ型 str](#str)

Examples:

```Rust
let s = String::new();

let hello1 = String::from("Hello, world!");

let mut hello2 = String::from("Hello, ");

hello2.push('w');
hello2.push_str("orld!");
```

#### new (Method)

[Method String::new](https://doc.rust-lang.org/std/string/struct.String.html#method.new)

`pub const fn new() -> String`

空の `String` を生成する。
デフォルトでバッファを割り当てないので低コストだが、利用するバッファ量がわかっているならば、 `with_capacity` メソッドを代わりに使うことを検討せよ。

### ToString (Trait)

[Trait std::string::ToString](https://doc.rust-lang.org/std/string/trait.ToString.html)

値を `String` に変換するためのトレイト。  
`ToString` は直接実装すべきではない。[Display](#display-trait)を実装することで、 `ToString` の実装が得られる。

#### to_string (Require Method)

`fn to_string(&self) -> String`

Examples:

```Rust
let i = 5;
let five = String::from("5");

assert_eq!(five, i.to_string());
```

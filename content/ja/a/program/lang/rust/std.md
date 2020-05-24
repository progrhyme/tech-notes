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

## io

[Module std::io](https://doc.rust-lang.org/std/io/index.html)

基礎的なI/O機能を提供する。

### stdin

[Function std::io::stdin](https://doc.rust-lang.org/std/io/fn.stdin.html)

`pub fn stdin() -> Stdin`

当該プロセスの新しい標準入力ハンドルを生成する。

Examples:

```Rust
// Using implicit synchronization
use std::io::{self, Read};

fn main() -> io::Result<()> {
    let mut buffer = String::new();
    io::stdin().read_to_string(&mut buffer)?;
    Ok(())
}
```

### Stdin

[Struct std::io::Stdin](https://doc.rust-lang.org/std/io/struct.Stdin.html)

プロセスの標準入力ストリームのハンドル。  
個々のハンドルは、当該プロセスに対する入力データのグローバルバッファの参照を共有する。
ハンドルは `BufRead` メソッドにフルアクセスを得るためにロックされることがある。

Examples:

```Rust
use std::io;

let mut input = String::new();
match io::stdin().read_line(&mut input) {
    Ok(n) => {
        println!("{} bytes read", n);
        println!("{}", input);
    }
    Err(error) => println!("error: {}", error),
}
```

#### read_line

[Method Stdin::read_line](https://doc.rust-lang.org/std/string/struct.String.html#method.new)

`pub fn read_line(&self, buf: &mut String) -> Result<usize>`

当該ハンドルをロックして入力行を読み込む。

詳しくは [BufRead::read_line](https://doc.rust-lang.org/std/io/trait.BufRead.html#method.read_line) を見よ。

## prelude

[Module std::prelude](https://doc.rust-lang.org/std/prelude/)

全てのRustプログラムで自動的にimportされる必要最小限のライブラリ。  
`std::io::prelude` のように、独自のpreludeを持つライブラリも多いそうだ。

## str

[Module std::str](https://doc.rust-lang.org/std/str/)

See also [プリミティブ型 str](#str)

## string

[Module std::string](https://doc.rust-lang.org/std/string/)

### String

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

#### new

[Method String::new](https://doc.rust-lang.org/std/string/struct.String.html#method.new)

`pub const fn new() -> String`

空の `String` を生成する。
デフォルトでバッファを割り当てないので低コストだが、利用するバッファ量がわかっているならば、 `with_capacity` メソッドを代わりに使うことを検討せよ。

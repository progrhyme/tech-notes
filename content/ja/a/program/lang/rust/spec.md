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

---
title: "std::fmt"
linkTitle: "fmt"
description: >
  [Module std::fmt](https://doc.rust-lang.org/std/fmt/)
date: 2020-05-31T01:23:57+09:00
weight: 150
---

このモジュールで [format!]({{<ref "_index.md">}}#format) の書式が実装されている（という意味だと思う）。

## format書式解説

[Module std::fmt](https://doc.rust-lang.org/std/fmt/)に書かれている。

### Positional parameters

どの引数を参照するか、0からの連番で指定できる。  
指定しない場合は「次の引数」になる。

```Rust
format!("{1} {} {0} {}", 1, 2); // => "2 1 1 2"
```

### Named parameters

Examples:

```Rust
format!("{argument}", argument = "test");   // => "test"
format!("{name} {}", 1, name = 2);          // => "2 1"
format!("{a} {c} {b}", a="a", b='b', c=3);  // => "a 3 b"
```

まだたくさんあるが、出くわしたら追記していく。

## Debug (Trait)

[Trait std::fmt::Debug](https://doc.rust-lang.org/std/fmt/trait.Debug.html)

> `?` formatting

プログラマーに役立つ出力を行う。  
一般に、単に `derive` して使えばいい。  
`#?` という書式指定と共に使われると、見やすく出力される。

Examples:

```Rust
#[derive(Debug)]
struct Point {
    x: i32,
    y: i32,
}

let origin = Point { x: 0, y: 0 };

assert_eq!(format!("The origin is: {:?}", origin), "The origin is: Point { x: 0, y: 0 }");
```

## Display (Trait)

[Trait std::fmt::Display](https://doc.rust-lang.org/std/fmt/trait.Display.html)

> Format trait for an empty format, `{}`.

[Debug](#debug-trait)に似ているが、ユーザー向けの出力をする。 `derive` 不可。

Examples:

```Rust
use std::fmt;

struct Point {
    x: i32,
    y: i32,
}

impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}

let origin = Point { x: 0, y: 0 };

assert_eq!(format!("The origin is: {}", origin), "The origin is: (0, 0)");
```

### fmt (Required Method)

`fn fmt(&self, f: &mut Formatter) -> Result<(), Error>`

値を与えられたフォーマッタでフォーマットする。

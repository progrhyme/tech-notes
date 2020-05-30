---
title: "std::io"
linkTitle: "io"
description: >
  [Module std::io](https://doc.rust-lang.org/std/io/index.html)
date: 2020-05-31T01:23:54+09:00
weight: 200
---

基礎的なI/O機能を提供する。

## stderr (Function)

[Function std::io::stderr](https://doc.rust-lang.org/std/io/fn.stderr.html)

`pub fn stderr() -> Stderr`

当該プロセスの新しい標準エラー出力ハンドルを生成する。

Examples:

```Rust
use std::io::{self, Write};

// Using implicit synchronization
fn main() -> io::Result<()> {
    io::stderr().write_all(b"hello world")?;
    Ok(())
}

// Using explicit synchronization
fn main() -> io::Result<()> {
    let stderr = io::stderr();
    let mut handle = stderr.lock();
    handle.write_all(b"hello world")?;
    Ok(())
}
```

## stdin (Function)

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

## stdout (Function)

[Function std::io::stdout](https://doc.rust-lang.org/std/io/fn.stdout.html)

当該プロセスの新しい標準出力ハンドルを生成する。

## Stderr (Struct)

[Struct std::io::Stderr](https://doc.rust-lang.org/std/io/struct.Stderr.html)

プロセスの標準エラー出力ストリームのハンドル。

詳しくは[io::stderr]()を見よ。

## Stdin (Struct)

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

### read_line (Method)

[Method Stdin::read_line](https://doc.rust-lang.org/std/string/struct.String.html#method.new)

`pub fn read_line(&self, buf: &mut String) -> Result<usize>`

当該ハンドルをロックして入力行を読み込む。

詳しくは [BufRead::read_line](https://doc.rust-lang.org/std/io/trait.BufRead.html#method.read_line) を見よ。

## Stdout (Struct)

[Struct std::io::Stdout](https://doc.rust-lang.org/std/io/struct.Stdout.html)

プロセスの標準出力ストリームのハンドル。  
[io::stdout](#stdout-function)関数によって生成される。

## Write (Trait)

### flush (Required Method)

https://doc.rust-lang.org/std/io/trait.Write.html#tymethod.flush

`fn flush(&mut self) -> Result<()>`

出力ストリームをフラッシュする。

---
title: "testing"
linkTitle: "testing"
description: https://golang.org/pkg/testing/
date: 2020-06-28T19:12:32+09:00
weight: 820
---

## testing

https://golang.org/pkg/testing/

テストやベンチマークで利用するパッケージ。

Examples:

```go
import testing

func TestAbs(t *testing.T) {
    got := Abs(-1)
    if got != 1 {
        t.Errorf("Abs(-1) = %d; want 1", got)
    }
}
```

### type T

テストの状態を保持する。

#### func Errorf

https://golang.org/pkg/testing/#T.Errorf

```go
func (c *T) Errorf(format string, args ...interface{})
```

- Errorメソッドの書式指定対応版
- よく使われる
- Logf + Fail

#### func Run

https://golang.org/pkg/testing/#T.Run

```go
func (t *T) Run(name string, f func(t *T)) bool
```

サブテストを実行する。

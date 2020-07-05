---
title: "errors"
linkTitle: "errors"
description: https://golang.org/pkg/errors/
date: 2020-06-27T22:50:40+09:00
weight: 80
---

## About

Go標準のエラーパッケージ。

Examples:

```go
func do() error {
    :
    if !check() {
        return errors.New("Something is wrong!")
    }
    :
    return nil
}
```

関連項目:

- [道場#例外処理]({{<ref "/a/program/go/dojo/_index.md">}}#例外処理)
- [fmt.Errorf]({{<ref "fmt.md">}}#func-errorf)

Info:

- Go 1.13で `.Is`, `.As`, `.Unwrap` が加わり、それまでgithub.com/pkg/errorsじゃないとできなかったようなことができるようになった。

参考:

- [pkg/errors から徐々に Go 1.13 errors へ移行する - blog.syfm](https://syfm.hatenablog.com/entry/2019/12/27/193348)
- [Go 1.13時代のエラー実装者のお作法 - Qiita](https://qiita.com/shibukawa/items/e633e426a6e67ea2e830)

## func As

https://golang.org/pkg/errors/#As

```go
func As(err error, target interface{}) bool
```

Example:

```go
// errがos.PathError型の値をラップしているときに真
var perr *os.PathError
if errors.As(err, &perr) {
	fmt.Println(perr.Path)
}
```

## func Is

```go
func Is(err, target error) bool
```

Example:

```go
// errがos.ErrExistをラップしているときに真
if errors.Is(err, os.ErrExist)
```

## func Unwrap

```go
func Unwrap(err error) error
```

内包するエラーを返す。

Example:

```go
type myerr struct {
	msg string
	err error
}

func (e *myerr) Error() string {
	return fmt.Sprintf("%s << %s", e.msg, e.err.Error())
}

func (e *myerr) Unwrap() error {
	return e.err
}

//err := fmt.Errorf("Error occured! %w\n", errors.New("I am guilty!"))
err := &myerr{msg: "Error occured!", err: errors.New("I am guilty!")}
fmt.Printf("Error: %v\n", err)
```

https://play.golang.org/p/kAFNUR_XHl5

実行結果:

```
Error: Error occured! << I am guilty!
```

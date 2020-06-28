---
title: "net"
linkTitle: "net"
description: https://golang.org/pkg/net/
date: 2020-06-28T19:31:11+09:00
weight: 500
---

## net

https://golang.org/pkg/net/

ネットワーク通信の汎用的なインタフェースを提供する。

Examples:

```go
// HTTP client
conn, err := net.Dial("tcp", "golang.org:80")
if err != nil {
	// handle error
}
fmt.Fprintf(conn, "GET / HTTP/1.0\r\n\r\n")
status, err := bufio.NewReader(conn).ReadString('\n')

// TCP server
ln, err := net.Listen("tcp", ":8080")
if err != nil {
	// handle error
}
for {
	conn, err := ln.Accept()
	if err != nil {
		// handle error
	}
	go handleConnection(conn)
}
```

### type Dialer

https://golang.org/pkg/net/#Dialer

宛先に通信するためのオプションを保持する。  
各オプションがゼロ値であれば、オプション無しを意味し、単にDial関数を呼ぶに等しい。

```go
type Dialer struct {
  // コネクションタイムアウト
  // デフォルトはタイムアウトしない
  Timeout time.Duration
  :
}
```

## net/http

https://golang.org/pkg/net/http/

HTTPクライアント・サーバ機能を提供するライブラリ。

クライアントは処理が終わったらレスポンスBODYを閉じないと駄目。

Example:

```go
resp, err := http.Get("http://example.com/")
if err != nil {
	// handle error
}
defer resp.Body.Close()
body, err := ioutil.ReadAll(resp.Body)
// :
```

参考:

- [Goのnet/httpのtimeoutについて - Carpe Diem](https://christina04.hatenablog.com/entry/go-timeouts)

### Examples

リクエスト結果をファイルに書き込む:

```go
resp, err := http.Get("...")
check(err)
defer resp.Body.Close()
out, err := os.Create("filename.ext")
if err != nil {
    // panic?
}
defer out.Close()
io.Copy(out, resp.Body)
```

参考:

- [How to pipe an HTTP response to a file in Go? - Stack Overflow](https://stackoverflow.com/questions/16311232/how-to-pipe-an-http-response-to-a-file-in-go)

### Variables

```go
var DefaultClient = &Client{}
```

#### DefaultTransport

https://golang.org/pkg/net/http/#RoundTripper

```go
var DefaultTransport RoundTripper = &Transport{
    Proxy: ProxyFromEnvironment,
    DialContext: (&net.Dialer{
        Timeout:   30 * time.Second,
        KeepAlive: 30 * time.Second,
        DualStack: true,
    }).DialContext,
    ForceAttemptHTTP2:     true,
    MaxIdleConns:          100,
    IdleConnTimeout:       90 * time.Second,
    TLSHandshakeTimeout:   10 * time.Second,
    ExpectContinueTimeout: 1 * time.Second,
}
```

### type Client

https://golang.org/pkg/net/http/#Client

HTTPクライアント。

```go
type Client struct {
    // デフォルトではDefaultTransportが使われる
    Transport RoundTripper
    // HTTPリクエストのタイムリミット。
    // デフォルト（ゼロ値）ではタイムアウトしない。
    Timeout time.Duration
    :
}
```

## net/url

https://golang.org/pkg/net/url/

URLパーサとクエリのエスケープを実装する。

### URLパスの結合

雑に次のようにやると失敗する:

```go
url := "https://example.com/"
loc := "path/to/index.html"
fullURL := path.Join(url, loc) //=> "https:/example.com/path/to/index.html"
```

スキーム部分もパスの一部と解釈されておかしなことになる。

面倒だが、汎用的に対処するには、次のようにする。

```go
// エラー処理省略
urlObj, _ := url.Parse(url)
urlObj.Path = path.Join(urlObj.Path, loc)
fullURL := urlObj.String() //=> "https://example.com/path/to/index.html"
```

### func Parse

https://golang.org/pkg/net/url/#Parse

```go
func Parse(rawurl string) (*URL, error)
```

URL文字列をパースしてURL構造体の値を作る。

### type URL

https://golang.org/pkg/net/url/#URL

```go
type URL struct {
    Scheme     string
    Opaque     string    // encoded opaque data
    User       *Userinfo // username and password information
    Host       string    // host or host:port
    Path       string    // path (relative paths may omit leading slash)
    RawPath    string    // encoded path hint (see EscapedPath method); added in Go 1.5
    ForceQuery bool      // append a query ('?') even if RawQuery is empty; added in Go 1.7
    RawQuery   string    // encoded query values, without '?'
    Fragment   string    // fragment for references, without '#'
}
```

#### func String

https://golang.org/pkg/net/url/#URL.String

```go
func (u *URL) String() string
```

URL文字列を作って返す。

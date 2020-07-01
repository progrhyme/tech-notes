---
title: "encoding"
linkTitle: "encoding"
description: https://golang.org/pkg/encoding/
date: 2020-07-01T23:13:37+09:00
weight: 70
---

## encoding

https://golang.org/pkg/encoding/

データをバイト列とテキストに相互変換するためのインタフェースを定義する。

## encoding/json

https://golang.org/pkg/encoding/json/

RFC 7159で定められたJSONフォーマット仕様に従うエンコード・デコード機能を実装する。

Example:

```go
blob := `["gopher","armadillo","zebra","unknown","gopher","bee","gopher","zebra"]`
var zoo []Animal
if err := json.Unmarshal([]byte(blob), &zoo); err != nil {
  log.Fatal(err)
}
```

公式リソース:

- [JSON and Go - The Go Blog](https://blog.golang.org/json)

関連項目:

- [道場#構造化データファイルの取り扱い]({{<ref "/a/program/go/dojo.md">}}#構造化データファイルの取り扱い)

### structタグの使い方

リファレンス: https://golang.org/pkg/encoding/json/#Marshal

`json` タグの最初の値がJSONのキー名として使われる。  
他には以下のタグが指定できる。

 tag | Marshal（エンコード）時 | Unmarshal（デコード）時
-----|-------------------------|-------------------------
 `omitempty` | ゼロ値であれば出力しない | ゼロ値であれば無視される
 `-` | 出力しない | 無視される
 `string` | 出力時にクォートされる | クォートされていても型に合わせて変換する。クォートされてないとエラー

Examples:

```go
type User struct {
  ID       string                 // JSONキー名は "ID"
  Login    string  `json:"login"` // JSONキー名は "login"
  Password string  `json:"pasword,-"`
  Sex      SexType `json:"sex,omitempty"`
  Age      int     `json:"age,string"`
}
```

関連項目:

- [言語仕様#構造体-タグ]({{<ref "/a/program/go/spec.md">}}#タグ)

参考:

- [Golangで構造体を使ったJSON操作で出来ることを調べてみた | Developers.IO](https://dev.classmethod.jp/articles/struct-json/)
- [GoでStructタグを使用する方法](https://www.codeflow.site/ja/article/how-to-use-struct-tags-in-go)

### pretty print

後述のMarshalIdentや、json.EncoderのSetIndentを使う。

参考:

- [golang : json の pretty print (タブやスペースの指定) - i++](http://increment.hatenablog.com/entry/2017/12/01/081200)

### func Marshal

https://golang.org/pkg/encoding/json/#Marshal

```go
func Marshal(v interface{}) ([]byte, error)
```

vをJSONに変換したバイト列を返す。

Example:

```go
type ColorGroup struct {
  ID     int
  Name   string
  Colors []string
}
group := ColorGroup{
  ID:     1,
  Name:   "Reds",
  Colors: []string{"Crimson", "Red", "Ruby", "Maroon"},
}
b, err := json.Marshal(group)
//=> {"ID":1,"Name":"Reds","Colors":["Crimson","Red","Ruby","Maroon"]}
```

### func MarshalIndent

https://golang.org/pkg/encoding/json/#MarshalIndent

```go
func MarshalIndent(v interface{}, prefix, indent string) ([]byte, error)
```

Examples:

```go
data := map[string]int{
  "a": 1,
  "b": 2,
}

json, err := json.MarshalIndent(data, "<prefix>", "<indent>")
/*
{
<prefix><indent>"a": 1,
<prefix><indent>"b": 2
<prefix>}
*/
```

https://play.golang.org/p/6jHI-MRx0z

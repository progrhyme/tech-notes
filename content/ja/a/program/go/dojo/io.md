---
title: "入出力"
linkTitle: "入出力"
date: 2020-07-05T12:48:06+09:00
weight: 130
---

標準入出力とファイル入出力関連。

## 関連項目

- [pkg (stdlib) > bufio]({{<ref "../std-pkg/_index.md">}}#bufio)
- [pkg (stdlib) > fmt]({{<ref "../std-pkg/fmt.md">}})
- [pkg (stdlib) > io]({{<ref "../std-pkg/_index.md">}}#io)
- [pkg (stdlib) > io/ioutil]({{<ref "../std-pkg/_index.md">}}#ioioutil)

特に、ファイル入出力に関するもの:

- [pkg (stdlib) > path/filepath]({{<ref "../std-pkg/path.md">}}#pathfilepath)

参考:

- [逆引きGolang (ファイル)](https://ashitani.jp/golangtips/tips_file.html)
- [Goでテキストファイルを読み書きする時に使う標準パッケージ - Qiita](https://qiita.com/qt-luigi/items/2c13ad68e7d9f8f8c0f2)
- [How to read/write from/to file using Go? - Stack Overflow](https://stackoverflow.com/questions/1821811/how-to-read-write-from-to-file-using-go)

## テキストの読取り
### 空白区切りのテキストを読み取る

半角スペースやタブ区切りの文字列を読み取るとき。

- フィールド数が固定なら `fmt.Scan` 系の関数が使える
  - フィールド数が異なるものがあるとエラーになる
- フィールド数が不定の場合、 `bufio.Scanner` を使う
  - 分割したいときは [strings.Fields]({{<ref "/a/program/go/std-pkg/strings.md">}}#func-fields) でスライスにできる

## 標準入出力
### 標準入力

メモ:

- さくっと使うなら `fmt.Scan` 系が便利
- 大量に読み込む必要があるときは `bufio.Scanner` を使う

関連項目:

- [pkg (stdlib) > fmt#Scan]({{<ref "../std-pkg/fmt.md">}}#func-scan)

参考:

- [【Golang】fmt.Scanとbufio.Scannerの速度比較 - tsuchinaga](https://scrapbox.io/tsuchinaga/%E3%80%90Golang%E3%80%91fmt.Scan%E3%81%A8bufio.Scanner%E3%81%AE%E9%80%9F%E5%BA%A6%E6%AF%94%E8%BC%83)
- [Go 言語で標準入力から読み込む競技プログラミングのアレ --- 改訂第二版 - Qiita](https://qiita.com/tnoda_/items/b503a72eac82862d30c6)

### TTYにつながっているか判定

CLIで、インタラクティブかどうかによって処理を変えたいことがある。  
そんなときは[golang.org/x/crypto/ssh/terminal](https://pkg.go.dev/golang.org/x/crypto/ssh/terminal)を使う。

Examples:

```go
import (
    "golang.org/x/crypto/ssh/terminal"
)

if terminal.IsTerminal(0) {
    // 標準入力はTTY
} else {
    // 標準入力はTTYでない
}
```

Hint:

- 標準出力なら `IsTerminal(1)` で

参考:

- [Golangで標準入力がパイプで渡されたものか判定する - Qiita](https://qiita.com/tanksuzuki/items/e712717675faf4efb07a)

関連項目:

- [CLI#TTY]({{<ref "/a/cli/_index.md">}}#tty)

## ファイル入出力
### ファイルを開いて書込み

```go
func writeBytesToFile(b []byte, path string, flag int, perm os.FileMode) {
  file, err := os.OpenFile(path, flag, perm)
  if err != nil {
    log.Fatal(err)
  }
  defer file.Close()
  if _, err = file.Write(b); err != nil {
    log.Fatal(err)
  }
}

// ファイルがなければ新規作成。あれば既存の内容を消して上書き
writeBytesToFile(b, path, os.O_WRONLY|os.O_CREATE|os.O_TRUNC, 0666)
// ファイルがなければ新規作成。あれば内容を追記する
writeBytesToFile(b, path, os.O_WRONLY|os.O_CREATE|os.O_APPEND, 0666)
```

## 1つの入力から複数の出力先に出力

出力先が2つなら、[io.TeeReader]({{<ref "/a/program/go/std-pkg/io.md">}}#func-teereader)で複製するのが手軽だと思う。

参考:

- [go - Golang io.copy twice on the request body - Stack Overflow](https://stackoverflow.com/questions/25671305/golang-io-copy-twice-on-the-request-body)
- [Forwarding reader to multiple consumers - Michal Pristas - Medium](https://medium.com/@MichalPristas/forwarding-reader-to-multiple-consumers-a1574a9db4d6)

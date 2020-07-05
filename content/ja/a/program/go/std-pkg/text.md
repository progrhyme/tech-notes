---
title: "text"
linkTitle: "text"
date: 2020-06-28T19:12:51+09:00
weight: 830
---

## text/template

https://golang.org/pkg/text/template/

関連項目:

- [道場#テンプレート]({{<ref "../dojo/_index.md">}}#テンプレート)

Examples:

```go
const letter = `
Dear {{.Name}},
{{if .Attended}}
It was a pleasure to see you at the wedding.
{{- else}}
It is a shame you couldn't make it to the wedding.
{{- end}}
{{with .Gift -}}
Thank you for the lovely {{.}}.
{{end}}
Best wishes,
Josie
`

// Prepare some data to insert into the template.
type recipient struct {
    Name, Gift string
    Attended   bool
}
var recipients = []recipient{
    {"Aunt Mildred", "bone china tea set", true},
    {"Uncle John", "moleskin pants", false},
    {"Cousin Rodney", "", false},
}

// Create a new template and parse the letter into it.
t := template.Must(template.New("letter").Parse(letter))

// Execute the template for each recipient.
for _, r := range recipients {
    err := t.Execute(os.Stdout, r)
    if err != nil {
        log.Println("executing template:", err)
    }
}
```

実行すると次のようになる:

```
Dear Aunt Mildred,

It was a pleasure to see you at the wedding.
Thank you for the lovely bone china tea set.

Best wishes,
Josie

Dear Uncle John,

It is a shame you couldn't make it to the wedding.
Thank you for the lovely moleskin pants.

Best wishes,
Josie

Dear Cousin Rodney,

It is a shame you couldn't make it to the wedding.

Best wishes,
Josie
```

### type Template

https://golang.org/pkg/text/template/#Template

```go
type Template struct {
    *parse.Tree
    // contains filtered or unexported fields
}
```

パースされたテンプレート。

#### func Delims

https://golang.org/pkg/text/template/#Template.Delims

```go
func (t *Template) Delims(left, right string) *Template
```

デリミタ（区切り文字）を設定する。  
デフォルトは `{{`, `}}` 。  
テンプレートを返すので、メソッドチェインできる。
（なんかここだけRubyっぽい）

```go
const script = `export <<.EnvKey>>=${<<.EnvKey>>:-"<<.Default>>"}
`
t := template.Must(template.New("script").Delims("<<", ">>").Parse(script))
t.Execute(os.Stdout, struct{ EnvKey, Default string}{"FOO", "foo"})
```

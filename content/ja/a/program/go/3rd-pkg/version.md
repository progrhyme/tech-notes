---
title: "バージョン"
linkTitle: "バージョン"
description: >-
  version, SemVer
date: 2020-07-07T07:28:18+09:00
weight: 2600
---

## blang/semver

- https://github.com/blang/semver
- https://pkg.go.dev/github.com/blang/semver/v4

semVerを取り扱う人気のパッケージ。  
`X.Y.Z` 形式でないものを `semver.Make` に食わせるとエラーになって `0.0.0` になってしまう。

Example:

```go
raw := []string{"1.2.3", "1.0", "1.3", "2", "0.4.2"}
vs := make([]semver.Version, len(raw))
for i, r := range raw {
	v, err := semver.Make(r)
	if err != nil {
		fmt.Printf("Error parsing version: %s. %v\n", r, err)
	}

	vs[i] = v
}

semver.Sort(vs)
fmt.Printf("sorted: %v\n", vs)
/*
Error parsing version: 1.0. No Major.Minor.Patch elements found
Error parsing version: 1.3. No Major.Minor.Patch elements found
Error parsing version: 2. No Major.Minor.Patch elements found
sorted: [0.0.0 0.0.0 0.0.0 0.4.2 1.2.3]
*/
```

https://play.golang.org/p/OZVwXRRnl4s

## hashicorp/go-version

- https://github.com/hashicorp/go-version
- https://pkg.go.dev/github.com/hashicorp/go-version

SemVer以外も想定するならこちらを使うのがよさそう。

Tips:

- `Version#.Original` で元のバージョンを取り出せるようだ

### バージョンの比較

Example:

```go
var result bool
v := version.NewVersion("1.0")
result = v.Equal(cur)
result = v.GreaterThan(cur)
result = v.GreaterThanOrEqual(cur)
result = v.LessThan(cur)
result = v.LessThanOrEqual(cur)

var ret int
ret = v.Compare(cur)
// v < cur => -1
// v = cur =>  0
// v > cur =>  1
```

### バージョンのソート

Example:

```go
raw := []string{"1.1", "0.7.1", "1.4-beta", "1.4", "2"}
vs := make([]*version.Version, len(raw))
for i, r := range raw {
	v, err := version.NewVersion(r)
	if err != nil {
		fmt.Printf("Error parsing version: %s. %v\n", r, err)
	}

	vs[i] = v
}

sort.Sort(version.Collection(vs))
fmt.Printf("sorted: %v\n", vs)
//=> sorted: [0.7.1 1.1.0 1.4.0-beta 1.4.0 2.0.0]
```

https://play.golang.org/p/B_OBt8NeImn

## Masterminds/semver

- https://pkg.go.dev/github.com/Masterminds/semver/v3

blang/semverと違い、1桁や2桁のバージョンも解釈できる。  
hashicorp/go-versionとほぼ一緒で、インタフェースもよく似ている。

Example:

```go
raw := []string{"1.2.3", "1.0", "1.3", "2", "0.4.2",}
vs := make([]*semver.Version, len(raw))
for i, r := range raw {
	v, err := semver.NewVersion(r)
	if err != nil {
		t.Errorf("Error parsing version: %s", err)
	}

	vs[i] = v
}

sort.Sort(semver.Collection(vs))
//=> sorted: [0.4.2 1.0.0 1.2.3 1.3.0 2.0.0]
```

https://play.golang.org/p/y6ABmgtJ9Yf

Tips:

- `Version#.Original` で元のバージョンを取り出せるようだ

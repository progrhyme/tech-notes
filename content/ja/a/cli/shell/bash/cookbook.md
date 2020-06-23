---
title: "Cookbooks"
linkTitle: "Cookbooks"
description: >
  スクリプティングのための応用的なコードスニペット集っぽいもの。
  基本的な文法機能の解説は別に書く。
date: 2020-04-28T12:04:10+09:00
---

See Also:

- [シェルスクリプト]({{< ref "/a/cli/shell/script/_index.md" >}})
  - [Cookbooks]({{< ref "/a/cli/shell/script/cookbook.md" >}})

NOTE:

- このページに書いているが、実はPOSIX対応の機能もあるかもしれない。

## joinとsplit

join:

```sh
arr=(a "b c" $'d\ne' f)

# ',' で結合
str="$(IFS=,; echo "${arr[*]}")"
IFS=, eval 'str="${arr[*]}"'

# ', ' で結合
str=$(printf ", %s" "${arr[@]}")
str=${str:2}
```

split:

```sh
str=$'a,b c,d\ne,f'

IFS=, eval 'arr=($str)'
```

参考:

- [Bashの配列でjoinやsplitする - Qiita](https://qiita.com/kawaz/items/b82da76ac93b32ddc364)

## 複数行のコメントアウト

`:` とヒアドキュメントを組み合わせる。

```sh
: << "__EOCOMMENT__"

コメントアウトしたいコード

__EOCOMMENT__
```

参考:

- [bashで複数行コメントアウトする方法 - Qiita](https://qiita.com/imura81gt/items/a2998147bd7ae8056b26 "bashで複数行コメントアウトする方法 - Qiita")

## 論理演算

```bash
((2 > 1)) # $? => 0
((1 > 1)) # $? => 1
(($(seq 1 3 | wc -w) > 2)) # $? => 0

if true; then echo ok; fi #=> ok
```

## 数値の操作

```bash
i=0
echo $((i++)) #=> 0
echo $((++i)) #=> 2
```

## 連番によるループ

```bash
$ n=0
$ for i in $(seq $n $((n + 2))); do echo $i; done
0
1
2
```

## 正規表現でグループ化と後方参照

マッチした文字列は、グループ化されたものも含めてBASH_REMATCH配列変数に格納される。

```sh
# bash

if [[ "2020-06-24" =~ ^([0-9]{4})-([0-9]{2})-([0-9]{2})$ ]] ; then
  ymd="${BASH_REMATCH[0]}"   #=> 2020-06-24
  year="${BASH_REMATCH[1]}"  #=> 2020
  month="${BASH_REMATCH[2]}" #=> 06
  day="${BASH_REMATCH[3]}"   #=> 24
fi
```

参考:

- [\[Bash\]正規表現マッチした部分文字列を再利用する方法 · DQNEO起業日記](http://dqn.sakusakutto.jp/2013/06/bash_rematch_regexp.html)
- [bashでif に正規表現を使った文字列マッチ条件分岐 - それマグで！](https://takuya-1st.hatenablog.jp/entry/2016/12/22/175514)

## 多重ループとbreak, continue

`break 2` や `continue 2` のように後ろに数字を与えることで、上の階層のループを抜けられるようだ。

Example:

```sh
for ((i=1; i <= 4; i++)); do
  for ((j=1; j <= 3; j++)); do
    echo "(i, j) = ($i, $j)"
    if ((i > 2)); then
      if ((j == 2)); then
        echo End of loop
        break 2
      fi
    elif ((i > 1 && j == 2)); then
      continue 2
    fi
    echo blah blah
  done
  echo "[$i] end"
done
```

実行結果:

```
(i, j) = (1, 1)
blah blah
(i, j) = (1, 2)
blah blah
(i, j) = (1, 3)
blah blah
[1] end
(i, j) = (2, 1)
blah blah
(i, j) = (2, 2)
(i, j) = (3, 1)
blah blah
(i, j) = (3, 2)
End of loop
```

参考:

- [bash のbreak、continue、return、exit | 敗走王のブログ](https://ameblo.jp/dagyah/entry-12341581495.html)

## 文字列操作
### 部分文字列の削除

以下、 [Bash scripting](http://iishikawa.s371.xrea.com/note/bash-script.html#idm2045339272) より。

- `${var%pattern}` … 後方からパターンの最短マッチを削除
- `${var%%pattern}` … 後方からパターンの最長マッチを削除
- `${var#pattern}` … 前方からパターンの最短マッチを削除
- `${var##pattern}` … 前方からパターンの最長マッチを削除

パスからディレクトリ名やファイル名を取り出すのによく使う。

```bash
fullpath=/a/b/c.txt
echo ${fullpath##*/} # c.txt
echo ${fullpath%/*} # /a/b
filename=d.e.txt
echo ${filename%.*} # d.e
echo ${filename##*.} # txt
```

たぶん、Bash に限らず POSIX で使える。  
下に載ってる。

http://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_06_02

### 文字列の部分切り出し

```bash
$ echo $str
1234567890

$ echo ${str:3:4}
4567
```

参考:

- [シェルスクリプトで部分文字列を切り出す - 理系学生日記](http://kiririmode.hatenablog.jp/entry/20170913/1505228400)

### 文字列を部分的に置換

- `${var/x/y}` ... `$var` 文字列の `x` を `y` に置換（1回のみ）
- `${var//x/y}` ... `$var` 文字列の `x` を `y` に置換（全てマッチ）

参考: [bashの変数をsplitして配列を作る方法: 小粋空間](http://www.koikikukan.com/archives/2019/05/09-235555.php)

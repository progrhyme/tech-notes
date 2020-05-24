---
title: "gitコマンド"
linkTitle: "git"
date: 2020-05-25T03:03:50+09:00
---

当面、このページはリファレンス的に各サブコマンドの解説など記す。  
ユースケースについては[Git#How-to]({{<ref "_index.md">}}#how-to)を参照。

## 参考資料

- [【Git】基本コマンド - Qiita](http://qiita.com/konweb/items/621722f67fdd8f86a017)

## apply

```bash
## git diffコマンドで作ったpatchを適用する
git apply file.patch
```

参考:

- [Git でパッチファイルを作成する \| まくまくGitノート](https://maku77.github.io/git/git-patch.html)


## archive

NOTE:

- tar を使わないとファイルに実行ビットがついてしまうようだ。

参考:

- [Git リポジトリの内容を zip ファイルにする - Qiita](http://qiita.com/usamik26/items/9a2d14aea30cb01a60c6 "Git リポジトリの内容を zip ファイルにする - Qiita")

## branch

https://git-scm.com/docs/git-branch

```sh
# ローカルのbranchを表示
git branch
## マージ済みのbranchを表示
git branch --merged
## 出力フォーマット指定
git branch --format="<FORMAT>"

# 今のbranchを元に新しいbranchを作る
git branch <newbranch>

# 既存のbranchを元に新しいbranchを作る
git branch <oldbranch> <newbranch>
```

`--format` オプションで指定できるフォーマットについては[git-for-each-ref](#for-each-ref)を見よ。

## checkout

```sh
## topicブランチを作成
git checkout -b topic

## remoteブランチからローカルブランチを作成
git checkout -b foo origin/foo

## 空ブランチを作る
git checkout --orphan empty
```

参考:

- [gitの空ブランチを作る - Qiita](https://qiita.com/akiko-pusu/items/7c0a99b8cb37882d2cfe "gitの空ブランチを作る - Qiita")


## cherry-pick

別ブランチで開発中の機能などをコミット単位で取り込むときに使う。

```bash
git cherry-pick <SHA1>
## マージコミットのcherry-pick
git cherry-pick -m 1 <SHA1>
```

参考:

- [merge commitをcherry-pickする - Qiita](http://qiita.com/takc923/items/8e2d87d692f840b14464 "merge commitをcherry-pickする - Qiita")


## clone

https://git-scm.com/docs/git-clone

```bash
## 深さ1の shallow clone
git clone --depth 1 <URL>

## ブランチ指定
git clone --branch BRANCH URL
```

## commit

https://git-scm.com/docs/git-commit

```bash
# 変更・削除したファイルを全てコミットする
git commit --[a]ll
# 変更点を表示してコミット
git commit -v
# 空コミット
git commit --allow-empty
# コミットメッセージを変更
git commit --amend
```

## diff

```sh
## スペース等の差分を無視
git diff -w
## ファイル名のみ表示
git diff --name-only
```

参考:

- [colordiffを使わずにdiffをカラー表示する - ももいろテクノロジー](http://inaz2.hatenablog.com/entry/2014/07/03/003551)

## fetch

```bash
## remote で削除された branch について、local のトラッキングブランチも消す
git fetch -p|--prune
```

## for-each-ref

https://git-scm.com/docs/git-for-each-ref

local branch, remote branchのHEAD, tagの情報を表示。

```sh
# A simple example showing the use of shell eval on the output, demonstrating the use of --shell.
# List the prefixes of all heads:

#!/bin/sh

git for-each-ref --shell --format="ref=%(refname)" refs/heads | \
while read entry; do
  eval "$entry"
  echo `dirname $ref`
done
```

FORMATで指定できるフィールド:

 フィールド | 意味
----------|------
 `refname` | The name of the ref (the part after $GIT_DIR/).
 `refname:short` | branch, tagなど明らかな名前がついているものはこれで参照できる
 `objecttype` | blob, tree, commit, tag
 `objectsize` |
 `objectname` |

## log

```bash
## 過去のコミットから対象文字列を含むコミットを検索
git log -S 文字列

## 1行で表示
git log --pretty=oneline
git log --oneline --graph --decorate

## フォーマット指定
git log --format="%H" # full commit hash のみ
```

参考:

- [Git - リビジョンの選択](https://git-scm.com/book/ja/v1/Git-%E3%81%AE%E3%81%95%E3%81%BE%E3%81%96%E3%81%BE%E3%81%AA%E3%83%84%E3%83%BC%E3%83%AB-%E3%83%AA%E3%83%93%E3%82%B8%E3%83%A7%E3%83%B3%E3%81%AE%E9%81%B8%E6%8A%9E "Git - リビジョンの選択")
- [git logのオプションあれこれ - 煙と消えるその前に](http://heart-shaped-chocolate.hatenablog.jp/entry/2013/07/16/035104 "git logのオプションあれこれ - 煙と消えるその前に")
- [git log をいい感じに alias して色付きで見やすくしておく - Qiita](http://qiita.com/key-amb/items/9ee8339d2da971581cfb "git log をいい感じに alias して色付きで見やすくしておく - Qiita")

## pull

https://git-scm.com/docs/git-pull

```sh
# リファレンスには書いてないが、fetch時に--pruneしてくれるらしい
git pull --prune
```

 Option | 効果
--------|-----
 --depth=N | 取得する履歴数を制限する。shallowリポジトリの場合、履歴数を指定した数に増減させる

参考:

- [リモートで消されたブランチが手元で残ってしまう件を解消する - Qiita](https://qiita.com/yuichielectric/items/84cd61915a1236f19221)

## rebase

```bash
## 過去のNコミットを編集
git rebase -i HEAD~N
## 1st コミットから編集
git rebase -i --root
```

参考:

- [First commit が git rebase -i できない問題 → git rebase -i --root でできる - 納豆には卵を入れる派です。](http://d.hatena.ne.jp/ken_c_lo/20130421/1366558065 "First commit が git rebase -i できない問題 → git rebase -i --root でできる - 納豆には卵を入れる派です。")


## remote

リモートリポジトリの管理。

```bash
## リモートリポジトリ一覧
git remote
git remote -v

## リモートリポジトリ追加
git remote add <リポジトリ名> <URL>

## リモートリポジトリ削除
git remote rm <リポジトリ名>

## URL変更
git remote set-url <リポジトリ名> <URL>

## リポジトリ名変更
git remote rename <リポジトリ名> <新しいリポジトリ名>
```

参考:

- [これで完璧! git remoteでリポジトリを【追加,削除,確認,変更】 | 侍エンジニア塾ブログ（Samurai Blog） - プログラミング入門者向けサイト](https://www.sejuku.net/blog/71492)


## revert

```bash
git revert <SHA1>
## マージコミットの取消し
git revert -m 1 <SHA1>
```

参考:

- https://github.com/git/git/blob/master/Documentation/howto/revert-a-faulty-merge.txt
- [gitのmerge-commitをrevertする - 車輪を再発明 / koba04の日記](http://d.hatena.ne.jp/koba04/20121122/1353512656 "gitのmerge-commitをrevertする - 車輪を再発明 / koba04の日記")

## submodule

https://git-scm.com/docs/git-submodule

なんだかんだで割りと使っている。

```bash
# submodule追加
git submodule add <git-url> <local-path>

# 全submodule更新
git submodule foreach git pull origin master
```

sumobuleの削除 => https://github.com/progrhyme/git-wraps/blob/master/bin/git-submodule-delete

参考:

- [Git submodule の基礎 - Qiita](http://qiita.com/sotarok/items/0d525e568a6088f6f6bb "Git submodule の基礎 - Qiita")
- [git submoduleしてるリポジトリをリモートの最新に更新する - Qiita](http://qiita.com/kshimo69/items/ac22d414d756ea08943f "git submoduleしてるリポジトリをリモートの最新に更新する - Qiita")

### 向き先url変更

1. `.gitmodules` の向き先を新urlに変更
1. `git submodule sync` で反映
   - `.git/config` に変更が反映される
1. `git submodule update` とかで更新

参考:

- [submodule の向き先 url を変更する - Qiita](http://qiita.com/8mamo10/items/fd11d8c7a2d928b39173 "submodule の向き先 url を変更する - Qiita")

## tag

SYNOPSIS:

```sh
## 作成
git tag <タグ名>
## 注釈付き
git tag -a <タグ名> -m <メッセージ>

## 表示
git show <タグ名>
## 一覧
git tag

## 削除
git tag -d <タグ名>

## リモートに反映
git push <リモート> <タグ名>
git push --tags

## 削除反映
git push <リモート> :<タグ名>
```

参考:

- [【Git】tag関連コマンド - Qiita](https://qiita.com/chihiro/items/cba40015b1aa2c73b78a)
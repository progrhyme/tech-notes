---
title: "Git"
linkTitle: "Git"
description: >
  https://git-scm.com/
date: 2020-04-27T23:03:01+09:00
weight: 200
---

## プロトコル

https://git-scm.com/book/en/v2/Git-on-the-Server-The-Protocols

- Local Protocol
- HTTP Protocols
- SSH Protocol
- Git Protocol ... 最も高速だが、認証がない

参考:

- [github - What are the supported git url formats? - Stack Overflow](https://stackoverflow.com/questions/31801271/what-are-the-supported-git-url-formats)

## config

https://git-scm.com/docs/git-config

### aliasの設定

Examples:

```INI
[alias]
    st  = status
    dfc = diff --cached
```

Tips:

- 右辺を `!` から記述すると外部コマンドを記述できる

参考:

- [gitで便利なエイリアス達 - Qiita](https://qiita.com/peccul/items/90dd469e2f72babbc106)
- [git aliasで外部コマンドを呼び出して便利にしてみる - Qiita](https://qiita.com/akirashi/items/2b5cf0f32777aaaf6287)

### include

別ファイルをincludeできる

```INI
[include]
    path = .gitconfig.local
```

参考:

- [.gitconfigで別ファイルを読み込む - 3100](https://z3100.hatenadiary.org/entry/20120505/1336203155)

### includeIf

条件に基づいて別ファイルをincludeする。

参考:

- [git-configのConditional includesでユーザ情報を切り替える - kawaken's blog](http://kawaken.hateblo.jp/entry/2017/08/05/235904)

## How-to

See also [gitコマンド]({{<ref "cli.md">}})

### CommitterとAuthorを変更する

HEADのcommitを修正する場合:

```sh
git config --local user.name "YOUR NAME"
git config --local user.email your-address@example.com
git commit --amend --reset-author
```

過去の履歴についても変更したい場合:

```sh
git rebase -i <commit hash>
# 該当するコミットを `e` で選ぶ
git commit --amend --reset-author 
git rebase --continue
```

参考:

- [過去のgitコミットのCommitとAuthor情報を修正する - ひと夏の技術](https://tech-1natsu.hatenablog.com/entry/2018/10/19/021855)
- [Git の Commit Author と Commiter を変更する - Qiita](https://qiita.com/sea_mountain/items/d70216a5bc16a88ed932)

### 歴史を改ざんする

See [Git - 歴史の書き換え](https://git-scm.com/book/ja/v2/Git-%E3%81%AE%E3%81%95%E3%81%BE%E3%81%96%E3%81%BE%E3%81%AA%E3%83%84%E3%83%BC%E3%83%AB-%E6%AD%B4%E5%8F%B2%E3%81%AE%E6%9B%B8%E3%81%8D%E6%8F%9B%E3%81%88)

#### 特定のファイル・ディレクトリの履歴を完全に削除

```bash
## file
git filter-branch --tree-filter 'rm -f path/to/file' HEAD
## directory
git filter-branch --tree-filter 'rm -rf path/to/dir/' HEAD
```

参考:

- [Git ファイルの履歴を完全に削除する](https://gist.github.com/ktx2207/3167fa69531bdd6b44f1)


### マージコミットを cherry-pick

merge commit を cherry-pick

```bash
git cherry-pick -m 1 <merge commit のハッシュ>
```

参考:

- [merge commitをcherry-pickする - Qiita](http://qiita.com/takc923/items/8e2d87d692f840b14464 "merge commitをcherry-pickする - Qiita")

### マージ済みブランチを掃除する

色んな人がやっていて、aliasに設定したりサブコマンドを作ったりしている。

自分でも[2020-05-04に作った]({{< ref "20200504.md" >}}#git-pull---pruneしてマージ済みローカルブランチを掃除するgitのサブコマンドを作った)。

参考:

- [gitでbranchをお掃除する際のチートシート - Qiita](https://qiita.com/kenshiroh/items/44dcf4b094e841bb42a2)

### 特定のファイルを Git 管理対象から除外する

①`.gitignore` や `.git/info/exclude` を使う

②既に Git 管理下にあるファイルをワーキングツリーで敢えて除外する

```bash
git update-index —assume-unchanged [ファイル名]
git update-index —skip-worktree [ファイル名]

## 確認
git ls-files -v

## 取り消し
git update-index —no-assume-unchanged [ファイル名]
git update-index —no-skip-worktree [ファイル名]
```

git ls-files -v の表示:

- assume-unchanged 設定のファイルは、状態が小文字で表示される
- skip-worktree 設定のファイルは、状態が S と表示される

参考:

- [既に git 管理しているファイルをあえて無視したい - Qiita](http://qiita.com/usamik26/items/56d0d3ba7a1300625f92)


### リポジトリをサブディレクトリで分割

#### サブディレクトリが1つの場合

```sh
git clone original_dir new_dir
cd new_dir
git filter-branch --subdirectory-filter sub_dir_name HEAD
```

参考:

- [gitリポジトリのサブディレクトリを別のリポジトリとして抽出する方法 - 拡張現実ライフ](https://akio0911.net/archives/3421)

#### サブディレクトリが複数の場合

参考:

- [git filter branch \- Detach many subdirectories into a new, separate Git repository \- Stack Overflow](https://stackoverflow.com/questions/2982055/detach-many-subdirectories-into-a-new-separate-git-repository)

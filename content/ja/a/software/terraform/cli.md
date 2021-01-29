---
title: "CLI"
linkTitle: "CLI"
description: >
  terraform command
date: 2020-04-26T23:06:08+09:00
weight: 200
---

https://www.terraform.io/docs/commands/

## import

https://www.terraform.io/docs/import/usage.html

`terraform import` コマンドにより、既存インフラをTerraform管理下に置くことができる。

一部インフラを手動で作った後、リソースのidを指定して取り込む、といった使い方ができる。

参考:

- [terraform importの使い方メモ - Qiita](https://qiita.com/tyasu/items/32b23dd76d25f7af712f "terraform importの使い方メモ - Qiita")

## output

https://www.terraform.io/docs/commands/output.html

stateファイルから値を出力する。

```sh
terraform output [options] [NAME]
```

## plan

https://www.terraform.io/docs/commands/plan.html

Examples:

```sh
# 対象を限定する
terraform plan -target=resource_type1.identifier1 -target=resource_type2.identifier2

# planファイルを書き出す
terraform plan -out=path/to/tfplan
```

## state

https://www.terraform.io/docs/commands/state/

stateの管理・編集を行うコマンド。

SYNOPSIS:

```sh
terraform state list [filtering-arg]   # terraform管理下のリソース一覧
terraform state pull                   # リモートのstateファイルをダウンロードして標準出力に表示
terraform state push [OPTION] PATH     # ローカルのstateファイルをリモートにアップロード
terraform state mv SOURCE DESTINATION  # リソースの名称変更。module化も可能
terraform state rm リソース             # リソースをterraform管理から除く = tfstateファイルから削除
```

## workspace

https://www.terraform.io/docs/cli/commands/workspace/

```sh
terraform workspace new $env     # workspace作成
terraform workspace list         # 一覧表示
terraform workspace select $env  # workspace切替え
```

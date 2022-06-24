---
title: "エディタ"
linkTitle: "エディタ"
date: 2020-05-10T08:41:30+09:00
weight: 1100
---

各種エディタやIDEでTerraformを書くための設定など。

## IntelliJ IDEA

See also [IntelliJ IDEA]({{< ref "/a/software/editor/idea.md" >}})

### Plugins

- [HashiCorp Terraform / HCL language support - IntelliJ IDEs | JetBrains](https://plugins.jetbrains.com/plugin/7808-hashicorp-terraform--hcl-language-support)
- File Watcher ... ファイル保存時に `terraform fmt` を実行するため

### 設定

- File Watcherによる `terraform fmt` を設定する

## Visual Studio Code

See also [Visual Studio Code]({{< ref "/a/software/editor/vscode.md" >}})

参考:

- [VSCodeでTerraformを書くときの設定(2019/11/07追記: HCL2対応) - Qiita](https://qiita.com/pypypyo14/items/5520f3defa55119f3a1a)

### Extensions

- [HashiCorp Terraform - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=HashiCorp.terraform)
  - 2020年5月、公式になった。当時は「mauve.terraform」だったが、2022年6月現在は「HashiCorp.terraform」となっている。

参考:

- [Supporting the HashiCorp Terraform Extension for Visual Studio Code](https://www.hashicorp.com/blog/supporting-the-hashicorp-terraform-extension-for-visual-studio-code/)

### 設定

- `terraform-ls` ... terraformの実行ファイルのパスを指定する。自動フォーマットなどで必要
- 自動フォーマット（ `editor.formatOnSave` ）をONにしておく -> `terraform fmt` が掛かるようになる

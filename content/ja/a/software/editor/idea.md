---
title: "IntelliJ IDEA"
linkTitle: "IntelliJ IDEA"
description: >
  https://www.jetbrains.com/idea/
date: 2020-04-29T10:44:28+09:00
weight: 30
---

## Usage

- 画面分割 ... `Window > Editor Tabs > (Split Vertically|Split Horizontally)`

参考:

- [IntelliJの使い方 - Qiita](https://qiita.com/pipi_taro/items/859d445960bb79a3ac78)
- [IntelliJ IDEA 初期設定・プラグイン・ショートカットコマンド - Qiita](https://qiita.com/non0311/items/71109f284b6b32f1b25e)

### ショートカットキー

macOS

 キー | 機能
-----|------
 `+⌘+Shift+f` | 検索 / パス内検索

参考:

- [プロジェクト内のターゲットを検索および置換する — IntelliJ IDEA](https://pleiades.io/help/idea/finding-and-replacing-text-in-project.html#limit_search)

### 行の折り返し（Soft-Wrap）

```
Preferences > Editor > General > SoftWraps
> Use original line’s indent for wrapped parts
```

### 矩形選択

メニュー: `Edit > Column Selection Mode` でON/OFFできる。

参考:

- [IntelliJ IDEA - 【IntelliJ IDEA】フリーカーソル＆矩形選択の解除の方法｜teratail](https://teratail.com/questions/117537)

### File Typeの関連付け

`Preferences > Editor > File Types` で関連付けを設定できる。  
まだ関連付けがない拡張子のファイルであれば、エディタ上で右クリックして「Associate File Type」を選んで設定することもできる。

## Plugins
### File Watchers

ファイルを監視して自動で実行されるアクションを設定できる。  
例えば、ファイルの変更を監視してコードフォーマッタを適用するとか。

[ファイル監視 - 公式ヘルプ | IntelliJ IDEA](https://pleiades.io/help/idea/using-file-watchers.html)

## How to Upgrade
### Ubuntu

- [2020年に2018年版から2020.1にアップデートしたときのログ]({{< ref "20200429.md" >}}#ubuntu-1804でintellij-ideaを20201にアップデート)
- [2018年に2017年版から2018.1にアップデートしたときのログ](https://sites.google.com/site/progrhymetechwiki/home/memo/2018/20180331#TOC-Ubuntu-16.04-IntelliJ-IDEA-)


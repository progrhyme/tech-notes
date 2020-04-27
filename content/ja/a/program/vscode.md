---
title: "Visual Studio Code"
linkTitle: "VS Code"
description: >
  https://code.visualstudio.com/
date: 2020-04-27T22:33:58+09:00
weight: 40
---

Micfosoftが提供するOSSのクロスプラットフォームなコードエディタ。  
Electronをベースにしており、IDE並の機能を持つ。

3rd Partyの拡張機能も多数あり、機能を拡充することができる。

## Documentation

- https://code.visualstudio.com/docs
  - Get Started:
    - [Visual Studio Code Key Bindings](https://code.visualstudio.com/docs/getstarted/keybindings)
  - User Guide:
    - [Managing Extensions in Visual Studio Code](https://code.visualstudio.com/docs/editor/extension-gallery)


## Features
### スニペット機能

- ユーザ定義のスニペットを作成可能
  - `File > Preferences > User Snippets`
  - コメント付きJSON形式で書く
  - グローバルなスニペット
  - ワークスペースごとのスニペット
- スニペットが有効になると、補完で選択可能になる

参考:

- [独自のスニペットを作成 | 非公式 - Visual Studio Code Docs](https://vscode-doc-jp.github.io/docs/userguide/userdefinedsnippets.html)
- [VS Codeをスニペット作成は簡単で便利だった！ - lisz-works](https://www.lisz-works.com/entry/vscode-snippets)


## Preferences

昔はJSON設定ファイルを直接編集するようなスタイルだったが、2018年9月現在、GUIで設定できる項目も増えてきたようだ。

2種類の設定がある。

- ユーザ設定 ... ワークスペースによらない、ユーザ環境で常に有効になる設定。
- ワークスペース設定 ... ワークスペースの `.vscode/settings.json` に保存される。

Quick Reference:

| config | 値（\*） | 意味 |
|----------|-----|--------|
| `editor.insertSpaces` | true, false | ソフトタブ（タブキーで半角スペースを挿入）のon/off |
| `editor.renderWhitespace` | none, all, boundary | スペースやタブを描画するかどうか。 `boundary` では単語境界は描画しない |

（\*）デフォルト値は太字

参考:

- [VSCodeのエディター設定の話 - タブ文字がなぜか半角スペースになってしまう - Qiita](https://qiita.com/spica/items/cfae8492804b8d3f8726)


### 言語ごとの設定を行う

インデントなどの設定を言語ごとに変えることができる。

settings.jsonで `"[ruby]": {}` などのエントリを作って、その中に設定を記述すればいい。  
コマンドパレットで `Preferences: Configure language specific settings` と入力し、設定したい言語を選ぶやり方もある。

参考:

- [vscode - Visual Studio Codeで言語ごとにインデントの設定をしたい - スタック・オーバーフロー](https://ja.stackoverflow.com/questions/34014/visual-studio-code%E3%81%A7%E8%A8%80%E8%AA%9E%E3%81%94%E3%81%A8%E3%81%AB%E3%82%A4%E3%83%B3%E3%83%87%E3%83%B3%E3%83%88%E3%81%AE%E8%A8%AD%E5%AE%9A%E3%82%92%E3%81%97%E3%81%9F%E3%81%84)


### インデント設定

| config | 値（\*） | 意味 |
|----------|-----|--------|
| `editor.detectIndentation` | **true**, false | ファイルタイプごとのインデント設定を有効にする |
| `editor.insertSpaces` | true, false | ソフトタブ（タブキーで半角スペースを挿入）のon/off |
| `editor.tabSize` | **4** | インデント幅 |

（\*）デフォルト値は太字

なぜか設定が反映されないときや、一時的に設定を変更したいときは、画面右下のインデント設定をクリックすることでアドホックに変更が可能。

参考:

- [VS Codeでインデントを設定するには：Visual Studio Code TIPS - ＠IT](https://www.atmarkit.co.jp/ait/articles/1805/25/news039.html)
- [【Visual Studio Code】インデント幅の変更方法と、変えても反映されない時の対処法](https://oua-iea-programmer.blogspot.com/2017/04/visual-studio-code.html)
- [vscode - Visual Studio Codeで言語ごとにインデントの設定をしたい - スタック・オーバーフロー](https://ja.stackoverflow.com/questions/34014/visual-studio-code%e3%81%a7%e8%a8%80%e8%aa%9e%e3%81%94%e3%81%a8%e3%81%ab%e3%82%a4%e3%83%b3%e3%83%87%e3%83%b3%e3%83%88%e3%81%ae%e8%a8%ad%e5%ae%9a%e3%82%92%e3%81%97%e3%81%9f%e3%81%84)


### フォント設定

| config | 値（\*） | 意味 |
|----------|-----|--------|
| `editor.fontSize` | | エディタのフォントサイズ |

（\*）デフォルト値は太字

参考:

- [Visual Studio Codeでフォントサイズをいい感じにする - Qiita](https://qiita.com/tkyaji/items/45d5f88047e99c29dda2)


### ファイルを常に新しいタブで開く

`workbench.editor.enablePreview: false` に設定し、プレビューを無効化する。

参考:

- [\[Visual\-Studio\-Code\] ファイルを常に新しいタブで開くようにvscodeを設定するには？ \| CODE Q&A 問題解決 \[日本語\]](https://code.i-harness.com/)

### テキストの折り返し

デフォルトは `editor.wordWrap` が折り返さない設定(= `off`)になっている。  
その他、次のオプションが有る:

- `on` ... エディタの右端で折り返す
- `wordWrapColumn` ... `editor.wordWrapColumn` で設定した値で折り返す
- `bounded` ... `editor.wordWrapColumn` 設定値とエディタの幅の小さい方で折り返す

参考:

- [VS Codeでテキストの折り返しを設定するには：Visual Studio Code TIPS - ＠IT](http://www.atmarkit.co.jp/ait/articles/1807/27/news035.html)


## ショートカットキー

 Win/Linux | Mac | 機能
---------------|-------|---------
 `Ctrl+,` | `⌘+,` | 設定画面を開く
 `Ctrl+Shift+p` |  | コマンドパレットを開く
 `Ctrl+Shift+x` |  | 拡張機能を開く
 `Ctrl+Shift+@` | `⌘+Shift+@` | ターミナルを開く
 `Ctrl+k v` | `⌘+k v` | Markdownファイルのプレビュー画面をサイドバイサイドで表示
 `Ctrl+Shift+v` | `⌘+Shift+v` | Markdownファイルのプレビュー画面を別タブで表示
 `Ctrl+k Ctrl+s` | `⌘+k ⌘+s` | キーバインド一覧を開く
 `Ctrl+k Ctrl+t` | `⌘+k ⌘+t` | カラーテーマ(配色)設定

参考:

- [Visual Studio Code キーボード ショートカット - Qiita](https://qiita.com/oruponu/items/ae9c720d4522c1606daf)
- [VS CodeでMarkdownをプレビューするには？：Visual Studio Code TIPS - ＠IT](http://www.atmarkit.co.jp/ait/articles/1804/20/news030.html)


### キーバインドの変更

↑のキーバインド一覧から変更可能


## Extensions
### 改行コードの表示

- [code-eol](https://marketplace.visualstudio.com/items?itemName=sohamkamani.code-eol)
  - 設定値: `code-eol.color` ... 改行を表す記号の文字色を16進数のカラーコードで指定。
    - 例: `"#841a75"` (ラズベリー色)
- [line-endings](https://marketplace.visualstudio.com/items?itemName=steditor.line-endings)

2018年9月、code-eolを入れて使っている。

### textlint

- [vscode-textlint](https://marketplace.visualstudio.com/items?itemName=taichi.vscode-textlint)

日本語の書き方など指摘・修正してくれるLintツール。

使い方:

- [VS Codeでtextlintを使って文章をチェックする - Qiita](https://qiita.com/azu/items/2c565a38df5ed4c9f4e1#%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)


## How-to
### VS Codeの更新

Ubuntu:

1. debパッケージをダウンロード
1. `sudo dpkg -i code_xxx.deb`

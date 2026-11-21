---
date: '2026-11-21'
description: https://zensical.org/
---

# Zensical

Python製の静的サイトジェネレータ。Material for MkDocs の作者たちが作っている。

- Documentation: https://zensical.org/docs/
- Source: https://github.com/zensical/zensical

以下は、Zensical 0.1.3 時点の情報。Hugo + Docsy からの移行の記録は、[2026-11-21 のメモ](../../memo/2026/20261121.md) にある。

## Getting Started

[uv](https://docs.astral.sh/uv/) で管理する場合:

```sh
uv init --bare --name my-site
uv add --dev zensical
uv run zensical new .             # 雛形を作る(zensical.toml、docs/、GitHub Actions のワークフロー)
uv run zensical serve             # プレビュー(http://localhost:8000/)
uv run zensical build --clean     # site/ にビルドする
```

- `uv init` が書く `requires-python` は、実行環境の Python のバージョン(例: `>=3.15`)になることがある。Zensical は Python 3.11 以上が要件なので、必要なら `>=3.11` に直す。

## 設定(zensical.toml)

`zensical new` の雛形から、よく変える設定。

| 設定 | 内容 |
| :--- | :--- |
| `site_url`、`site_name` | 公開 URL とサイト名 |
| `repo_url`、`repo_name` | ヘッダーのリポジトリへのリンク |
| `nav` | 全ページを明記する。並び順を決める(Hugo の `weight` の代わり)。省略すると、`docs/` 下の階層から自動で作られる(下記) |
| `theme.language` | `"ja"` |
| `theme.features` | 機能の ON/OFF。`navigation.tabs`(最上位の項目をタブにする)、`navigation.sections`(最上位の項目をセクション見出しにする)など |
| `theme.icon.logo` | ヘッダーのロゴ(例: `lucide/square-pen`) |
| `markdown_extensions` の `toc.slugify` | 日本語の見出しをアンカーに残す |
| `plugins.privacy` | 外部リンクを別タブで開く |

### nav

セクションは、`{ "ラベル" = [ ... ] }` の入れ子で書く。セクションの先頭に `index.md` を置くと(`navigation.indexes`)、それがセクションの索引ページになる。

```toml
nav = [
  { "Home" = [
    "index.md",
    { "Memorandum" = [
      "memo/index.md",
      { "2026" = [
        "memo/2026/index.md",
        { "2026-11-21" = "memo/2026/20261121.md" },
      ] },
    ] },
  ] },
]
```

- 記事を追加・削除・移動したら、`nav` も更新する。
- `navigation.tabs` を有効にすると、最上位の項目がタブになる。

#### nav を省略する(自動生成)

`nav` を設定しないと、`docs/` 下のファイル階層から、サイドバーが自動で作られる。記事を追加しても、`nav` を更新しなくてよい。
挙動は、次のとおり。

- 並び順は、ファイル名・ディレクトリ名の順になる(例: メモは、古い日付が先)。
- ページのラベルは、ページの最初の `#` 見出しになる。
- セクション(ディレクトリ)のラベルは、ディレクトリ名から作られる(`cli/` は `Cli`、`aws/` は `Aws`)。`index.md` のフロントマターに `title: AWS` と書いても、セクションのラベルは `Aws` のままになる(ページ自体のタイトルは変わる)。
- 並び順やラベルを細かく制御したいときは、`nav` を明記する。

### docs_dir

Markdown を探すディレクトリ。`zensical.toml` からの相対パスで、既定は `docs`。

```toml
[project]
docs_dir = "docs"
```

- 単一のパスだけを指定できる。複数のディレクトリを指定する方法は、見つからなかった。
- プロジェクトのルート(`.`)は指定できない。公式は、一時的な制限としていて、`docs/` などのサブディレクトリに移すよう案内している。
- `docs_dir` の外のファイルは、監視の対象外になる。公式は、対応をバックログとしている。
- `docs/` 以外のディレクトリも含めて閲覧したいときは、`docs_dir` の下にシンボリックリンクやコピーを集める方法になる。シンボリックリンクが正しく扱われるかは、確認していない。
- 除外は `exclude_docs`(`.gitignore` 構文、`docs_dir` からの相対)で指定する。

### 日本語の見出しのアンカー

既定のスラッグ化では、日本語が落とされて、見出しへのリンク(`#見出し`)が壊れる。[pymdownx.slugs](https://facelessuser.github.io/pymdown-extensions/extras/slugs/) を指定して、日本語を残す。

```toml
[project.markdown_extensions]
toc.permalink = true
toc.slugify = { object = "pymdownx.slugs.slugify", kwds = { case = "lower" } }
```

### 外部リンクを別タブで開く

Material for MkDocs の [privacy プラグイン](https://squidfunk.github.io/mkdocs-material/plugins/privacy/)のリンク属性の機能を使う。このプラグインは、本来は外部アセットのダウンロード(GDPR 対応)が主目的なので、そちらは無効にする。

```toml
[project.plugins.privacy]
assets = false  # 外部アセットのダウンロードはしない
links_attr_map = { target = "_blank" }
```

- 外部リンクは、`target="_blank" rel="noopener"` になる。`rel="noopener"` は、`links_noopener` の既定値(有効)による。
- 内部リンクは変わらない。

## デプロイ(GitHub Pages)

GitHub Actions でビルドして、デプロイする。雛形のワークフローは `pip install zensical` を使う。uv を使う場合は、次のようにする。

```yaml
steps:
  - uses: actions/configure-pages@v6
  - uses: actions/checkout@v7
  - uses: astral-sh/setup-uv@v7
  - run: uv sync --locked
  - run: uv run zensical build --clean
  - uses: actions/upload-pages-artifact@v5
    with:
      path: site
  - uses: actions/deploy-pages@v5
```

- リポジトリの Settings > Pages で、公開元を「GitHub Actions」にする。
- ワークフローに `permissions`(`contents: read`、`pages: write`、`id-token: write`)と `environment: github-pages` が要る(雛形にある)。

## 動作のメモ

- ページ名は、本文の最初の `#` 見出しから決まる。Hugo のように、フロントマターの `title` が自動で見出しにはならない。
- `ref` ショートコードのような機能はない。ページ間のリンクは、`.md` への相対パスで書く(`[systemd](../systemd/index.md)`)。
- Docsy のような、子ページの一覧の自動表示はない。
- ビルドが、壊れたリンク(`anchor does not exist` など)を警告してくれるので、リンク切れの洗い出しに使える。
- `zensical serve` の起動中に `zensical build --clean` を実行すると、キャッシュの競合で失敗する。`--clean` なしなら通る。
- Markdown のパーサは Python-Markdown。CommonMark と違う点がある。→ [Python-Markdown](../../program/python/package.md#python-markdown)

## 参考

- https://zensical.org/docs/get-started/
- https://zensical.org/docs/setup/basics/ ... `docs_dir` などの基本設定
- [2026-11-21 のメモ](../../memo/2026/20261121.md) ... Hugo + Docsy からの移行の記録

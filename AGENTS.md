# AGENTS.md

AIエージェント向けのガイドライン。

## 1. リポジトリの概要

- IT 技術に関する個人的なメモを公開するサイト「progrhyme's Tech Notes」のソース。
- 公開先: https://progrhy.me/tech-notes/ (GitHub Pages)
- ビルド: [Zensical](https://zensical.org/)。Python の依存は uv で管理する。
- デプロイ: `main` への push で GitHub Actions(`.github/workflows/docs.yml`)が実行する。ビルドの前に、`scripts/inject_revision_dates.py` が、記事のフロントマターに作成日と最終更新日を挿入する(CI のチェックアウトだけに入り、コミットされない。ローカルでは実行しない)。
- 旧 Hugo 版は `archive/hugo-doxy` ブランチに保存している。このブランチは変更しない。

## 2. 構成

```text
docs/             記事(Markdown)。ディレクトリがそのままサイトの階層になる
zensical.toml     サイトの設定。nav に全ページを明記する
agent/            エージェント向けの共通コンテンツ(サイトには出ない)
  index/            記事の概要のインデックス
  rules/            共通ルール
  skills/           共通スキル(実体)
.agents/skills/   agent/skills/ の各スキルへのシンボリックリンク
.agents/rules/    agent/rules/ のルールを参照するルールファイル(フロントマターは .agents/ の書式)
.claude/skills/   .agents/skills/ と同じ(Claude Code 用)
.claude/rules/    .agents/rules/ と同じ(フロントマターは Claude Code の書式)
scripts/          補助スクリプト(Python、標準ライブラリのみ)
tests/            scripts/ のテスト(pytest)。tests/fixtures/ に、テスト用の小さなサイトがある
pyproject.toml    Python の依存(uv)と、pytest の設定
uv.lock           ロックファイル
.github/workflows/docs.yml   デプロイ
```

## 3. コマンド

```sh
uv sync                        # 依存を入れる
uv run zensical serve          # プレビュー(http://localhost:8000/)
uv run zensical build --clean  # site/ にビルド(コミットしない)
uv run pytest                  # scripts/ のテスト
```

- 記事や設定を変更したら、`uv run zensical build --clean` でビルドが通ることを確認する。
- `scripts/` を変更したら、`uv run pytest` が通ることを確認する。

## 4. コンテンツのルール

記事を書く・直すときは、次のルールに従う。実体は `agent/rules/` にある。

- [記事の書き方](agent/rules/content-writing.md)
- [記事の構成の変更](agent/rules/content-structure.md): ページの追加・削除・移動・大きな変更のとき。`nav` とインデックスの更新

記事の追加・更新は、スキル `write-doc`([SKILL.md](agent/skills/write-doc/SKILL.md))の手順で行う。

## 5. 変更の進め方と承認

- **Git 操作**
  - コミットと push は、事前にメッセージ(またはプラン)を提示し、ユーザーの明示的な承認(「ok」等)を得てから実行する。
  - `main` への push は、公開サイトに反映される。特に慎重に扱う。
  - 履歴の書き換え(force push、`git reset --hard` など)は、ユーザーの明示的な指示がなければ行わない。

## 6. Git の運用ルール

### コミットメッセージの形式

```text
<絵文字> <プレフィックス>: <要約>
```

- メッセージの先頭には、プレフィックスに対応する絵文字を1つ付ける(下の表を参照)。
    - 例: `➕ add: 2026-11-21 のメモを追加`、`🐛 fix: ビルドの警告を修正`
- 要約は日本語で書く。技術用語は英語のままにする。
- 必要なら、空行のあとに本文(変更の理由や内訳)を書く。
- 1つのコミットには、1つの目的の変更だけを含める。

### プレフィックス

文書コンテンツの変更:

| 絵文字 | プレフィックス | 内容 |
| :--- | :--- | :--- |
| ➕ | `add:` | 文書コンテンツの追加 |
| ✏️ | `correct:` | 文書コンテンツの誤りの修正 |
| 📝 | `modify:` | 文書コンテンツの通常の変更 |
| ♻️ | `refactor:` | 文書の記述やファイル構成の整理(内容の意味は変えない) |
| 🗑️ | `remove:` | 文書コンテンツの削除 |

サイト・リポジトリの変更:

| 絵文字 | プレフィックス | 内容 |
| :--- | :--- | :--- |
| ✨ | `feat:` | サイトの機能・設定の追加(テーマ、検索、拡張機能など) |
| 🐛 | `fix:` | サイトの設定、ビルド、デプロイの不具合の修正 |
| 🔒️ | `security:` | セキュリティに関する修正・対応 |
| 👷 | `ci:` | CI/CD(GitHub Actions)の変更 |
| 🏗️ | `build:` | 依存関係(uv、Zensical)やビルド設定の変更 |
| 📚 | `docs:` | `README.md` や `AGENTS.md` など、リポジトリ自体の文書の更新 |
| 🔧 | `chore:` | その他、サイトの内容や挙動に影響しない変更 |
| ⏪️ | `revert:` | 以前のコミットの打ち消し |

- 記事の内容に関する変更は、`feat:` や `fix:` ではなく、文書コンテンツ用のプレフィックスを使う。
- 迷う場合は、`modify:`(文書)または `chore:`(それ以外)を使うか、ユーザーに確認する。

### ブランチ

- 通常は `main` で作業する。`main` が公開サイトの元になる。
- 大きな変更や試行は、作業用ブランチを切ってよい。マージ前にビルドの確認を行う。

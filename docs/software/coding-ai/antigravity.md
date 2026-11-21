# Antigravity

公式サイト: [Google Antigravity](https://antigravity.google/)

Google のコーディングエージェント(エージェント型の IDE と、CLI)。ここでは、リポジトリに置いて使う機能(ルール、スキル)の置き方をまとめる。

## ルール(.agents/rules/)

- ワークスペースのルールは、`.agents/rules/` に置く(2026-11-21 時点の既定のパス)。従来のパスの `.agent/rules/` も、同時点で使える。
- `rules/` の中の `.md` ファイルは、すべて、先頭に YAML フロントマターで `trigger` を宣言する。`trigger` は次の4つ。
    - `always_on`
    - `model_decision`: `description` が必要。タスクが説明に合うときに、エージェントがルールの全文を読む。
    - `glob`: `globs` が必要。該当するファイルを扱うときに、自動で適用される。
    - `manual`
- `globs` は、カンマ区切りの1つの文字列で書く。単数形の `glob:` も受け付けられる。
- サブフォルダの `rules/` は、読み込まれない。ワークスペース(または git のルート)直下の `.agents/rules/` だけが対象。

```markdown
---
trigger: glob
globs: "docs/**/*.md, zensical.toml"
---

# 記事の構成の変更

(ルールの内容)
```

!!! warning
    フロントマターがない、または `trigger` の値が不正なファイルは、黙って無視される。値は snake_case で書く(`alwaysOn` のような camelCase は不可)。

## スキル

- ワークスペースのスキルは、`<ワークスペースのルート>/.agents/skills/<スキル名>/SKILL.md` に置く。親フォルダの `.agents/skills/` も、リポジトリのルートまで読まれる。チームで共有するために、バージョン管理にコミットする。
- `SKILL.md` は、YAML フロントマターの `name`、`description` と、本文でできている。`description` が、スキルを使う場面の判断に使われる。ほかに、`scripts/`、`examples/`、`resources/` を置ける。
- 全ワークスペース共通のスキルの置き場所は、資料によって異なる。2026-11-21 時点の公式ドキュメントでは `~/.gemini/config/skills/`、コードラボでは `~/.gemini/antigravity/skills/`(公式ドキュメントでは、従来のパスとして使えるとされる)。CLI は、`~/.gemini/skills/` も読む。エージェントのパネルの Customizations で、実際に有効なスキルを確認できる。

## 参考

- [Rules - Google Antigravity](https://antigravity.google/docs/rules.md): ルールの置き場所、`trigger`、`globs`
- [Agent skills - Google Antigravity](https://antigravity.google/docs/skills.md): スキルの置き場所と構成
- [Authoring Google Antigravity Skills](https://codelabs.developers.google.com/getting-started-with-antigravity-skills): スキルの作成(コードラボ)

# Claude Code

公式サイト: [Claude Code](https://claude.com/product/claude-code)、[ドキュメント](https://code.claude.com/docs/)

Anthropic のコーディングエージェント。ここでは、指示、ルール、スキルの置き場所と、読み込まれ方をまとめる。

## 指示ファイル（CLAUDE.md、AGENTS.md）

- Claude Code は、`CLAUDE.md` を読む。v2.1.277（2026-09-18）で、`AGENTS.md` のサポートが追加された[^release-2-1-277]。Bedrock、Vertex、Foundry では、v2.1.277 の時点では使えない。
- `/config` の「Project instructions」で、読む対象を切り替える（2026-11-23 に、公式ドキュメントのメモリのページで確認した）。
    - `claude-md-or-agents-md`（既定）: `CLAUDE.md` を読む。作業ディレクトリとその上に、`CLAUDE.md` も `CLAUDE.local.md` もないときだけ、`AGENTS.md` を読む。
    - `claude-md-and-agents-md`: 両方を読む。各ディレクトリで、`CLAUDE.md`、`AGENTS.md` の順に読む。
    - `claude-md`: `CLAUDE.md` だけを読む。
    - `managed-only`: 組織が管理する指示だけを読む。
- `@パス` で、ほかのファイルを取り込める。相対パスは、取り込む側のファイルからの位置で解決される。取り込みの入れ子は、最大4段まで。
- `AGENTS.md` を使いつつ、Claude Code だけの指示を足したいときは、`CLAUDE.md` から `AGENTS.md` を取り込む。

```markdown
@AGENTS.md

## Claude Code 向けの追加の指示
```

- ユーザー単位の指示は、`~/.claude/CLAUDE.md` に置く。

### サブディレクトリへの置き方

指示ファイルは、プロジェクトのルートだけでなく、任意のサブディレクトリにも置ける。起動時に読まれるのは、作業ディレクトリとその上のディレクトリのファイルで、サブディレクトリのファイルは、必要になったときに読まれる。

- `CLAUDE.md`: そのディレクトリのほかのファイルを、Claude が読む、書く、編集したとき。
- `AGENTS.md`: そのディレクトリのファイルを Read ツールで開いたとき。ただし、同じディレクトリに `CLAUDE.md`（`CLAUDE.local.md` を含む）がないときに限る。
- 読まれないもの: `AGENTS.local.md`、`AGENTS.override.md`、`.agents/` 配下のファイル。

2026-11-23 に試して確認した（詳細は [2026-11-23 のメモ](../../memo/2026/20261123.md)）。`CLAUDE.md` のないプロジェクトで、ルートの `AGENTS.md` は、会話の最初から読み込まれた。サブディレクトリの `AGENTS.md` は、作成した直後には読み込まれず、同じディレクトリのファイルを Read したあとに、内容が会話の文脈に追加された。読み込みは作業の開始後になるので、作業の前の判断には、効かない可能性がある。

## ルール（.claude/rules/）

指示をテーマごとのファイルに分けて置ける。

- フロントマターの `paths` に glob を書くと、該当するファイルを扱うときだけ、そのルールが読み込まれる。
- `paths` がないルールは、セッションの開始時に読み込まれる。

```markdown
---
paths:
  - "docs/**/*.md"
---

ルールの本文
```

- ユーザー単位のルールは、`~/.claude/rules/` に置く。

## スキル

- プロジェクトのスキルは `.claude/skills/<name>/SKILL.md`、個人のスキルは `~/.claude/skills/` に置く。プラグインに含めることもできる。プラグインのスキルは、通常は `プラグイン名:スキル名` の名前空間で区別される（例外は、次の節の、ディレクトリ直下に `SKILL.md` を置く場合）。
- `SKILL.md` は、フロントマターと、手順の本文でできている。フロントマターの `description` に、どんなときに使うかを書く。これを元に、Claude がスキルを選ぶ。

### スキルのフォルダをプラグインとして使う（skills-dir プラグイン）

`~/.claude/skills/` または `<project>/.claude/skills/` の下のディレクトリに `.claude-plugin/plugin.json` を置くと、そのディレクトリがプラグインとして読み込まれる。マーケットプレイスからインストールしなくてよい。2026-11-23 に、公式ドキュメントの [Create a Claude Code plugin](https://code.claude.com/docs/en/plugins/create)、[Plugin loading reference](https://code.claude.com/docs/en/plugins/loading)、[Plugin manifest reference](https://code.claude.com/docs/en/plugins-reference) で確認した。ドキュメントは、この機能を experimental や preview とは表示していない。導入されたバージョンも書かれていない。

- 置き場所: 個人用は `~/.claude/skills/<dir>/`、プロジェクト用は `<project>/.claude/skills/<dir>/`。個人用とプロジェクト用に同じ名前のプラグインがあると、個人用が読み込まれ、プロジェクト用は捨てられる。
- 読み込み: Claude Code は、セッションの開始時に、フラグやインストールの操作なしで、自動的に読み込む。実行中のセッションには、`/reload-plugins` で反映する。
    - 個人用は、信頼の確認が要らない。
    - プロジェクト用は、ワークスペースの信頼のダイアログを承認するまで、読み込まれない。Claude Code を、リポジトリのルートで起動しないと、読み込まれない。
- 識別子: `<plugin-name>@skills-dir`。`<plugin-name>` は、`plugin.json` の `name`。`skills-dir` は、マーケットプレイス名の位置に入る予約名で、マーケットプレイス名には使えない。設定ファイルの `enabledPlugins` や、`claude plugin list --json` で使う。
- 構成: `.claude-plugin/` には `plugin.json` だけを置く。スキルの置き方は、2通りある。
    - `skills/<skill-name>/SKILL.md`: `/<plugin-name>:<skill-name>` の名前空間つきで呼び出す。
    - ディレクトリ直下の `SKILL.md`: 名前空間なしで、`/<dir>` で呼び出す。
- 無効化: `plugin.json` の `defaultEnabled`（既定は `true`）、設定ファイルの `enabledPlugins` の `"<plugin-name>@skills-dir"`、または `claude plugin disable <plugin-name>@skills-dir` で行う。
- キャッシュ: ディレクトリは、その場で読み込まれ、キャッシュにコピーされない。

!!! note
    管理者が、次のいずれかの設定で skills-dir プラグインを止めていると、プラグインは、エラーなしでスキップされる。`/plugin` や `claude plugin list` にも出ない。

    - `strictPluginOnlyCustomization`
    - `strictKnownMarketplaces`（`{ "source": "skills-dir" }` のエントリを含まない場合）
    - `blockedMarketplaces`

2026-11-23 時点で、ドキュメントに書かれていないこと:

- シンボリックリンク: `~/.claude/skills/` の中のリンクの扱いは、書かれていない。2026-11-23 に、`~/.claude/skills/<dir>` から、別の場所にあるプラグインのディレクトリへのシンボリックリンクを作って試した。リンクを作ったセッションとは別のセッションで、リンク先のプラグインのスキルが認識された。
- バージョン管理、更新、`dependencies`、`${CLAUDE_PLUGIN_ROOT}` の値: skills-dir プラグインでの扱いは、書かれていない。

## 参考

- [How Claude remembers your project - Claude Code Docs](https://code.claude.com/docs/en/memory): CLAUDE.md、`@` による取り込み、`.claude/rules/`
- [Skills - Claude Code Docs](https://code.claude.com/docs/en/skills): スキルの置き場所とフロントマター
- [Feature Request: Support AGENTS.md · Issue #6235 · anthropics/claude-code](https://github.com/anthropics/claude-code/issues/6235): `AGENTS.md` 対応の要望

[^release-2-1-277]: [Release v2.1.277 · anthropics/claude-code](https://github.com/anthropics/claude-code/releases/tag/v2.1.277)

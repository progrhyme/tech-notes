# Claude Code

公式サイト: [Claude Code](https://claude.com/product/claude-code)、[ドキュメント](https://code.claude.com/docs/)

Anthropic のコーディングエージェント。ここでは、リポジトリに置いて使う機能(指示、ルール、スキル)の置き方をまとめる。

## 指示ファイル(CLAUDE.md)

- Claude Code は、`CLAUDE.md` を読む。v2.1.277(9月18日のリリース)で、`AGENTS.md` のサポートが追加された[^release-2-1-277]。
- リリースノートの記述: `CLAUDE.md` がないプロジェクトでは、代わりに `AGENTS.md` を読む。`/config` の「Project instructions」で変更できる。Bedrock、Vertex、Foundry では、v2.1.277 の時点では使えない。
- `CLAUDE.md` がある場合は、`CLAUDE.md` が使われると考えられる。「Project instructions」の選択肢の内容は、リリースノートには書かれていない。
- `AGENTS.md` を使いつつ、Claude Code だけの指示を足したいときは、`CLAUDE.md` から `AGENTS.md` を取り込む。

```markdown
@AGENTS.md

## Claude Code 向けの追加の指示
```

!!! note
    2026-11-21 に確認した、公式ドキュメントのメモリのページには、「`AGENTS.md` は読まない」とあった。リリースノートとの食い違いは、ドキュメントの更新が追いついていないためと考えられる(推測)。`CLAUDE.md` と `AGENTS.md` が両方あるときの扱い、`CLAUDE.local.md` の扱いは、リリースノートに記述がなく、未確認。

- `@パス` で、ほかのファイルを取り込める。相対パスは、取り込む側のファイルからの位置で解決される。取り込みの入れ子は、最大4段まで。
- ユーザー単位の指示は、`~/.claude/CLAUDE.md` に置く。

## ルール(.claude/rules/)

指示をテーマごとのファイルに分けて置ける。

- フロントマターの `paths` に glob を書くと、該当するファイルを扱うときだけ、そのルールが読み込まれる。
- `paths` がないルールは、セッションの開始時に読み込まれる。

```markdown
---
paths:
  - "docs/**/*.md"
---

# 記事の書き方

(ルールの内容)
```

- ユーザー単位のルールは、`~/.claude/rules/` に置く。

## スキル

- プロジェクトのスキルは `.claude/skills/<name>/SKILL.md`、個人のスキルは `~/.claude/skills/` に置く。プラグインに含めることもできる。
- `SKILL.md` は、フロントマターと、手順の本文でできている。フロントマターの `name` は省略でき、省略するとディレクトリ名になる。`description` に、どんなときに使うかを書く。これを元に、Claude がスキルを選ぶ。
- 同梱のスキルと同じ名前のスキルを、プロジェクトや個人で作ると、そちらが優先される。プラグインのスキルは、`プラグイン名:スキル名` の名前空間で区別される。

## 参考

- [How Claude remembers your project - Claude Code Docs](https://code.claude.com/docs/en/memory): CLAUDE.md、`@` による取り込み、`.claude/rules/`
- [Skills - Claude Code Docs](https://code.claude.com/docs/en/skills): スキルの置き場所とフロントマター
- [Feature Request: Support AGENTS.md · Issue #6235 · anthropics/claude-code](https://github.com/anthropics/claude-code/issues/6235): `AGENTS.md` 対応の要望

[^release-2-1-277]: [Release v2.1.277 · anthropics/claude-code](https://github.com/anthropics/claude-code/releases/tag/v2.1.277)(公式のリリースノート。「Added AGENTS.md support」の項目)

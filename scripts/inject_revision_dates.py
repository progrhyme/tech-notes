#!/usr/bin/env python3
"""docs/ の記事のフロントマターに、作成日と最終更新日を挿入する。

Zensical は、MkDocs 時代の git-revision-date-localized プラグインに対応していない。
代わりに、テーマが読むフィールドを、Git の履歴から作って、フロントマターに書く。

- revision_date:               最終更新日(そのファイルに触れたコミットの、最も新しい author date)
- git_creation_date_localized: 作成日(同、最も古い author date。リネームを追跡する)

日付は、YYYY-MM-DD の文字列。

CI(GitHub Actions)で、デプロイの前に実行する。ソースのファイルが変わるので、ローカルでは
実行しない(環境変数 CI がないときは、--force がなければ拒否する)。
CI のチェックアウトは、履歴の全体を取ること(actions/checkout の fetch-depth: 0)。
書き戻すときに、改行は LF に、BOM は取り除く(CI のチェックアウトだけで、コミットされないため)。

使い方: uv run python scripts/inject_revision_dates.py [--root DIR] [--dry-run] [--force]
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from revision_lib.frontmatter import set_fields
from revision_lib.gitdates import GitError, file_dates, is_shallow, is_work_tree

# このファイルは <root>/scripts/ にある。
ROOT = Path(__file__).resolve().parents[1]

DOCS_DIR = "docs"
UPDATED_KEY = "revision_date"
CREATED_KEY = "git_creation_date_localized"


def check_environment(root: Path, force: bool) -> None:
    """実行してよい環境か調べる。だめなら、メッセージを添えて終了する(git の失敗は GitError)。"""
    if not (os.environ.get("CI") or force):
        sys.exit(
            "error: ソースのファイルを書き換えるので、ローカルでは実行しない"
            "(CI で実行する。どうしても必要なときは --force)"
        )
    if not (root / DOCS_DIR).is_dir():
        sys.exit(f"error: {DOCS_DIR}/ が見つからない: {root / DOCS_DIR}")
    if not is_work_tree(root):
        sys.exit(f"error: Git のリポジトリではない: {root}")
    if is_shallow(root):
        sys.exit(
            "error: 浅いクローンでは、日付が正しく取れない"
            "(actions/checkout に fetch-depth: 0 を指定する)"
        )


def inject(root: Path, dry_run: bool) -> tuple[int, list[str]]:
    """docs/ のすべての .md に日付を挿入する。(挿入した数, 履歴がなくスキップしたパス) を返す。"""
    injected = 0
    skipped: list[str] = []
    for path in sorted((root / DOCS_DIR).rglob("*.md")):
        rel = path.relative_to(root).as_posix()
        dates = file_dates(root, rel)
        if dates is None:
            skipped.append(rel)
            continue
        text = path.read_text(encoding="utf-8-sig")  # BOM を取り除き、改行を LF にする
        new_text = set_fields(text, {UPDATED_KEY: dates.updated, CREATED_KEY: dates.created})
        if not dry_run:
            path.write_text(new_text, encoding="utf-8", newline="\n")
        injected += 1
    return injected, skipped


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--root", default=str(ROOT), help="リポジトリのルート(既定: このファイルの位置から決める)")
    parser.add_argument("--dry-run", action="store_true", help="ファイルを書き換えずに、件数だけ出す")
    parser.add_argument("--force", action="store_true", help="環境変数 CI がなくても実行する")
    args = parser.parse_args()

    root = Path(args.root)
    try:
        check_environment(root, args.force)
        injected, skipped = inject(root, args.dry_run)
    except GitError as e:
        sys.exit(f"error: {e}")

    for rel in skipped:
        print(f"warning: Git の履歴がないので、スキップした: {rel}", file=sys.stderr)
    action = "挿入する(dry-run)" if args.dry_run else "挿入した"
    print(f"日付を{action}: {injected} ファイル、スキップ: {len(skipped)} ファイル")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""docs/ の記事の概要インデックス(agent/index/)を扱うスクリプト。

Python 標準ライブラリのみを使う。`uv run python scripts/docindex.py <サブコマンド>` で実行する。

サブコマンド:
  extract [パス...]   ページごとに、description、H1、H2、行数を出す(--json で JSON)
  draft [ディレクトリ] インデックスの下書き用に、nav の順で、材料つきの項目の雛形を出す
  check              docs/ のページとインデックスの項目の過不足を調べる

対象は docs/ 配下の *.md。docs/memo/ は対象外。
パスは docs/ からの相対パス(例: cli/jq.md)で書く。

機能は scripts/docindex_lib/ のモジュールにある。このファイルは、コマンドラインの処理だけを持つ。
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path

from docindex_lib.catalog import DOCS_DIR, TargetError, all_pages, select_pages
from docindex_lib.checking import INDEX_DIR, MAX_SUMMARY_LEN, collect_entries, find_problems
from docindex_lib.formatting import format_draft, format_material
from docindex_lib.nav import sort_by_nav
from docindex_lib.pages import read_page

# このファイルは <root>/scripts/ にある。
ROOT = Path(__file__).resolve().parents[1]


def cmd_extract(args: argparse.Namespace) -> int:
    root = Path(args.root)
    docs = root / DOCS_DIR
    rels = sort_by_nav(root, select_pages(docs, args.paths))
    pages = [read_page(docs, rel) for rel in rels]
    if args.json:
        json.dump([asdict(page) for page in pages], sys.stdout, ensure_ascii=False, indent=2)
        print()
        return 0
    for page in pages:
        print(format_material(page))
    return 0


def cmd_draft(args: argparse.Namespace) -> int:
    root = Path(args.root)
    docs = root / DOCS_DIR
    targets = [args.directory] if args.directory else []
    for rel in sort_by_nav(root, select_pages(docs, targets)):
        print(format_draft(read_page(docs, rel)))
    return 0


def cmd_check(args: argparse.Namespace) -> int:
    root = Path(args.root)
    pages = set(all_pages(root / DOCS_DIR))
    entries = collect_entries(root / INDEX_DIR)
    errors, warnings = find_problems(pages, entries, args.max_len)

    for message in warnings:
        print(f"warning: {message}")
    for message in errors:
        print(f"error: {message}")
    print(f"ページ {len(pages)}、項目 {len(entries)}、エラー {len(errors)}、警告 {len(warnings)}")
    return 1 if errors or (args.strict and warnings) else 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--root", default=str(ROOT), help="リポジトリのルート(既定: このファイルの位置から決める)"
    )
    subparsers = parser.add_subparsers(dest="cmd", required=True)

    extract = subparsers.add_parser("extract", help="ページの材料を出す")
    extract.add_argument(
        "paths", nargs="*", help="docs/ からの相対パス(ファイルまたはディレクトリ)。省略すると全ページ"
    )
    extract.add_argument("--json", action="store_true", help="JSON で出す")
    extract.set_defaults(func=cmd_extract)

    draft = subparsers.add_parser("draft", help="インデックスの下書きの雛形を出す")
    draft.add_argument(
        "directory", nargs="?", help="docs/ からの相対パス。`.` は docs/ 直下。省略すると全ページ"
    )
    draft.set_defaults(func=cmd_draft)

    check = subparsers.add_parser("check", help="docs/ とインデックスの過不足を調べる")
    check.add_argument(
        "--max-len", type=int, default=MAX_SUMMARY_LEN, help="概要の長さの上限(文字数)"
    )
    check.add_argument("--strict", action="store_true", help="警告もエラーとして扱う")
    check.set_defaults(func=cmd_check)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    docs = Path(args.root) / DOCS_DIR
    if not docs.is_dir():
        # docs/ がないと、ページが0件のまま check が成功してしまう。
        sys.exit(f"error: {DOCS_DIR}/ が見つからない: {docs}")
    try:
        return args.func(args)
    except TargetError as e:
        sys.exit(f"error: {e}")


if __name__ == "__main__":
    sys.exit(main())

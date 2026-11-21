"""docs/ のページの一覧と、パスによる絞り込み。"""

from __future__ import annotations

from pathlib import Path

DOCS_DIR = "docs"
EXCLUDED_DIR = "memo"  # 概要の対象外のディレクトリ(docs/ 直下)


class TargetError(Exception):
    """対象のパスが見つからない、など、利用者の指定に起因するエラー。"""


def all_pages(docs: Path) -> list[str]:
    """docs/ からの相対パスで、対象のページをすべて返す(パス順)。"""
    return sorted(
        rel.as_posix()
        for rel in (p.relative_to(docs) for p in docs.rglob("*.md"))
        if rel.parts[0] != EXCLUDED_DIR
    )


def select_pages(docs: Path, targets: list[str]) -> list[str]:
    """パスまたはディレクトリ(docs/ からの相対)で、対象のページを選ぶ。"""
    pages = all_pages(docs)
    if not targets:
        return pages
    chosen: set[str] = set()
    for target in targets:
        target = target.strip("/")
        if target in ("", "."):  # docs/ 直下のページ
            chosen |= {rel for rel in pages if "/" not in rel}
        elif target in pages:
            chosen.add(target)
        else:
            under = {rel for rel in pages if rel.startswith(target + "/")}
            if not under:
                raise TargetError(f"対象が見つからない: {target}")
            chosen |= under
    return sorted(chosen)

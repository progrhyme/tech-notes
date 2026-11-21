"""インデックスの項目の収集と、docs/ のページとの突き合わせ。"""

from __future__ import annotations

import re
from pathlib import Path
from typing import NamedTuple

INDEX_DIR = Path("agent") / "index"
TOP_INDEX_FILE = "index.md"  # docs/ 直下のページを載せるインデックスのファイル
MAX_SUMMARY_LEN = 60

# インデックスの項目: `パス` — 概要(行頭の「- 」は許容する)
ENTRY_RE = re.compile(r"^(?:[-*]\s+)?`([^`]+\.md)`\s+—\s*(.*)$")


class Entry(NamedTuple):
    """インデックスの1項目。"""

    file: str  # agent/index/ からの相対パス
    line: int
    summary: str


def expected_index_location(rel: str) -> tuple[str, str | None]:
    """ページを載せるべきインデックスの場所を、(ファイル, ディレクトリ) で返す。

    パスは agent/index/ からの相対パス。docs/ 直下のページは、TOP_INDEX_FILE に載せる。
    それ以外は、トップレベルのディレクトリ名 <top> について、<top>.md、または、
    分割された <top>/ 配下のファイルに載せる(ディレクトリは <top>/)。
    """
    parts = rel.split("/")
    if len(parts) == 1:
        return TOP_INDEX_FILE, None
    return f"{parts[0]}.md", f"{parts[0]}/"


def collect_entries(index_dir: Path) -> dict[str, list[Entry]]:
    """agent/index/ 配下のファイルから、パスごとの項目を集める。"""
    entries: dict[str, list[Entry]] = {}
    if not index_dir.is_dir():
        return entries
    for file in sorted(index_dir.rglob("*.md")):
        rel_file = file.relative_to(index_dir).as_posix()
        for number, line in enumerate(file.read_text(encoding="utf-8").splitlines(), 1):
            match = ENTRY_RE.match(line)
            if match:
                entries.setdefault(match.group(1), []).append(
                    Entry(rel_file, number, match.group(2).strip())
                )
    return entries


def is_expected_file(file: str, rel: str) -> bool:
    """項目 rel を、インデックスのファイル file に載せてよいか。"""
    exact, prefix = expected_index_location(rel)
    return file == exact or (prefix is not None and file.startswith(prefix))


def missing_entries(pages: set[str], entries: dict[str, list[Entry]]) -> list[str]:
    return [f"項目がない: {rel}" for rel in sorted(pages - entries.keys())]


def stale_entries(pages: set[str], entries: dict[str, list[Entry]]) -> list[str]:
    return [
        f"実体がない項目: {rel}  ({entry.file}:{entry.line})"
        for rel in sorted(entries.keys() - pages)
        for entry in entries[rel]
    ]


def duplicate_entries(entries: dict[str, list[Entry]]) -> list[str]:
    errors = []
    for rel, found in sorted(entries.items()):
        if len(found) > 1:
            where = ", ".join(f"{e.file}:{e.line}" for e in found)
            errors.append(f"項目が重複: {rel}  ({where})")
    return errors


def check_entry(
    rel: str, entry: Entry, page_exists: bool, max_len: int
) -> tuple[list[str], list[str]]:
    """1つの項目の置き場所と概要を調べて、(エラー, 警告) のメッセージを返す。"""
    errors: list[str] = []
    warnings: list[str] = []
    where = f"{entry.file}:{entry.line}"
    if page_exists and not is_expected_file(entry.file, rel):
        expected = expected_index_location(rel)[0]
        errors.append(f"置き場所が違う項目: {rel}  ({where}。期待: {expected})")
    if not entry.summary or entry.summary.startswith("TODO"):
        errors.append(f"概要が未記入: {rel}  ({where})")
    elif len(entry.summary) > max_len:
        warnings.append(f"概要が長い({len(entry.summary)}字): {rel}  ({where})")
    return errors, warnings


def find_problems(
    pages: set[str], entries: dict[str, list[Entry]], max_len: int
) -> tuple[list[str], list[str]]:
    """ページと項目を突き合わせて、(エラー, 警告) のメッセージを返す。"""
    errors = [
        *missing_entries(pages, entries),
        *stale_entries(pages, entries),
        *duplicate_entries(entries),
    ]
    warnings: list[str] = []
    for rel, found in sorted(entries.items()):
        for entry in found:
            entry_errors, entry_warnings = check_entry(rel, entry, rel in pages, max_len)
            errors += entry_errors
            warnings += entry_warnings
    return errors, warnings

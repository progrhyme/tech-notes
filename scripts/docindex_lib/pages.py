"""Markdown ページから、概要の材料(description、H1、H2 など)を取り出す。"""

from __future__ import annotations

import re
from collections.abc import Iterator
from dataclasses import dataclass, field
from pathlib import Path

# 見出しとして情報が乏しいもの(小文字で比べる)。
GENERIC_HEADINGS = {
    "about", "はじめに", "tips", "参考", "参考資料", "参考情報", "getting started",
    "documentation", "概要", "reference", "references", "リファレンス", "links",
    "その他", "メモ", "memo", "see also", "関連", "関連リンク", "まとめ",
}

SMALL_PAGE_LINES = 15

FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
FRONT_MATTER_RE = re.compile(r"---\n(.*?)\n---\n", re.S)


@dataclass
class Page:
    path: str  # docs/ からの相対パス
    lines: int = 0
    description: str = ""
    h1: str = ""
    h2: list[str] = field(default_factory=list)
    flags: list[str] = field(default_factory=list)


def read_page(docs: Path, rel: str) -> Page:
    return parse_page(rel, (docs / rel).read_text(encoding="utf-8"))


def parse_page(rel: str, text: str) -> Page:
    page = Page(path=rel, lines=len(text.splitlines()))
    body = text
    front = FRONT_MATTER_RE.match(text)
    if front:
        page.description = parse_description(front.group(1))
        body = text[front.end():]
    for level, title in headings_outside_fences(body):
        if level == 1 and not page.h1:
            page.h1 = title
        elif level == 2:
            page.h2.append(title)
    page.flags = make_flags(page)
    return page


def headings_outside_fences(body: str) -> Iterator[tuple[int, str]]:
    """コードブロックの外にある見出しを、(レベル, 題名) で順に返す。"""
    fence = None  # 開いているコードブロックの区切り(例: "```")
    for line in body.splitlines():
        fence_match = FENCE_RE.match(line)
        if fence_match:
            mark = fence_match.group(1)
            if fence is None:
                fence = mark
            elif mark[0] == fence[0] and len(mark) >= len(fence):
                fence = None
            continue
        if fence is not None:
            continue
        heading = HEADING_RE.match(line)
        if heading:
            yield len(heading.group(1)), heading.group(2)


DESCRIPTION_KEY = "description:"


def parse_description(front: str) -> str:
    """フロントマターから description を取り出す(単純な YAML のみ対応)。"""
    lines = front.splitlines()
    start = next((i for i, line in enumerate(lines) if line.startswith(DESCRIPTION_KEY)), None)
    if start is None:
        return ""
    parts = [lines[start][len(DESCRIPTION_KEY):], *continuation_lines(lines, start + 1)]
    return unquote(" ".join(" ".join(parts).split()))


def continuation_lines(lines: list[str], start: int) -> list[str]:
    """YAML の値の続き(start 以降の、空行または字下げされた行)を返す。"""
    found = []
    for line in lines[start:]:
        if line != "" and line[0] not in " \t":
            break
        found.append(line)
    return found


def unquote(value: str) -> str:
    """前後が同じ引用符(' または ")なら、外す。"""
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
        return value[1:-1].strip()
    return value


def is_generic(title: str) -> bool:
    return title.strip().lower() in GENERIC_HEADINGS


def description_is_url(desc: str) -> bool:
    return bool(re.match(r"^(\[.*\]\()?https?://", desc))


def make_flags(page: Page) -> list[str]:
    flags = []
    if not [h for h in page.h2 if not is_generic(h)]:
        flags.append("review")  # 意味のある H2 がない。本文の冒頭を読むか、要確認にする
    if page.lines <= SMALL_PAGE_LINES:
        flags.append("small")
    if page.description and description_is_url(page.description):
        flags.append("url-desc")
    return flags

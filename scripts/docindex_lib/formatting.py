"""ページの材料と、インデックスの下書きの整形。"""

from __future__ import annotations

from .pages import Page, is_generic


def format_h2(page: Page) -> str:
    """H2 を " / " でつなぐ。汎用的な見出しは括弧で囲む。"""
    joined = " / ".join(f"({h})" if is_generic(h) else h for h in page.h2)
    return joined or "(なし)"


def material_lines(page: Page) -> list[str]:
    """ページの材料を、行のリストで返す。"""
    lines = [f"H1: {page.h1}", f"H2: {format_h2(page)}"]
    if page.description:
        lines.append(f"description: {page.description}")
    if page.flags:
        lines.append("flags: " + ", ".join(page.flags))
    return lines


def format_material(page: Page) -> str:
    return "\n".join([f"## {page.path}  ({page.lines}行)", *material_lines(page)]) + "\n"


def format_draft(page: Page) -> str:
    return "\n".join([f"`{page.path}` — TODO", *(f"  {line}" for line in material_lines(page))])

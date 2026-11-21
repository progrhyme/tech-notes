"""zensical.toml の nav から、ページの順序を取る。"""

from __future__ import annotations

import tomllib
from collections.abc import Iterator
from pathlib import Path

NAV_CONFIG = "zensical.toml"


def iter_nav_paths(items: list) -> Iterator[str]:
    """nav の項目から、ページのパスを、現れる順に返す。"""
    for item in items:
        if isinstance(item, str):
            yield item
        elif isinstance(item, dict):
            for value in item.values():
                yield from iter_nav_paths(value if isinstance(value, list) else [value])


def nav_order(root: Path) -> list[str]:
    """zensical.toml の nav に現れる順で、md のパスを返す。"""
    conf = tomllib.loads((root / NAV_CONFIG).read_text(encoding="utf-8"))
    nav = conf.get("project", {}).get("nav", [])
    return [rel for rel in iter_nav_paths(nav) if rel.endswith(".md")]


def sort_by_order(order: list[str], pages: list[str]) -> list[str]:
    """order に現れる順に並べる。order にないものは、最後にパス順で付ける。"""
    position = {rel: i for i, rel in enumerate(order)}
    return sorted(pages, key=lambda rel: (position.get(rel, len(position)), rel))


def sort_by_nav(root: Path, pages: list[str]) -> list[str]:
    """nav の順に並べる。nav にないものは、最後にパス順で付ける。"""
    return sort_by_order(nav_order(root), pages)

"""Markdown のフロントマター(YAML)に、キーと値を設定する。

単純な `key: value` の行だけを扱う。値は、1行の文字列で、単一引用符で囲んで書く
(YAML で日付型などに変換されないようにするため)。
text の改行は LF、先頭に BOM がないことを前提にする(呼び出し側で正規化する)。
"""

from __future__ import annotations

import re

# 先頭の `---` から、次の `---` の行まで。中身が空でもよい。
FRONT_MATTER_RE = re.compile(r"---\n(.*?\n)?---[ \t]*(?:\n|\Z)", re.S)


def format_line(key: str, value: str) -> str:
    """`key: 'value'` の行を作る。値の中の `'` は、`''` にする。値に改行を含めてはいけない。"""
    if "\n" in value or "\r" in value:
        raise ValueError(f"値に改行を含められない: {value!r}")
    escaped = value.replace("'", "''")
    return f"{key}: '{escaped}'"


def set_fields(text: str, fields: dict[str, str]) -> str:
    """text のフロントマターに、fields を設定した文字列を返す。

    - 既にあるキーは、値を置き換える(複数行の値は、続きの行ごと置き換える)。
    - ないキーは、フロントマターの末尾に足す。
    - フロントマターがなければ、先頭に作る。
    """
    match = FRONT_MATTER_RE.match(text)
    if match:
        # str.splitlines() は、U+2028 などでも分割して、値を壊すので、\n だけで分割する。
        body = match.group(1)
        lines = body[:-1].split("\n") if body else []
        rest = text[match.end():]
    else:
        lines = []
        rest = "\n" + text
    for key, value in fields.items():
        lines = replace_or_append(lines, key, format_line(key, value))
    return "---\n" + "".join(f"{line}\n" for line in lines) + "---\n" + rest


def replace_or_append(lines: list[str], key: str, new_line: str) -> list[str]:
    """lines の中の、トップレベルの `key:` の行を new_line に置き換える。なければ末尾に足す。"""
    start = next((i for i, line in enumerate(lines) if line.startswith(f"{key}:")), None)
    if start is None:
        return [*lines, new_line]
    end = start + 1
    while end < len(lines) and (lines[end] == "" or lines[end][0] in " \t"):
        end += 1
    return [*lines[:start], new_line, *lines[end:]]

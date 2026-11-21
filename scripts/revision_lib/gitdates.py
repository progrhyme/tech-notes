"""Git の履歴から、ファイルの作成日と最終更新日を取る。"""

from __future__ import annotations

import os
import subprocess
from dataclasses import dataclass
from pathlib import Path


class GitError(Exception):
    """git コマンドの失敗。"""


@dataclass(frozen=True)
class FileDates:
    created: str  # YYYY-MM-DD。ファイルに触れたコミットの author date のうち、最も古いもの
    updated: str  # YYYY-MM-DD。同、最も新しいもの


def run_git(repo: Path, *args: str) -> str:
    """repo で git を実行して、標準出力を返す。失敗したら GitError。

    - パスは、glob ではなく、そのままの文字列として扱う(`--literal-pathspecs`)。
    - メッセージの言語を揃えるため、ロケールは C にする。
    """
    try:
        result = subprocess.run(
            ["git", "--literal-pathspecs", "-C", str(repo), *args],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            env={**os.environ, "LC_ALL": "C"},
        )
    except FileNotFoundError as e:
        raise GitError("git コマンドが見つからない") from e
    if result.returncode != 0:
        raise GitError(result.stderr.strip() or f"git {' '.join(args)} が失敗した")
    return result.stdout


def is_work_tree(repo: Path) -> bool:
    """repo が Git の作業ツリーの中か。リポジトリでないとき以外の git の失敗は、GitError にする。"""
    try:
        return run_git(repo, "rev-parse", "--is-inside-work-tree").strip() == "true"
    except GitError as e:
        if "not a git repository" in str(e).lower():
            return False
        raise


def is_shallow(repo: Path) -> bool:
    """浅いクローン(履歴が一部しかない)か。"""
    return run_git(repo, "rev-parse", "--is-shallow-repository").strip() == "true"


def file_dates(repo: Path, rel: str) -> FileDates | None:
    """rel(repo からの相対パス)の、作成日と最終更新日を返す。履歴がなければ None。

    日付は、author date の日付部分(author のタイムゾーンのまま)。リネームは追跡する。
    """
    out = run_git(repo, "log", "--follow", "--no-show-signature", "--format=%as", "--", rel)
    dates = out.split()
    if not dates:
        return None
    return FileDates(created=min(dates), updated=max(dates))

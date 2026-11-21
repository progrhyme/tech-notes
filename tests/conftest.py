"""テスト共通の fixture。

実行: リポジトリのルートで `uv run pytest`
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "docindex.py"

# docs/ より小さな、テスト用のサイト(docs/、zensical.toml、agent/index/)。
FIXTURE_SITE = Path(__file__).resolve().parent / "fixtures" / "site"

# fixture の対象ページを、nav の順に並べたもの(memo/ は対象外。software/extra.md は nav にない)。
FIXTURE_PAGES_IN_NAV_ORDER = [
    "index.md",
    "software/index.md",
    "software/git.md",
    "software/k8s/index.md",
    "software/k8s/pod.md",
    "cli/index.md",
    "cli/jq.md",
    "cli/shell/bash.md",
    "char.md",
    "os/index.md",
    "software/extra.md",
]


@pytest.fixture
def fixture_site() -> Path:
    """テスト用サイトのルート(読み取り専用として使う)。"""
    return FIXTURE_SITE


@pytest.fixture
def fixture_docs() -> Path:
    return FIXTURE_SITE / "docs"


@pytest.fixture
def pages_in_nav_order() -> list[str]:
    return list(FIXTURE_PAGES_IN_NAV_ORDER)


@pytest.fixture
def site_copy(tmp_path: Path) -> Path:
    """テスト用サイトを一時ディレクトリにコピーして返す(自由に変更してよい)。"""
    dest = tmp_path / "site"
    shutil.copytree(FIXTURE_SITE, dest)
    return dest


@pytest.fixture
def run_cli() -> Callable[..., subprocess.CompletedProcess[str]]:
    """scripts/docindex.py を、別プロセスで実行する関数。"""

    def run(*args: str | Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), *map(str, args)],
            capture_output=True,
            text=True,
            encoding="utf-8",
        )

    return run

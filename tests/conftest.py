"""テスト共通の fixture。

実行: リポジトリのルートで `uv run pytest`
"""

from __future__ import annotations

import os
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


@pytest.fixture(autouse=True)
def isolated_git_env(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """開発者の Git の設定や環境変数に、テストの結果が左右されないようにする。"""
    for name in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "CI"):
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setenv("HOME", str(tmp_path))
    monkeypatch.setenv("GIT_CONFIG_GLOBAL", os.devnull)
    monkeypatch.setenv("GIT_CONFIG_SYSTEM", os.devnull)
    # tmp_path より上のディレクトリにあるリポジトリを、拾わないようにする。
    monkeypatch.setenv("GIT_CEILING_DIRECTORIES", str(tmp_path.parent))


class GitRepo:
    """テスト用の Git リポジトリ。コミットの日時を指定できる。"""

    def __init__(self, path: Path) -> None:
        self.path = path

    def git(self, *args: str, date: str | None = None) -> str:
        """リポジトリで git を実行する。date は、`2026-04-01` または `2026-04-01T00:30:00+09:00`。"""
        env = dict(os.environ)
        if date:
            timestamp = date if "T" in date else f"{date}T12:00:00+09:00"
            env["GIT_AUTHOR_DATE"] = env["GIT_COMMITTER_DATE"] = timestamp
        result = subprocess.run(
            ["git", "-C", str(self.path), *args],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            env=env,
        )
        return result.stdout

    def write(self, rel: str, text: str) -> Path:
        """リポジトリの中に、ファイルを書く(必要なディレクトリも作る)。"""
        path = self.path / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def commit(self, message: str, date: str) -> None:
        """すべての変更をコミットする。date は、`git()` と同じ書式。"""
        self.git("add", "-A")
        self.git("commit", "-q", "-m", message, date=date)


@pytest.fixture
def git_repo(tmp_path: Path) -> GitRepo:
    """空の Git リポジトリ(ユーザー設定済み、署名なし)。"""
    path = tmp_path / "repo"
    path.mkdir()
    repo = GitRepo(path)
    repo.git("init", "-q", "-b", "main")
    repo.git("config", "user.name", "Test")
    repo.git("config", "user.email", "test@example.com")
    repo.git("config", "commit.gpgsign", "false")
    return repo

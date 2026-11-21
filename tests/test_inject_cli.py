"""scripts/inject_revision_dates.py を、別プロセスで実行して、結果のファイルと終了コードを調べる。"""

import os
import subprocess
import sys
from pathlib import Path

import pytest
from conftest import REPO_ROOT

INJECT = REPO_ROOT / "scripts" / "inject_revision_dates.py"

FRONT = "---\ndate: '2020-01-01T00:00:00+09:00'\ndescription: 概要\n---\n\n# A\n"


def run_inject(repo: Path, *args: str, ci: bool = True) -> subprocess.CompletedProcess[str]:
    """scripts/inject_revision_dates.py を、別プロセスで実行する(ci=True なら、環境変数 CI を付ける)。"""
    env = dict(os.environ)  # CI は、autouse の fixture で、取り除いてある
    if ci:
        env["CI"] = "true"
    return subprocess.run(
        [sys.executable, str(INJECT), "--root", str(repo), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=env,
    )


@pytest.fixture
def site(git_repo):
    """docs/ に2ページ(記事とメモ)があり、記事は2回コミットされたリポジトリ。"""
    git_repo.write("docs/a.md", FRONT)
    git_repo.write("docs/memo/2026/m.md", "# メモ\n")
    git_repo.commit("add", "2026-01-10")
    git_repo.write("docs/a.md", FRONT + "\n追記\n")
    git_repo.commit("modify", "2026-02-20")
    return git_repo


def test_injects_dates_and_keeps_existing_front_matter(site):
    result = run_inject(site.path)
    assert result.returncode == 0, result.stderr
    assert "日付を挿入した: 2 ファイル、スキップ: 0 ファイル" in result.stdout
    assert (site.path / "docs/a.md").read_text(encoding="utf-8") == (
        "---\ndate: '2020-01-01T00:00:00+09:00'\ndescription: 概要\n"
        "revision_date: '2026-02-20'\ngit_creation_date_localized: '2026-01-10'\n---\n\n# A\n\n追記\n"
    )


def test_pages_without_front_matter_and_memo_pages_are_included(site):
    run_inject(site.path)
    assert (site.path / "docs/memo/2026/m.md").read_text(encoding="utf-8") == (
        "---\nrevision_date: '2026-01-10'\ngit_creation_date_localized: '2026-01-10'\n---\n\n# メモ\n"
    )


def test_running_twice_gives_the_same_result(site):
    run_inject(site.path)
    first = (site.path / "docs/a.md").read_text(encoding="utf-8")
    run_inject(site.path)
    assert (site.path / "docs/a.md").read_text(encoding="utf-8") == first


def test_dry_run_changes_nothing(site):
    before = (site.path / "docs/a.md").read_text(encoding="utf-8")
    result = run_inject(site.path, "--dry-run")
    assert result.returncode == 0
    assert "挿入する(dry-run): 2 ファイル" in result.stdout
    assert (site.path / "docs/a.md").read_text(encoding="utf-8") == before


def test_refuses_to_run_without_ci(site):
    before = (site.path / "docs/a.md").read_text(encoding="utf-8")
    result = run_inject(site.path, ci=False)
    assert result.returncode == 1
    assert "ローカルでは実行しない" in result.stderr
    assert (site.path / "docs/a.md").read_text(encoding="utf-8") == before


def test_force_allows_running_without_ci(site):
    assert run_inject(site.path, "--force", ci=False).returncode == 0


def test_refuses_shallow_clone(site, tmp_path):
    clone = tmp_path / "shallow"
    site.git("clone", "-q", "--depth", "1", f"file://{site.path}", str(clone))
    result = run_inject(clone)
    assert result.returncode == 1
    assert "fetch-depth: 0" in result.stderr


def test_untracked_file_is_skipped_with_warning(site):
    site.write("docs/untracked.md", "# 未追跡\n")
    result = run_inject(site.path)
    assert result.returncode == 0
    assert "日付を挿入した: 2 ファイル、スキップ: 1 ファイル" in result.stdout
    assert "docs/untracked.md" in result.stderr
    assert (site.path / "docs/untracked.md").read_text(encoding="utf-8") == "# 未追跡\n"


def test_non_markdown_files_are_ignored(site):
    site.write("docs/data.txt", "x\n")
    site.commit("add txt", "2026-03-01")
    run_inject(site.path)
    assert (site.path / "docs/data.txt").read_text(encoding="utf-8") == "x\n"


def test_fails_without_docs_dir(tmp_path):
    result = run_inject(tmp_path)
    assert result.returncode == 1
    assert "docs/ が見つからない" in result.stderr


def test_fails_outside_a_git_repository(tmp_path):
    (tmp_path / "docs").mkdir()
    result = run_inject(tmp_path)
    assert result.returncode == 1
    assert "Git のリポジトリではない" in result.stderr


def test_crlf_file_is_rewritten_with_lf_without_duplicating_front_matter(git_repo):
    path = git_repo.path / "docs/crlf.md"
    path.parent.mkdir(parents=True)
    path.write_bytes(b"---\r\ndescription: x\r\n---\r\n\r\n# A\r\n")
    git_repo.commit("add crlf", "2026-01-10")
    run_inject(git_repo.path)
    assert path.read_bytes() == (
        b"---\ndescription: x\nrevision_date: '2026-01-10'\n"
        b"git_creation_date_localized: '2026-01-10'\n---\n\n# A\n"
    )


def test_bom_is_removed_without_duplicating_front_matter(git_repo):
    path = git_repo.path / "docs/bom.md"
    path.parent.mkdir(parents=True)
    path.write_bytes("\ufeff---\ndescription: x\n---\n\n# A\n".encode("utf-8"))
    git_repo.commit("add bom", "2026-01-10")
    run_inject(git_repo.path)
    assert path.read_text(encoding="utf-8") == (
        "---\ndescription: x\nrevision_date: '2026-01-10'\n"
        "git_creation_date_localized: '2026-01-10'\n---\n\n# A\n"
    )


def test_file_names_with_glob_characters_get_their_own_dates(git_repo):
    git_repo.write("docs/a*.md", "# star\n")
    git_repo.commit("add star", "2026-01-10")
    git_repo.write("docs/ab.md", "# ab\n")
    git_repo.commit("add ab", "2026-06-01")
    run_inject(git_repo.path)
    star = (git_repo.path / "docs/a*.md").read_text(encoding="utf-8")
    assert "revision_date: '2026-01-10'" in star

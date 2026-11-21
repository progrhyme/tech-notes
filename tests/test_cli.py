"""scripts/docindex.py を、別プロセスで実行して、出力と終了コードを調べる。"""

import json
import re
from pathlib import Path


def stub_lines(stdout: str) -> list[str]:
    return [line for line in stdout.splitlines() if line.startswith("`")]


# --- check ---


def test_check_passes_on_consistent_site(run_cli, fixture_site):
    result = run_cli("--root", fixture_site, "check")
    assert result.returncode == 0, result.stdout
    assert "ページ 11、項目 11、エラー 0、警告 0" in result.stdout


def test_check_fails_when_index_file_is_missing(run_cli, site_copy):
    (site_copy / "agent" / "index" / "os.md").unlink()
    result = run_cli("--root", site_copy, "check")
    assert result.returncode == 1
    assert "error: 項目がない: os/index.md" in result.stdout


def test_check_fails_for_new_page_without_entry(run_cli, site_copy):
    (site_copy / "docs" / "new.md").write_text("# New\n", encoding="utf-8")
    result = run_cli("--root", site_copy, "check")
    assert result.returncode == 1
    assert "error: 項目がない: new.md" in result.stdout


def test_check_needs_no_entry_for_memo_pages(run_cli, site_copy):
    (site_copy / "docs" / "memo" / "2026" / "20260102.md").write_text("# メモ\n", encoding="utf-8")
    assert run_cli("--root", site_copy, "check").returncode == 0


def test_check_fails_for_stale_entry_after_page_removal(run_cli, site_copy):
    (site_copy / "docs" / "char.md").unlink()
    result = run_cli("--root", site_copy, "check")
    assert result.returncode == 1
    assert "error: 実体がない項目: char.md" in result.stdout


def test_check_warns_on_long_summary_and_strict_fails(run_cli, site_copy):
    cli_index = site_copy / "agent" / "index" / "cli.md"
    text = cli_index.read_text(encoding="utf-8")
    cli_index.write_text(
        re.sub(r"^(- `cli/jq.md` — ).*$", r"\1" + "あ" * 61, text, flags=re.M), encoding="utf-8"
    )

    normal = run_cli("--root", site_copy, "check")
    assert normal.returncode == 0
    assert "warning: 概要が長い(61字): cli/jq.md" in normal.stdout
    assert run_cli("--root", site_copy, "check", "--strict").returncode == 1
    assert run_cli("--root", site_copy, "check", "--max-len", "100").returncode == 0


def test_check_fails_without_docs_dir(run_cli, tmp_path):
    result = run_cli("--root", tmp_path, "check")
    assert result.returncode == 1
    assert "docs/ が見つからない" in result.stderr


# --- extract ---


def test_extract_json_lists_pages_in_nav_order(run_cli, fixture_site, pages_in_nav_order):
    result = run_cli("--root", fixture_site, "extract", "--json")
    assert result.returncode == 0, result.stderr
    assert [page["path"] for page in json.loads(result.stdout)] == pages_in_nav_order


def test_extract_json_has_parsed_fields(run_cli, fixture_site):
    result = run_cli("--root", fixture_site, "extract", "--json", "cli/jq.md")
    (page,) = json.loads(result.stdout)
    assert page["h1"] == "jq"
    assert page["h2"] == ["Filters", "Options"]


def test_extract_text_output(run_cli, fixture_site):
    result = run_cli("--root", fixture_site, "extract", "os/index.md")
    assert result.returncode == 0
    assert "## os/index.md" in result.stdout
    assert "flags: review, small" in result.stdout


def test_extract_fails_for_unknown_target(run_cli, fixture_site):
    result = run_cli("--root", fixture_site, "extract", "nosuch")
    assert result.returncode == 1
    assert "error: 対象が見つからない: nosuch" in result.stderr


# --- draft ---


def test_draft_for_directory_follows_nav_order(run_cli, fixture_site):
    result = run_cli("--root", fixture_site, "draft", "cli")
    assert result.returncode == 0, result.stderr
    assert stub_lines(result.stdout) == [
        "`cli/index.md` — TODO",
        "`cli/jq.md` — TODO",
        "`cli/shell/bash.md` — TODO",
    ]


def test_draft_for_top_level_pages(run_cli, fixture_site):
    result = run_cli("--root", fixture_site, "draft", ".")
    assert stub_lines(result.stdout) == ["`index.md` — TODO", "`char.md` — TODO"]


def test_draft_without_argument_covers_all_pages(run_cli, fixture_site, pages_in_nav_order):
    result = run_cli("--root", fixture_site, "draft")
    assert len(stub_lines(result.stdout)) == len(pages_in_nav_order)


# --- 実リポジトリ ---


def test_extract_runs_on_this_repository(run_cli):
    """既定の --root(このリポジトリ)で、コマンドが動くことだけを確かめる。"""
    result = run_cli("extract", "--json", "index.md")
    assert result.returncode == 0, result.stderr
    assert Path(json.loads(result.stdout)[0]["path"]).name == "index.md"

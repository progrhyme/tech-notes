import pytest
from docindex_lib.catalog import all_pages
from docindex_lib.checking import (
    Entry,
    check_entry,
    collect_entries,
    duplicate_entries,
    expected_index_location,
    find_problems,
    is_expected_file,
    missing_entries,
    stale_entries,
)


@pytest.mark.parametrize(
    ("file", "rel", "expected"),
    [
        pytest.param("index.md", "a.md", True, id="top-level-page-in-top-index"),
        pytest.param("cli.md", "a.md", False, id="top-level-page-in-directory-file"),
        pytest.param("cli.md", "cli/b.md", True, id="directory-file"),
        pytest.param("cli/index.md", "cli/b.md", True, id="split-directory"),
        pytest.param("os.md", "cli/b.md", False, id="other-directory-file"),
        pytest.param("cli2/index.md", "cli/b.md", False, id="similar-directory-name"),
    ],
)
def test_is_expected_file(file, rel, expected):
    assert is_expected_file(file, rel) is expected


def test_missing_and_stale_entries_are_sorted():
    entries = {"x.md": [Entry("index.md", 1, "概要")], "w.md": [Entry("index.md", 2, "概要")]}
    assert missing_entries({"b.md", "a.md"}, {}) == ["項目がない: a.md", "項目がない: b.md"]
    assert stale_entries(set(), entries) == [
        "実体がない項目: w.md  (index.md:2)",
        "実体がない項目: x.md  (index.md:1)",
    ]


def test_duplicate_entries_ignores_single_entries():
    entries = {"a.md": [Entry("index.md", 1, "概要")]}
    assert duplicate_entries(entries) == []


def test_check_entry_reports_all_problems_of_one_entry():
    errors, warnings = check_entry("cli/b.md", Entry("os.md", 3, "TODO"), True, 60)
    assert len(errors) == 2
    assert "置き場所が違う項目" in errors[0]
    assert "概要が未記入" in errors[1]
    assert warnings == []


def test_check_entry_skips_location_check_when_page_does_not_exist():
    errors, _ = check_entry("cli/b.md", Entry("os.md", 3, "概要"), False, 60)
    assert errors == []


@pytest.mark.parametrize(
    ("rel", "expected"),
    [
        pytest.param("index.md", ("index.md", None), id="top-level-page"),
        pytest.param("cli/jq.md", ("cli.md", "cli/"), id="page-in-directory"),
        pytest.param(
            "software/k8s/pod.md", ("software.md", "software/"), id="deep-page-uses-top-directory"
        ),
    ],
)
def test_expected_index_location(rel, expected):
    assert expected_index_location(rel) == expected


def test_collect_entries_from_fixture(fixture_site):
    entries = collect_entries(fixture_site / "agent" / "index")
    assert set(entries) == set(all_pages(fixture_site / "docs"))
    assert [e.file for e in entries["cli/jq.md"]] == ["cli.md"]
    assert [e.file for e in entries["software/git.md"]] == ["software/index.md"]
    assert [e.file for e in entries["software/k8s/pod.md"]] == ["software/k8s.md"]


def test_entry_has_line_number_and_summary(tmp_path):
    (tmp_path / "a.md").write_text("# 見出し\n\n`a.md` — 概要A\n", encoding="utf-8")
    assert collect_entries(tmp_path) == {"a.md": [Entry("a.md", 3, "概要A")]}


def test_collect_entries_accepts_list_markers_and_compact_separator(tmp_path):
    (tmp_path / "a.md").write_text("- `a.md` — 概要A\n* `b.md` —概要B\n", encoding="utf-8")
    entries = collect_entries(tmp_path)
    assert entries["a.md"][0].summary == "概要A"
    assert entries["b.md"][0].summary == "概要B"


def test_collect_entries_ignores_non_entry_lines(tmp_path):
    text = "# `a.md` — 見出し\n`memo/` は対象外。\n`a.txt` — md ではない\n説明 `b.md` — 行頭ではない\n"
    (tmp_path / "a.md").write_text(text, encoding="utf-8")
    assert collect_entries(tmp_path) == {}


def test_collect_entries_with_missing_index_dir(tmp_path):
    assert collect_entries(tmp_path / "nosuch") == {}


def test_consistent_fixture_has_no_problems(fixture_site):
    pages = set(all_pages(fixture_site / "docs"))
    entries = collect_entries(fixture_site / "agent" / "index")
    assert find_problems(pages, entries, 60) == ([], [])


def test_missing_entry():
    assert find_problems({"a.md"}, {}, 60) == (["項目がない: a.md"], [])


def test_stale_entry():
    errors, _ = find_problems(set(), {"a.md": [Entry("index.md", 4, "概要")]}, 60)
    assert errors == ["実体がない項目: a.md  (index.md:4)"]


def test_duplicate_entry():
    entries = {"a.md": [Entry("index.md", 1, "概要"), Entry("index.md", 2, "概要")]}
    errors, _ = find_problems({"a.md"}, entries, 60)
    assert errors == ["項目が重複: a.md  (index.md:1, index.md:2)"]


def test_entry_in_wrong_file():
    errors, _ = find_problems({"cli/b.md"}, {"cli/b.md": [Entry("os.md", 3, "概要")]}, 60)
    assert len(errors) == 1
    assert "置き場所が違う項目: cli/b.md" in errors[0]
    assert "期待: cli.md" in errors[0]


def test_top_level_page_in_directory_file_is_wrong():
    errors, _ = find_problems({"a.md"}, {"a.md": [Entry("cli.md", 3, "概要")]}, 60)
    assert "置き場所が違う項目: a.md" in errors[0]


def test_entry_in_split_directory_is_accepted():
    entries = {"cli/b.md": [Entry("cli/index.md", 3, "概要")]}
    assert find_problems({"cli/b.md"}, entries, 60) == ([], [])


@pytest.mark.parametrize("summary", ["TODO", ""])
def test_unfinished_summary_is_an_error(summary):
    errors, _ = find_problems({"a.md"}, {"a.md": [Entry("index.md", 5, summary)]}, 60)
    assert errors == ["概要が未記入: a.md  (index.md:5)"]


def test_long_summary_is_a_warning():
    errors, warnings = find_problems({"a.md"}, {"a.md": [Entry("index.md", 1, "あ" * 61)]}, 60)
    assert errors == []
    assert warnings == ["概要が長い(61字): a.md  (index.md:1)"]


def test_summary_at_the_limit_is_accepted():
    entries = {"a.md": [Entry("index.md", 1, "あ" * 60)]}
    assert find_problems({"a.md"}, entries, 60) == ([], [])


def test_max_len_is_configurable():
    _, warnings = find_problems({"a.md"}, {"a.md": [Entry("index.md", 1, "あ" * 11)]}, 10)
    assert len(warnings) == 1

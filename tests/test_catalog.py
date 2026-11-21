import pytest
from docindex_lib.catalog import TargetError, all_pages, select_pages


def test_all_pages_lists_pages_in_path_order(fixture_docs, pages_in_nav_order):
    assert all_pages(fixture_docs) == sorted(pages_in_nav_order)


def test_all_pages_excludes_memo(fixture_docs):
    assert not [rel for rel in all_pages(fixture_docs) if rel.startswith("memo/")]


def test_select_without_targets_selects_all(fixture_docs):
    assert select_pages(fixture_docs, []) == all_pages(fixture_docs)


@pytest.mark.parametrize(
    ("targets", "expected"),
    [
        pytest.param(["cli/jq.md"], ["cli/jq.md"], id="file"),
        pytest.param(
            ["cli"],
            ["cli/index.md", "cli/jq.md", "cli/shell/bash.md"],
            id="directory-includes-subdirectories",
        ),
        pytest.param(["."], ["char.md", "index.md"], id="dot-selects-top-level-pages-only"),
        pytest.param(["os", "cli/jq.md"], ["cli/jq.md", "os/index.md"], id="merged-and-sorted"),
    ],
)
def test_select_pages(fixture_docs, targets, expected):
    assert select_pages(fixture_docs, targets) == expected


def test_select_ignores_trailing_slash(fixture_docs):
    assert select_pages(fixture_docs, ["software/k8s/"]) == select_pages(
        fixture_docs, ["software/k8s"]
    )


@pytest.mark.parametrize(
    "target",
    [
        pytest.param("nosuch", id="unknown"),
        pytest.param("cl", id="directory-name-prefix-does-not-match"),
        pytest.param("memo", id="memo-is-not-selectable"),
    ],
)
def test_select_unknown_target_raises(fixture_docs, target):
    with pytest.raises(TargetError):
        select_pages(fixture_docs, [target])

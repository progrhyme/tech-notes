from docindex_lib.nav import iter_nav_paths, nav_order, sort_by_nav, sort_by_order


def test_sort_by_order_follows_the_given_order():
    assert sort_by_order(["b.md", "a.md", "c.md"], ["c.md", "a.md", "b.md"]) == [
        "b.md",
        "a.md",
        "c.md",
    ]


def test_sort_by_order_puts_unlisted_pages_last_in_path_order():
    assert sort_by_order(["b.md"], ["z.md", "b.md", "a.md"]) == ["b.md", "a.md", "z.md"]


def test_sort_by_order_with_empty_order_sorts_by_path():
    assert sort_by_order([], ["b.md", "a.md"]) == ["a.md", "b.md"]


def test_iter_nav_paths_flattens_nested_items_in_order():
    items = ["a.md", {"X": "b.md"}, {"Y": ["c.md", {"Z": "d.md"}]}]
    assert list(iter_nav_paths(items)) == ["a.md", "b.md", "c.md", "d.md"]


def test_iter_nav_paths_empty():
    assert list(iter_nav_paths([])) == []


def test_nav_order_reads_fixture_nav(fixture_site):
    assert nav_order(fixture_site) == [
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
        "memo/index.md",
        "memo/2026/20260101.md",
    ]


def test_nav_order_without_nav(tmp_path):
    (tmp_path / "zensical.toml").write_text('[project]\nsite_name = "x"\n')
    assert nav_order(tmp_path) == []


def test_nav_order_drops_non_md_entries(tmp_path):
    (tmp_path / "zensical.toml").write_text(
        '[project]\nnav = ["a.md", { "Ext" = "https://example.com/" }]\n'
    )
    assert nav_order(tmp_path) == ["a.md"]


def test_sort_by_nav_sorts_in_nav_order(fixture_site):
    pages = ["os/index.md", "char.md", "cli/jq.md", "index.md"]
    assert sort_by_nav(fixture_site, pages) == ["index.md", "cli/jq.md", "char.md", "os/index.md"]


def test_sort_by_nav_puts_pages_not_in_nav_last_in_path_order(fixture_site):
    pages = ["z.md", "a.md", "software/index.md"]
    assert sort_by_nav(fixture_site, pages) == ["software/index.md", "a.md", "z.md"]

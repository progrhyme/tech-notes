import pytest
from docindex_lib.pages import (
    Page,
    continuation_lines,
    description_is_url,
    headings_outside_fences,
    is_generic,
    make_flags,
    parse_description,
    parse_page,
    read_page,
    unquote,
)


@pytest.mark.parametrize(
    ("lines", "start", "expected"),
    [
        pytest.param(["a: 1", "  b", "", "c: 2"], 1, ["  b", ""], id="indented-and-blank"),
        pytest.param(["a: 1", "b: 2"], 1, [], id="no-continuation"),
        pytest.param(["a: 1", "\tb"], 1, ["\tb"], id="tab-indent"),
        pytest.param(["a: 1"], 1, [], id="at-end"),
    ],
)
def test_continuation_lines(lines, start, expected):
    assert continuation_lines(lines, start) == expected


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        pytest.param("'abc'", "abc", id="single"),
        pytest.param('"abc"', "abc", id="double"),
        pytest.param("'abc  '", "abc", id="inner-trailing-space"),
        pytest.param("'abc\"", "'abc\"", id="mismatched-quotes"),
        pytest.param("'", "'", id="single-character"),
        pytest.param("abc", "abc", id="unquoted"),
    ],
)
def test_unquote(value, expected):
    assert unquote(value) == expected


def headings(body: str) -> list[tuple[int, str]]:
    return list(headings_outside_fences(body))


@pytest.mark.parametrize(
    ("body", "expected"),
    [
        pytest.param("# A\n\ntext\n## B\n### C\n", [(1, "A"), (2, "B"), (3, "C")], id="levels"),
        pytest.param(
            "# A\n```sh\n# comment\n## not heading\n```\n## B\n",
            [(1, "A"), (2, "B")],
            id="backtick-fence",
        ),
        pytest.param("~~~\n# x\n~~~\n# y\n", [(1, "y")], id="tilde-fence"),
        pytest.param(
            "````md\n```\n# x\n```\n# y\n````\n# z\n",
            [(1, "z")],
            id="shorter-fence-does-not-close-longer",
        ),
        pytest.param(
            "```\n~~~\n# x\n```\n# y\n", [(1, "y")], id="other-fence-char-does-not-close"
        ),
        pytest.param("## Title ##\n", [(2, "Title")], id="trailing-hashes"),
        pytest.param("#hashtag\n", [], id="no-space-after-hashes"),
        pytest.param("# A\n```\n# B\n", [(1, "A")], id="unclosed-fence-hides-the-rest"),
    ],
)
def test_headings_outside_fences(body, expected):
    assert headings(body) == expected


@pytest.mark.parametrize(
    ("front", "expected"),
    [
        pytest.param("date: x\ndescription: 概要", "概要", id="plain"),
        pytest.param("description: 'abc'", "abc", id="single-quoted"),
        pytest.param('description: "abc"', "abc", id="double-quoted"),
        pytest.param(
            "date: 'x'\ndescription: 'Operating System\n\n  '\nother: 1",
            "Operating System",
            id="multiline-quoted",
        ),
        pytest.param("description: a\n  b\nnext: 1", "a b", id="continuation-lines"),
        pytest.param("date: x", "", id="missing"),
        pytest.param("description: https://example.com/", "https://example.com/", id="url"),
    ],
)
def test_parse_description(front, expected):
    assert parse_description(front) == expected


@pytest.mark.parametrize("title", ["About", "  TIPS ", "はじめに", "Getting Started"])
def test_generic_titles(title):
    assert is_generic(title)


@pytest.mark.parametrize("title", ["Unicode", "ライフサイクル"])
def test_meaningful_titles(title):
    assert not is_generic(title)


@pytest.mark.parametrize(
    "desc", ["https://example.com/", "http://example.com", "[x](https://example.com/)"]
)
def test_description_is_url(desc):
    assert description_is_url(desc)


@pytest.mark.parametrize(
    "desc", ["文章", "UEFI. https://uefi.org/", "Basic Input/Output System"]
)
def test_text_description_is_not_url(desc):
    assert not description_is_url(desc)


@pytest.mark.parametrize(
    ("page", "expected"),
    [
        pytest.param(Page(path="a.md", lines=100, h2=["Real"]), [], id="ordinary"),
        pytest.param(Page(path="a.md", lines=100, h2=["About"]), ["review"], id="only-generic-h2"),
        pytest.param(Page(path="a.md", lines=100), ["review"], id="no-h2"),
        pytest.param(Page(path="a.md", lines=15, h2=["Real"]), ["small"], id="small-boundary"),
        pytest.param(Page(path="a.md", lines=16, h2=["Real"]), [], id="just-over-small"),
        pytest.param(
            Page(path="a.md", lines=100, h2=["Real"], description="https://example.com"),
            ["url-desc"],
            id="url-description",
        ),
        pytest.param(
            Page(path="a.md", lines=3, description="https://example.com"),
            ["review", "small", "url-desc"],
            id="flags-are-ordered",
        ),
    ],
)
def test_make_flags(page, expected):
    assert make_flags(page) == expected


def test_parse_page_extracts_front_matter_and_headings():
    text = "---\ndate: x\ndescription: 概要\n---\n\n# 題名\n\n## 節1\n\n## 節2\n"
    page = parse_page("a.md", text)
    assert page.path == "a.md"
    assert page.description == "概要"
    assert page.h1 == "題名"
    assert page.h2 == ["節1", "節2"]
    assert page.lines == len(text.splitlines())


def test_parse_page_without_front_matter():
    page = parse_page("a.md", "# 題名\n\n## 節\n")
    assert page.description == ""
    assert page.h1 == "題名"


def test_parse_page_uses_only_first_h1():
    assert parse_page("a.md", "# 一つ目\n# 二つ目\n").h1 == "一つ目"


def test_parse_page_does_not_collect_h3():
    assert parse_page("a.md", "# A\n### 小節\n").h2 == []


def test_parse_page_ignores_headings_in_front_matter():
    text = "---\ndescription: x\n# not heading\n---\n# 題名\n"
    assert parse_page("a.md", text).h1 == "題名"


def test_read_page_ignores_code_block_comments(fixture_docs):
    page = read_page(fixture_docs, "cli/jq.md")
    assert page.h1 == "jq"
    assert page.h2 == ["Filters", "Options"]


def test_read_page_with_long_fence_containing_inner_fence(fixture_docs):
    assert read_page(fixture_docs, "software/git.md").h2 == ["branch", "commit", "tag"]


def test_read_page_with_multiline_description_and_no_h2(fixture_docs):
    page = read_page(fixture_docs, "os/index.md")
    assert page.description == "Operating System"
    assert page.h2 == []
    assert page.flags == ["review", "small"]


def test_read_page_with_url_description_and_generic_h2(fixture_docs):
    page = read_page(fixture_docs, "cli/index.md")
    assert page.description == "https://example.com/cli"
    assert page.h2 == ["About", "シェル"]
    assert page.flags == ["small", "url-desc"]  # 13行なので small にも当たる


def test_read_page_without_front_matter(fixture_docs):
    page = read_page(fixture_docs, "index.md")
    assert page.description == ""
    assert page.h2 == ["利用技術", "About"]

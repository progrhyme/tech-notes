import pytest
from revision_lib.frontmatter import format_line, replace_or_append, set_fields

FIELDS = {"revision_date": "2026-11-21", "git_creation_date_localized": "2026-01-02"}
NEW_LINES = "revision_date: '2026-11-21'\ngit_creation_date_localized: '2026-01-02'\n"


def test_creates_front_matter_when_missing():
    assert set_fields("# 題名\n\n本文\n", FIELDS) == f"---\n{NEW_LINES}---\n\n# 題名\n\n本文\n"


def test_appends_to_existing_front_matter():
    text = "---\ndate: '2020-01-01T00:00:00+09:00'\ndescription: https://example.com/\n---\n\n# 題名\n"
    assert set_fields(text, FIELDS) == (
        "---\ndate: '2020-01-01T00:00:00+09:00'\ndescription: https://example.com/\n"
        f"{NEW_LINES}---\n\n# 題名\n"
    )


def test_replaces_existing_values_in_place():
    text = (
        "---\nrevision_date: '2020-01-01'\ndate: x\n"
        "git_creation_date_localized: '2019-01-01'\n---\n本文\n"
    )
    assert set_fields(text, FIELDS) == (
        "---\nrevision_date: '2026-11-21'\ndate: x\n"
        "git_creation_date_localized: '2026-01-02'\n---\n本文\n"
    )


def test_replaces_multiline_value_with_its_continuation_lines():
    text = "---\nrevision_date: 'a\n\n  b'\ndate: x\n---\n本文\n"
    assert set_fields(text, {"revision_date": "2026-11-21"}) == (
        "---\nrevision_date: '2026-11-21'\ndate: x\n---\n本文\n"
    )


def test_empty_front_matter():
    assert set_fields("---\n---\n# 題名\n", FIELDS) == f"---\n{NEW_LINES}---\n# 題名\n"


def test_horizontal_rule_in_body_is_not_front_matter():
    text = "# 題名\n\n---\n\n本文\n"
    assert set_fields(text, FIELDS) == f"---\n{NEW_LINES}---\n\n# 題名\n\n---\n\n本文\n"


def test_only_the_first_front_matter_is_edited():
    text = "---\ndate: x\n---\n\n本文\n\n---\nrevision_date: keep\n---\n"
    result = set_fields(text, {"revision_date": "2026-11-21"})
    assert result.startswith("---\ndate: x\nrevision_date: '2026-11-21'\n---\n")
    assert result.endswith("---\nrevision_date: keep\n---\n")


def test_is_idempotent():
    once = set_fields("# 題名\n", FIELDS)
    assert set_fields(once, FIELDS) == once


def test_similar_key_names_are_not_replaced():
    text = "---\nrevision_date_note: keep\n---\n"
    assert set_fields(text, {"revision_date": "2026-11-21"}) == (
        "---\nrevision_date_note: keep\nrevision_date: '2026-11-21'\n---\n"
    )


def test_quote_in_value_is_escaped():
    assert format_line("k", "it's") == "k: 'it''s'"


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        pytest.param([], ["k: 'v'"], id="empty"),
        pytest.param(["a: 1"], ["a: 1", "k: 'v'"], id="append"),
        pytest.param(["k: 1", "a: 2"], ["k: 'v'", "a: 2"], id="replace"),
        pytest.param(["  k: 1"], ["  k: 1", "k: 'v'"], id="indented-key-is-not-top-level"),
    ],
)
def test_replace_or_append(lines, expected):
    assert replace_or_append(lines, "k", "k: 'v'") == expected


@pytest.mark.parametrize("char", ["\u2028", "\u2029", "\x85", "\x0c", "\x1c"])
def test_unicode_line_separators_in_existing_values_are_kept(char):
    text = f"---\ndescription: a{char}b\n---\n本文\n"
    assert set_fields(text, {"revision_date": "2026-11-21"}) == (
        f"---\ndescription: a{char}b\nrevision_date: '2026-11-21'\n---\n本文\n"
    )


def test_unclosed_front_matter_is_treated_as_body():
    text = "---\ndate: x\n\n# 題名\n"
    assert set_fields(text, FIELDS) == f"---\n{NEW_LINES}---\n\n---\ndate: x\n\n# 題名\n"


@pytest.mark.parametrize("value", ["a\nb", "a\rb"])
def test_value_with_line_break_is_rejected(value):
    with pytest.raises(ValueError):
        format_line("k", value)

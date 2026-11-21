from dataclasses import replace

import pytest
from docindex_lib.formatting import format_draft, format_h2, format_material, material_lines
from docindex_lib.pages import Page


@pytest.fixture
def page() -> Page:
    return Page(
        path="cli/jq.md",
        lines=20,
        description="jq の説明",
        h1="jq",
        h2=["Filters", "About"],
        flags=["url-desc"],
    )


def test_format_h2_joins_with_slash_and_marks_generic_headings(page):
    assert format_h2(page) == "Filters / (About)"


def test_format_h2_without_h2(page):
    assert format_h2(replace(page, h2=[])) == "(なし)"


def test_material_lines_with_all_fields(page):
    assert material_lines(page) == [
        "H1: jq",
        "H2: Filters / (About)",
        "description: jq の説明",
        "flags: url-desc",
    ]


def test_material_lines_omit_empty_description_and_flags(page):
    assert material_lines(replace(page, description="", flags=[])) == [
        "H1: jq",
        "H2: Filters / (About)",
    ]


def test_material_lines_with_multiple_flags(page):
    assert material_lines(replace(page, flags=["review", "small"]))[-1] == "flags: review, small"


def test_format_material_header_has_path_and_line_count(page):
    text = format_material(page)
    assert text.splitlines()[0] == "## cli/jq.md  (20行)"
    assert text.endswith("\n")


def test_format_draft_is_a_stub_line_and_indented_material(page):
    draft = format_draft(replace(page, description="", flags=[]))
    assert draft.splitlines() == ["`cli/jq.md` — TODO", "  H1: jq", "  H2: Filters / (About)"]

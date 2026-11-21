import pytest
from revision_lib import gitdates
from revision_lib.gitdates import FileDates, GitError, file_dates, is_shallow, is_work_tree, run_git


def test_dates_are_first_and_last_commit_dates(git_repo):
    git_repo.write("docs/a.md", "1\n")
    git_repo.commit("add", "2026-01-10")
    git_repo.write("docs/a.md", "2\n")
    git_repo.commit("modify", "2026-02-20")
    git_repo.write("docs/a.md", "3\n")
    git_repo.commit("modify again", "2026-03-30")
    assert file_dates(git_repo.path, "docs/a.md") == FileDates("2026-01-10", "2026-03-30")


def test_only_commits_touching_the_file_count(git_repo):
    git_repo.write("docs/a.md", "a\n")
    git_repo.commit("add a", "2026-01-10")
    git_repo.write("docs/b.md", "b\n")
    git_repo.commit("add b", "2026-05-01")
    assert file_dates(git_repo.path, "docs/a.md") == FileDates("2026-01-10", "2026-01-10")


def test_rename_is_followed(git_repo):
    git_repo.write("docs/old.md", "本文\n" * 20)
    git_repo.commit("add", "2026-01-01")
    git_repo.git("mv", "docs/old.md", "docs/new.md")
    git_repo.commit("rename", "2026-02-01")
    git_repo.write("docs/new.md", "本文\n" * 20 + "追記\n")
    git_repo.commit("modify", "2026-03-01")
    assert file_dates(git_repo.path, "docs/new.md") == FileDates("2026-01-01", "2026-03-01")


def test_author_date_is_used_in_its_own_timezone(git_repo):
    git_repo.write("docs/a.md", "1\n")
    # UTC では 2026-03-31 だが、author のタイムゾーン(+09:00)では 2026-04-01。
    git_repo.commit("just after midnight in JST", "2026-04-01T00:30:00+09:00")
    assert file_dates(git_repo.path, "docs/a.md") == FileDates("2026-04-01", "2026-04-01")


def test_untracked_file_has_no_dates(git_repo):
    git_repo.write("docs/a.md", "1\n")
    git_repo.commit("add", "2026-01-10")
    git_repo.write("docs/untracked.md", "x\n")
    assert file_dates(git_repo.path, "docs/untracked.md") is None


@pytest.mark.parametrize("name", ["a*.md", "b[1].md", "c?.md", "空 白.md", "日本語.md"])
def test_special_file_names_are_taken_literally(git_repo, name):
    git_repo.write(f"docs/{name}", "target\n")
    git_repo.commit("add target", "2026-01-10")
    for other in ("ab.md", "b1.md", "c1.md", "x.md"):
        git_repo.write(f"docs/{other}", "other\n")
    git_repo.commit("add others", "2026-06-01")
    assert file_dates(git_repo.path, f"docs/{name}") == FileDates("2026-01-10", "2026-01-10")


def test_is_work_tree(git_repo, tmp_path):
    assert is_work_tree(git_repo.path)
    assert not is_work_tree(tmp_path)


def test_is_work_tree_does_not_hide_other_git_failures(tmp_path, monkeypatch):
    def broken(repo, *args):
        raise GitError("fatal: detected dubious ownership in repository")

    monkeypatch.setattr(gitdates, "run_git", broken)
    with pytest.raises(GitError, match="dubious ownership"):
        is_work_tree(tmp_path)


def test_is_shallow(git_repo, tmp_path):
    git_repo.write("a.md", "1\n")
    git_repo.commit("first", "2026-01-01")
    git_repo.write("a.md", "2\n")
    git_repo.commit("second", "2026-01-02")
    clone = tmp_path / "shallow"
    git_repo.git("clone", "-q", "--depth", "1", f"file://{git_repo.path}", str(clone))
    assert not is_shallow(git_repo.path)
    assert is_shallow(clone)


def test_git_failure_raises(tmp_path):
    with pytest.raises(GitError):
        run_git(tmp_path, "log")

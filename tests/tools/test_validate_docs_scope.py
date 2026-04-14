from tools.validate_docs_scope import markdown_path_allowed, validate_paths


def test_allows_non_markdown_anywhere() -> None:
    assert markdown_path_allowed("src/app.py")
    assert markdown_path_allowed("random/path/image.png")


def test_allows_root_control_markdown() -> None:
    assert markdown_path_allowed("README.md")
    assert markdown_path_allowed("AGENTS.md")
    assert markdown_path_allowed("CLAUDE.md")
    assert markdown_path_allowed("CONTRIBUTING.md")


def test_disallows_unknown_root_markdown() -> None:
    assert not markdown_path_allowed("notes.md")


def test_allows_markdown_in_approved_prefixes() -> None:
    allowed_paths = [
        ".github/pull_request_template.md",
        "docs/index.md",
        "projects/main-submission/README.md",
        "projects/experiments/README.md",
        "assets/README.md",
        "tasks/todo.md",
    ]

    for path in allowed_paths:
        assert markdown_path_allowed(path), path


def test_disallows_markdown_outside_approved_prefixes() -> None:
    disallowed_paths = [
        "random/notes.md",
        "src/README.md",
        "misc/tips.md",
    ]

    for path in disallowed_paths:
        assert not markdown_path_allowed(path), path


def test_validate_paths_reports_invalid() -> None:
    valid, invalid = validate_paths([
        "docs/index.md",
        "projects/main-submission/src/main.py",
        "src/README.md",
    ])

    assert "docs/index.md" in valid
    assert "projects/main-submission/src/main.py" in valid
    assert "src/README.md" in invalid

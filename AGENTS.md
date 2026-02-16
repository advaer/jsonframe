# Repository Guidelines

## Project Overview

jsonframe is a lightweight Python library (Python 3.10+) for standardizing JSON API response envelopes. It provides three classes — `SuccessFrame`, `ErrorDetail`, `ErrorFrame` — each with a `.to_dict()` method. Built on Pydantic v2, no framework dependencies.

## Architecture

```
src/jsonframe/
├── __init__.py    # public exports: SuccessFrame, ErrorDetail, ErrorFrame
├── frames.py      # public API — three classes with .to_dict()
├── models.py      # internal Pydantic models (_SuccessModel, _ErrorDetailModel) — not exported
└── py.typed       # PEP 561 marker
tests/
└── test_frames.py # pytest unit tests
```

- Public classes are plain Python, not Pydantic models. They use composition with internal `_SuccessModel` and `_ErrorDetailModel` models (underscore-prefixed = private).
- `SuccessFrame[T]` is generic. Output always includes `"data"` key; `"meta"` only when provided.
- `ErrorDetail.to_dict()` returns a plain string when only `message` is set, or a structured dict when `code`/`meta` are provided.
- `ErrorFrame` wraps `ErrorDetail` under a `"detail"` key.

### Wire Format

Success: `{"data": ..., "meta": {...}}` — meta is optional
Error (simple): `{"detail": "message"}`
Error (structured): `{"detail": {"code": "...", "message": "...", "meta": {...}}}`

## Build, Test, and Development Commands

```bash
uv run pytest                                   # run all tests
uv run pytest tests/test_frames.py::test_name   # run a single test
```

- Package builds use the **uv** `uv_build` backend (see `pyproject.toml`).
- Version is maintained in both `pyproject.toml` and `__init__.py`.
- No linter or formatter is configured.

## Coding Style & Naming Conventions

- Python 3.10+ with explicit type hints (e.g., `dict[str, Any]`, `str | None`).
- 4-space indentation, double quotes, and straightforward class-based APIs.
- Internal helpers are underscore-prefixed (e.g., `_SuccessModel`); public classes are `PascalCase`.
- Keep changes consistent with existing style.

## Testing Guidelines

- Tests are written with pytest.
- Name test files `test_*.py` and use `test_*` functions.
- Focus on contract-level behavior (success frames, error frames, metadata).

## Commit & Pull Request Guidelines

- Commit history uses Conventional Commit-style prefixes (`refactor:`, `chore:`, etc.) with breaking markers like `refactor!:`. Follow that pattern.
- PRs should include a concise summary, rationale, and any relevant API behavior changes.
- Link related issues when applicable and include test output or notes for changes to public responses.

# Repository Guidelines

## Project Structure & Module Organization
- `src/jsonframe/` holds the library code (`builders.py`, `models.py`, and optional `fastapi.py`).
- `tests/` contains pytest tests (currently `tests/test_builders.py`).
- `dist/` is for build artifacts and should not be edited by hand.
- `pyproject.toml` defines dependencies, build backend, and project metadata.

## Build, Test, and Development Commands
- `uv sync --dev` installs locked dependencies, including dev tools like pytest.
- `uv run pytest` runs the full test suite.
- `uv build` builds the package into `dist/` for publishing.

## Coding Style & Naming Conventions
- Python code uses 4-space indentation and standard PEP 8 conventions.
- Use snake_case for functions/variables and `Test*`/`test_*` naming for tests.
- Public API functions are simple and explicit (e.g., `ok`, `ok_paged`, `error`).
- No formatter or linter is configured; keep changes consistent with existing code style.

## Testing Guidelines
- Framework: pytest.
- Test files follow `tests/test_*.py` naming; test functions start with `test_`.
- Add coverage for new behavior in `src/jsonframe/` and keep tests focused on JSON frame shapes and metadata.

## Commit & Pull Request Guidelines
- Commit messages follow Conventional Commits (e.g., `feat: add paged responses`).
- PRs should include a clear description, any relevant issue links, and test results.
- If you change public APIs, update `README.md` with usage examples.

## Architecture Overview
- The core API surface is in `src/jsonframe/__init__.py`, which re-exports key helpers.
- Response shapes are defined in `src/jsonframe/models.py`; builder helpers live in `src/jsonframe/builders.py`.
- Optional FastAPI integration is isolated in `src/jsonframe/fastapi.py` to avoid hard dependencies.

## Optional Dependencies
- FastAPI support is optional; install via `uv add "jsonframe[fastapi]"` when needed.
- Keep optional integrations isolated in `src/jsonframe/fastapi.py`.

## Release Notes
- Document user-facing changes in `README.md` when APIs or behavior change.
- Keep version bumps in `pyproject.toml` aligned with the change scope (patch/minor/major).
- Tag releases in Git and ensure `uv build` artifacts in `dist/` are generated only for publishing.

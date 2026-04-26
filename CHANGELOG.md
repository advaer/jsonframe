# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Public docstrings on `SuccessFrame`, `ErrorDetail`, and `ErrorFrame`.
- Edge-case tests: empty `meta={}` on `SuccessFrame` and `ErrorDetail`, meta/data key non-collision, `ErrorDetail` default return type, internal-model export boundary.
- Python 3.13 and 3.14 classifiers; `Topic :: Software Development :: Libraries`, `Topic :: Software Development :: Libraries :: Python Modules`, and `Operating System :: OS Independent`.
- Dev tooling: `ruff` (lint + format, line-length 100, rules `E F W I B UP SIM`) and `ty` (type checker), both configured under `[tool.ruff]` / `[tool.ty.src]` in `pyproject.toml`.

### Changed
- **Behavior:** `SuccessFrame(data=..., meta={})` now emits `"meta": {}` instead of silently dropping the key. Passing `meta=None` (the default) still omits it.
- Loosened `pydantic` dependency floor from `>=2.12.5` to `>=2.0`.
- Loosened `uv_build` build requirement from `>=0.9.18,<0.10.0` to `>=0.9,<0.12`.
- Adopted PEP 639 license metadata (`license = "MIT"` + `license-files`); removed deprecated `License :: OSI Approved :: MIT License` classifier.
- `__version__` is now read from package metadata via `importlib.metadata`, making `pyproject.toml` the single source of truth.

## [0.3.1] - 2026

### Changed
- Use Pydantic models for `ErrorDetail`; rename internal models with underscore prefix.

## [0.3.0] - 2026

### Added
- `ok()` and `error()` helper functions as shortcuts for `SuccessFrame(...).to_dict()` and `ErrorFrame(...).to_dict()`.

## [0.2.0] - 2026

### Changed
- **Breaking:** Replaced function-based API with class-based `SuccessFrame`, `ErrorDetail`, `ErrorFrame` (all expose `.to_dict()`).

## [0.1.2] - 2026

### Added
- FastAPI integration notes in README.

## [0.1.1] - 2026

### Changed
- Refactored response builders for clarity; renamed helpers.

## [0.1.0] - 2026

### Added
- Initial public API: response builders for success and error envelopes, with `ErrorFrame` model.
- Repository guidelines and FastAPI integration examples.

## [0.0.1] - 2026

### Added
- Initial project scaffolding: `pyproject.toml`, README, license, basic Frame class.

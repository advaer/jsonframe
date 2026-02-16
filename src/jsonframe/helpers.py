from __future__ import annotations

from typing import Any

from .frames import ErrorFrame, SuccessFrame


def ok(data: Any = None, *, meta: dict[str, Any] | None = None) -> dict[str, Any]:
    """Shortcut for SuccessFrame(data, meta=meta).to_dict()."""
    return SuccessFrame(data, meta=meta).to_dict()


def error(
    message: str = "",
    *,
    code: str | None = None,
    meta: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Shortcut for ErrorFrame(message=message, code=code, meta=meta).to_dict()."""
    return ErrorFrame(message=message, code=code, meta=meta).to_dict()

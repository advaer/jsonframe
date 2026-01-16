from __future__ import annotations

from typing import Any, TypeVar

from .models import ErrorFrame, ErrorInfo, Frame, PageMeta

T = TypeVar("T")


def ok(data: T | None = None, *, meta: dict[str, Any] | None = None) -> Frame[T]:
    return Frame[T](data=data, meta=meta)


def list_ok(items: list[T], *, meta: dict[str, Any] | None = None) -> Frame[list[T]]:
    return Frame[list[T]](data=items, meta=meta)


def paged(
    items: list[T],
    *,
    total: int,
    limit: int,
    offset: int,
    meta: dict[str, Any] | None = None,
) -> Frame[list[T]]:
    page = PageMeta(total=total, limit=limit, offset=offset).model_dump()
    merged_meta: dict[str, Any] = {**(meta or {}), "page": page}
    return Frame[list[T]](data=items, meta=merged_meta)


def fail(
    *,
    code: str,
    message: str,
    details: Any | None = None,
    meta: dict[str, Any] | None = None,
    trace_id: str | None = None,
) -> ErrorFrame:
    return ErrorFrame(
        error=ErrorInfo(code=code, message=message, details=details, trace_id=trace_id),
        meta=meta,
    )

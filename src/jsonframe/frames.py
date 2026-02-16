from __future__ import annotations

from typing import Any, Generic, TypeVar

from .models import _Frame

T = TypeVar("T")


class ErrorDetail:
    def __init__(
        self,
        *,
        message: str = "",
        code: str | None = None,
        meta: dict[str, Any] | None = None,
    ) -> None:
        self._message = message
        self._code = code
        self._meta = meta

    def to_dict(self) -> str | dict[str, Any]:
        if self._code is None and self._meta is None:
            return self._message
        result: dict[str, Any] = {"code": self._code, "message": self._message}
        if self._meta is not None:
            result["meta"] = self._meta
        return result


class ErrorFrame:
    def __init__(
        self,
        *,
        message: str = "",
        code: str | None = None,
        meta: dict[str, Any] | None = None,
    ) -> None:
        self._detail = ErrorDetail(message=message, code=code, meta=meta)

    def to_dict(self) -> dict[str, Any]:
        return {"detail": self._detail.to_dict()}


class SuccessFrame(Generic[T]):
    def __init__(
        self,
        data: T | None = None,
        *,
        meta: dict[str, Any] | None = None,
    ) -> None:
        self._frame = _Frame(data=data, meta=meta or None)

    def to_dict(self) -> dict[str, Any]:
        payload = self._frame.model_dump(exclude_none=True)
        if "data" not in payload:
            payload["data"] = None
        return payload

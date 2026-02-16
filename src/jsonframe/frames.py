from __future__ import annotations

from typing import Any, Generic, TypeVar

from .models import _ErrorDetailModel, _SuccessModel

T = TypeVar("T")


class ErrorDetail:
    def __init__(
        self,
        *,
        message: str = "",
        code: str | None = None,
        meta: dict[str, Any] | None = None,
    ) -> None:
        self._model = _ErrorDetailModel(message=message, code=code, meta=meta)

    def to_dict(self) -> str | dict[str, Any]:
        if self._model.code is None and self._model.meta is None:
            return self._model.message
        payload = self._model.model_dump()
        if self._model.meta is None:
            payload.pop("meta")
        return payload


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
        self._frame = _SuccessModel(data=data, meta=meta or None)

    def to_dict(self) -> dict[str, Any]:
        payload = self._frame.model_dump(exclude_none=True)
        if "data" not in payload:
            payload["data"] = None
        return payload

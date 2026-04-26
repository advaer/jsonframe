from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class _SuccessModel(BaseModel, Generic[T]):
    data: T | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)


class _ErrorDetailModel(BaseModel):
    code: str | None = Field(default=None)
    message: str = Field(default="")
    meta: dict[str, Any] | None = Field(default=None)

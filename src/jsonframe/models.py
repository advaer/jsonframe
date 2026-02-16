from __future__ import annotations

from typing import Any, Generic, TypeVar
from pydantic import BaseModel, Field

T = TypeVar("T")


class _Frame(BaseModel, Generic[T]):
    data: T | None = Field(default=None)
    meta: dict[str, Any] | None = Field(default=None)


class _PageMeta(BaseModel):
    total: int
    limit: int
    offset: int

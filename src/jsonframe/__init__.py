from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Generic, Mapping, Optional, TypeVar

__all__ = ["Frame", "__version__"]

__version__ = "0.0.1"

T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class Frame(Generic[T]):
    """
    A small, typed JSON "frame" that separates metadata from payload.

    This is intentionally minimal in 0.0.x:
    - `data` holds your payload
    - `meta` holds transport/protocol-level metadata (trace ids, pagination, etc.)
    - `error` is a structured error object (optional)
    """

    data: T
    meta: Mapping[str, Any] = field(default_factory=dict)
    error: Optional[Mapping[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "data": self.data,
            "meta": dict(self.meta),
            "error": None if self.error is None else dict(self.error),
        }

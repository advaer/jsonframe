from __future__ import annotations

from typing import Any

from fastapi import HTTPException
from fastapi.responses import JSONResponse

from .builders import fail
from .models import ErrorFrame, Frame


def json(
    frame: Frame[Any] | ErrorFrame,
    *,
    status_code: int = 200,
    headers: dict[str, str] | None = None,
) -> JSONResponse:
    """
    Returns a FastAPI JSONResponse with consistent framing and status_code control.
    """
    return JSONResponse(
        status_code=status_code,
        content=frame.model_dump(exclude_none=True),
        headers=headers,
    )


def http_error(
    status_code: int,
    *,
    code: str,
    message: str,
    details: Any | None = None,
    meta: dict[str, Any] | None = None,
    trace_id: str | None = None,
) -> HTTPException:
    """
    Raises HTTPException where `detail` is a framed error payload.
    """
    payload = fail(code=code, message=message, details=details, meta=meta, trace_id=trace_id)
    return HTTPException(status_code=status_code, detail=payload.model_dump(exclude_none=True))

import pytest

fastapi = pytest.importorskip("fastapi")

from jsonframe.fastapi import http_error


def test_http_error_detail_shape():
    exc = http_error(404, code="not_found", message="Missing")
    assert isinstance(exc, fastapi.HTTPException)
    assert exc.detail == {
        "error": {
            "code": "not_found",
            "message": "Missing",
        },
    }

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


def test_http_error_detail_string():
    exc = http_error(400, message="Bad request")
    assert isinstance(exc, fastapi.HTTPException)
    assert exc.detail == "Bad request"


def test_http_error_detail_with_context_and_meta():
    exc = http_error(
        422,
        code="invalid",
        message="Validation failed",
        context={"field": "name"},
        meta={"request_id": "req_123"},
    )
    assert isinstance(exc, fastapi.HTTPException)
    assert exc.detail == {
        "error": {
            "code": "invalid",
            "message": "Validation failed",
            "context": {"field": "name"},
        },
        "meta": {"request_id": "req_123"},
    }

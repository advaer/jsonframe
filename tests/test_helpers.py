from jsonframe.helpers import error, ok, ok_paged


def test_ok_includes_data_key_when_none():
    payload = ok()
    assert payload == {"data": None}


def test_ok_preserves_meta_and_sets_data():
    payload = ok(meta={"request_id": "req_123"})
    assert payload == {"data": None, "meta": {"request_id": "req_123"}}


def test_ok_paged_merges_meta_with_page():
    payload = ok_paged(
        data=[{"id": 1}],
        total=10,
        limit=5,
        offset=0,
        meta={"request_id": "req_123"},
    )
    assert payload["data"] == [{"id": 1}]
    assert payload["meta"]["request_id"] == "req_123"
    assert payload["meta"]["page"] == {"total": 10, "limit": 5, "offset": 0}


def test_error_simple_detail():
    payload = error(message="missing")
    assert payload == {"detail": "missing"}


def test_error_structured_detail_omits_empty_fields():
    payload = error(message="missing", code="not_found")
    assert payload == {"detail": {"error": {"code": "not_found", "message": "missing"}}}


def test_error_structured_detail_with_context_and_meta():
    payload = error(
        message="missing",
        code="not_found",
        context={"user_id": 1},
        meta={"request_id": "req_123"},
    )
    assert payload == {
        "detail": {
            "error": {
                "code": "not_found",
                "message": "missing",
                "context": {"user_id": 1},
            },
            "meta": {"request_id": "req_123"},
        }
    }

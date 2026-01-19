from jsonframe.builders import build_error, build_ok, build_ok_paged


def test_ok_defaults():
    frame = build_ok()
    assert frame.data is None
    assert frame.meta is None


def test_list_ok_payload():
    frame = build_ok([{"id": 1}, {"id": 2}])
    assert frame.data == [{"id": 1}, {"id": 2}]


def test_paged_meta_shape():
    frame = build_ok_paged(data=[{"id": 1}], total=10, limit=5, offset=0)
    assert frame.meta["page"]["total"] == 10
    assert frame.meta["page"]["limit"] == 5
    assert frame.meta["page"]["offset"] == 0


def test_fail_payload_string():
    frame = build_error(message="missing")
    assert frame.detail == "missing"


def test_fail_payload_object():
    frame = build_error(
        code="not_found",
        message="missing",
        context={"user_id": 1},
        meta={"request_id": "req_123"},
    )
    detail = frame.detail
    assert detail.error.code == "not_found"
    assert detail.error.message == "missing"
    assert detail.error.context == {"user_id": 1}
    assert detail.meta == {"request_id": "req_123"}


def test_error_meta_omitted_when_none():
    frame = build_error(code="not_found", message="missing")
    detail = frame.detail
    assert detail.meta is None

from jsonframe import error, ok, ok_paged


def test_ok_defaults():
    frame = ok()
    assert frame.data is None
    assert frame.meta is None


def test_list_ok_payload():
    frame = ok([{"id": 1}, {"id": 2}])
    assert frame.data == [{"id": 1}, {"id": 2}]


def test_paged_meta_shape():
    frame = ok_paged(data=[{"id": 1}], total=10, limit=5, offset=0)
    assert frame.meta["page"]["total"] == 10
    assert frame.meta["page"]["limit"] == 5
    assert frame.meta["page"]["offset"] == 0


def test_fail_payload():
    frame = error(code="not_found", message="missing")
    assert frame.error.code == "not_found"
    assert frame.error.message == "missing"
    assert frame.meta is None

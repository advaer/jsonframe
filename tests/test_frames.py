from jsonframe import SuccessFrame, ErrorDetail, ErrorFrame


# --- SuccessFrame ---

def test_success_default():
    assert SuccessFrame().to_dict() == {"data": None}


def test_success_dict_data():
    assert SuccessFrame(data={"id": 1}).to_dict() == {"data": {"id": 1}}


def test_success_scalar_data():
    assert SuccessFrame(data="scalar").to_dict() == {"data": "scalar"}


def test_success_list_data():
    assert SuccessFrame(data=[1, 2]).to_dict() == {"data": [1, 2]}


def test_success_with_meta():
    result = SuccessFrame(data="x", meta={"k": "v"}).to_dict()
    assert result == {"data": "x", "meta": {"k": "v"}}


def test_success_no_meta_key_when_none():
    result = SuccessFrame(data="x").to_dict()
    assert "meta" not in result


def test_success_pagination_via_meta():
    page = {"total": 10, "limit": 5, "offset": 0}
    result = SuccessFrame(data=[1, 2, 3], meta={"page": page}).to_dict()
    assert result == {"data": [1, 2, 3], "meta": {"page": page}}


# --- ErrorDetail ---

def test_error_detail_simple():
    assert ErrorDetail(message="msg").to_dict() == "msg"


def test_error_detail_default_message():
    assert ErrorDetail().to_dict() == ""


def test_error_detail_with_code():
    assert ErrorDetail(message="msg", code="x").to_dict() == {"code": "x", "message": "msg"}


def test_error_detail_with_meta_no_code():
    result = ErrorDetail(message="msg", meta={"k": "v"}).to_dict()
    assert result == {"code": None, "message": "msg", "meta": {"k": "v"}}


def test_error_detail_with_code_and_meta():
    result = ErrorDetail(message="msg", code="x", meta={"k": "v"}).to_dict()
    assert result == {"code": "x", "message": "msg", "meta": {"k": "v"}}


def test_error_detail_no_context_key():
    result = ErrorDetail(message="msg", code="x", meta={"k": "v"}).to_dict()
    assert "context" not in result


def test_error_detail_no_error_nesting():
    result = ErrorDetail(message="msg", code="x").to_dict()
    assert "error" not in result


# --- ErrorFrame ---

def test_error_frame_simple():
    assert ErrorFrame(message="msg").to_dict() == {"detail": "msg"}


def test_error_frame_structured():
    result = ErrorFrame(message="msg", code="x").to_dict()
    assert result == {"detail": {"code": "x", "message": "msg"}}


def test_error_frame_with_meta():
    result = ErrorFrame(message="msg", code="x", meta={"k": "v"}).to_dict()
    assert result == {"detail": {"code": "x", "message": "msg", "meta": {"k": "v"}}}


def test_error_frame_single_key():
    result = ErrorFrame(message="msg", code="x", meta={"k": "v"}).to_dict()
    assert list(result.keys()) == ["detail"]

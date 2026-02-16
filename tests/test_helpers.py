from jsonframe import ok, error, SuccessFrame, ErrorFrame


# --- ok() ---

def test_ok_default():
    assert ok() == SuccessFrame().to_dict()


def test_ok_with_data():
    assert ok(data={"id": 1}) == SuccessFrame(data={"id": 1}).to_dict()


def test_ok_with_data_and_meta():
    assert ok(data=[1, 2], meta={"total": 2}) == SuccessFrame(data=[1, 2], meta={"total": 2}).to_dict()


# --- error() ---

def test_error_default():
    assert error() == ErrorFrame().to_dict()


def test_error_simple_message():
    assert error(message="not found") == ErrorFrame(message="not found").to_dict()


def test_error_with_code():
    assert error(message="fail", code="E01") == ErrorFrame(message="fail", code="E01").to_dict()


def test_error_with_code_and_meta():
    assert error(message="fail", code="E01", meta={"field": "x"}) == ErrorFrame(message="fail", code="E01", meta={"field": "x"}).to_dict()

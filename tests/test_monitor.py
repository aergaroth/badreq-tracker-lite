from app.monitor import analyze_request


def test_benign_request_is_not_flagged():
    event = analyze_request(
        ip="127.0.0.1",
        path="/search",
        payload="hello world"
    )

    assert event is None


def test_xss_payload_is_detected():
    event = analyze_request(
        ip="127.0.0.1",
        path="/search",
        payload="<script>alert(1)</script>"
    )

    assert event is not None
    assert event["type"] == "suspicious_input"
    assert event["pattern"] == "<script"


def test_sqli_payload_is_detected():
    event = analyze_request(
        ip="127.0.0.1",
        path="/login",
        payload="admin or 1=1"
    )

    assert event is not None
    assert event["pattern"] == "or 1=1"

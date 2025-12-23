from datetime import datetime, UTC
from prometheus_client import Counter

SUSPICIOUS_PATTERNS = [
    "select",
    "union",
    "<script",
    "../",
    "or 1=1",
]

REQUESTS_TOTAL = Counter(
    "badreq_requests_total",
    "Total number of HTTP requests received"
)

SUSPICIOUS_REQUESTS_TOTAL = Counter(
    "badreq_suspicious_requests_total",
    "Total number of suspicious HTTP requests detected"
)

SUSPICIOUS_BY_PATTERN = Counter(
    "badreq_suspicious_requests_by_pattern",
    "Suspicious requests by detected pattern",
    ["pattern"]
)


def analyze_request(ip: str, path: str, payload: str | None):
    REQUESTS_TOTAL.inc()
    if not payload:
        return None

    payload_lower = payload.lower()

    for pattern in SUSPICIOUS_PATTERNS:
        if pattern in payload_lower:
            return {
                "timestamp": datetime.now(UTC).isoformat(),
                "ip": ip,
                "path": path,
                "payload": payload,
                "type": "suspicious_input",
                "pattern": pattern,
            }
    SUSPICIOUS_REQUESTS_TOTAL.inc()
    SUSPICIOUS_BY_PATTERN.labels(pattern=pattern).inc()

    return None

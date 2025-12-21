# app/monitor.py
from datetime import datetime

SUSPICIOUS_PATTERNS = [
    "select",
    "union",
    "<script",
    "../",
    "or 1=1",
]

def analyze_request(ip: str, path: str, payload: str | None):
    if not payload:
        return None

    payload_lower = payload.lower()

    for pattern in SUSPICIOUS_PATTERNS:
        if pattern in payload_lower:
            return {
                "timestamp": datetime.utcnow().isoformat(),
                "ip": ip,
                "path": path,
                "payload": payload,
                "type": "suspicious_input",
                "pattern": pattern,
            }

    return None

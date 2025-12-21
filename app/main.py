# app/main.py
from flask import Flask, request, jsonify
import json
from app.monitor import analyze_request

app = Flask(__name__)

LOG_FILE = "events.json"


def log_event(event: dict):
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(event) + "\n")


@app.route("/login", methods=["POST"])
def login():
    data = request.json or {}
    payload = f"{data.get('username')}:{data.get('password')}"

    event = analyze_request(
        ip=request.remote_addr,
        path=request.path,
        payload=payload,
    )

    if event:
        log_event(event)

    return jsonify({"status": "ok"}), 200


@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q", "")

    event = analyze_request(
        ip=request.remote_addr,
        path=request.path,
        payload=query,
    )

    if event:
        log_event(event)

    return jsonify({"query": query}), 200


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

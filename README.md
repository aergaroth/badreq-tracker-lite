# BadReq Tracker Lite

BadReq Tracker Lite – lightweight DevSecOps application that detects and logs suspicious HTTP requests (SQLi, XSS, brute-force patterns) in runtime.

The project is designed as an **educational and portfolio-ready example** of:
- runtime request inspection,
- basic attack pattern detection,
- containerized application delivery,
- DevSecOps hygiene (non-root containers, clean repo, CI-ready).

> This is **not** a WAF or SIEM replacement. 
> The goal is clarity, simplicity, and showcasing good engineering practices.

---

## Features

- Detects suspicious request payloads (SQLi, XSS, path traversal patterns)
- Logs detected events in structured JSON format
- Simple REST API (Flask)
- Dockerized application running as a **non-root user**
- Clean separation between runtime artifacts and source code

---

## Tech Stack

- **Python 3**
- **Flask**
- **Docker**
- JSON-based event logging (runtime)
- CI/CD ready (tests and security scans planned)

---

## Project Structure

```text
.
├── app/
│   ├── main.py          # Flask application
│   ├── monitor.py       # Request analysis and detection logic
│   └── __init__.py
├── tests/
│   └── test_monitor.py
├── Dockerfile
├── requirements.txt
├── .gitignore
├── .dockerignore
└── README.md
```
---

## Running Locally

### Requirements

- Python 3.10+
- pip

```bash
pip install -r requirements.txt
python -m app.main
```

## Application will be available at:
```
http://localhost:5000
```
---

## Running with Docker

Build image:

```bash
docker run -p 5000:5000 badreq-tracker-lite
```
Run container

```bash
docker run -p 5000:5000 badreq-tracker-lite
```

---

## Example Requests
```
curl "http://localhost:5000/search?q=<script>alert(1)</script>"
```
### Suspicious login attempt
```
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin or 1=1"}'
```
Detected events are logged to a runtime-generated events.json file
(which is intentionally excluded from version control).

---

## Security Notes

- Application runs as a non-root user inside the container

- Runtime logs and artifacts are excluded via .gitignore and .dockerignore

- No secrets or credentials are stored in the repository

---

## Roadmap

Planned improvements:

- Unit tests for detection logic (pytest)

- CI pipeline (GitHub Actions)

- Static security analysis (Bandit)

- Metrics and monitoring (Prometheus)

- Alerting (Slack / webhook)

## License
This project is licensed under the GNU General Public License v3.0.

## Author
Sebastian Grochowski

Created as a DevSecOps portfolio project.


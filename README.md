# BadReq Tracker Lite

[![CI](https://github.com/aergaroth/badreq-tracker-lite/actions/workflows/ci.yml/badge.svg)](https://github.com/aergaroth/badreq-tracker-lite/actions/workflows/ci.yml)


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

- Runtime detection of suspicious HTTP requests (SQLi, XSS, traversal)
- Security event logging and Prometheus metrics
- REST API (Flask) with containerized, non-root execution
- Automated CI with testing and SAST (Bandit)

---

## Tech Stack

- **Python 3**
- **Flask**
- **Docker**
- JSON-based event logging (runtime)
- CI/CD ready (tests and security scans)

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
├── .github/
│   └── workflows/
│       └── ci.yml
├── Dockerfile
├── requirements.txt
├── .gitignore
├── .dockerignore
├── LICENSE
└── README.md

```
---

## Local Development

### Requirements

#### Runtime

- Python **3.10+**
- pip

#### Development / CI

- pytest (unit tests)
- bandit (statioc security analysis)

> Development tools are used locally and in CI pipelines.
> They are not required to run the application in production.

### Instalation
```bash
pip install -r requirements.txt
```
### Run
``` bash
python -m app.main
```
---
 
## Application will be available at:
```
http://localhost:5000
```
---

## Running with Docker

Build image:

```bash
docker build -t badreq-tracker-lite .
```
Run container:

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

## Metrics & Monitoring

The application exposes Prometheus-compatible metrics at:

```bash
/metrics
```

### Custom security metrics
- `badreq_requests_total` – total number of HTTP requests
- `badreq_suspicious_requests_total` – total number of detected suspicious requests
- `badreq_suspicious_requests_by_pattern` – breakdown of suspicious requests by detected pattern

Default Python and process metrics are also exposed to provide runtime context.

---

## Roadmap

### Implemented
- Runtime detection of suspicious HTTP requests (SQLi, XSS, brute-force patterns)
- Unit tests for detection logic (pytest)
- CI pipeline with security scanning (GitHub Actions + Bandit)
- Prometheus-compatible metrics for security observability
- Dockerized application running as a non-root user

### Next steps
- Prometheus integration via docker-compose
- Basic security alerting based on metrics (threshold-based)
- Configuration separation for development and production environments

### Possible extensions
- Grafana dashboards for security metrics
- GeoIP enrichment for detected requests
- Infrastructure-as-Code deployment (Terraform)

---

## License
This project is licensed under the GNU General Public License v3.0.

## Author
Sebastian Grochowski

*Created as a portfolio project.*


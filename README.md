# BadReq Tracker Lite

[![CI](https://github.com/aergaroth/badreq-tracker-lite/actions/workflows/ci.yml/badge.svg)](https://github.com/aergaroth/badreq-tracker-lite/actions/workflows/ci.yml)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Prometheus](https://img.shields.io/badge/metrics-Prometheus-orange)
![SAST](https://img.shields.io/badge/SAST-Bandit-yellow)

**BadReq Tracker Lite** – lightweight DevSecOps application that detects and logs suspicious HTTP requests (SQLi, XSS, brute-force patterns) in runtime.

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
- Structured security event logging in JSON format
- Prometheus-compatible metrics for security observability
- REST API built with Flask
- Containerized application running as a **non-root user**
- Automated CI pipeline with testing and static security analysis (Bandit)


## Production Use Cases

BadReq Tracker Lite is designed as a **lightweight security observability component** rather than a full-scale security platform.

It can be realistically used in production environments as:

- An **early-warning signal** for suspicious traffic patterns before introducing a full WAF or SIEM
- A **security telemetry sidecar** for internal services and APIs
- A **signal source** for alerting and dashboards based on Prometheus metrics
- A **development and staging environment guardrail**, providing visibility into malformed or malicious requests
- A **learning and validation tool** for DevSecOps and SRE teams to understand real traffic patterns

The application intentionally focuses on **detection and visibility**, leaving enforcement decisions to
upstream systems such as reverse proxies, API gateways, or WAFs.

> In production, BadReq Tracker Lite would typically run behind a reverse proxy  
> and feed metrics into a centralized monitoring or alerting system.

## Why It Matters

In many real-world environments, full security platforms are introduced too late
or without sufficient visibility into actual traffic.

BadReq Tracker Lite provides **immediate insight** with minimal operational overhead,
making it a practical first step toward more advanced security controls.

---

## Tech Stack

- **Python 3**
- **Flask**
- **Docker**
- JSON-based event logging (runtime)
- CI/CD ready (tests and security scans)
- Prometheus (metrics & monitoring)

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
├── monitoring/
│   ├── alertmanager.yml
│   ├── prometheus.yml
│   └── rules
│       └── alerts.yml
├── docker-compose.yml
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
- bandit (static security analysis)

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
Application will be available at:
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

## Running with Docker Compose (Observability Stack)

Docker Compose is used to run the application together with Prometheus
for metrics scraping and security observability.

### Requirements

Docker

Docker Compose (v2) (Docker CLI plugin)

### Run
```bash
docker compose up --build
```

This will start:

- Application: ``` http://localhost:5000```

- Prometheus UI: ``` http://localhost:9090```

- Alertmanager UI: ``` http://localhost:9093```

---

## Example Requests

Suspicious search request:
```
curl "http://localhost:5000/search?q=<script>alert(1)</script>"
```
Suspicious login attempt:
```
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin or 1=1"}'
```
Detected events are logged to a runtime-generated  ``` events.json``` file
(which is intentionally excluded from version control).

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

## Alerting Notes

Alerting is implemented using **Prometheus rules and Alertmanager**.

Slack notifications are demonstrated using **Incoming Webhooks**.
No secrets or webhook URLs are stored in the repository.

>In production environments, legacy webhooks should be replaced by a Slack App,
>a dedicated webhook receiver, or an incident management system.

---

## Security Notes

- Application runs as a **non-root user** inside the container

- Runtime logs and artifacts are excluded via ```.gitignore``` and ```.dockerignore```

- No secrets or credentials are stored in the repository

---

## Roadmap

### Implemented
- Runtime detection of suspicious HTTP requests (SQLi, XSS, brute-force patterns)
- Unit tests for detection logic (pytest)
- CI pipeline with automated testing and SAST (GitHub Actions + Bandit)
- Prometheus-compatible metrics and monitoring via Docker Compose
- Metric-based security alerting
- Non-root containerized deployment


### Possible extensions
- Grafana dashboards for security metrics
- GeoIP enrichment for detected requests
- Kubernetes deployment
- Infrastructure-as-Code deployment (Terraform)

---

## License
This project is licensed under the GNU General Public License v3.0.

## Author
Sebastian Grochowski

*Created as a portfolio project.*


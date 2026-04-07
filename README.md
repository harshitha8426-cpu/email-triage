# OpenEnv: Email Triage & Routing

A complete, real-world OpenEnv simulation for an enterprise email inbox management task. The environment is accessible via a FastAPI server, providing standard `reset`, `step`, and `state` endpoints.

## Motivation
Email triage is a classic real-world task where humans spend hours reading policies and deciding whether to archive, forward to correct departments, or write boilerplate replies. This environment provides continuous partial rewards to train agents to intelligently follow these policies.

## Interface Specifications

### Observation Space
- `current_email`: Contains `id`, `sender`, `subject`, and `body` strings. Returns `null` if the episode is done.
- `inbox_count`: Integer representing how many emails are left.
- `policy_snippets`: String providing the context / company policy for handling emails.

### Action Space
Agents must provide actions mapping to:
- `action_type`: `"archive"`, `"forward"`, or `"reply"`
- `target_email`: Address string (required if `action_type` is `"forward"`)
- `draft_body`: Response text (required if `action_type` is `"reply"`)

### Tasks
Detailed in `openenv.yaml`. Range from `easy` (simple spam and unambiguous forwards) to `hard` (complex routing, phishing, and vendor replies).

## Setup Instructions

### 1. Running Locally (Docker)
Build and run the containerized API. It will be available on `http://localhost:8000`.

```bash
docker build -t openenv-email-triage .
docker run -p 8000:8000 openenv-email-triage
```

### 2. Without Docker (Python)
```bash
pip install -r requirements.txt
uvicorn server:app --host 0.0.0.0 --port 8000
```

### 3. Running Baseline
Runs a zero-shot LLM (requires `OPENAI_API_KEY`) against the three tasks.
```bash

python baseline.py
```

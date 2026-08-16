# TinySIEM

TinySIEM is a small, local detection engine for learning how telemetry becomes an alert. It is a teaching project, not a production SIEM.

See the [project plan](docs/project_plan.md) for the mission, milestones, and explicit non-goals.

## Development

Requires Python 3.12 or newer.

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e '.[test]'
pytest
tinysiem --help
```

Changes are developed through pull requests. GitHub Actions runs the test suite, and its test check must pass before merging to `main`.

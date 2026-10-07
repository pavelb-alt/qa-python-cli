# Agent notes

- This repo is a pure Python CLI (`qa-cli`, stdlib only: argparse). No web server, no DB, no secrets.
- `docker-compose.base44.yml` installs it editable (`pip install -e .`) and serves a preview harness on
  port 3000 defined inline in the compose file (not app code). `/?args=greet --name Pavel` runs
  `qa-cli greet --name Pavel` in a subprocess; source edits apply on the next request, no restart needed.
- Changes to `pyproject.toml` (e.g. new entry points) need `docker compose -f docker-compose.base44.yml restart cli`.
- Quick check: `docker compose -f docker-compose.base44.yml exec -T cli qa-cli greet --name Pavel` → `Hello, Pavel!`.
- No test suite exists.

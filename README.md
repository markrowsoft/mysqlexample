# MySQL Python example

Minimal demo: start Percona in Docker, create a table, insert a row from Python, and print it.

## Prerequisites

- [uv](https://docs.astral.sh/uv/) (Python package manager)
- Docker Desktop
- Python 3.10+
- MySQL client (`mysql` CLI) for schema setup

## Quick start

1. Start the database:
   ```bash
   docker compose up -d
   ```
2. Wait ~10 seconds, then create the schema:
   ```bash
   mysql -u root -proot -h 127.0.0.1 < create_sql.sql
   ```
3. Install dependencies (latest compatible versions; no version pins):
   ```bash
   uv sync --group dev
   ```
4. Run the demo (prompts for name, phone, SSN):
   ```bash
   uv run python saveShow.py
   ```
5. Stop the database:
   ```bash
   docker compose down
   ```

Or run everything with `./run.sh` (starts the stack, installs deps, runs the script, tears down).

Connection defaults are `root` / `root` on `127.0.0.1` / `myusers`. Override with `MYSQL_HOST`, `MYSQL_USER`, `MYSQL_PASSWORD`, and `MYSQL_DATABASE`.

## Tests and dependency resolution

Dependencies are **not version-pinned**. Installs use whatever `uv` resolves as current. That keeps you on newer releases and reduces stale CVE noise from locked pins.

**You must run the unit tests after install** (and after any dependency change):

```bash
uv sync --group dev
uv run pytest -v
```

If installs or tests fail because of a bad or incompatible resolution:

1. Upgrade tools: `uv self update`
2. Clear and re-resolve: `rm -rf .venv && uv sync --group dev`
3. If a package breaks the build, temporarily constrain it in `pyproject.toml`, re-run tests, and prefer the newest working release.
4. Re-run `uv run pytest -v` until green before using the demo.

## Note

Local demo only. Default DB password is `root`. Do not use for real PII.

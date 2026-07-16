# MySQL Python example

Minimal demo: start Percona in Docker, create a table, insert a row from Python, and print it.

## Prerequisites

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
3. Install dependencies:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
4. Run the demo (prompts for name, phone, SSN):
   ```bash
   python saveShow.py
   ```
5. Stop the database:
   ```bash
   docker compose down
   ```

Or run everything with `./run.sh` (starts the stack, installs deps, runs the script, tears down).

Connection defaults are `root` / `root` on `127.0.0.1` / `myusers`. Override with `MYSQL_HOST`, `MYSQL_USER`, `MYSQL_PASSWORD`, and `MYSQL_DATABASE`.

## Tests

```bash
source .venv/bin/activate
pytest -v
```

## Note

Local demo only. Default DB password is `root`. Do not use for real PII.

#!/bin/bash
set -euo pipefail

# Start DB, create schema, install deps with uv, run the demo, tear down.

if ! command -v uv >/dev/null 2>&1; then
  echo "uv is required. Install: https://docs.astral.sh/uv/getting-started/installation/" >&2
  exit 1
fi

if docker compose version >/dev/null 2>&1; then
  COMPOSE="docker compose"
else
  COMPOSE="docker-compose"
fi

$COMPOSE up -d
echo "waiting 10 seconds for docker"
sleep 10

./create_table.sh

uv sync --group dev
uv run python saveShow.py

sleep 5
$COMPOSE down

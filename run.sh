#!/bin/bash
set -euo pipefail

# Start DB, create schema, install deps, run the demo, tear down.

if docker compose version >/dev/null 2>&1; then
  COMPOSE="docker compose"
else
  COMPOSE="docker-compose"
fi

$COMPOSE up -d
echo "waiting 10 seconds for docker"
sleep 10

./create_table.sh

python3 -m venv .venv
# shellcheck disable=SC1091
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

python3 saveShow.py

sleep 5
$COMPOSE down

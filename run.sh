#!/bin/bash
docker-compose up -d
echo "waiting 30 seconds for docker"
sleep 30
source create_table.sh
python -m venv .venv
python -m pip install pip --upgrade
python -m pip install -r requirements.txt
. ./.venv/bin/activate
python saveShow.py

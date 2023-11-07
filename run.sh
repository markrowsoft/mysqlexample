#!/bin/bash
docker-compose up -d
echo "waiting 30 seconds for docker"
sleep 30
source create_table.sh
python3 -m venv .venv
python3 -m pip install pip --upgrade
python3 -m pip install -r requirements.txt
. ./.venv/bin/activate
python3 saveShow.py

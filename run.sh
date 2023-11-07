#!/bin/bash
docker-compose up -d
sleep 200
source create_table.sh
. ./.venv/bin/activate
python saveShow.py

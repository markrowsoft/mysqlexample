#!/bin/bash
docker-compose up -d
echo "waiting 10 seconds for docker"
sleep 10
source create_table.sh
python3 -m venv .venv
python3 -m pip install pip --upgrade
python3 -m pip install -r requirements.txt
. ./.venv/bin/activate
python3 -m pip install pip --upgrade
python3 -m pip install mysql-connector-python
pip freeze > requirements.txt
python3 saveShow.py
sleep 5
# rm -rf ./.venv
docker-compose down

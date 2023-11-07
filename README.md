# mysqlexample on MacOS mysql insert and select basic example
- install docker desktop: https://www.docker.com/products/docker-desktop/
- install python3
- install mysql 8 client
- run sql create script
- run `python3 -m pip install -r requirements.txt`


- from terminal run `run.sh` to do all of this :
``` bash
  #!/bin/bash
#  uncomment below to install brew
####################################################

# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

## install mysql8 client
# brew mysql-client@8.0

####################################################
# uncomment below to install Docker Desktop on MacOS
####################################################
# curl -fsSL https://download.docker.com/mac/stable/Docker.dmg -o ~/Docker.dmg
# hdiutil detach /Volumes/Docker
# cp -R /Volumes/Docker/Docker.app ~/Applications/
# hdiutil detach /Volumes/Docker
# open ~/Applications/Docker.app

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
```

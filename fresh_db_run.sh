#!/bin/bash

# with the assumption of python environment is activated

# start the docker compose
# navigate to the directory of the script
cd "$(dirname "$0")"

# start the docker compose
docker-compose up -d

sleep 5

# start backend code
cd backend/src
python main.py &

# capture the PID of the main.py process
MAIN_PY_PID=$!

cd database
python init_db.py

fg %1

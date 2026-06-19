#!/bin/bash
cd "$(dirname "$0")"
rm -rf venv
python3 -m venv venv
./venv/bin/python3 -m pip install --upgrade pip
./venv/bin/python3 -m pip install flask

if [ -f "requirements.txt" ]; then
    ./venv/bin/python3 -m pip install -r requirements.txt
fi
open http://127.0.0.1:5000
./venv/bin/python3 app.py
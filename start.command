#!/bin/bash
cd "$(dirname "$0")"
pip3 install -r requirements.txt
open "http://127.0.0.1:5000/"
python3 app.py

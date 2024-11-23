#!/bin/bash

reset

clear
set -e

set -x

sudo apt update

sudo apt install -y python3-pip

sudo apt install -y python3-flask

sudo apt install -y python3.12-venv

python3 -m venv my_venv

source my_venv/bin/activate

pip install -r requirements.txt   



##pip install flask

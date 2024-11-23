#!/bin/bash

reset

clear
set -e

set -x

sudo apt update

sudo apt install -y python3-pip


python3 -m venv my_venv

pip install -r requirements.txt   



##pip install flask

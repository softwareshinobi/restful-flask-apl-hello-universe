#!/bin/bash

reset

clear
set -e

set -x

sudo apt install -f python3-pip

pip install -r requirements.txt   



##pip install flask

#!/bin/bash
apt update && apt upgrade -y
apt install vim python3 python pip virtualenv build-essential python3-dev python -y

mkdir /deploy
mkdir /deploy/App
mkdir /deploy/envs
cd /deploy/envs
virtualenv -p python3 envoficio
source envoficio/bin/activate
pip install django pillow xhtml2pdf

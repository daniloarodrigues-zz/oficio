#!/bin/bash
apt update && apt upgrade -y
apt install vim python3 python virtualenv build-essential python3-dev python -y
apt install python-pip -y

DIR=/
FILE=deploy

if [ -e "$DIR$FILE" ] ; then
echo "Os diretórios já existem"
else
mkdir /deploy
mkdir /deploy/App
mkdir /deploy/envs
fi

cd /deploy/envs
virtualenv -p python3 envoficio
source envoficio/bin/activate
pip install django pillow xhtml2pdf gunicorn

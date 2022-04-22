#!/usr/bin/env bash

DJANGODIR=/home/ubuntu/emqx/messenger/              # Django project directory

cd $DJANGODIR
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

./manage.py migrate --noinput

./manage.py runserver

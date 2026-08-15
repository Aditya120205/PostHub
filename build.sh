#!/usr/bin/env bash

pip install -r requirements.txt

cd django_web_app

python manage.py collectstatic --no-input
python manage.py migrate
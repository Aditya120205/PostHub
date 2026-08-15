#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python django_web_app/manage.py collectstatic --no-input
python django_web_app/manage.py migrate
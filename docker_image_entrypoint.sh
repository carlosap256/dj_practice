#!/bin/sh

#  "dj_practice.settings_preproduction"

cd /dj_practice

python manage.py makemigrations --settings="${DJANGO_SETTINGS_FILE}"
python manage.py migrate --settings="${DJANGO_SETTINGS_FILE}"

python manage.py collectstatic --noinput --settings="${DJANGO_SETTINGS_FILE}"

DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_FILE} gunicorn dj_practice.wsgi --bind 0.0.0.0:8000 --workers 1

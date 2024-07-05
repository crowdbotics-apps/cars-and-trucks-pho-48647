#!/bin/bash

python manage.py migrate --noinput

waitress-serve --port=$PORT cars_and_trucks_pho_48647.wsgi:application

#!/bin/bash

cd /home/anthonphax/django-xperience
git pull
python manage.py migrate
python manage.py collectstatic -y

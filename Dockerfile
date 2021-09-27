FROM python:3-alpine

ENV PYTHONUNBUFFERED=1

RUN pip install djangorestframework

COPY django_rest_api/ /

ENTRYPOINT python manage.py runserver 0.0.0.0:8000

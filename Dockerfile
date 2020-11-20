FROM python:3.6

ENV PYTHONUNBUFFERED 1


WORKDIR /code/
COPY . /code/

RUN pip install Django==2.2.17
RUN pip install djangorestframework
RUN pip install psycopg2-binary
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin
EXPOSE 8000

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py runserver 0:8000

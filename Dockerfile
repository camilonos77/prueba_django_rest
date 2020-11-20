FROM python:3.5

ENV PYTHONUNBUFFERED 1


WORKDIR /code/
COPY . /code/

RUN pip install Django==2.2.17
RUN pip install djangorestframework
RUN pip install psycopg2-binary
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin
EXPOSE 8000
FROM python:3.9

RUN apt-get install libpq-dev

RUN mkdir /app
ADD app/requirements.txt /app/

RUN pip install -r /app/requirements.txt

WORKDIR /app

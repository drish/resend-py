FROM python:3.11.5

RUN pip install --upgrade pip

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN pip install tox

ENV APP_HOME /app

ADD . $APP_HOME
WORKDIR $APP_HOME
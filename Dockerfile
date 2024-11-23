FROM ubuntu

## install python3

RUN set -xe \
    && apt-get update \
    && apt-get install -y python3 \
    && apt-get install -y python3-pip

## install rytr api situation

RUN set -xe \
    && pip install flask_cors \
    && pip install flask

## Add The Python/Flask Files

ADD . /

## On Container start, run the Python API file

CMD ["python3", "app.py"]

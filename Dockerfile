FROM python:2-onbuild

RUN apt-get update && \
    apt-get install -y git gettext && \
    apt-get autoremove -y && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR app

ADD . /app

RUN pip install -r requirements.txt

ENTRYPOINT /app/entrypoint.sh

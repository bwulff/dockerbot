FROM python:2-onbuild
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y git gettext && \
    apt-get autoremove -y && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /app
WORKDIR /app

ADD . /app/

RUN pip install -r /app/requirements.txt 

CMD ["sh", "/app/entrypoint.sh"]

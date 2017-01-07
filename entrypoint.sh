#!/bin/bash

# apply configuration
envsubst </app/config.yml.tmpl >/app/config.yml

# start docker-event client
docker-events -c /app/config.yml -m dockerbot


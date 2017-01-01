#!/bin/bash

# apply configuration
envsubst <config.yml.tmpl >config.yml

# start docker-event client
docker-event -s /tmp/docker.socket -c config.yml -f docker-bot.py


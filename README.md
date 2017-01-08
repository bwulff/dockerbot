# Docker Notifier #

Script that post messages to a Slack channel when a Docker container dies.

## Configuration ##

The Slack API token and the channel to post to need to be configured via environment variables. Also the host's Docker socket needs to be shared with the container.

__Example:__

`docker run --name bot -v /var/run/docker.sock:/var/run/docker.sock:ro -e DOCKERBOT_API_TOKEN=api-token-12345 -e DOCKERBOT_CHANNEL=general slidewiki/dockerbot`



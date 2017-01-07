import docker_events
from slacker import Slacker


#@docker_events.stop.subscribe
#def docker_event(client, docker_event, config):
#    notify(config, "Container stopped: {} ({})".format(docker_event['Actor']['Attributes']['name'], docker_event['Actor']['Attributes']['image']))


@docker_events.die.subscribe
def docker_event(client, docker_event, config):
    notify(config, "Container died: {} ({})".format(docker_event['Actor']['Attributes']['name'], docker_event['Actor']['Attributes']['image']))


def notify(config, message):
    slack = Slacker(config['slack']['api-token'])
    slack.chat.post_message('#{}'.format(config['slack']['channel']), message)
    print('#{}: {}'.format(config['slack']['channel'], message))
    


import docker_events
from slacker import Slacker

@docker_events.stop.subscribe
def docker_event(client, docker_event, config):
    '''
    Send a message about the event to Slack channel
    '''

    slack = Slacker(config['slack']['api-token'])

    message = "Container died: {} ({})".format(docker_event['Actor']['Attributes']['name'],docker_event['Actor']['Attributes']['image'])
    print('#{}: {}'.format(config['slack']['channel'], message))
    # slack.chat.post_message('#{}'.format(config['slack']['channel']), message)
    
    


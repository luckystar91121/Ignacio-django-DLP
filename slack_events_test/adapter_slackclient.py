from django.conf import settings
SLACK_VERIFICATION_TOKEN = settings.SLACK_VERIFICATION_TOKEN
SLACK_BOT_TOKEN = settings.SLACK_BOT_TOKEN

import logging
logging.getLogger().setLevel(logging.INFO)

from pyee import EventEmitter
from slack import WebClient
import re
from .models import *

CLIENT = WebClient(SLACK_BOT_TOKEN)

class SlackEventAdapter(EventEmitter):
    def __init__(self, verification_token):
        EventEmitter.__init__(self)
        self.verification_token = verification_token

slack_events_adapter = SlackEventAdapter(SLACK_VERIFICATION_TOKEN)

# Example responder to greetings
@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data["event"]    
    if message.get('subtype') is None:
        content = message.get('text')
        regular_expressions = Regular_Expression.objects.all()
        if len(regular_expressions) > 0:
            for regular in regular_expressions:
                # print(expression)
                detected_msg = re.sub(regular.expression, "(Detected)", content)
                logging.info(regular.expression)
                logging.info(detected_msg)
                Detected_Message.objects.create(
                    regression = regular,
                    content = detected_msg
                )

# Example reaction emoji echo
@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
    event = event_data["event"]
    emoji = event["reaction"]
    channel = event["item"]["channel"]
    text = ":%s:" % emoji
    logging.info("chat.postMessage: channel: %s text: %s" % (channel, text))
    CLIENT.api_call("chat.postMessage", channel=channel, text=text)
# app/slack_bot.py

import os
from slack_bolt import App
from slack_bolt.adapter.fastapi import SlackRequestHandler

# app = App(token=os.environ["SLACK_BOT_TOKEN"])
app = App()
app_handler = SlackRequestHandler(app)


@app.event("app_mention")
def handle_app_mentions(body, say, logger):
    logger.info(body)
    say("What's up?")


@app.event("message")
def handle_message():
    pass

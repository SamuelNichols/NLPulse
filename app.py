import os

from interactions import (
    Client,
    Intents,
)
from interactions.api.events import Component

token = os.getenv("DISCORD_BOT_TOKEN")

bot = Client(intents=Intents.DEFAULT)

bot.load_extension("extensions.__init__")

bot.start(token)

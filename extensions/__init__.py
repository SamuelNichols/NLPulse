import logging
import datetime
import interactions
from constants import EXTENSIONS


class Core(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client
        [self.client.load_extension(extension) for extension in EXTENSIONS]


def setup(client) -> None:
    print("loaded all extensions")
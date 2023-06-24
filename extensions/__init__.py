import interactions
from constants import EXTENSIONS


class Core(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client
        for extension in EXTENSIONS:
            self.client.load_extension(extension)


def setup(client) -> None:
    Core(client)
    print("all extensions loaded")
    
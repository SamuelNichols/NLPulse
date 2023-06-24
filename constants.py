import os

TOKEN = os.getenv("HARUHI_BOT_TOKEN")
"""The token of the bot."""

import os

def get_all_extensions(directory: str) -> list[str]:
    extensions = []
    for root, _dirs, files in os.walk(directory):
        for file in files:
            if not file.__contains__("_") and not root.__contains__("_"):
                extension = root.replace("/", ".") + "." + file.replace(".py", "")
                extensions.append(extension)
    return extensions

EXTENSIONS = get_all_extensions("extensions/")

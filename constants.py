import os

TOKEN = os.getenv("HARUHI_BOT_TOKEN")
"""The token of the bot."""

import os

def get_all_extensions(directory: str) -> list[str]:
    for root, _dirs, files in os.walk(directory):
        for file in files:
            if not file.startswith("_"):
                return root.replace("/", ".") + "." + file.replace(".py", "")

EXTENSIONS = get_all_extensions("extensions/")

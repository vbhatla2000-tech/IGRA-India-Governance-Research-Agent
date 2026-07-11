import json
import os
from datetime import datetime

CONFIG_PATH = "config/igra_config.json"

def load_config():
    with open(CONFIG_PATH, "r") as file:
        return json.load(file)

def start_runtime():
    config = load_config()

    print("=" * 40)
    print("IGRA Runtime Started")
    print("Project:", config["project"])
    print("Version:", config["version"])
    print("Time:", datetime.now())
    print("Status: ONLINE")
    print("=" * 40)

if __name__ == "__main__":
    start_runtime()


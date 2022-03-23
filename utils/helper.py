import json
import os
from contextlib import suppress

config=None

def load_config(file):
    global config
    if config is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', file)
        with suppress(FileNotFoundError):
            with open(config_file) as f:
                config = json.load(f)
    return config


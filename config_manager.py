import json
from os import path

cached_config = None


def load_config():
    global cached_config

    if cached_config:
        return cached_config

    config_file = open(path.abspath(
        path.join(__file__, '../config.json')), 'r')
    serialized_config = config_file.read()
    config_file.close()

    config = json.loads(serialized_config)
    cached_config = config

    return config

from pathlib import Path
from configparser import ConfigParser

from ticket import Interpark


def read_config():
    config = None
    configer_path = Path("./config.ini")
    if not configer_path.exists():
        raise FileNotFoundError("Config file was not found.")
    config = ConfigParser()
    config.read(configer_path)
    return config


if __name__ == "__main__":
    config = read_config()
    Interpark(config).exectue()

    # TODO: read config file
    # TODO: execute
    pass

import json
import os

class Config:
    def __init__(self, arguments) -> None:
        self._arguments = arguments
        with open(self._config_file_path(), "r", encoding="utf-8") as file:
            config = json.loads(file.read())
        self._sensors_paths = config["sensors_paths"]

    def _config_file_path(self) -> str:
        paths = [
            self._arguments.config_file_path,
            "./.temps.config.json",
            "~/.temps.config.json",
            "/etc/temps/config.json"
        ]
        for path in paths:
            if path is None:
                continue
            path = os.path.expanduser(os.path.expandvars(path))
            if os.path.isfile(path):
                return path
        raise FileNotFoundError("Couldn't find the config file")

    @property
    def sensors_paths(self) -> list:
        return self._sensors_paths

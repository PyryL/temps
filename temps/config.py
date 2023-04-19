import json
from os import path

class Config:
    def __init__(self, file_path: str = "~/.tempconfig.json") -> None:
        with open(path.expanduser(file_path), "r", encoding="utf-8") as file:
            config = json.loads(file.read())
        self._sensors_paths = config["sensors_paths"]

    @property
    def sensors_paths(self) -> list:
        return self._sensors_paths

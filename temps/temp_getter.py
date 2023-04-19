import subprocess
import json
from temps.config import Config

def get_from_dict_by_key_path(dictionary: dict, key_path: list):
    result = dictionary
    for key in key_path:
        result = result.get(key)
    return result

class TempGetter:
    def __init__(self, config: Config) -> None:
        self._config = config

    def get_temps(self) -> list:
        sensors_data = json.loads(subprocess.check_output("sensors -j", shell=True, text=True))
        result = []
        for item in self._config.sensors_paths:
            result.append((
                item["title"],
                get_from_dict_by_key_path(sensors_data, item["current_temp_path"]),
                get_from_dict_by_key_path(sensors_data, item["limit_temp_path"])
            ))
        return result

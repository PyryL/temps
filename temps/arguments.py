import argparse

class Arguments:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Monitor CPU, GPU & other temperatures")
        parser.add_argument("-c", "--config")
        parser.add_argument("-v", "--version", action="version", version="0.1.0")
        self._arguments = parser.parse_args()

    @property
    def config_file_path(self) -> str:
        return self._arguments.config

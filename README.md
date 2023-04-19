# Temps

_Monitor CPU, GPU & other temperatures_

## Installation

Initialize environment and install Python dependencies by running

```
poetry install
```

Install `sensors` with

```
apt install lm-sensors
```

Create a config file at `~/.tempconfig.json` as described in [Configuration section](#configuration) below.

## Usage

Application can be run with command

```
poetry run python main.py
```

## Configuration

Configuration is kept in `~/.tempconfig.json` file. It is a JSON dictionary formatted file with the following keys.

### `sensors_paths`

Value of this key is an array where every item is a dictionary as follows:

key | value
---  | ---
`title` | A string that describes this temperature
`current_temp_path` | An array of strings that lead to the current temperature in the output of `sensors -j`.
`limit_temp_path` | Similar key path as `current_temp_path` but for maximum temperature instead of current.

Temperatures will be outputted in the order they appear in this array.

## Building

Python application can be built to native application by running

```
poetry run pyinstaller --onefile --name temps main.py
```

The executable file will appear at `dist/temps`.

## License

Copyright (c) 2023 Pyry Lahtinen

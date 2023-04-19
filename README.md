# Temps

_Monitor CPU, GPU & other temperatures_

## Installation

Install `sensors` with

```
apt install lm-sensors
```

Create a config file at `~/.tempconfig.json`. Refer the next section about the content of that file.

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

## License

Copyright (c) 2023 Pyry Lahtinen

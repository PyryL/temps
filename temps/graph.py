
class Grapher:
    def __init__(self) -> None:
        self._graphs = []

    def add_graph(self, title: str, current_temp: float, limit_temp: float) -> None:
        self._graphs.append((current_temp, limit_temp, title))

    def print(self) -> None:
        bar_width = 12
        title_length = max([len(t[2]) for t in self._graphs])
        for (current_temp, limit_temp, title) in self._graphs:
            padded_title = f"{title:<{title_length}}"
            percent = current_temp / limit_temp
            bar_char_count = round((100*percent) // (100/bar_width))
            bar_char_count = max(min(bar_char_count, bar_width), 0)
            bar_character = "#" if percent < 1 else "!"
            bar_str = "[" + bar_character*bar_char_count + " "*(bar_width-bar_char_count) + "]"
            suffix = f"{current_temp:3.0f} / {limit_temp:3.0f}"
            print(' '.join([padded_title, bar_str, suffix]))

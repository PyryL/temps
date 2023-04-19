
class Grapher:
    def __init__(self) -> None:
        self._graphs = []

    def add_graph(self, percent: float, prefix: str, suffix: str) -> None:
        self._graphs.append((percent, prefix, suffix))

    def print(self) -> None:
        bar_width = 12
        prefix_length = max([len(t[1]) for t in self._graphs])
        for (percent, prefix, suffix) in self._graphs:
            padded_prefix = f"{prefix:<{prefix_length}}"
            bar_char_count = round((100*percent) // (100/bar_width))
            bar_char_count = min(bar_char_count, bar_width)
            bar_character = "#" if percent < 1 else "!"
            bar_str = "[" + bar_character*bar_char_count + " "*(bar_width-bar_char_count) + "]"
            print(' '.join([padded_prefix, bar_str, suffix]))

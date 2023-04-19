from temps import TempGetter, Grapher, Config, Arguments

def main():
    arguments = Arguments()
    config = Config(arguments)
    temp_getter = TempGetter(config)
    graph = Grapher()
    for result in temp_getter.get_temps():
        graph.add_graph(result[0], result[1], result[2])
    graph.print()

if __name__ == "__main__":
    main()

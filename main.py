from temps import TempGetter, Grapher

def main():
    cpu_temp = TempGetter.get_cpu_temp()
    acpi_temp = TempGetter.get_acpi_temp()
    graph = Grapher()
    graph.add_graph("CPU", cpu_temp[0], cpu_temp[1])
    graph.add_graph("ACPI", acpi_temp[0], acpi_temp[1])
    graph.add_graph("Test", 112.48454884365865, 87)
    graph.print()

if __name__ == "__main__":
    main()

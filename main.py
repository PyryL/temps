from temps import TempGetter, Grapher

def main():
    cpu_temp = TempGetter.get_cpu_temp()
    acpi_temp = TempGetter.get_acpi_temp()
    graph = Grapher()
    graph.add_graph(cpu_temp[0]/cpu_temp[1], "CPU", f"{cpu_temp[0]} / {cpu_temp[1]}")
    graph.add_graph(acpi_temp[0]/acpi_temp[1], "ACPI", f"{acpi_temp[0]} / {acpi_temp[1]}")
    graph.add_graph(112/87, "Test", f"{112} / {87}")
    graph.print()

if __name__ == "__main__":
    main()

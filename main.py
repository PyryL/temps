import subprocess
import json

def get_cpu_temp():
    """ Returns (current, max) tuple in Celsius """
    output = subprocess.check_output("sensors -j", shell=True, text=True)
    output = json.loads(output)
    return (
        output["coretemp-isa-0000"]["Package id 0"]["temp1_input"],
        output["coretemp-isa-0000"]["Package id 0"]["temp1_max"]
    )

def get_acpi_temp():
    """ Returns (current, critical) tuple in Celsius """
    output = subprocess.check_output("sensors -j", shell=True, text=True)
    output = json.loads(output)
    # TODO: handle multiple
    return (
        output["acpitz-acpi-0"]["temp1"]["temp1_input"],
        output["acpitz-acpi-0"]["temp1"]["temp1_crit"]
    )

if __name__ == "__main__":
    cpu_temp = get_cpu_temp()
    acpi_temp = get_acpi_temp()
    print(f" CPU: {cpu_temp[0]} / {cpu_temp[1]}")
    print(f"ACPI: {acpi_temp[0]} / {acpi_temp[1]}")

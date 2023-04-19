import subprocess
import json

class TempGetter:
    @classmethod
    def get_cpu_temp(cls):
        """ Returns (current, max) tuple in Celsius """
        output = subprocess.check_output("sensors -j", shell=True, text=True)
        output = json.loads(output)
        return (
            output["coretemp-isa-0000"]["Package id 0"]["temp1_input"],
            output["coretemp-isa-0000"]["Package id 0"]["temp1_max"]
        )

    @classmethod
    def get_acpi_temp(cls):
        """ Returns (current, critical) tuple in Celsius """
        output = subprocess.check_output("sensors -j", shell=True, text=True)
        output = json.loads(output)
        # TODO: handle multiple
        return (
            output["acpitz-acpi-0"]["temp1"]["temp1_input"],
            output["acpitz-acpi-0"]["temp1"]["temp1_crit"]
        )

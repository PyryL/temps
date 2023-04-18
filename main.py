import os
import re
import subprocess

def get_cpu_temp():
    import json
    output = subprocess.check_output("sensors -j", shell=True, text=True)
    output = json.loads(output)
    return (
        output["coretemp-isa-0000"]["Package id 0"]["temp1_input"],
        output["coretemp-isa-0000"]["Package id 0"]["temp1_max"]
    )

if __name__ == "__main__":
    cpu_temp = get_cpu_temp()
    print(f"{cpu_temp[0]} / {cpu_temp[1]}")

import os
import subprocess

battery_dir = "/sys/class/power_supply"

batteries = []
status = []
check = os.listdir(battery_dir)


for i in check:
    battery = subprocess.check_output(['cat', battery_dir + '/'+  i + '/capacity' ]).decode('utf-8').strip()
    battery_status = subprocess.check_output(['cat', battery_dir + '/' + i + '/status']).decode('utf-8').strip()
    if battery_status == "Charging":
        status.append("")
    else: 
        status.append("")

    batteries.append(battery)

if len(batteries) > 0:
    for i in range(len(batteries)):
        print(f"{status[i]}  {batteries[i]}% ", end="")
else:
    print("")








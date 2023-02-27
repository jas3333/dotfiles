import subprocess

adap_sync = subprocess.check_output(["hyprctl", "getoption", "misc:vfr"]).decode("utf-8")
print(adap_sync)

if "int: 0" in adap_sync:
    subprocess.call(["hyprctl", "keyword", "misc:vfr", "on"])
    subprocess.call(["notify-send", "Adaptive Sync Enabled"])
else:
    subprocess.call(["hyprctl", "keyword", "misc:vfr", "off"])
    subprocess.call(["notify-send", "Adaptive Sync Disabled"])

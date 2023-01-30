import subprocess

adap_sync = subprocess.check_output(["hyprctl", "getoption", "misc:no_vfr"]).decode("utf-8")

if "int: 1" in adap_sync:
    subprocess.call(["hyprctl","--batch" ,"keyword misc:no_vfr false; keyword misc:no_direct_scanout 1"])
    subprocess.call(["notify-send", "Adaptive Sync Enabled"])
else:
    subprocess.call(["hyprctl", "--batch", "keyword misc:no_vfr true; keyword misc:no_direct_scanout 0"])
    subprocess.call(["notify-send", "Adaptive Sync Disabled"])

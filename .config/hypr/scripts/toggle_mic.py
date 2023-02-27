import subprocess

get_mic_status = subprocess.check_output(["amixer", "set", "Capture", "toggle"]).decode("utf-8")
print(get_mic_status)

if "off" in get_mic_status:
    subprocess.run(["notify-send", "Mic off"])
elif "on" in get_mic_status:
    subprocess.run(["notify-send", "Mic on"])

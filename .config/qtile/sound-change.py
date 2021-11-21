import subprocess

result = subprocess.run(["pactl", "get-default-sink"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
get_stupid_always_changing_number_grrr = subprocess.run(["pactl", "list", "short", "sinks"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

stupid_line = get_stupid_always_changing_number_grrr.stdout
stupid_list = []
index = result.stdout


for n in range(3):
    stupid_list.append(stupid_line.splitlines()[n])


for i in range(3):
    test = stupid_list[i]
    if "hdmi" in test:
        stupid_hdmi_number = test[0:2]
    elif "usb" in test:
        stupid_usb_number = test[0:2]


if "usb" in index:
    subprocess.run(["pactl", "set-default-sink", stupid_hdmi_number])
elif "hdmi" in index:
    subprocess.run(["pactl", "set-default-sink", stupid_usb_number])

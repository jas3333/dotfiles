#! /usr/bin/env python

import subprocess

result = subprocess.run(["pactl", "get-default-sink"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
get_stupid_always_changing_number_grrr = subprocess.run(["pactl", "list", "short", "sinks"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

stupid_line = get_stupid_always_changing_number_grrr.stdout
stupid_list = []
index = result.stdout
hdmi_text = "Switching to HDMI output."
usb_text = "Switching to USB output."


for i in range(3):
    stupid_list.append(stupid_line.splitlines()[i])
    test = stupid_list[i]
    if "hdmi" in test:
        stupid_hdmi_number = test[0:2]
    elif "usb" in test:
        stupid_usb_number = test[0:2]


if "usb" in index:
    subprocess.run(["pactl", "set-default-sink", stupid_hdmi_number])
    subprocess.run(["dunstify", hdmi_text])
elif "hdmi" in index:
    subprocess.run(["pactl", "set-default-sink", stupid_usb_number])
    subprocess.run(["dunstify", usb_text])

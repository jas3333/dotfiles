#! /usr/bin/env python

import subprocess

result = subprocess.run(["pactl", "get-default-sink"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
get_sink = subprocess.run(["pactl", "list", "short", "sinks"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

sink_line = get_sink.stdout
sink_list = []
index = result.stdout
hdmi_text = "Switching to HDMI output."
usb_text = "Switching to USB output."


for i in range(3):
    sink_list.append(sink_line.splitlines()[i])
    test = sink_list[i]
    if "hdmi" in test:
        hdmi_sink = test[0:2]
    elif "usb" in test:
        usb_sink = test[0:2]


if "usb" in index:
    subprocess.run(["pactl", "set-default-sink", hdmi_sink])
    subprocess.run(["dunstify", hdmi_text])
elif "hdmi" in index:
    subprocess.run(["pactl", "set-default-sink", usb_sink])
    subprocess.run(["dunstify", usb_text])

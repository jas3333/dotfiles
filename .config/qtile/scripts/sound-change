#! /usr/bin/env python
import subprocess

current_sink = subprocess.run(['pamixer', '--get-default-sink'], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True).stdout
get_sinks = subprocess.run(['pamixer', '--list-sinks'], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True).stdout.splitlines()
get_sinks.remove('Sinks:')

hdmi_text = "Switching to HDMI output."
usb_text = "Switching to USB output."
bluethooth_text = 'Switching to Bluethooth output.'
usb = 0
hdmi = 0
bluethooth = 0

for sink in get_sinks:
    if 'usb' in sink:
        usb = sink.split()[0]
    elif 'hdmi' in sink:
        hdmi = sink.split()[0]
    elif 'bluez' in sink:
        bluethooth = sink.split()[0]


if 'usb' in current_sink:
    subprocess.run(['pactl', 'set-default-sink', str(hdmi)])
    subprocess.run(["dunstify", hdmi_text])
elif 'hdmi' in current_sink and int(bluethooth) > 0:
    subprocess.run(['pactl', 'set-default-sink', str(bluethooth)])
    subprocess.run(["dunstify", bluethooth_text])
elif 'hdmi' in current_sink and int(bluethooth) == 0:
    subprocess.run(['pactl', 'set-default-sink', str(usb)])
    subprocess.run(["dunstify", usb_text])
elif 'bluez' in current_sink:
    subprocess.run(['pactl', 'set-default-sink', str(usb)])
    subprocess.run(["dunstify", usb_text])

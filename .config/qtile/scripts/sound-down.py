#! /usr/bin/env python

import subprocess

result = subprocess.run(["amixer", "-D", "pulse", "sset", "Master", "5%-"], 
                        stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

output = subprocess.run(["get-volume"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

if len(output.stdout) == 5:
    volume_number = output.stdout[0:3]
elif len(output.stdout) == 4:
    volume_number = output.stdout[0:2]
else:
    volume_number = output.stdout[0:1]

subprocess.run(["dunstify", "-h", "string:x-canonical-private-synchronous:audio",
                "Volume: " + volume_number, "-h", "int:value:"+volume_number])

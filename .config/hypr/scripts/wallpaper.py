#!/usr/bin/env python 
import subprocess
import os
import random

STEP = 7
FPS = 60
ANGLE = 30
path = "/home/jas/wallpaper/all/"
images = subprocess.run(["ls", path], stdout=subprocess.PIPE).stdout.decode("utf-8").split()
image = path + random.choice(images)

# subprocess.run(["hyprctl", "dispatch", "swww", "img", image, "--transition-step", f"{STEP}", "--transition-fps", f"{FPS}", "--transition-angle", f"{ANGLE}", "--transition-type", "wipe"])
os.system(f"swww img {image} --transition-step {STEP} --transition-fps {FPS} --transition-angle {ANGLE} --transition-type wipe")

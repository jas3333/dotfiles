#!/usr/bin/env python 
import subprocess
import random

STEP = 120
FPS = 60

ANGLES = [30, 45, 180]
ANGLE = random.choice(ANGLES)

path = "/home/jas/wallpaper/scenic2/"
images = subprocess.run(["ls", path], stdout=subprocess.PIPE).stdout.decode("utf-8").split()
image = path + random.choice(images)
print(image)

subprocess.run(["swww", "img", image, "--transition-step", f"{STEP}", "--transition-fps", f"{FPS}", "--transition-angle", f"{ANGLE}", "--transition-type", "wipe"])

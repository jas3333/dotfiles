#!/usr/bin/env python 
import subprocess
import random

STEP = 30
FPS = 60

ANGLES = [45, 90, 180]
ANGLE = random.choice(ANGLES)

if ANGLE == 90:
    STEP = 5

path = "/home/jas/wallpaper/CurrentSet/"
images = subprocess.run(["ls", path], stdout=subprocess.PIPE).stdout.decode("utf-8").split()
image = path + random.choice(images)
print(image)

subprocess.run(["swww", "img", image, "--transition-step", f"{STEP}", "--transition-fps", f"{FPS}", "--transition-angle", f"{ANGLE}", "--transition-type", "wipe"])

import re
from math import sqrt
from PIL import Image

with open("input.txt", "r") as f:
    lines = f.readlines()

regexp = re.compile(r"-?\d+")
robots = []
for line in lines:
    robots.append([int(z) for z in regexp.findall(line)])
w, h = 101, 103

NUM_STATES = 10403  # computed with count_states.py

def check(robots, t):
    RESULT = 6516       # manually found result
    return t == RESULT

# simulate robot movement
for t in range(1, NUM_STATES+1):
    for r in robots:
        r[0], r[1] = (r[0] + r[2]) % w, (r[1] + r[3]) % h
    if check(robots, t):
        # save image
        img = Image.new("RGB", (w, h))
        pxl = img.load()
        for r in robots:
            pxl[r[0], r[1]] = (255, 255, 255)
        img.save(f"out{t:05d}.png")

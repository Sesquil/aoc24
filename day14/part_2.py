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

# check if robot positions are approximately evenly distributed
def check(robots):
    cx, cy = [0]*w, [0]*h
    for r in robots:
        cx[r[0]] += 1
        cy[r[1]] += 1
    ex, ey = len(robots) / w, len(robots) / h
    """
    f = 4.0  # heuristic factor for deviation
    return any(c > f*ex for c in cx) and any(c > f*ey for c in cy)
    """
    dx = sum(abs(c-ex) for c in cx) / w
    dy = sum(abs(c-ey) for c in cy) / h
    return dx > 0.5*ex and dy > 0.5*ey

# simulate robot movement
for t in range(1, NUM_STATES+1):
    for r in robots:
        r[0], r[1] = (r[0] + r[2]) % w, (r[1] + r[3]) % h
    if check(robots):
        print(t)
        # save image
        img = Image.new("RGB", (w, h))
        pxl = img.load()
        for r in robots:
            pxl[r[0], r[1]] = (255, 255, 255)
        img.save(f"out{t:05d}.png")

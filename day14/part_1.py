import re

with open("input.txt", "r") as f:
    lines = f.readlines()

regexp = re.compile(r"-?\d+")
robots = []
for line in lines:
    robots.append([int(z) for z in regexp.findall(line)])
w, h = 101, 103

# simulate robot movement
for _ in range(100):
    for r in robots:
        r[0], r[1] = (r[0] + r[2]) % w, (r[1] + r[3]) % h

# count robots in quadrants
num = [0]*4
for r in robots:
    if r[0] != w//2 and r[1] != h//2:
        q = (0 if r[0] < w//2 else 1) + (0 if r[1] < h//2 else 2)
        num[q] += 1
res = num[0] * num[1] * num[2] * num[3]
print(res)

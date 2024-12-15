import re

with open("input.txt", "r") as f:
    lines = f.readlines()

regexp = re.compile(r"-?\d+")
robots = []
for line in lines:
    robots.append([int(z) for z in regexp.findall(line)])
w, h = 101, 103

# Simulate robot movement and count states
states = set()
while True:
    for r in robots:
        r[0], r[1] = (r[0] + r[2]) % w, (r[1] + r[3]) % h
    state = bytes([r[0] for r in robots] + [r[1] for r in robots])
    if state in states:
        break
    states.add(state)
print(len(states), "states found")

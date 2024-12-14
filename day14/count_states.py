import re

with open("input.txt", "r") as f:
    lines = f.readlines()

regexp = re.compile(r"-?\d+")
robots = []
for line in lines:
    robots.append([int(z) for z in regexp.findall(line)])
w, h = 101, 103

# simulate robot movement and count states
states = set()
level = [[" "]*w for _ in range(h)]
while True:
    for r in robots:
        level[r[1]][r[0]] = " "
        r[0], r[1] = (r[0] + r[2]) % w, (r[1] + r[3]) % h
        level[r[1]][r[0]] = "x"
    state = "".join("".join(row) for row in level)
    if state in states:
        break
    states.add(state)
print(len(states), "states found")

level = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        level.append([c for c in line.strip()])

h, w = len(level), len(level[0])
sx, sy = next((level[y].index("S"), y) for y in range(h) if "S" in level[y])
tx, ty = next((level[y].index("E"), y) for y in range(h) if "E" in level[y])

STEP = [(0,-1), (1,0), (0,1), (-1,0)]

# Compute path
p = []
x, y = sx, sy
while x != tx or y != ty:
    p.append((x, y))
    level[y][x] = "#"
    for dx, dy in STEP:
        nx, ny = x+dx, y+dy
        if level[ny][nx] != "#":
            x, y = nx, ny
            break
for x, y in p:
    level[y][x] = "."
level[sy][sx] = "S"
p.append((tx, ty))
idx = {}
for i, (x, y) in enumerate(p):
    idx[(x, y)] = i
time = len(p) - 1

MAX_PS = 20
CHEAT_STEPS = [(dx, dy) for dx in range(-MAX_PS, MAX_PS+1) \
               for dy in range(-MAX_PS, MAX_PS+1) if 2 <= abs(dx) + abs(dy) <= MAX_PS]

# Count time savings for cheats
t_cheats = {dt: 0 for dt in range(time)}
for i, (x, y) in enumerate(p):
    for dx, dy in CHEAT_STEPS:
        nx, ny = x+dx, y+dy
        if nx >= 0 and nx < w and ny >= 0 and ny < h and (nx, ny) in idx:
            j = idx[(nx, ny)]
            if j > i+3:
                dist = abs(dx) + abs(dy)
                t = i + time - j + dist
                dt = time - t
                if dt > 0:
                    t_cheats[dt] += 1
#print("\n".join(f"{c} cheats saving {dt} ps" for dt, c in sorted(t_cheats.items()) if c > 0))

res = sum(c for dt, c in t_cheats.items() if dt >= 100)
print(res)

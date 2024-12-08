with open("input.txt", "r") as f:
    level = [line.strip() for line in f.readlines()]

STEP = [(0,-1), (1,0), (0,1), (-1,0)]
def lookup(x, y, d):
    lx, ly = x + STEP[d][0], y + STEP[d][1]
    return "" if lx < 0 or lx >= m or ly < 0 or ly >= n else level[ly][lx]

n, m = len(level), len(level[0])
for y in range(n):
    if "^" in level[y]:
        sx, sy = level[y].index("^"), y
        break

x, y, c, d = sx, sy, "^", 0
pos = set()
while c:
    c = lookup(x, y, d)
    if c == "#":
        d = (d + 1) % 4
    else:
        pos.add((x, y))
        x += STEP[d][0]; y += STEP[d][1]
pos.remove((sx, sy))

DIRS = [1, 2, 4, 8]
def check_loop(sx, sy, ox, oy):
    level[oy] = level[oy][:ox] + "#" + level[oy][ox+1:]
    x, y, c, d = sx, sy, "^", 0
    mem = [[0]*m for _ in range(n)]
    res = False
    while c:
        if mem[y][x] & DIRS[d]:
            res = True
            break
        mem[y][x] |= DIRS[d]
        c = lookup(x, y, d)
        if c == "#":
            d = (d + 1) % 4
        else:
            x += STEP[d][0]; y += STEP[d][1]
    level[oy] = level[oy][:ox] + "." + level[oy][ox+1:]
    return res

res = sum(check_loop(sx, sy, ox, oy) for (ox, oy) in pos)
print(res)

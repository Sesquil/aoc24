with open('input.txt', 'r') as f:
    level = [[c for c in line.strip()] for line in f.readlines()]

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
while c:
    c = lookup(x, y, d)
    if c == "#":
        d = (d + 1) % 4
    else:
        level[y][x] = "X"
        x += STEP[d][0]; y += STEP[d][1]
level[sy][sx] = "^"

DIRS = [1, 2, 4, 8]
def check_loop(sx, sy, ox, oy):
    x, y, c, d = sx, sy, "^", 0
    mem = [[0]*m for _ in range(n)]
    level[oy][ox] = "#"
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
    level[oy][ox] = "X"    
    return res

res = sum(sum(check_loop(sx, sy, ox, oy) for ox in range(m) \
              if level[oy][ox] == "X") for oy in range(n))
print(res)

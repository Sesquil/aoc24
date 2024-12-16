level = []
with open("example1.txt", "r") as f:
    for line in f.readlines():
        level.append([c for c in line.strip()])

h, w = len(level), len(level[0])
sx, sy = next((level[y].index("S"), y) for y in range(h) if "S" in level[y])
tx, ty = next((level[y].index("E"), y) for y in range(h) if "E" in level[y])

# Find all s-t-paths via backtracking w/o recursion
STEP = [(0,-1), (1,0), (0,1), (-1,0)]
paths = []
def solve(x, y, d):
    stack = [(x, y, d, 0, [], 0)]
    while stack:
        x, y, d, s, p, i = stack.pop()
        if level[y][x] == "E":
            paths.append((s, p))
            continue
        if i == 0:
            level[y][x] = "x"
            nd = d
        elif i == 1:
            nd = (d-1)%4
        elif i == 2:
            nd = (d+1)%4
        else:
            level[y][x] = "."
            continue
        stack.append((x, y, d, s, p, i+1))
        dx, dy = STEP[nd]
        nx, ny = x+dx, y+dy
        if level[ny][nx] == "." or level[ny][nx] == "E":
            stack.append((nx, ny, nd, s + (1 if nd == d else 1001), p + [(x, y)], 0))

solve(sx, sy, 1)
level[ty][tx] = "O"
s_min = min(s for s, _ in paths)
for s, p in paths:
    if s == s_min:
        for x, y in p:
            level[y][x] = "O"
res = sum(row.count("O") for row in level)
print(res)

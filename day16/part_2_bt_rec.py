level = []
with open("example1.txt", "r") as f:
    for line in f.readlines():
        level.append([c for c in line.strip()])

h, w = len(level), len(level[0])
sx, sy = next((level[y].index("S"), y) for y in range(h) if "S" in level[y])
tx, ty = next((level[y].index("E"), y) for y in range(h) if "E" in level[y])

# Find all s-t-paths via backtracking with recursion
STEP = [(0,-1), (1,0), (0,1), (-1,0)]
paths = []
def solve(x, y, d, s, p):
    if level[y][x] == "E":
        paths.append((s, p))
        return
    level[y][x] = "x"
    for nd in (d, (d-1)%4, (d+1)%4):
        dx, dy = STEP[nd]
        nx, ny = x+dx, y+dy
        if level[ny][nx] == "." or level[ny][nx] == "E":
            solve(nx, ny, nd, s + (1 if nd == d else 1001), p + [(x, y)])
    level[y][x] = "."

solve(sx, sy, 1, 0, [])
level[ty][tx] = "O"
s_min = min(s for s, _ in paths)
for s, p in paths:
    if s == s_min:
        for x, y in p:
            level[y][x] = "O"
res = sum(row.count("O") for row in level)
print(res)

with open("input.txt", "r") as f:
    level = [[int(c) for c in line.strip()] for line in f.readlines()]

# Find trails via backtracking
STEP = [(0,-1), (1,0), (0,1), (-1,0)]
pos = []
def solve(x, y, z, s):
    if z > 9:
        return s+1
    for dx, dy in STEP:
        nx, ny = x+dx, y+dy
        if nx >= 0 and nx < m and ny >= 0 and ny < n and level[ny][nx] == z:
            level[ny][nx] = -z
            pos.append((nx, ny))
            s = solve(nx, ny, z+1, s)
    return s

n, m = len(level), len(level[0])
res = 0
for y in range(n):
    for x in range(m):
        if level[y][x] == 0:
            s = solve(x, y, 1, 0)
            if s > 0:
                res += s
                #print(f"Trailhead at {(x, y)}, score {s}")
            # Revert steps
            for nx, ny in pos:
                level[ny][nx] = -level[ny][nx]
            pos.clear()
print(res)

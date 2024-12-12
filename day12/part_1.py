with open("input.txt", "r") as f:
    level = [["."] + [c for c in line.strip()] + ["."] for line in f.readlines()]

n, m = len(level) + 2, len(level[0])
level = [["."]*m] + level + [["."]*m]

# Find region area and perimeter via flood-fill
STEP = [(-1,0), (1,0), (0,-1), (0,1)]
def solve(x, y):
    c = level[y][x]
    c_visited = c.lower()
    level[y][x] = c_visited
    stack = [(x, y)]
    area, peri = 0, 0
    while stack:
        x, y = stack.pop()
        area += 1
        for dx, dy in STEP:
            nx, ny = x+dx, y+dy
            if level[ny][nx] == c:
                stack.append((nx, ny))
                level[ny][nx] = c_visited
            elif level[ny][nx] != c_visited:
                peri += 1
    #print(c, area, peri)
    return area * peri

res = 0
for y in range(1, n-1):
    for x in range(1, m-1):
        if level[y][x] >= "A" and level[y][x] <= "Z":
            res += solve(x, y)
            #print("\n".join("".join(row) for row in level))
print(res)

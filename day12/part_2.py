with open("input.txt", "r") as f:
    level = [["."] + [c for c in line.strip()] + ["."] for line in f.readlines()]

n, m = len(level) + 2, len(level[0])
level = [["."]*m] + level + [["."]*m]

# Find region area and corners via flood-fill
STEP = [(-1,0), (1,0), (0,-1), (0,1)]
def solve(x, y):
    c = level[y][x]
    c_visited = c.lower()
    level[y][x] = c_visited
    stack = [(x, y)]
    region = []
    while stack:
        x, y = stack.pop()
        region.append((x, y))
        for dx, dy in STEP:
            nx, ny = x+dx, y+dy
            if level[ny][nx] == c:
                stack.append((nx, ny))
                level[ny][nx] = c_visited
    area = len(region)
    corners = 0
    for x, y in region:
        for dx, dy in STEP:
            if (level[y+dy][x+dx] != c_visited and level[y+dx][x-dy] != c_visited) or \
               (level[y+dy][x+dx] == c_visited and level[y+dx][x-dy] == c_visited and
                level[y+dy+dx][x+dx-dy] != c_visited):
                corners +=1
    #print(c, area, corners)
    return area * corners

res = 0
for y in range(1, n-1):
    for x in range(1, m-1):
        if level[y][x] >= "A" and level[y][x] <= "Z":
            res += solve(x, y)
print(res)

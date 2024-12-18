from collections import deque

with open("input.txt", "r") as f:
    lines = f.readlines()

pos = [tuple(int(c) for c in l.strip().split(",")) for l in lines]
w, h = 71, 71
n = 1024
level = [[" "]*w for _ in range(h)]
for x, y in pos[:n]:
    level[y][x] = "#"

# Find shortest path with BFS
STEP = [(0,-1), (1,0), (0,1), (-1,0)]
def bfs():
    queue = deque([(0, 0)])
    level[0][0] = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in STEP:
            nx, ny = x+dx, y+dy
            if nx >= 0 and ny >= 0 and nx < w and ny < h and level[ny][nx] == " ":
                if nx == w-1 and ny == h-1:
                    return level[y][x] + 1
                level[ny][nx] = level[y][x] + 1
                queue.append((nx, ny))
    return None

res = bfs()
print(res)

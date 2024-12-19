from collections import deque

with open("input.txt", "r") as f:
    lines = f.readlines()

pos = [tuple(int(c) for c in l.strip().split(",")) for l in lines]
w, h = 71, 71
n = 1024

STEP = [(0,-1), (1,0), (0,1), (-1,0)]
def bfs(n):
    # Block n fields
    level = [[" "]*w for _ in range(h)]
    for x, y in pos[:n]:
        level[y][x] = "#"
    # Find shortest path with BFS
    queue = deque([(0, 0)])
    level[0][0] = "O"
    while queue:
        x, y = queue.popleft()
        for dx, dy in STEP:
            nx, ny = x+dx, y+dy
            if nx >= 0 and ny >= 0 and nx < w and ny < h and level[ny][nx] == " ":
                if nx == w-1 and ny == h-1:
                    return True
                level[ny][nx] = "O"
                queue.append((nx, ny))
    return False

# Find min. number of blocking bytes with binary search
res = None
l, r = n+1, len(pos)
while l <= r:
    i = (l+r)//2
    if bfs(i):
        l = i
    elif not bfs(i-1):
        r = i
    else:
        res = pos[i-1]
        break

print(f"{res[0]},{res[1]}")

from heapq import *

level = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        level.append([c for c in line.strip()])

h, w = len(level), len(level[0])
sx, sy = next((level[y].index("S"), y) for y in range(h) if "S" in level[y])
ex, ey = next((level[y].index("E"), y) for y in range(h) if "E" in level[y])

# Find cheapest path via modified BFS with priority queue
STEP = [(0,-1), (1,0), (0,1), (-1,0)]
def solve(x, y, d):
    res = 0
    pqueue = [(0, x, y, d)]
    while pqueue:
        s, x, y, d = heappop(pqueue)
        if level[y][x] == "E":
            res = s
            break
        level[y][x] = "x"
        for nd in (d, (d-1)%4, (d+1)%4):
            dx, dy = STEP[nd]
            nx, ny = x+dx, y+dy
            if level[ny][nx] == "." or level[ny][nx] == "E":
                heappush(pqueue, (s + (1 if nd == d else 1001), nx, ny, nd))
    return res

res = solve(sx, sy, 1)
print(res)

from heapq import *
from math import inf

level = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        level.append([c for c in line.strip()])

h, w = len(level), len(level[0])
sx, sy = next((level[y].index("S"), y) for y in range(h) if "S" in level[y])
tx, ty = next((level[y].index("E"), y) for y in range(h) if "E" in level[y])

STEP = [(0,-1), (1,0), (0,1), (-1,0)]

# Build graph from input
graph = {}
for y in range(1, h-1):
    for x in range(1, w-1):
        if level[y][x] != "#":
            for d in range(4):
                graph[(x, y, d)] = [((x, y, (d+i)%4), 1000) for i in (-1, 1)]
for y in range(1, h-1):
    for x in range(1, w-1):
        if level[y][x] != "#":
            for nd, (dx, dy) in enumerate(STEP):
                nx, ny = x+dx, y+dy
                if level[ny][nx] != "#":
                    graph[(x, y, nd)].append(((nx, ny, nd), 1))

# Find min. cost from start via Dijkstra algorithm
def solve(x, y, d):
    done = {u: False for u in graph}
    cost = {u: inf for u in graph}
    cost[(x, y, d)] = 0
    todo = [(cost[u], u) for u in graph]
    heapify(todo)
    while todo:
        cost_u, u = heappop(todo)
        if done[u]:
            continue
        if cost_u is inf:
            break
        done[u] = True
        for v, c in graph[u]:
            if not done[v] and cost_u + c < cost[v]:
                cost[v] = cost_u + c
                heappush(todo, (cost[v], v))
    return cost

cost = solve(sx, sy, 1)
res = min(cost[(tx, ty, d)] for d in range(4))
print(res)

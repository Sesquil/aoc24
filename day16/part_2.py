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
                graph[(x, y, d)] = []
for y in range(1, h-1):
    for x in range(1, w-1):
        if level[y][x] != "#":
            for nd, (dx, dy) in enumerate(STEP):
                nx, ny = x+dx, y+dy
                if level[ny][nx] != "#":
                    graph[(x, y, nd)].append(((nx, ny, nd), 1))
                    graph[(x, y, (nd-1)%4)].append(((nx, ny, nd), 1001))
                    graph[(x, y, (nd+1)%4)].append(((nx, ny, nd), 1001))

# Find min. cost from given node via Dijkstra algorithm
def solve(x, y, dirs):
    done = {u: False for u in graph}
    cost = {u: inf for u in graph}
    for d in dirs:
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

# Count fields on cheapest paths
cost_from_s = solve(sx, sy, [1])
cost_from_t = solve(tx, ty, [0, 1, 2, 3])
s_min = min(cost_from_s[(tx, ty, d)] for d in range(4))
res = 0
for y in range(1, h-1):
    for x in range(1, w-1):
        ok = False
        for d in range(4):
            if any(cost_from_s.get((x, y, d), inf) + abs(i)*1000 + \
                   cost_from_t.get((x, y, (d+2+i)%4), inf) == s_min \
                   for i in range(-1, 2)):
                res += 1
                break
print(res)
